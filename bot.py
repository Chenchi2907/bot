
import discord
from discord.ext import commands
import os
from main import Main
intents=discord.Intents.all()
intents.members=True
from datetime import datetime
import time
from meme import Main_second
from music import music_cog
#try add this 
#if the above don't work, try with this
#intents = discord.Intents()

bot=commands.Bot(command_prefix='!',intents=intents,help_command=None)
@bot.command(name='help')
async def help(ctx):
    embed=discord.Embed(
        title='Help',
        description='Help for you',
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("Bot is online")
    await bot.add_cog(Main(bot))
    await bot.add_cog(Main_second(bot))
    await bot.add_cog(music_cog(bot))

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(1034052336596824176)
    em=discord.Embed(
        title=f'Welcom',
        color=discord.Color.random(),
        timestamp=datetime.utcnow()
        ).add_field(
        name=f'<1035844076228059136> Rules',
        value=f'<#1042775868382134292>'
        ).add_field(
        name=f'<1035844076228059136> Chat',
        value='<#1042776334931345489>'
        ).add_field(
        name=f'Total members',
        value=f'{member.guild.member_count}'
        ).set_footer(text=f'{member.name} just joined')
    await channel.send(embed=em)



async def on_member_remove(member):
    channel=bot.get_channel(1034052502431219712)
    await channel.send(f'{member} left!')



bot.run('MTAwODk0NzUzMzIzNTYxNzk0Mw.GF66rN.nXgKxEbI9H0KjUItQHZH7qBOVLjthPTPCYpWzU')





