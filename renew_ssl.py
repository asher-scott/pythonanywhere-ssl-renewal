#!/usr/bin/python3
import datetime
import os
import subprocess

"""
This script can be run to renew several LetsEncrypt SSL certificates on PythonAnywhere.
For configuration, all we need is to configure the domain names.

Beware: This is for renewal. For initial installation, the steps in https://help.pythonanywhere.com/pages/LetsEncrypt/
        should be followed for each domain, so that everything (PA scripts, certificate directories) is where expected.
"""

DOMAIN_NAMES = []  # FILL THIS IN
DAYS_BEFORE_EXPIRE = 3

LBL = "[PA-SSL-RENEWAL]"


def certificate_expires_soon(domain_name: str, in_days=3):
    date_parts = (
        subprocess.check_output(
            "openssl x509 -enddate -noout -in ~/letsencrypt/{}/cert.pem".format(
                domain_name
            ),
            shell=True,
            universal_newlines=True,
        )
        .replace("notAfter=", "")
        .split()
    )
    date_string = date_parts[1] + date_parts[0] + date_parts[3]
    expire_date = datetime.datetime.strptime(date_string, "%d%b%Y")

    if datetime.datetime.now() + datetime.timedelta(days=in_days) > expire_date:
        print("%s Certificate for %s expires soon (%s)" % (LBL, domain_name, expire_date))
        return True
    return False


def generate_new_certificate(domain_name: str):
    print("%s Generating certificate for  %s ..." % (LBL, domain_name))
    os.system(
        "~/dehydrated/dehydrated --cron --config ~/letsencrypt/config"
        " --domain {} --out ~/letsencrypt --challenge http-01 ".format(domain_name)
    )


def install_new_certificate(domain_name: str):
    print("%s Installing certificate for  %s ..." % (LBL, domain_name))
    os.system("pa_install_webapp_letsencrypt_ssl.py {}".format(domain_name))


if __name__ == "__main__":

    for domain in DOMAIN_NAMES:
        if certificate_expires_soon(domain, in_days=DAYS_BEFORE_EXPIRE):
            generate_new_certificate(domain)
            install_new_certificate(domain)
        else:
            print("%s Current certificate for %s is up to date!" % (LBL, domain))
