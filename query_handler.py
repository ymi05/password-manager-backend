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
            message = json.dumps(cursor.fetchone()[0])
    return message

def exec_query_with_records(sql_query):
    records = None
    with db_connection.Db_Connection() as conn:
        logging.info("Connection established")
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            row = cursor.fetchone()
            data = []
            while row:
                data.append(row)
                row = cursor.fetchone()
            print(data)
    # return records

# exec_query_with_records("SELECT * FROM Profile WHERE name = 'Youssef'")