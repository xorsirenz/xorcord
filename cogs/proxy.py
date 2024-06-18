import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

#url = 'https://free-proxy-list.net/'
url = 'https://ipecho.net/plain'
class Proxy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='// no argument needed')
    async def getproxies(self, ctx):
        r = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('tbody')

        proxies = []
        with open('proxy_list.txt', 'w') as f:
            for row in table:
                if row.find_all('td')[4].text == 'elite proxy':
                    proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
                    proxies.append(proxy)
                else:
                    pass

            for proxy in proxies:
                try:
                    proxy_list = requests.get(
                            url, proxies={"http": proxy, "https": proxy}, timeout=1)
                    f.write(f'{proxy_list}')
                    print(proxy_list)
                except OSError as e:
                    print(e)
                    #await ctx.message.edit(f'{len(proxies)} new proxies were added')
                    #return proxies
            print('finished checking proxies')

async def setup(bot):
    await bot.add_cog(Proxy(bot))
