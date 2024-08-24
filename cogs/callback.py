import discord
from discord.ext import commands
import aiohttp
from config import TOKEN, CALLBACK_CHANNEL, API_URL

api_url = API_URL


class Callback(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        await self.bot.process_commands(message)
        words = [f'{self.bot.user.id}', '<INSERT>', '<WORDS>', '<HERE>']
        content = message.content.lower()
        for word in words:
            if word in content:
                payload = { 'content' : f"```{message.guild} {message.channel}\n{message.author}/{message.author.id}\n\n{content}```" }
                headers = { 'authorization': TOKEN }
                callback_channel = CALLBACK_CHANNEL

                async with aiohttp.ClientSession() as session: 
                    r = await session.post(f"{api_url}{callback_channel}/messages", 
                    data=payload, headers=headers, ssl=False)
                    #await message.channel.send(f"hi")

async def setup(bot):
    await bot.add_cog(Callback(bot))
