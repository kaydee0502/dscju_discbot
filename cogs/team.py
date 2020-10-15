#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:11:48 2020

@author: kaydee
"""

# bot.py
# bot.py
import os

import discord
from discord.ext import commands

#bad_word_checker = re.compile(bw).search
class Team(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(discord.__version__)
        print('Team cog ready!')
        
        
    
    
    @commands.command(name = "helpme")
    async def test(self,ctx):
        print("cmd ran")
        await ctx.send("`Help command!`")
        
    @commands.command(name= "team")
    async def test2(self,ctx,*,arg=None):
        if arg:
            print(arg)
            embed=discord.Embed(title="DSC JU Team", url="https://cdn.discordapp.com/attachments/520265639680671747/533389224913797122/rtgang.jpeg", description="Here are the team members of DSC JU who are always ready to help and guide you!", color=0x26cee0)
            embed.set_author(name="Developer Students Club", url="https://cdn.discordapp.com/attachments/520265639680671747/533389224913797122/rtgang.jpeg", icon_url="https://cdn.discordapp.com/attachments/520265639680671747/533389224913797122/rtgang.jpeg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/520265639680671747/533389224913797122/rtgang.jpeg")
            embed.add_field(name="Avni Shrivastava", value="Chapter Lead", inline=False)
            embed.add_field(name="Samiksha Jain Bajaj", value="Core", inline=True)
            embed.add_field(name="Sakshit Tinker \u200B", value="Core \u200B", inline=True)
            embed.add_field(name="Aditi Devgan", value="Core", inline=True)
            embed.add_field(name="Nikhil Seksari", value="Core", inline=True)
            embed.add_field(name="Dhananjay Sharma", value="Management Lead", inline=True)
            embed.add_field(name="Mansi Gurnani", value="Management Co-Lead", inline=True)
            embed.add_field(name="Prerna Tripathi", value="Documentation Lead", inline=True)
            embed.add_field(name="Tripty", value="Documentation Co-Lead", inline=True)
            embed.add_field(name="Harshit Sharma", value="PR Lead", inline=True)
            embed.add_field(name="Vanisha Bhardwaj", value="PR Co-Lead", inline=True)
            embed.add_field(name="Aakash Verma", value="Digital marketing Lead", inline=True)
            embed.add_field(name="Samiksha Paliwal", value="RPA Lead", inline=True)
            embed.add_field(name="Anshi Gupta", value="Data Science Lead", inline=True)
            embed.add_field(name="Kshitij Dhama", value="Data Science Co Lead", inline=True)
            embed.add_field(name="Arpit Goyal", value="WebD Lead", inline=True)
            embed.add_field(name="Mitali Agrawal", value="WebD Co Lead", inline=True)
            embed.add_field(name="Kashit Duhan", value="Game Dev Lead", inline=True)
            embed.add_field(name="Utkarsh Gupta", value="Game Dev Co Lead", inline=True)
            embed.add_field(name="Lakshya Kulshreshtha", value="Graphics Lead", inline=True)
            embed.add_field(name="Ayushi Pancholi", value="Graphics Co Lead", inline=True)
            embed.add_field(name="Vijay Ojha", value="Media Lead", inline=True)
            embed.add_field(name="Venkatesh Acharya", value="Cybersecurity Lead", inline=True)
            embed.add_field(name="Akshat Joshi", value="Cloud Lead", inline=True)
            embed.add_field(name="Mohit Bansal", value="Cloud Co Lead", inline=True)
            embed.add_field(name="Aviral Chaturvedi", value="Flutter Lead", inline=True)
            embed.add_field(name="Mohit Singh", value="Flutter Co Lead", inline=True)
            embed.set_footer(text="Click on top link to get their contacts!")
            await ctx.send(embed=embed)
        else:
            await ctx.send("To use team command:\n\nUse space seperated keywords with with command. Example : `.team flutter`\n\nValid keywords are :\n\n> Core members : `core`\n> Web Development : `webd`\n> Data Science : `ds`\n> Cloud : `cloud`\n> Flutter : `flutter`\n> Management : `management`\n> Documentation : `doc`\n> RPA : `rpa`\n> Media : `media`\n> Game Development : `gamedev`\n> Cybersecurity : `cyber`\n> Graphics : `graphics`\n> Marketing and Corporate Relations : `pr`\n> Digital Marketing : `social`")
            
    
    

def setup(client):
    client.add_cog(Team(client))









































