import logging
import azure.functions as func
import pyodbc
import time
import os
import json
import textwrap
from configparser import ConfigParser
# from sms_sender import SMS_Client
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import query_handler

def main(req: func.HttpRequest) -> func.HttpResponse:

    profile_id = str(req.params.get('profile_id'))
    URL = req.params.get('URL')
    website_app_name = req.params.get("website_app_name")
    username = req.params.get('username')
    password = req.params.get('password')

    if not profile_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            profile_id = req_body.get('profile_id')
    if not website_app_name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            website_app_name = req_body.get('website_app_name')
    if not URL:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            URL = req_body.get('URL')
    if not username:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')
    if not password:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            password = req_body.get('password')
   
    if profile_id and website_app_name and password and username: 
        add_account_query = "EXEC Account_Add @Profile_id = '"+profile_id+"'"+" , @Website_app_name = '"+website_app_name+"'"+" , @Username = '"+username+"'"+" , @Password ='"+password+"';"
        if URL:
            add_account_query = "EXEC Account_Add @Profile_id = '"+profile_id+"'"+" , @URL = '"+URL+"'"+" , @Website_app_name = '"+website_app_name+"'"+" , @Username = '"+username+"'"+" , @Password ='"+password+"';"

        response = query_handler.exec_query_with_message(add_account_query)
        response = json.loads(response)[0]
        return func.HttpResponse(
            json.dumps(response) ,
            mimetype="application/json"
        )
    else:

        return func.HttpResponse(
            "There is a missing parameter in your request",
            status_code=200
        )






# add_account?profile_id=1&website_app_name=twitter.com&username=yousse123&password=fehf43fh43f