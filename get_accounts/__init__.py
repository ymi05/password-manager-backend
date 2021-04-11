import logging
import azure.functions as func
import pyodbc
import time
import os
import json
import textwrap
from configparser import ConfigParser
# from sms_sender import SMS_Client
# NOTE: UNCOMMENT THIS WHEN DONE
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import query_handler

def main(req: func.HttpRequest) -> func.HttpResponse:

    profile_id = req.params.get('profile_id')

    if not profile_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            profile_id = req_body.get('profile_id')
   
    if profile_id : 
        get_accounts_query = "EXEC Accounts_Get "+"@Profile_id='"+profile_id+"';"
        response = query_handler.exec_query_with_records(get_accounts_query)
        data = {}
        data["accounts"] = []
        for record in response:
            account = {}
         
            
            account["accoutn_id"] = record[0]
            account["URL"] = record[1]
            account["website_app_name"] = record[2]
            account["username"] = record[3]
            account["password"] = record[4]

            data["accounts"].append(account)

        return func.HttpResponse(
            json.dumps(data) ,
            mimetype="application/json"
            )
    else:
        # TODO: turn this into a json response
        return func.HttpResponse(
            "There is a missing parameter in your request",
            status_code=200
        )




