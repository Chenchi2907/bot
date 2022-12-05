import discord
from discord.ext import commands
from discord import activity
import urllib.request as req
import json

import random
import urllib.request as req
url='https://memes.tw/wtf/api'
request=req.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
with req.urlopen(request) as re:
    data=json.load(re)
    
 
class Main_second(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def meme(self,ctx):
       
        memeData=data
        meme=random.choice(memeData)
        memeurl=meme["src"]

        memename=meme["title"]
        memeposter=meme['author']["name"]
        memesrc=meme["url"]
       
        embed=discord.Embed(title=memename,colour=discord.Color.blue())
        embed.set_image(url=memeurl)
        embed.set_footer(text=f'Meme by: {memeposter} | Post {memesrc}')

        await ctx.send(embed=embed)
        
    