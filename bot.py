import discord
from discord import app_commands
from discord.ext import commands
from config import BOT_TOKEN
from utils import get_current_user

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("bots ready")

@bot.command()
async def login(ctx: commands.Context):
    await ctx.send('[oabot/auth](http://localhost:5000)')

bot.run(BOT_TOKEN)
