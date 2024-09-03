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
 
async def main():
    try:
        async with bot:
            banner()
            await load_ext()
            await bot.start(TOKEN)
    except asyncio.CancelledError:
        print(f'\nxorcord closed')
        pass

if __name__ == '__main__':
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
            TOKEN = config.get('token')
    except FileNotFoundError:
        print('no config found')
        config = {
                'token': input('discord token: '),
                'callback_channel': input('private discord channel id: ')
                }
        with open('config.json', 'w') as file:
            json.dump(config, file, indent=4)
            TOKEN = config.get('token')
    asyncio.run(main())
