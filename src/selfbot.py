#!/usr/bin/env python3
import os
import aiohttp
import asyncio
import json
import logging
import sys
import discord
from discord.ext import commands

API_URL = 'https://discord.com/api/v10/'
bot = commands.Bot(command_prefix='-', self_bot=True)
logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

@bot.event
async def on_ready():
    print(f'logged in as: {bot.user.name}\ndiscord id: {bot.user.id}')

@bot.command(brief='// <extension>')
async def load(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    print(f'loaded extension: {extension}')

@bot.command(brief='// <extension>')
async def reload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await bot.load_extension(f'cogs.{extension}')
    await ctx.message.delete()
    print(f'reloaded extension: {extension}')

@bot.command(brief='// <extension>')
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    print(f'unloaded extension: {extension}')

async def load_ext():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')
            print(f'loaded extension {file}')

def banner():
    os.system('clear')
    print(f"                                                           ")
    print(f" ██   ██  ██████  ██████   ██████  ██████  ██████  ██████  ")
    print(f"  ██ ██  ██    ██ ██   ██ ██      ██    ██ ██   ██ ██   ██ ")
    print(f"   ███   ██    ██ ██████  ██      ██    ██ ██████  ██   ██ ")
    print(f"  ██ ██  ██    ██ ██   ██ ██      ██    ██ ██   ██ ██   ██ ")
    print(f" ██   ██  ██████  ██   ██  ██████  ██████  ██   ██ ██████  ")                                                      
    print(f"                     Github[xorsirenz]         ((self)bot) ")
    print(f"                                                           ")

def get_token():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        print('no config found')
        config = {
                'token': input('discord token: '),
                'listener_channel_id': input('enter discord channel id for listener: ')
                }
        with open('config.json', 'w') as file:
            json.dump(config, file, indent=4)
    finally:
            token = config.get('token')
            return token

async def main():
    try:
        async with bot:
            token = get_token()
            banner()
            await load_ext()
            await bot.start(token)
    except asyncio.CancelledError:
        print(f'\nxorcord closed')
        pass

if __name__ == '__main__':
    asyncio.run(main())
