import discord
from discord.ext import commands
import json
with open('setting.json',mode='r',encoding="utf-8") as jfile:
    jdata=json.load(jfile)
#try add this 
intents=intents=discord.Intents.all()

#if the above don't work, try with this
#intents = discord.Intents()
#intents.members = True

TOKEN = 'MTAwODk0NzUzMzIzNTYxNzk0Mw.GWyHXz.3GcrNdobFdZYCUBm_5xfwdZhBA6HXNyDZKfD7o'
bot=commands.Bot(command_prefix='!',intents=intents)

#Events

@bot.event
async def  on_member_join(member):
    channel=bot.get_channel(int(jdata['Welcom_channal']))
    await channel.send(f'{member} join!' )



@bot.event
async def  on_member_remove(member):
    channel=bot.get_channel(int(jdata['leave_channal']))
    await channel.send(f'{member} left!' )
  
@bot.command()
async def test(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')
bot.run(jdata["TOKEN"])