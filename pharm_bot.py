#!/usr/bin/env python

from mmpy_bot import Bot, Settings
from my_plugin import MyPlugin
import logging
from ps_utils import get_credentials
from Pharm_plugin import Pharm_plugin
from GL_plugin import GL_plugin

if __name__ == '__main__':
    app_name = 'Pharm_bot'
    log_directory = '/var/log/{}'.format(app_name)
    log_level = logging.DEBUG

    setup_logger(app_name, log_directory, log_level)
    config_section = 'pharm_bot'
    try:
        url, port, token, team = get_credentials(config_section)
        bot = Bot(
            settings=Settings(MATTERMOST_URL=url,
                              MATTERMOST_PORT=port,
                              BOT_TOKEN=token,
                              BOT_TEAM=team,
                              SSL_VERIFY=True,
                              ),  # Either specify your settings here or as environment variables.
            plugins=[Pharm_plugin(),
                     GL_plugin()],  # Add your own plugins here.
        )
        bot.run()
    except (Exception, EOFError) as ex:
        logging.exception("uh, oh .... we got an exception!!")
        raise SystemExit(-1)
