import pyodbc
import json
import os
import logging
from config_file_handler import read_config_file
import traceback
class Db_Connection:
  
    def __init__(self  , config_file_path = os.path.dirname(__file__) , config_file = "config.ini" ):
        """[summary]
            Class that establishes a connection with the SQL database
        Args:
            config_file_path (str, optional): Location of the config file. Defaults to os.path.dirname(__file__).
            config_file (str, optional): File name. Defaults to "config.ini".
        """       
        self.connection_string = None
        self.config_file = config_file
        self.config_file_path = config_file_path
        self.set_connection_string()
        self.conn = None
        try:
            self.conn = pyodbc.connect(self.connection_string) 
            logging.info("Connection established")
            print("Connection established")
        except:
            logging.info("Unable to set up conneciton")
            
            self.__exit__()
        
      
    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        self.conn.close()

    def set_connection_string(self):
        database_server , database_name , database_username , database_password = read_config_file(self.config_file_path , self.config_file , "server.credentials" , ["server" , "database" , "username" , "password"])
        driver= '{ODBC Driver 17 for SQL Server}'  
        self.connection_string = 'DRIVER='+driver+';SERVER='+database_server+';PORT=1433;DATABASE='+database_name+';UID='+database_username+';PWD='+database_password+';ENCYRPT=yes;TrustServerCertificate=no;Connection Timeout=30;'
