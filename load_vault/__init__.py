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
from profile_is_verified import profile_is_verified
import query_handler

def main(req: func.HttpRequest) -> func.HttpResponse:

    profile_id = str(req.params.get('profile_id'))
    vault_id = str(req.params.get('vault_id'))
    encrypted_vault = req.params.get('encrypted_vault')

    if not profile_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            profile_id = req_body.get('profile_id')

    if not encrypted_vault:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            encrypted_vault = req_body.get('encrypted_vault')
   

    respone = {"message":"There is a missing parameter in your request"}
    if not encrypted_vault:
        encrypted_vault = ""
    if profile_id: 
        response = {'message':"Please verify your account"}
        if profile_is_verified(profile_id):
  

            load_vault_query = "EXEC Vault_load @Profile_id = '"+profile_id+"', @Encrypted_Vault = '"+encrypted_vault+ "';"

            response = query_handler.exec_query_with_message(load_vault_query)
            response = json.loads(response)[0]

    return func.HttpResponse(
        json.dumps(response) ,
        mimetype="application/json"
    )

