import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import random
import chalk
import pickle
import asyncio as asyncio
import os
from tinydb import TinyDB, Query
from os import path
import collections
from profanity import profanity

bot = commands.Bot("-")
db = TinyDB('db.json')
startup_extensions = ['Music']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='music is not on!'))

class Main_Commands():
    def __init__(self,bot):
        self.bot = bot

@bot.event
@asyncio.coroutine
def on_message(message):

    print('HI!')
    
    

@bot.event
async def on_message(message):
##    if not os.path.isfile("dict.pickle"):
##        pickle_out = open("dict.pickle","wb")
##        pickle.dump(test,pickle_out)
##        pickle_out.close()

    args = message.content.split(" ")
    if message.content.upper().startswith('-RPS'):
        choice = random.choice(['scissors','rock','paper'])
        if message.content.upper().endswith('SCISSORS'):
            await bot.send_message(message.channel, 'I chose ' + choice + '!')
            if choice == 'scissors':
                await bot.send_message(message.channel, 'This is a tie!')
            if choice == 'rock':
                await bot.send_message(message.channel, 'I have won! Muahaha!')
            if choice == 'paper':
                await bot.send_message(message.channel, 'You won!')
        elif message.content.upper().endswith('ROCK'):
            await bot.send_message(message.channel, 'I chose ' + choice + '!')
            if choice == 'scissors':
                await bot.send_message(message.channel, 'You won!')
            if choice == 'rock':
                await bot.send_message(message.channel, 'This is a tie!')
            if choice == 'paper':
                await bot.send_message(message.channel, 'I have won! Muahaha!')
        elif message.content.upper().endswith('PAPER'):
            await bot.send_message(message.channel, 'I chose ' + choice + '!')
            if choice == 'scissors':
                await bot.send_message(message.channel, 'I have won! Muahaha!')
            if choice == 'rock':
                await bot.send_message(message.channel, 'You won!')
            if choice == 'paper':
                await bot.send_message(message.channel, 'This is a tie!')
        else:
            await bot.send_message(message.channel,'My choice, ' + choice + ', beats your choice, ' + ' '.join(args[1:]) + '!')
            await bot.send_message(message.channel,'I have won! Muahaha!')
    
    elif message.content.upper().startswith('-8BALL'):
        await bot.send_message(message.channel,random.choice(['It is certain!:8ball:',
                                                                 'It is decidedly so!:8ball:',
                                                                 'Without a doubt!:8ball:',
                                                                 'Yes–definitely!:8ball:',
                                                                 'You may rely on it!:8ball:',
                                                                 'As I see it, yes!:8ball:',
                                                                 'Most Likely!:8ball:',
                                                                 'Outlook good!:8ball:',
                                                                 'Yes!:8ball:',
                                                                 'Signs point to yes!:8ball:'
                                                                 'Don’t count on it!:8ball:',
                                                                 'My reply is no!:8ball:',
                                                                 'My sources say no!:8ball:',
                                                                 'Outlook not so good, and very doubtful!:8ball:',
                                                                 'Reply hazy, try again!:8ball:',
                                                                 'Ask again later!:8ball:',
                                                                 'Better not tell you now!:8ball:',
                                                                 'Cannot predict now!:8ball:',
                                                                 'Concentrate and ask again!:8ball:']))
        
    elif profanity.contains_profanity(message.content):
         await bot.delete_message(message)
         await bot.send_message(message.channel, message.author.mention + ' Please restrict from profanity! That is against the rules of this server!')
         await bot.send_message(bot.get_channel('406252820459946004'),embed=discord.Embed(color=discord.Color.red(),description=(message.author.mention + ' has sweared once!')))

    elif message.content.upper().startswith('-SAY'):
        args = message.content.split(" ")
        await bot.send_message(message.channel,"%s" % (message.author.mention + ' says ' + " ".join(args[1:])))

    if message.content.upper().startswith('-START'):
        await bot.send_message(message.channel, 'Type hi 4 times.')
        for i in range(4):
            msg = await bot.wait_for_message(author=message.author, content='hi')
            fmt = '{} left to go...'
            await bot.send_message(message.channel, fmt.format(3 - i))

        await bot.send_message(message.channel, 'Good job! You know how to count!')

    if message.content.upper().startswith('-RANDOM'):
        await bot.send_message(message.channel,embed=discord.Embed(color=discord.Color.blue(),description=('Random!')))

    if message.content.upper().startswith('-TEST'):
        number = random.randint(1,101)
        print(number)
        await bot.send_message(message.channel,'I have picked a number between 1 and 100! Do -number and your guess to guess!')
        
        def check(msg):
            return msg.content.upper().startswith('-NUMBER')

        for i in range(5):
            msg = await bot.wait_for_message(author=message.author, check=check)
            args = msg.content.split(" ")
            fmt = '{} tries left...'
            print(number)
            if msg.content.endswith(str(number)):
                await bot.send_message(message.channel,'Congratulations! You guessed ' + str(number) + ' which was my number!' )
                if i > 0:
                    await bot.send_message(bot.get_channel('406252820459946004'),embed=discord.Embed(color=discord.Color.green(),description=(message.author.mention + ' has guessed my number, {}, correctly using'.format(number) + ' {} tries!'.format(i+1))))
                else:
                    await bot.send_message(bot.get_channel('406252820459946004'),embed=discord.Embed(color=discord.Color.green(),description=(message.author.mention + ' has guessed my number, {}, correctly on their first try!'.format(number))))
                i = 4
            else:
                if int(str(args[1])) < number:
                    await bot.send_message(message.channel, 'My number is higher than your guess!')
                else:
                    await bot.send_message(message.channel, 'My number is lower than your guess!')

                if i < 4:
                    await bot.send_message(message.channel, fmt.format(4 - i))

                else:
                    await bot.send_message(message.channel, 'Ahh, better luck next time! My number was ' + str(number) + '!')

