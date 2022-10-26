import discord
from discord.ext import commands

#try add this 
intents=intents=discord.Intents.all()

#if the above don't work, try with this
#intents = discord.Intents()
#intents.members = True

TOKEN = 'MTAwODk0NzUzMzIzNTYxNzk0Mw.Ghqvn_.SpsJjZYHBkRCHUEtJ3YvfG3-EdaB6FB_8DUY2U'
bot=commands.Bot(command_prefix='!',intents=intents)

#Events
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')

@bot.event
async def  on_member_join(member):
    channel=bot.get_channel(1034052336596824176)
    await channel.send(f'{member} join!' )



@bot.event
async def  on_member_remove(member):
    channel=bot.get_channel(1034052502431219712)
    await channel.send(f'{member} left!' )
bot.run(TOKEN)