#-----------------------#

from typing import Awaitable
import discord
from discord import channel
from discord import message
from discord import client
from discord import guild
from discord.ext import commands
import time
from discord.ext.commands.core import check
from keep_alive import keep_alive

#-----------------------#


print("""

   ▄████████    ▄████████     ███        ▄████████ 
  ███    ███   ███    ███ ▀█████████▄   ███    ███ 
  ███    █▀    ███    █▀     ▀███▀▀██   ███    ███ 
  ███         ▄███▄▄▄         ███   ▀   ███    ███ 
▀███████████ ▀▀███▀▀▀         ███     ▀███████████ 
         ███   ███    █▄      ███       ███    ███ 
   ▄█    ███   ███    ███     ███       ███    ███ 
 ▄████████▀    ██████████    ▄████▀     ███    █▀  
                                                   
""")

#-----------------------#TOKEN


global TOKEN
TOKEN = "TOKEN HERE" # YOUR TOKEN GOES HERE


#-----------------------#PREFIX

bot = commands.Bot(command_prefix="!", self_bot = True)
bot.remove_command('help')


#-----------------------#START

@bot.event
async def ready():
  print("connected")

#-----------------------#PRUGE


@bot.command()
async def purge(ctx, amount=99999999):

    await ctx.send("https://ogusers.com/uploads/avatars/avatar_315433.gif")
    
    await ctx.send("""
    ```> PURGING  ```
    """)


    await ctx.channel.purge(limit=amount)



    await ctx.send("https://cdn.discordapp.com/attachments/754220909199360042/764370332139257866/image0.gif")

    await ctx.send("""
    ```> PURGED  ```
    """)

    
#-----------------------#KICK

@bot.command()

async def kick(ctx, member : discord.Member, *, reason=None):

  await ctx.send("https://cdn.discordapp.com/attachments/754220909199360042/758237204375142400/image0.gif")
  await ctx.send("""
  ``` KICKED ``` """)

  await member.kick(reason=reason)

#-----------------------#BAN

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await ctx.send("https://cdn.discordapp.com/attachments/754220909199360042/755699958069329990/image0.gif")
  await ctx.send("""
  ``` BANNED ```""")


  await member.ban(reason=reason)

#-----------------------#UNBAN

@bot.command()
async def unban(ctx, *,member):

  banned_users= await ctx.guild.bans()
  member_name, member_dsicriminator = member.split('#')


  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_dsicriminator):
      await ctx.guild.unban(user)
      await ctx.send("https://cdn.discordapp.com/attachments/754220909199360042/754263219375177828/image0.gif")
      await ctx.send(f"```UNBANNED```")
      return



#-----------------------# CHANNEL DEL

@bot.command()
async def delchannels(ctx):

  await ctx.send("https://cdn.discordapp.com/attachments/754220909199360042/754263041255931904/image0.gif")
  await ctx.send("``` DELETING ```")

  for x in ctx.guild.channels:
        await x.delete()

    
#-----------------------#CREATE CHANNELS


@bot.command()
async def makechannels(ctx):

  await ctx.send("https://media.discordapp.net/attachments/804708552710815747/820125113571344434/image0.gif")
  await ctx.send("```CREATING```")

  guild = ctx.message.guild

  for x in range (500):
    await guild.create_text_channel('✦|')


#-----------------------#CHANNEL LIST

@bot.command()
async def listchannels(ctx):

  await ctx.send("https://media.discordapp.net/attachments/755957691381186560/815945415747829760/image4.gif")
  await ctx.send("```CHANNELS```")

  for x in ctx.guild.channels:
    await ctx.send(f'=====> {x} <=====')


#-----------------------#FRIENDSLIST

@bot.command()
async def listfriends(ctx):

  await ctx.send("https://media.discordapp.net/attachments/804708552710815747/805220577937719306/image0.gif")
  await ctx.send("```FRIENDS```")
  friends = bot.user.friends


  for person in friends:
    await ctx.send(f'{person}')


#-----------------------# DM Friends


@bot.command()
async def dmfriends(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/754220909199360042/789291425270464532/avatar_146.gif")
  await ctx.send("```MESSAGE TO DM FRIENDS LIST```")

  friends = bot.user.friends

  def check(m):
    return m.author.id == ctx.author.id

  message = await bot.wait_for('message',check=check)
  
  await ctx.send("```SENT TO```\n---------")

  for user in friends:
    await user.send(message.content)
    time.sleep(2)
    await ctx.send(f'{user}')


#-----------------------# Avatar

@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

#-----------------------# NITRO

@bot.command()
async def nitrogen(ctx):

  await ctx.send("https://media.discordapp.net/attachments/822783040580354068/831495976619081747/unknown.png")
  await ctx.send("```NITRO GEN```\n  DOWNLOAD:  https://gofile.io/d/YlFiYk")
  await ctx.send ("GUIDE: <https://pastebin.com/XPeCCvgb>")


#-----------------------# HELP

@bot.command()
async def help(ctx):
  await ctx.send("https://ogusers.com/uploads/avatars/avatar_301248.gif")
  await ctx.send("```!purge\n!kick @user\n!ban @user\n!unban user#0000\n!delchannels\n!makechannels\n!listchannels\n!listfriends\n!dmfriends\n!avatar @user\n!nitrogen```")

#-----------------------# RUN

keep_alive()
bot.run(TOKEN,bot=False)

#-----------------------# 