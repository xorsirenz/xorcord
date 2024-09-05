import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief='// <@username> or <user_id>', help='kicks user from server')
    async def kick(self, ctx, user:discord.User):
        await ctx.guild.kick(user)
        await ctx.message.delete()
        print(f'you kicked {user}')

    @commands.command(brief='// <@username> or <user_id>', help='bans user from server')
    async def ban(self, ctx, user:discord.User):
        await ctx.guild.ban(user)
        await ctx.message.delete()
        print(f'you banned {user}')

    @commands.command(brief='// <@username> or <user_id>', help='bans user from server')
    async def leave(self, ctx):
        await ctx.message.delete()
        await ctx.guild.leave()
        print(f'you left the server: {ctx.guild}')

async def setup(bot):
    await bot.add_cog(Admin(bot))
