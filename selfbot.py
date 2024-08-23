import os
import aiohttp
import asyncio
import logging
import sys
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-", self_bot=True)
logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

@bot.event
async def on_ready():
    print(f'logged in as: {bot.user.name}\ndiscord id: {bot.user.id}')

@bot.command(brief='// <extension>')
async def load(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    print(f"loaded extension: {extension}")

@bot.command(brief='// <extension>')
async def reload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await bot.load_extension(f'cogs.{extension}')
    print(f"reloaded extension: {extension}")

@bot.command(brief='// <extension>')
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    print(f"unloaded extension: {extension}")

async def load_ext():
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and file != 'admin.py':
            await bot.load_extension(f'cogs.{file[:-3]}')
            print(f"loaded extension {file}")

async def main():
    async with bot:
        await load_ext()
        await bot.start(TOKEN)


if __name__ == '__main__':
    try:
        with open('config.py', 'r') as file:
            file.close()
    except FileNotFoundError:
        print('no config file found')
        user_token = input('Enter discord token:\n > ')
        callback_channel = input('Enter private discord channel id:\n > ')
        with open('config.py', 'a') as file:
            file.write(f"from urllib import parse\nAPI_URL = 'https://discord.com/api/v10/channels/'\nTOKEN = '{user_token}'\nCALLBACK_CHANNEL = '{callback_channel}'")
            file.close()
        with open('raiders.txt', 'a') as f:
            f.write(user_token)
            f.close()
    finally:
        print('loading xorcord')      
        from config import TOKEN
        asyncio.run(main())
