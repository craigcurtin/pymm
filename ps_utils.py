from configparser import ConfigParser
import os
from pathlib import Path
import logging


def get_credentials(section_name, mm_config_file_name=None):
    """url, port, token, team = get_credentials(section_name)"""
    config = ConfigParser()

    if db_config_file_name is None:
        db_config_file_name = ".mm_service.conf"

    # Note: ${HOME}/.mm_service.conf
    cred_file = Path("{}/{}".format(os.environ.get('HOME'), mm_config_file_name))
    assert os.path.isfile(cred_file), "error can't read MM credentials file ... {}".format(cred_file)
    config.read(cred_file)

    url = config.get(section_name, 'url')
    port = config.get(section_name, 'port')
    token = config.get(section_name, 'token')
    team = config.get(section_name, 'team')

    logging.info("Reading MM credentials from: {}, using section: {}".format(cred_file, section_name))

    return url, port, token, team
