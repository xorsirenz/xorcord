import discord
from discord.ext import commands
import aiohttp
import csv

class Info(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief='// no arguemnt needed', help='sends link for oauth')
    async def login(self, ctx: commands.Context):
        await ctx.message.edit('[oabot/auth](http://localhost:5000)')

    @commands.command(brief='// <@username> or <user_id>', help='gives detail about user')
    async def user(self, ctx, user:discord.User):
        avatar = user.avatar
        user_id = user.id
        username = user.name
        display = user.display_name
        created_at = user.created_at.strftime("%d-%m-%Y %H:%M:%S")
        user_bot = user.bot

        response = f'[avatar]({avatar})```user id: {user_id}\ndisplay name: {display}\nusername: {username}\naccount created: {created_at}\nBot:{user_bot}```'
        await ctx.message.edit(response)

    @commands.command(brief='// no argument needed', help='gives detail of server you are in')
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

    @commands.command(brief='// no argument needed', help='save list of members in server to csv file')
    async def members(self, ctx):
        name = ctx.guild.name
        channels = await ctx.guild.fetch_channels()
        text_channels: list[discord.TextChannel] = [channel for channel in channels if isinstance(channel, discord.TextChannel)]
        members = await ctx.guild.fetch_members(channels=text_channels, cache=True, force_scraping=True, delay=0.1)
 
        with open(f'{name}_users.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(members) 
            print(f'list of members have been saved to {name}_users.csv')


async def setup(bot):
    await bot.add_cog(Info(bot))
