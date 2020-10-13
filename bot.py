# bot.py
# bot.py
import os

import discord
from discord.ext import commands




client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


"""
@client.event
async def on_message(message):
    print(message.content)
    #await message.channel.send(message.content)
"""


@client.command(name = "hi")
async def test(ctx):
    print("cmd ran")
    await ctx.send("Who I am? you name it :)")

client.run("NzY1MDg4MDYyMDM5NjU0NDQy.X4PtyA.hAi0kb5zTwAZ12EEkO6O3i4a6NA")
