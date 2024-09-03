import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief='// <@username> or <user_id>', help='kicks user from server')
    async def kick(self, ctx, user:discord.User):
        await ctx.guild.kick(user)

    @commands.command(brief='// <@username> or <user_id>', help='kicks user from server')
    async def ban(self, ctx, user:discord.User):
        await ctx.guild.ban(user)


async def setup(bot):
    await bot.add_cog(Admin(bot))
