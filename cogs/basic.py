#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:05:51 2020

@author: kaydee
"""
# bot.py
# bot.py
import os

import discord
from discord.ext import commands
from badwords import bw
import re
#bad_word_checker = re.compile(bw).search
class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(discord.__version__)
        print(f'{self.client.user} has connected to Discord!')
        await self.client.change_presence(status = discord.Status.do_not_disturb, activity = discord.Game("Under Development"))
        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print("yerr")
        await self.client.get_channel(765182984659140632).send(f"Welcome {member.mention}, to Developer Student Club - JECRC University, please introduce yourself in `#hello` channel :)")
        await member.send("Hi, welcome to the DSC JU's Discord Server, please don't forget to introduce yourself there. \n\n\nPlease consider following us on these social media platforms:\n\n> Instagram :\n> https://www.instagram.com/dsc.ju/ \n\n> LinkedIn : https://www.linkedin.com/company/developer-student-club-jecrc-university \n\n> FaceBook :\n> <https://www.facebook.com/DSC-JU-111575137375820/> \n\n> YouTube :\n> <https://www.youtube.com/channel/UC1gebMkOQCm2ebwJoG-eeag>\n\n\nEnjoy your stay!")
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print("cerr")
        await self.client.get_channel(765182984659140632).send(f"{member.name} has left!")
    
    
    @commands.Cog.listener()
    async def on_message(self,message):
        print("checking..")
        for badword in bw:
            #print(badword)
            if badword in message.content.lower().split():
                print("THIS",badword)
                await message.delete()
                await message.channel.send(f'{message.author.mention}! Your message has not passed moderation!')
            

    
    
    @commands.command(name = "hi")
    async def test(self,ctx):
        print("cmd ran")
        await ctx.send(f"Hi {ctx.author.mention} :)")
        
    @commands.command(name = "ping")
    async def cmd1(self,ctx):
        print("cmd ran")
        await ctx.send(f"ping : {round(self.client.latency * 1000)}ms")
    
    @commands.command(name = "doc")
    async def cmd2(self,ctx):
        print("cmd ran")
        await ctx.send("```This is a docstring........```")
    
    @commands.command(name = "clear")
    @commands.has_role("manage")
    async def cmd3(self, ctx, amt = 5):
        print("cmd ran")
        await ctx.channel.purge(limit = amt)
    

def setup(client):
    client.add_cog(Basic(client))









































