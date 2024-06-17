import discord
from discord.ext import commands
import aiohttp
from config import API_URL

api_url = API_URL

class Info(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='// <@username> or <user_id>')
    async def user(self, ctx, user:discord.User):
        user_id = user.id
        username = user.name
        created_at = user.created_at.strftime("%d-%m-%Y %H:%M:%S")
        user_bot = user.bot
        response = f'```user id: {user_id}\nusername: {username}\naccount created: {created_at}\nBot:{user_bot}```'
        await ctx.message.edit(response)

    @commands.command(brief='// no argument needed')
    async def server(self, ctx):
        name = ctx.guild.name
        guild_id = ctx.guild.id
        created = ctx.guild.created_at.strftime("%d-%m-%Y %H:%M:%S")
        online_count = ctx.guild.online_count
        member_count = ctx.guild.member_count
        mfa = ctx.guild.mfa_level
        owner = ctx.guild.owner
        owner_id = ctx.guild.owner_id
        response = f'```server: {name}\nserver id: {guild_id}\ncreated: {created}\nmembers: {online_count}/{member_count}\nmfa level: {mfa}\n\nowner: {owner}\nowner id: {owner_id}```'
        await ctx.message.edit(response)


async def setup(bot):
    await bot.add_cog(Info(bot))
