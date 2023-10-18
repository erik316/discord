import discord
from discord.ext import commands
import  random
  
tips = ["Don't throw trash outside', 'dont use a lot of plastic bags', 'dont throw away food', 'dont throw trash in the ocean, 'keep your yard clean that the trash from can be blown away and become litter', 'pick up trash from outside' "]
ocean_pounds = ('33 billion pounds')
total_ocean_pounds = ('75 to 199 tons')
total_pounds_per_day = ('3.5 million pounds')
total_pounds = ('4.5 trillion tons')
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
 
@bot.command()
async def nature_tips(ctx):
    await ctx.send(tips)

@bot.command()
async def how_many_ocean_pounds(ctx):
    await ctx.send(ocean_pounds)

@bot.command()
async def how_many_pounds_in_the_ocean_per_day(ctx):
    await ctx.send(total_ocean_pounds)

@bot.command()
async def how_many_pounds_in_the_world(ctx):
    await ctx.send(total_pounds)

@bot.command()
async def how_many_pounds_in_the_world_per_day(ctx):
    await ctx.send(total_pounds_per_day)

bot.run("Put your bots token here")
