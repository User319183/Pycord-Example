
import discord
import random
import json
from discord.ext import commands, tasks
import os
from itertools import cycle
from discord import Member
import asyncio as asyncio
from discord.utils import find
from discord.ext import tasks
from discord.utils import get
from discord.ext import *
from discord.ext.commands import *
from ctypes import *
from datetime import datetime
import aiohttp
from discord.ext import commands
from discord.commands import Option





if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]


intents = discord.Intents.default()



bot = commands.Bot(command_prefix="!", intents=intents)




@bot.listen()
async def on_ready():
    print(f'Bot has been activated! Modules loaded.')
    print(f'---------------------------------------')















@bot.slash_command(name="invite", description="invite for this bot",)
async def invite(ctx):
    embed = discord.Embed(title="Here's my invite!", color=0xD708CC, description="https://discord.com/api/oauth2/authorize?client_id=INSERT_CLIENT_ID&permissions=8&scope=bot%20applications.commands")
    await ctx.respond(embed=embed)



@bot.slash_command(name="help", description="Default Help Panel",)
async def help(ctx):
    embed=discord.Embed(title="Help Panel", color=0xD708CC, description = "Default help panel.")
    embed.add_field(name = "Commands", value = "1./ping \n 2. /info \n 3. /ephemeral")
    embed.add_field(name = "Support Server", value = "https://discord.gg/INVITE_CODE")
    await ctx.respond(embed=embed)
    
    
    
@bot.slash_command()
async def ping(ctx):
    await ctx.respond("Pong!")


#Info command for the bot
import platform # For stats

@bot.slash_command(
    name="info",
    description="Information about this bot.",

)
async def info(ctx):

    bot_embed_guilds = []

    for t in bot.guilds:
        bot_embed_guilds.append(t)
    embed = discord.Embed(title="Bot Info", description="General information about Anti-Hoist", color=0xD708CC)
    embed.add_field(name="Bot developer:", value="User319183#3149", inline=True)
    embed.add_field(name="Guild Count:", value=f"{len(bot_embed_guilds)}", inline=True)
    embed.add_field(name="Websocket Ping:", value=f"{round(bot.latency * 1000)}")
    await ctx.respond(embed=embed)
    
    
    
@bot.slash_command()
async def ephemeral(ctx, content: Option(str, "Content of message")):
    await ctx.respond(content, ephemeral=True)
    


#errors
@bot.listen()
async def on_application_command_error(ctx, error):
    embed = discord.Embed(title="An Error Occured", color=0xD708CC, description=f"```{str(error)}```")      
    embed.timestamp = discord.utils.utcnow() 
    await ctx.respond(embed=embed, ephemeral=True)
















bot.run(token)