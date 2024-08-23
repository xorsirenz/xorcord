from urllib import parse

API_URL = 'https://discord.com/api/v10/channels/'

#selfbot.py
TOKEN = '<SELFBOT_TOKEN>'
CALLBACK_CHANNEL = '<PRIVATE_CHANNEL_ID>'

#bot.py & webserver.py
CLIENT_ID = "<BOT_ID>"
BOT_TOKEN = "<BOT_TOKEN>"
CLIENT_SECRET = "<CLIENT_SECRET>"
REDIRECT_URI = "<http://localhost:5000/oauth/callback>"
OAUTH_URL = f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri{parse.quote(REDIRECT_URI)}&scope=identify+email+connections+guilds.join+guilds+messages.read"

#c2 server
ADMIN_TOKEN = '<ADMIN_TOKEN'
GUILD_API = 'https://discord.com/api/v9/guilds'
GUILD_ID = 'GUILD_ID'
SELF_ID = 'SELF_ID'
ROLE_ID = 'ROLE_ID'
