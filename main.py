import discord
from discord.ext import commands
import  random
  
tips = ["Dont throw trash outside', 'dont use a lot of plastic bags', 'dont throw away food', 'dont throw trash in the ocean, 'keep your yard clean that the trash from can be blown away and become litter', 'pick up trash from outside' "]
ocean_pounds = ('33 billion pounds')
total_pounds = ('4.5 trillion')
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
 
@bot.command()
async def nature_tip(ctx):
    await ctx.send(tips)

@bot.command()
async def how_many_ocean_pounds(ctx):
    await ctx.send(ocean_pounds)

@bot.command()
async def how_many_pounds_in_the_world(ctx):
    await ctx.send(total_pounds)

bot.run("MTE1NjYxMjM4ODY5NTU3MjU0Mw.G2fwW4.A31xZo7KLKAl56rvmrKU4G1bk-3YgjRb72yle8")