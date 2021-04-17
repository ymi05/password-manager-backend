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
from profile_is_verified import profile_is_verified
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
   

    response = {"message":"There is a missing parameter in your request"}
    if profile_id : 
        response = {"message": "Profile is not verified or does not exist"}
        if profile_is_verified(profile_id):
            get_accounts_query = "EXEC Accounts_Get "+"@Profile_id='"+profile_id+"';"
            response = query_handler.exec_query_with_records(get_accounts_query)

            data = {}
            data["messsage"] = "Profile found."
            data["accounts"] = []
            for record in response:
                account = {}
            
                account["account_id"] = record[0]
                account["website_app_name"] = record[1]
                account["username"] = record[2]
                account["password"] = record[3]

                data["accounts"].append(account)

            response = data
    return func.HttpResponse(
        json.dumps(response) ,
        mimetype="application/json"
    )




