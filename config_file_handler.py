import logging
from configparser import ConfigParser
import os
def read_config_file(directory , file_name , section , requested_params):
    config_parser = ConfigParser()
    config_file = os.path.join(directory, file_name)
    config_parser.read(config_file)

    data = []
    for param in requested_params:
        data.append(config_parser.get(section,param).replace("'",""))

    logging.info('Read credentials')
    return data