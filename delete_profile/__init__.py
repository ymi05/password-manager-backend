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


    if not profile_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            profile_id = req_body.get('profile_id')

   

    response = {"message":"There is a missing parameter in your request"}
    if profile_id: 
        delete_profile_query = "EXEC Profile_Delete "+"@Profile_id ='"+profile_id+"';"
        response = query_handler.exec_query_with_message(delete_profile_query)
        response = json.loads(response)[0]


        
    return func.HttpResponse(
        json.dumps(response) ,
        mimetype="application/json"
    )
