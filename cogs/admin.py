import requests
import json
import discord
from discord.ext import commands
from config import ADMIN_TOKEN, GUILD_API, GUILD_ID, SELF_ID, ROLE_ID

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

async def setup(bot):
    await bot.add_cog(Admin(bot))
