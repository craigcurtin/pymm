#!/usr/bin/env python

from mmpy_bot import Bot, Settings
from my_plugin import MyPlugin

from ps_utils import get_credentials
from Pharm_plugin import Pharm_plugin
from GL_plugin import GL_plugin

if __name__ == '__main__':
    config_section = 'pharm_bot'
    mm_uid, mm_token = get_credentials(config_section)
    bot = Bot(
        settings=Settings(
            MATTERMOST_URL="https://chat.ssctech.com/technology",
            MATTERMOST_PORT=443,
            BOT_TOKEN=mm_token,
            BOT_TEAM=mm_uid,
            SSL_VERIFY=True,
        ),  # Either specify your settings here or as environment variables.
        plugins=[Pharm_plugin(),
				 GL_plugin()],  # Add your own plugins here.
    )
    bot.run()
