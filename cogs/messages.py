import aiohttp
import asyncio
import discord
from discord.ext import commands
from config import TOKEN

token = TOKEN
api_url = 'https://discord.com/api/v9/channels/'


class Messages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def self_check(self, check):
        return check.ctx.author == self.bot.user

    @commands.command(brief='// <amount>')
    async def purge(self, ctx, amount=100):
        if amount < 100:
            await ctx.channel.purge(limit=amount, check=lambda message: message.author == ctx.author)
            return
        await ctx.message.edit(f'failed. 100 messages max.')

    @commands.command(brief='// <amount>')
    async def purgeall(self, ctx, amount:int):
        if amount < 100:
            await ctx.channel.purge(limit=amount)
            return
        await ctx.message.edit(f'failed. 100 messages max.')


async def setup(bot):
    await bot.add_cog(Messages(bot))
