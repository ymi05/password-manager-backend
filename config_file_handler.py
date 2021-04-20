import logging
from configparser import ConfigParser
import os
def read_config_file(directory , file_name , section , requested_params):
    """[summary]
        Gets data from the config file based on the requested ones
    Args:
        directory (str): location of the file
        file_name (str): file name
        section (str): which part of the config file we want
        requested_params (array): contains the values we want from the file

    Returns:
        Values of the variables for the selected section
    """    
    config_parser = ConfigParser()
    config_file = os.path.join(directory, file_name)
    config_parser.read(config_file)

    data = []
    for param in requested_params:
        data.append(config_parser.get(section,param).replace("'","")) # when getting data from a config file, they come with extra quotations

    logging.info('Read credentials')
    return data