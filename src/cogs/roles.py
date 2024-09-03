import requests
import json
import discord
from discord.ext import commands
from selfbot import API_URL

with open('config.json', 'r') as file:
    config = json.load(file)
    if 'admin_token' in config:
        ADMIN_TOKEN = config.get('admin_token')
    else:
        answer = input('setup admin server yes or no? > ')
        if answer.lower() == 'no':
            pass
        else:
            admin_config = {
                'admin_token': input('enter guild user admin token: '),
            }
            ADMIN_TOKEN = admin_config.get('admin_token')
            config.update(admin_config)
            with open('config.json', 'w') as file:
                json.dump(config, file, indent=4)

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='// <role_id>', help='removes role')
    async def rmrole(self, ctx, role:str):
        try:
            headers = {'authorization': ADMIN_TOKEN}
            guild_id = ctx.guild.id
            self_id = self.bot.user.id
            role_id = str(role)
            r = requests.delete(f'{API_URL}/guilds/{guild_id}/members/{self_id}/roles/{role_id}', headers=headers)
        except Exception as e:
            print(f'Error: {e}')

    @commands.command(brief='// <role_id>', help='gives admin role (needs server admin token)')
    async def admin(self, ctx, role:str):
        try:
            headers = {'authorization': ADMIN_TOKEN}
            guild_id = ctx.guild.id
            self_id = self.bot.user.id
            role_id = str(role)
            r = requests.put(f'{API_URL}/guilds/{guild_id}/members/{self_id}/roles/{role_id}', headers=headers)
        except Exception as e:
            print(f'Error: {e}')


async def setup(bot):
    await bot.add_cog(Roles(bot))
