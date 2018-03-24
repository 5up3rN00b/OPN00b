import discord
from discord.voice_client import VoiceClient
from discord.ext import commands

bot = commands.Bot("-")
startup_extensions = ['Music']

class Main_Commands():
    def __init__(self,bot):
        self.bot = bot

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='music is on!'))
    
@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{}:{}".format(type(e),__name__,e)
            print('Failed to load extension {}\n{}'.format(extension,exc))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")

##async def rps(ctx,arg):
##    await ctx.send(arg)
##
##async def flip(ctx,arg):
##    await ctx.send(arg)
##
##async def cool(ctx,arg):
##    await ctx.send(arg)
##
##async def say(ctx,arg):
##    await ctx.send(arg)
##
##async def start(ctx,arg):
##    await ctx.send(arg)
    


bot.run('NDA2Mjc1NzUyMTQ1ODQ2Mjgx.DYjhkA.6817KgHHb12WpczAOXXTtuukcZE')
