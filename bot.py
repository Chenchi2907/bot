import discord
from discord.ext import commands

#try add this 
intents=intents=discord.Intents.all()

#if the above don't work, try with this
#intents = discord.Intents()
#intents.members = True

TOKEN = 'MTAwODk0NzUzMzIzNTYxNzk0Mw.GXFDvr.QgxlA5sxpGPzMUpcrInJoqHuXXIR5QIJgLjBo0'
bot=commands.Bot(command_prefix='!',intents=intents)

#Events

@bot.event
async def  on_member_join(member):
    channel=bot.get_channel(1034052336596824176)
    await channel.send(f'{member} join!' )



@bot.event
async def  on_member_remove(member):
    channel=bot.get_channel(1034052502431219712)
    await channel.send(f'{member} left!' )
  
@bot.command()
async def test(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')
bot.run(TOKEN)