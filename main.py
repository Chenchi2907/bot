import discord
from discord.ext import commands
from discord import activity

class Main(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game('im online'))
        print('is online')
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

    