##    if message.content.upper().startswith('-HELP'):
##        await bot.send_message(message.channel, '`-rps *yourchoice*: Bot plays rock, paper, and scissors with you \n-help: Show this message \n-8ball: Bot says your prediction \n-say *yourdialog*: Bot repeats your dialog \n-start: Learn how to count to 4 \n-test: Play a guessing game with the bot \n-flip: Bot flips a coin \n-cool: See if you are cool \nThere will also be some easter eggs :)`')
                    
    if message.content.upper().startswith('-COOL'):
        await bot.send_message(message.channel, 'Who is cool? Type -name and the name.')

        def check(msg):
            return msg.content.upper().startswith('-NAME')

        message = await bot.wait_for_message(author=message.author, check=check)
        name = message.content[len('-name'):].strip()
        if message.content.endswith('Jiefu'):
            await bot.send_message(message.channel, '{} is cool indeed.'.format(name))
        else:
            if message.content.endswith('Jeff'):
                await bot.send_message(message.channel,'**Say your real name {}!**'.format(name))
            else:
                await bot.send_message(message.channel, '{}, sorry but you are not cool!'.format(name))

    args = message.content.split(" ")
    if message.content.upper().startswith('-MUTE'):
        if '406248427324702731' in [role.id for role in message.author.roles]:
            mute = discord.utils.get(message.server.roles,name='Muted')
            await bot.add_roles(message.mentions[0], mute)
            await bot.send_message(message.channel,str(message.mentions[0]) + ' has been muted!')
        else:
            await bot.send_message(message.channel,'{}, you do not have permission to use this command!'.format(message.author.mention))
            await bot.send_message(bot.get_channel('406252820459946004'),embed=discord.Embed(color=discord.Color.red(),description=(message.author.mention + ' has tried to mute someone without permissions!')))
        
##    content = pickle.load(pickle_in)
##    if message.content == content:
##        await bot.delete_message(message)
##        print('idiot')
##
##    else:
##        content = message.content
##        pickle_out = open("dict.pickle","wb")
##        pickle.dump(content,pickle_out)
##        pickle_out.close()

##    if message.content.upper().startswith('-FLIP'):
##         await bot.send_message(message.channel,random.choice(['Heads!','Tails!']))
##
##    args = message.content.split(" ")
##    d = collections.defaultdict(int)
##    print('1')
##    for x in range(0, len(args)):
##        print('2')
##        for c in args[x]:
##            d[c] += 1
##            print('hi')
##
##            if d[c] > 5:
##                print('4')
##                await bot.delete_message(message)
##                await bot.send_message(message.channel, message.author.mention + ' Please restrict from spamming letters!')
    
    args = message.content.split(" ")
    string = 'https://discord.gg'
    for x in range(0,len(args)):
        if string.lower() in args[x].lower():
            await bot.delete_message(message)
            await bot.send_message(message.channel, message.author.mention + ' Please restrict from advertising in this server! If you want, ask permission via owner!')

    args = message.content.split(" ")
    salty = ['trash','noob','bad','horrible','landfill','dumpster','fudge','darn','suicide','fml','wtf','supernoob','nibba','gay','lesbian','easy','suck']
    for y in range(0,len(args)):
        for x in range(0,len(salty)):
            if salty[x] in args[y]:
                await bot.send_message(message.channel,embed=discord.Embed(color=discord.Color.red(),description=('That is a little out there!')))

    args = message.content.split(" ")
    for x in range(0, len(args)):
        if args[x].lower() == 'hi':
            await bot.send_message(message.channel, 'Hi!')

    await bot.process_commands(message)

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

@bot.event
async def on_member_join(Member : discord.User):  

    roles = ["406258255472623617"]

    team_list = ["Player"]
    #entered_team = message.content[6:].lower()
    for team in team_list:

        role = discord.utils.get(server.roles, name=team)
        try:
            await client.add_roles(Member.name, role)
        except Exception as e:              
            #await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
        #except discord.Forbidden:
            #await client.send_message(message.channel, "I don't have perms to add roles.")
            pass

bot.run('NDA2Mjc1NzUyMTQ1ODQ2Mjgx.DYjhkA.6817KgHHb12WpczAOXXTtuukcZE')
