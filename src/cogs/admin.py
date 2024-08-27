import requests
import json
import discord
from discord.ext import commands

GUILD_API = 'https://discord.com/api/v9/guilds/'

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='// no argument needed')
    async def admin(self, ctx: commands.Context):
        headers = {
            'authorization': ADMIN_TOKEN
        }

        try:
            r = requests.put(f"{GUILD_API}/{GUILD_ID}/members/{SELF_ID}/roles/{ROLE_ID}", headers=headers)
            print(r)
        except Exception as e:
            print(f"Error: {e}")

    @commands.command(brief='// no argument needed')
    async def rmadmin(self, ctx: commands.Context):
        headers = {
            'authorization': ADMIN_TOKEN
        }

        try:
            r = requests.delete(f"{GUILD_API}/{GUILD_ID}/members/{SELF_ID}/roles/{ROLE_ID}", headers=headers)
            print(r)
        except Exception as e:
            print(f"Error:{e}")

try:
    with open('admin_config.json', 'r') as file:
        config = json.load(file)
        TOKEN = config.get('token')
except Exception:
    answer = input('setup admin server yes or no? > ')
    if answer.lower() == 'no':
        pass
    else:
        config = {
            'guild_id': input('enter guild id: '),
            'admin_token': input("enter guild user admin token: "),
            'self_id': input('enter your user id: '),
            'role_id': input('enter role id you want to use: ')
            }
        with open('admin_config.json', 'w') as file:
            json.dump(config, file, indent=4)
            GUILD_ID = config.get('guild_id')
            ADMIN_TOKEN = config.get('admin_token')
            SELF_ID = config.get('self_id')
            ROLE_ID = config.get('role_id')
finally:
    pass
    async def setup(bot):
        await bot.add_cog(Admin(bot))
