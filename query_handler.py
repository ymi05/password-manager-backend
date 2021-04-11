import logging
import json
import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
import db_connection

def exec_query_with_message(sql_query):
    message = None
    with db_connection.Db_Connection() as conn:
        logging.info("Connection established")
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            message = cursor.fetchone()[0]
            if message == None:
                return message

    return message

def exec_query_with_records(sql_query):
    records = []
    with db_connection.Db_Connection() as conn:
        logging.info("Connection established")
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            row = cursor.fetchone()
            while row:
                records.append(row)
                row = cursor.fetchone()

    return records

# profile_id = '1'
# URL = "3432432"
# website_app_name = "twttier"
# username = 'ruiewgru'
# password = 'sfdfsdf'
# query = "EXEC Account_Add "+"@Profile_id='"+profile_id+"'"+" , @URL='"+URL+"'"+" , @Website_app_name='"+website_app_name+"'"+" , @Username='"+username+"'"+" , @Password='"+password+"';"
# print(query)
# print(exec_query_with_message(query))
# profile_id = '2'
# query ="EXEC Accounts_Get "+"@Profile_id='"+profile_id+"';"
# print(exec_query_with_records(query))