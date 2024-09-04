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


async def setup(bot):
    await bot.add_cog(Admin(bot))
