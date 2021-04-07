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

    name = req.params.get('name')
    email = req.params.get('email')
    phone_no = req.params.get("phone_no")
    password = req.params.get('password')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if not phone_no:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('phone_no')
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
            name = req_body.get('password')
   
    if name and phone_no and password: 
        add_profile_query = "EXEC Profile_Add "+"@Full_Name='"+name+"'"+" , @Email='"+email+"'"+" , @Password='"+password+"'"+" , @Phone_No='"+phone_no+"';"
        response = query_handler.exec_query_with_message(add_profile_query)

        return func.HttpResponse(response)
    else:

        return func.HttpResponse(
            "There is a missing parameter in your request",
            status_code=200
        )




