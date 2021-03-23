from configparser import ConfigParser
import os
from pathlib import Path
import logging


def get_credentials(section_name, mm_config_file_name=None):
    """get_credentials for Mattermost credentilas"""
    config = ConfigParser()

    if db_config_file_name is None:
        db_config_file_name = ".mm_service.conf"

    # Note: ${HOME}/.mm_service.conf
    cred_file = Path("{}/{}".format(os.environ.get('HOME'), mm_config_file_name))
    assert os.path.isfile(cred_file), "error can't read MM credentials file ... {}".format(cred_file)
    config.read(cred_file)

    uid = config.get(section_name, 'uid')
    token = config.get(section_name, 'token')

    logging.info("Reading MM credentials from: {}, using section: {}".format(cred_file, section_name))

    return uid, token
