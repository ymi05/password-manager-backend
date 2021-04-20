import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from query_handler import exec_query_with_records
import json
import os
from config_file_handler import read_config_file
def send_mail( to_email , mail_content):

    sender_address , sender_pass = get_credenitals_from_config_file()

    receiver_address = to_email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'PManager Verification Code'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


def generate_verification_message(profile_id):
        data = exec_query_with_records("EXEC Verification_Code_get "+str(profile_id))
        data = json.loads(data[0][0])[0]
        name = data["name"]
        verification_code = data["verification_code"]
        email = data["email"]

        message = f"Hello! Here's your verification code: {verification_code} for PManager. If you did not sign up, please ignore this email!"
        return email , message

def generate_auth_message(profile_id):
    data = exec_query_with_records("EXEC Auth_Code_get "+str(profile_id))
    data = json.loads(data[0][0])[0]
    name = data["name"]
    authentication_code = data["authentication_code"]
    email = data["email"]

    message = f"Hello! Here's your authentication code: {authentication_code} for PManager. If you did not sign up, please change your password now!"
    return email , message


def get_credenitals_from_config_file(config_file = "config.ini" , config_file_path = os.path.dirname(__file__)):
    email , password = read_config_file(config_file_path , config_file , "email.credentials" , ["email" , "password"])
    return email , password