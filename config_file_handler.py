import logging
from configparser import ConfigParser
import os
def read_config_file(directory , file_name):
    config_parser = ConfigParser()
    config_file = os.path.join(directory, file_name)
    config_parser.read(config_file)

    database_server = config_parser.get("server.credentials","server").replace("'","")
    database_name = config_parser.get("server.credentials" , "database" ).replace("'","")
    database_username = config_parser.get("server.credentials" , "username" ).replace("'","")
    database_password = config_parser.get("server.credentials" , "password" ).replace("'","")
    logging.info('Read credentials')

    return database_server , database_name , database_username , database_password