import aiohttp
import asyncio
import json
import discord
from discord.ext import commands
from selfbot import API_URL

with open('config.json', 'r') as file:
    config = json.load(file)
TOKEN = config.get('token')

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
                tasks.append(asyncio.create_task(self.spam_msg(session, TOKEN, message, channel_id)))
        
            await asyncio.gather(*tasks)

    async def spam_msg(self, session, TOKEN, message, channel_id):
        headers = {
            'Authorization': TOKEN,
            'Content-Type': 'application/json'
        }

        spam_response = await session.post(f'{API_URL}{channel_id}/messages',
                                        headers=headers,
                                        json={'content': message})

    @commands.command(brief='// <user_id> <amount> <message>')
    async def spamdm(self, ctx, user_id:int, times:int,*, message:str):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(times):
                tasks.append(asyncio.create_task(self.spamdm_msg(session, TOKEN, user_id, message)))

            await asyncio.gather(*tasks)

    async def spamdm_msg(self, session, TOKEN, user_id, message):
        headers = {
                    'Authorization': TOKEN,
                    'Content-Type': 'application/json'
        }
        dm_channel = await session.post('https://discord.com/api/v10/users/@me/channels',
                                        headers=headers,
                                        json={'recipient_id': user_id})
        if dm_channel.status == 200:
            dm_channel_id = (await dm_channel.json())['id']
            dm_response = await session.post(f'{API_URL}{dm_channel_id}/messages',
                                        headers=headers,
                                        json={'content': message})

    @commands.command(brief='// <channel_id> <amount> <message>')
    async def raid(self, ctx, channel_id: int,  times: int, *, message: str):
        async with aiohttp.ClientSession() as session:
            with open('raiders.txt', 'r') as file:
                tokens = file.read().splitlines()

            tasks = []
            for token in tokens:
                for i in range(times):
                    tasks.append(asyncio.create_task(self.rmsg(session, token, channel_id, message)))

            await asyncio.gather(*tasks)

    async def rmsg(self, session, token, channel_id, message):
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        await session.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', headers=headers, json={'content': message})


async def setup(bot):
    await bot.add_cog(Messages(bot))
