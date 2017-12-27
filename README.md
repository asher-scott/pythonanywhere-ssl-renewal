# PythonAnywhere SSL Certificate Renewal Script
A python script for use with www.pythonanywhere.com that checks to see if an SSL script is unexpired. If it is expired, the script generates a new certificate and emails the support staff at pythonanywhere.com the details necessary for activative the newly generated script.

### Setup
If you haven't set up SSL on your domain for use with pythonanywhere please see [this page](https://help.pythonanywhere.com/pages/LetsEncrypt/) for details on how to do so.
If you have, then follow these steps to set up the automatic renewal script contained in this repository:
1. Clone this repository inside of your home directory in python anywhere
2. Edit the renew_ssl.py file and insert the proper values in the CONFIG dictionary.  Be sure to do this carefully! If you insert improper values into this dictionary, the script will not work.  The following are descriptions of each field in the config dictionary, examples are given as needed:
    * SMTP_SERVER - e.g. smtp.gmail.com
    * SMTP_USERNAME - Most likely your email address without the "@domain.com" part
    * SMPT_PASSWORD - The same password associated with your email address
    * SENDER_EMAIL_ADDRESS - Your email address
    * RECIEVER_EMAIL_ADDRESS - This should always be set to support@pythonanywhere.com
    * PYTHONANYWHERE_USERNAME - Your pythonanywhere username
    * CERTIFICATE_DIR - The directory for your SSL certificates.  e.g. /home/username/letsencrypt/www.yourdomain.com
    * DOMAIN_NAME - The domain name of your website. e.g. www.yourdomain.com
3. On your pythonanywhere dashboard, click on the "Tasks" tab, and create a task to run the renew_ssl.py script at whatever time interval you prefer.

If you configured everything properly, the script should be all set to go and you can forget about manually generating openssl certificates for as long as you'd like!
