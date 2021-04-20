import logging
import azure.functions as func
import pyodbc
import time
import os
import json
import textwrap
from configparser import ConfigParser
# from sms_sender import SMS_Client
import email_sender
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import query_handler

def main(req: func.HttpRequest) -> func.HttpResponse:

    name = req.params.get('name')
    email = req.params.get('email')
    password = req.params.get('password')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if not email:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            email = req_body.get('email')
    if not password:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            password = req_body.get('password')
   

    response = {"message":"There is a missing parameter in your request"}
    if name  and password and email: 
        add_profile_query = "EXEC Profile_Add "+"@Full_Name='"+name+"'"+" , @Email='"+email+"'"+" , @Password='"+password+"';"
        response = query_handler.exec_query_with_message(add_profile_query)
        data = json.loads(response)[0]
        response = data
    
        logging.info(response)
        # response = {'message': "error: try again later"}
        if "profile_id" in response:
            profile_id = response['profile_id']
            # sms_client = SMS_Client()
            # sms_client.send_verification_message(profile_id)
            to_email , message = email_sender.generate_verification_message(profile_id)
            email_sender.send_mail( to_email , message)
            response = data
        
    return func.HttpResponse(
        json.dumps(response) ,
        mimetype="application/json"
    )
