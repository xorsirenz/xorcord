import os
import aiohttp
import asyncio
import logging
import sys
import discord
from discord.ext import commands
from config import TOKEN

bot = commands.Bot(command_prefix="-", self_bot=True)
token = TOKEN
api_url = 'https://discord.com/api/v9/channels/'

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

@bot.event
async def on_ready():
    print(f'lessgo', {bot.user.name}, {bot.user.id})

@bot.command(brief='// <amount> <message>')
async def spam(ctx, times:int, *, message:str):
    channel_id = ctx.channel.id

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(times):
            tasks.append(asyncio.create_task(spamuwu(session, token, message, channel_id)))
        
        await asyncio.gather(*tasks)

async def spamuwu(session, token, message, channel_id):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    spam_response = await session.post(f'{api_url}{channel_id}/messages',
                        headers=headers,
                        json={'content': message})

@bot.command(brief='// <amount> <user_id> <message>')
async def spamdm(ctx, times:int, user_id:int, *, message:str):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(times):
            tasks.append(asyncio.create_task(spamdmuwu(session, token, user_id, message)))

        await asyncio.gather(*tasks)

async def spamdmuwu(session, token, user_id, message):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    dm_channel = await session.post('https://discord.com/api/v9/users/@me/channels',
                                    headers=headers,
                                    json={'recipient_id': user_id})
    if dm_channel.status == 200:
        dm_channel_id = (await dm_channel.json())['id']
        dm_response = await session.post(f'{api_url}{dm_channel_id}/messages',
                                        headers=headers,
                                        json={'content': message})


@bot.command(brief='// <extension>')
async def load(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    print(f"loaded extension {extension}")

@bot.command(brief='// <extension>')
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    print(f"unloaded extension {extension}")

@bot.command(brief='// <extension>')
async def reload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await bot.load_extension(f'cogs.{extension}')
    print(f"reloaded extension {extension}")

async def load_ext():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')
            print(f"loaded extension {file}")

async def main():
    async with bot:
        await load_ext()
        await bot.start(TOKEN)


asyncio.run(main())

