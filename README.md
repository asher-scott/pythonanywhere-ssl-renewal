# PythonAnywhere SSL Certificate Renewal Script
A python script for use with www.pythonanywhere.com that checks to see if SSL certificates are about to expire. If they are, the script generates new certificates and installs them.

### Setup
If you haven't set up SSL on your domain for use with pythonanywhere please see [this page](https://help.pythonanywhere.com/pages/LetsEncrypt/) for details on how to do so.
If you have, then follow these steps to set up the automatic renewal script contained in this repository:
1. Clone this repository inside of your home directory in python anywhere
2. Edit the renew_ssl.py file and insert the domains for which you have installed certificates values in the DOMAIN_NAMES list, e.g. `DOMAIN_NAMES = ["www.yourdomain.com", "anotherdomain.org"]`. Be sure to do this carefully! If you insert improper values here, the script will not work as intended. You can also change the DAYS_BEFORE_RENEWAL value to something you prefer.
3. On your pythonanywhere dashboard, click on the "Tasks" tab, and create a task to run the renew_ssl.py script at whatever time interval you prefer.

If you configured everything properly, the script should be all set to go and you can forget about manually generating openssl certificates for as long as you'd like!
