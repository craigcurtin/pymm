#!/usr/bin/env python

from mmpy_bot import Bot, Settings
from my_plugin import MyPlugin


if __name__ == '__main__':
	bot = Bot(
	    settings=Settings(
	        MATTERMOST_URL = "http://chat.example.com",
	        MATTERMOST_PORT = 443,
	        BOT_TOKEN = "a69155mvlsobcnqpfdceqihaa",
	        BOT_TEAM = "test",
	        SSL_VERIFY = True,
	    ),  # Either specify your settings here or as environment variables.
	    plugins=[MyPlugin()],  # Add your own plugins here.
	)
	bot.run()
