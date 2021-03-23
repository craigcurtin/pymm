import re

BOT_ANCHOR = '&'


class GL_plugin(Plugin):

    @listen_to("wake up", re.IGNORECASE)
    async def wake_up(self, message: Message):
        self.driver.reply_to(message, "I'm awake!")

    @listen_to('hi', re.IGNORECASE)
    async def hi(self, message):
        message.reply('I can understand hi or HI!')

    @listen_to('give me (.*)', re.IGNORECASE)
    async def give_me(self, message, something):
        self.driver.reply_to(message, 'Here is %s' % something)

    @listen_to('env status (.*)', re.IGNORECASE)
    async def env_status(self, message, something):
        self.driver.reply_to(message, 'Here is %s' % something)
