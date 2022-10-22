import discord
from discord.ext import commands 

bot=commands.Bot(command_prefix='aa')
@bot.event
async def on_ready():
    print('>>Bot is online<<')

@bot.event
async def  on_member_join(member):
    print(f'[member] join!')

@bot.event
async def  on_member_join(member):
    print(f'[member] leave!')

bot.run("MTAwODk0NzUzMzIzNTYxNzk0Mw.G614lM.Ort6ZAa1MNYAh7KdegRtgTnk7brZZI_oL8z1QU")
