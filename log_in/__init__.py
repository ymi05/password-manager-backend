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

from profile_is_verified import profile_is_verified
import query_handler

def main(req: func.HttpRequest) -> func.HttpResponse:

    email = req.params.get('email')
    password = req.params.get('password')


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
    
    
    response = {'message' : "There is a missing parameter in your request"}
    if password and email: 
        profile_authentication_query = "EXEC validate_profile @Email='"+email+"'"+" , @Password='"+password+"';"
        response = query_handler.exec_query_with_message(profile_authentication_query)
        data = json.loads(response)[0]
        if not data["valid"]:
            
            return func.HttpResponse(
            json.dumps({'valid':False}) ,
            mimetype="application/json"
        ) 

        
        if "profile_id" in data:
            profile_id = data['profile_id']

            response = {'message':"Please verify your account"}
            if profile_is_verified(profile_id) :
                to_email , message = email_sender.generate_auth_message(profile_id)
                email_sender.send_mail( to_email , message)
                response = data


    return func.HttpResponse(
        json.dumps(response) ,
        mimetype="application/json"
    )
