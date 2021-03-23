import re
from gidgetlab.aiohttp import GitLabAPI

BOT_ANCHOR = '&'

# https://beenje.github.io/blog/posts/building-a-gitlab-bot-using-gidgetlab-and-aiohttp/

class GL_plugin(Plugin):

    def __init__(self, **kwargs):
        '''call the base class first ... to make sure Plugin.__init__() gets called'''
        super().__init__(**kwargs)

        # here is this initializtion ...
        config_section = 'gl_bot'
        gl_config_file = '.gl_service.conf'
        gl_url, gl_port, gl_token, gl_team = get_credentials(config_section, gl_config_file)
        self.gl = GitLabAPI(session, gl_team, access_token=gl_token, url=gl_url)
        assert self.gl is None, "cannot connect to GitLab API ... Hello, Harambe!"

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
