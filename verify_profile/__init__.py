import logging
import azure.functions as func
import pyodbc
import time
import os
import json
import textwrap
from configparser import ConfigParser


import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import query_handler

def main(req: func.HttpRequest) -> func.HttpResponse:

    profile_id = req.params.get('profile_id')
    code = req.params.get('code')

    if not code:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            code = req_body.get('code')
    if not profile_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            profile_id = req_body.get('profile_id')

   
    if code and profile_id: 
        verify_profile_query = "EXEC Profile_Verify "+"@Profile_id='"+profile_id+"'"+" , @Verification_Code='"+code+"';"
        response = query_handler.exec_query_with_message(verify_profile_query)
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




