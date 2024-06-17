import os
import aiohttp
import asyncio
import logging
import sys
import discord
from discord.ext import commands
from config import TOKEN
from utils import get_current_user

bot = commands.Bot(command_prefix="-", self_bot=True)
logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
token = TOKEN

@bot.event
async def on_ready():
    print(f'lessgo', {bot.user.name}, {bot.user.id})

@bot.command(brief='// no arguemnt needed')
async def login(ctx: commands.Context):
    await ctx.message.edit('[oabot/auth](http://localhost:5000)')

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
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')
            print(f"loaded extension {file}")

async def main():
    async with bot:
        await load_ext()
        await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
