import discord
from discord.ext import commands

class Log(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # add user ID you wish to log inside the backets [] 
        users = []
        for user in users:
            if message.author.id == user:
                content = message.content.lower()
                payload = f"{message.guild} {message.channel}\n{message.author}/{message.author.id}\n{content}\n\n"
                with open(f'{message.author}.txt', 'a') as file:
                    file.write(payload)
                    file.close()
                    return

async def setup(bot):
    await bot.add_cog(Log(bot))
