import discord
from discord.ext import commands
import aiohttp
import json
from selfbot import API_URL

class Callback(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        await self.bot.process_commands(message)
        words = [f'{self.bot.user.id}',
                 'xorsirenz',
                 'xorcord'
                 ]
        content = message.content.lower()
        with open('config.json', 'r') as file:
            config = json.load(file)
        token = config.get('token') 
        callback_channel = config.get('callback_channel')
        for word in words:
            if word in content:
                payload = { 'content' : f"```{message.guild} {message.channel}\n{message.author}/{message.author.id}\n\n{content}```" }
                headers = { 'authorization': token }
                channel_id = callback_channel

                async with aiohttp.ClientSession() as session: 
                    r = await session.post(f"{API_URL}/channels/{channel_id}/messages",
                    data=payload, headers=headers, ssl=False)
                    print(f'\nNEW MENTION\n{message.guild} {message.channel}\n{message.author}/{message.author.id}\n{content}')
                    #await message.channel.send(f"hi")


async def setup(bot):
    await bot.add_cog(Callback(bot))
