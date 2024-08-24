from urllib import parse
#bot.py & webserver.py
API_URL = 'https://discord.com/api/v10/'
CLIENT_ID = "<BOT_ID>"
BOT_TOKEN = "<BOT_TOKEN>"
CLIENT_SECRET = "<CLIENT_SECRET>"
REDIRECT_URI = "<http://localhost:5000/oauth/callback>"
OAUTH_URL = f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri{parse.quote(REDIRECT_URI)}&scope=identify+email+connections+guilds.join+guilds+messages.read"
