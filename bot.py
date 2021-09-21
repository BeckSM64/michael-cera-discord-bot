#!/usr/bin/env python3
import os
import discord
import datetime
from os.path import join, dirname
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks

# Load .env file that holds the tokens and API keys
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Read in discord token from .env
TOKEN = os.getenv('DISCORD_TOKEN')

# Map that holds the start and end time for the bot to post
ceraTimeMap = {

    "start": datetime.time(6, 0, 0),
    "end"  : datetime.time(6, 1, 0)
}

# Give bot permissions
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

@bot.event
async def on_ready():
    await ceraLoop.start()

@tasks.loop(seconds=60)
async def ceraLoop():

    # Current time for comparison
    now = datetime.datetime.now().time()

    # Loop through all the servers that the bot is present in
    for guild in bot.guilds:

        # Post a random video at the specified time to the specified channel
        if time_in_range(ceraTimeMap["start"], ceraTimeMap["end"], now):

            # Post the same picture of Micael Cera in the first available text channel in the server
            await guild.text_channels[0].send(file=discord.File('TheSamePhotoOfMichaelCeraEveryday.jpg'))

bot.run(TOKEN)
