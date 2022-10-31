from typing_extensions import Self
import discord
from discord.ext import commands





#try add this 
intents=discord.Intents.all()


#if the above don't work, try with this
#intents = discord.Intents()
#intents.members = True


bot=commands.Bot(command_prefix='!',intents=intents,help_command=None)
@bot.event
async def on_ready():
    print("Bot is Ready")

@bot.command(name="help")
async def help(ctx):
    embed=discord.Embed(
        title='help',
        description="Help for you",
        color=discord.color.red()
    
    
    )
    await ctx.send(embed=embed)
    








bot.run('MTAwODk0NzUzMzIzNTYxNzk0Mw.GGwVdq.Aj53FsyS3keF6Db43QaISpm9yV7pjhaBW7khR4')





