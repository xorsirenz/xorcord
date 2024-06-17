import aiohttp
import asyncio
import discord
from discord.ext import commands
from config import TOKEN, API_URL

api_url = API_URL

class Messages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def self_check(self, check):
        return check.ctx.author == self.bot.user

    @commands.command(brief='// <amount>')
    async def purge(self, ctx, amount=100):
        if amount <= 100:
            await ctx.channel.purge(limit=amount, check=lambda message: message.author == ctx.author)
            return
        await ctx.message.edit(f'failed. 100 messages max.')

    @commands.command(brief='// <amount>')
    async def purgeall(self, ctx, amount:int):
        if amount <= 100:
            await ctx.channel.purge(limit=amount)
            return
        await ctx.message.edit(f'failed. 100 messages max.')

    @commands.command(brief='// <amount> <message>')
    async def spam(self, ctx, times:int, *, message:str):
        channel_id = ctx.channel.id

        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(times):
                tasks.append(asyncio.create_task(self.spamuwu(session, TOKEN, message, channel_id)))
        
            await asyncio.gather(*tasks)

    async def spamuwu(self, session, TOKEN, message, channel_id):
        headers = {
            'Authorization': TOKEN,
            'Content-Type': 'application/json'
        }

        spam_response = await session.post(f'{api_url}{channel_id}/messages',
                                        headers=headers,
                                        json={'content': message})

    @commands.command(brief='// <amount> <user_id> <message>')
    async def spamdm(self, ctx, times:int, user_id:int, *, message:str):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(times):
                tasks.append(asyncio.create_task(self.spamdmuwu(session, TOKEN, user_id, message)))

            await asyncio.gather(*tasks)

    async def spamdmuwu(self, session, TOKEN, user_id, message):
        headers = {
                    'Authorization': TOKEN,
                    'Content-Type': 'application/json'
        }
        dm_channel = await session.post('https://discord.com/api/v10/users/@me/channels',
                                        headers=headers,
                                        json={'recipient_id': user_id})
        if dm_channel.status == 200:
            dm_channel_id = (await dm_channel.json())['id']
            dm_response = await session.post(f'{api_url}{dm_channel_id}/messages',
                                        headers=headers,
                                        json={'content': message})


async def setup(bot):
    await bot.add_cog(Messages(bot))
