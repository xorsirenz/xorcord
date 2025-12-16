import discord
from discord.ext import commands

class AtoH(commands.Cog):

    def __init__(self, bot):
        self.bot= bot

    @commands.command(brief='// text wish to be converted to hex', help='converts ascii to hex')
    async def atoh(self, ctx, message:str):
        hex_binary = message.encode(encoding='utf_8')
        hex_text = hex_binary.hex()
        await ctx.message.edit(hex_text)

async def setup(bot):
    await bot.add_cog(AtoH(bot))
