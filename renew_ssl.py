#!/usr/bin/python
import datetime
import os
import smtplib
import subprocess

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CONFIG = {
    "SMTP_SERVER": "",
    "SMTP_USERNAME": "",
    "SMTP_PASSWORD": "",
    "SENDER_EMAIL_ADDRESS": "",
    "RECIEVER_EMAIL_ADDRESS": "",
    "PYTHONANYWHERE_USERNAME": ""
    "CERTIFICATE_DIR": "",
    "DOMAIN_NAME": ""
}

def certificate_expired():
    date_parts = subprocess.check_output("openssl x509 -enddate -noout -in ~/letsencrypt/{}/cert.pem".format(CONFIG['DOMAIN_NAME']), shell=True).strip("notAfter=").split(" ") 
    date_string = date_parts[1]+date_parts[0]+date_parts[3]
    expire_date = datetime.datetime.strptime(date_string, "%d%b%Y")

    if(datetime.datetime.now() + datetime.timedelta(days=3) > expire_date):
        return True
    return False

def generate_new_certificate():
    os.system("~/dehydrated/dehydrated --cron --config ~/letsencrypt/config --domain {} --out ~/letsencrypt --challenge http-01 ".format(CONFIG['DOMAIN_NAME']))


def send_renewal_email():
    body = """
    Username: {}
    Certificate Directory: {}
    Domain Name: {}
    
    Thank you!""".format(CONFIG['PYTHONANYWHERE_USERNAME'], CONFIG['CERTIFICATE_DIR'], CONFIG['DOMAIN_NAME'])

    email = MIMEMultipart()
    email['Subject'] = 'SSL Certificate Renewal'
    email.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP(CONFIG['SMTP_SERVER'], 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(CONFIG['SMTP_USERNAME'],CONFIG['SMTP_PASSWORD'])
    smtp.sendmail(CONFIG['SENDER_EMAIL_ADDRESS'], CONFIG['RECIEVER_EMAIL_ADDRESS'], email.as_string())
    smtp.quit()

if certificate_expired():
    generate_new_certificate()
    send_renewal_email()
else:
    print("Current certificates are up to date!")
