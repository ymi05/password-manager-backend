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

    profile_id = req.params.get('profile_id')
    account_id = req.params.get("account_id")

    if not profile_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            profile_id = req_body.get('profile_id')
    if not account_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            account_id = req_body.get('account_id')

    reponse = {'message' : "There is a missing parameter in your request"}
   
    if profile_id and account_id: 
        delete_account_query = "EXEC Account_Delete "+"@Profile_id='"+profile_id+"'"+" , @Account_id='"+account_id+"';"
        response = query_handler.exec_query_with_message(delete_account_query)
        response = json.loads(response)[0]

    return func.HttpResponse(
        json.dumps(response) ,
        mimetype="application/json"
    )



