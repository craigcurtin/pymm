import re
import logging

from mmpy_bot.plugins.base import Plugin, listen_to
from mmpy_bot.scheduler import schedule
from mmpy_bot.wrappers import Message

class Pharm_plugin(Plugin):
    """Pharm plugin bot listens on channel and does things for some folks"""

    @listen_to("wake up")
    async def wake_up(self, message: Message):
        logging.debug(message)
        self.driver.reply_to(message, "I'm awake!")

    @listen_to('hi', re.IGNORECASE)
    async def hi(self, message):
        logging.debug(message)
        message.reply('I can understand hi or HI!')

    @listen_to('give me (.*)', re.IGNORECASE)
    async def give_me(self, message, something):
        logging.debug(message)
        self.driver.reply_to(message, 'Here is %s' % something)

    @listen_to('env status (.*)', re.IGNORECASE)
    async def env_status(self, message, something):
        logging.debug(message)
        self.driver.reply_to(message, 'Here is %s' % something)
