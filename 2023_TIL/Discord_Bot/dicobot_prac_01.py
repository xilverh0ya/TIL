import discord
from discord.ext import commands
 
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command()
async def sushi(message):
    print('초밥명령어')
    await message.channel.send('초밥!')
    
@bot.command()
async def chicken(message):
    print('치킨명령어')
    await message.channel.send('치킨!!')
 
bot.run('MTA5Mjk2MTk1NzI5ODA1MzIyMQ.GBl1Wu.CeMZjt0XFMFJ6xkwRZLymwbXHesXlFY8pcfHno')