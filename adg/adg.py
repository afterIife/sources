class SELFBOT:
    __linecount__ = 2357
    __version__ = 1.0

import asyncio
import base64
import codecs
import ctypes
import datetime
import functools
import io
import json
import logging
import os
import random
import re
import smtplib
import string
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
import webbrowser
from itertools import cycle
from subprocess import call
from sys import platform
from threading import Thread
from urllib.parse import urlencode

import aiohttp
import colorama
import discord
import dns.name
import numpy
import pyPrivnote as pn
import requests
from bs4 import BeautifulSoup as bs4
from colorama import Fore, init
from discord.ext import commands, tasks
from gtts import gTTS
from PIL import Image
from pymongo import MongoClient
from selenium import webdriver

ctypes.windll.kernel32.SetConsoleTitleW('ADG Selfbot Is Currently Loading...')
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')
stream_url = config.get('stream_url')
tts_language = config.get('tts_language')
bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')
date = datetime.datetime.now()
ok = date.strftime('%H:%M:%S')
os.system('Title ADG  selfbot loading..')
os.system('mode 56, 23')
width = os.get_terminal_size().columns
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()
languages = {'hu':'Hungarian, Hungary',
 'nl':'Dutch, Netherlands',
 'no':'Norwegian, Norway',
 'pl':'Polish, Poland',
 'pt-BR':'Portuguese, Brazilian, Brazil',
 'ro':'Romanian, Romania',
 'fi':'Finnish, Finland',
 'sv-SE':'Swedish, Sweden',
 'vi':'Vietnamese, Vietnam',
 'tr':'Turkish, Turkey',
 'cs':'Czech, Czechia, Czech Republic',
 'el':'Greek, Greece',
 'bg':'Bulgarian, Bulgaria',
 'ru':'Russian, Russia',
 'uk':'Ukranian, Ukraine',
 'th':'Thai, Thailand',
 'zh-CN':'Chinese, China',
 'ja':'Japanese',
 'zh-TW':'Chinese, Taiwan',
 'ko':'Korean, Korea'}
locales = [
 'da', 'de',
 'en-GB', 'en-US',
 'es-ES', 'fr',
 'hr', 'it',
 'lt', 'hu',
 'nl', 'no',
 'pl', 'pt-BR',
 'ro', 'fi',
 'sv-SE', 'vi',
 'tr', 'cs',
 'el', 'bg',
 'ru', 'uk',
 'th', 'zh-CN',
 'ja', 'zh-TW',
 'ko']
m_numbers = [
 ':one:',
 ':two:',
 ':three:',
 ':four:',
 ':five:',
 ':six:']
m_offets = [
 (-1, -1),
 (0, -1),
 (1, -1),
 (-1, 0),
 (1, 0),
 (-1, 1),
 (0, 1),
 (1, 1)]

def startprint():
    if giveaway_sniper == True:
        giveaway = 'Active'
    else:
        giveaway = 'Disabled'
    if nitro_sniper == True:
        nitro = 'Active'
    else:
        nitro = 'Disabled'
    if slotbot_sniper == True:
        slotbot = 'Active'
    else:
        slotbot = 'Disabled'
    if privnote_sniper == True:
        privnote = 'Active'
    else:
        privnote = 'Disabled'
    print(f'''{Fore.RESET}
                {Fore.RED}       ╔═╗╔╦╗╔═╗        {Fore.RED}
                {Fore.LIGHTBLACK_EX}       ╠═╣ ║║║ ╦        {Fore.LIGHTBLACK_EX}
                {Fore.WHITE}       ╩ ╩═╩╝╚═╝        {Fore.WHITE}


           {Fore.LIGHTBLACK_EX}[{Fore.RED}{ok}{Fore.LIGHTBLACK_EX}]{Fore.RED} >{Fore.WHITE} User {Fore.LIGHTBLACK_EX}| {Fore.LIGHTGREEN_EX}{ADG.user.name}#{ADG.user.discriminator}                        {Fore.WHITE}
           {Fore.RED}[{Fore.LIGHTBLACK_EX}{ok}{Fore.RED}]{Fore.LIGHTBLACK_EX} >{Fore.RED} Prefix {Fore.LIGHTBLACK_EX}| {Fore.LIGHTGREEN_EX}{prefix}                               {Fore.WHITE}
           {Fore.LIGHTBLACK_EX}[{Fore.RED}{ok}{Fore.LIGHTBLACK_EX}]{Fore.RED} {Fore.RED}> {Fore.WHITE}Version {Fore.LIGHTBLACK_EX}| {Fore.LIGHTGREEN_EX}{SELFBOT.__version__}                            {Fore.WHITE}
           {Fore.RED}[{Fore.LIGHTBLACK_EX}{ok}{Fore.RED}]{Fore.LIGHTBLACK_EX} >{Fore.LIGHTBLACK_EX} {Fore.RED}Code Line {Fore.LIGHTBLACK_EX}| {Fore.LIGHTGREEN_EX}{SELFBOT.__linecount__}                         {Fore.WHITE}
           {Fore.LIGHTBLACK_EX}[{Fore.RED}{ok}{Fore.LIGHTBLACK_EX}]{Fore.RED} >{Fore.WHITE} Nitro Sniper {Fore.LIGHTBLACK_EX}| {Fore.LIGHTGREEN_EX}{nitro}                    {Fore.WHITE}
           {Fore.RED}[{Fore.LIGHTBLACK_EX}{ok}{Fore.RED}]{Fore.LIGHTBLACK_EX} >{Fore.RED} {Fore.RED}Giveaway Sniper {Fore.LIGHTBLACK_EX}| {Fore.LIGHTGREEN_EX}{giveaway}                 {Fore.WHITE}


                   {Fore.LIGHTBLACK_EX}|{Fore.MAGENTA}icy x dakari{Fore.LIGHTBLACK_EX}|
    ''' + Fore.RESET)
    time.sleep(3)


def Clear():
    os.system('cls')


Clear()

def Init():
    if config.get('token') == 'token-here':
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your token in the config.json file" + Fore.RESET)
    else:
        token = config.get('token')
    try:
        ADG.run(token, bot=False, reconnect=True)
        os.system('title selfbot')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}Incorrect token has been entered" + Fore.RESET)
        os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN} Incorrect Password or gmail, make sure you've enabled less-secure apps access" + Fore.RESET)
    else:
        target = input('Target Gmail: ')
        message = input('Message to send: ')
        counter = eval(input('Ammount of times: '))
        count = 0
        while True:
            if count < counter:
                count = 0
                _smpt.sendmail(username, target, message)
                count += 1

        if count == counter:
            pass


def GenAddress(addy: str):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    four_char = ''.join((random.choice(letters) for _ in range(4)))
    should_abbreviate = random.randint(0, 1)
    if should_abbreviate == 0:
        if 'street' in addy.lower():
            addy = addy.replace('Street', 'St.')
            addy = addy.replace('street', 'St.')
        elif 'st.' in addy.lower():
            addy = addy.replace('st.', 'Street')
            addy = addy.replace('St.', 'Street')
        if 'court' in addy.lower():
            addy = addy.replace('court', 'Ct.')
            addy = addy.replace('Court', 'Ct.')
        elif 'ct.' in addy.lower():
            addy = addy.replace('ct.', 'Court')
            addy = addy.replace('Ct.', 'Court')
        if 'rd.' in addy.lower():
            addy = addy.replace('rd.', 'Road')
            addy = addy.replace('Rd.', 'Road')
        elif 'road' in addy.lower():
            addy = addy.replace('road', 'Rd.')
            addy = addy.replace('Road', 'Rd.')
        if 'dr.' in addy.lower():
            addy = addy.replace('dr.', 'Drive')
            addy = addy.replace('Dr.', 'Drive')
        elif 'drive' in addy.lower():
            addy = addy.replace('drive', 'Dr.')
            addy = addy.replace('Drive', 'Dr.')
        if 'ln.' in addy.lower():
            addy = addy.replace('ln.', 'Lane')
            addy = addy.replace('Ln.', 'Lane')
        elif 'lane' in addy.lower():
            addy = addy.replace('lane', 'Ln.')
            addy = addy.replace('lane', 'Ln.')
    random_number = random.randint(1, 99)
    extra_list = ['Apartment', 'Unit', 'Room']
    random_extra = random.choice(extra_list)
    return four_char + ' ' + addy + ' ' + random_extra + ' ' + str(random_number)


def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token if token}
    for token in tokens:
        yield token


def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token if token}
    for token in tokens:
        yield token


class Login(discord.Client):

    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print('')
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print('-------------------------------')
        await self.logout()


def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))

    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))

    else:
        return


def async_executor():

    def outer(func):

        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = (functools.partial)(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=(message.lower()), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f"Images/{ctx.guild.id}-Dump.txt", 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices((string.ascii_letters + string.digits), k=16))
    return f"https://discord.gift/{code}"


def RandomColor():
    randcolor = discord.Color(random.randint(0, 16777215))
    return randcolor


def RandString():
    return ''.join((random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32))))


colorama.init()
ADG = discord.Client()
ADG = commands.Bot(description='ADG Selfbot',
  command_prefix=prefix,
  self_bot=True)
ADG.remove_command('help')
ADG.msgsniper = True
ADG.sniped_message_dict = {}
ADG.sniped_edited_message_dict = {}

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(name=('Current BTC price: ' + value + '$ USD'),
      url='https://www.twitch.tv/almightydakari')
    await ADG.change_presence(activity=btc_stream)

@ADG.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.User):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await ADG.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)

@ADG.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await ADG.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)


@ADG.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}You're missing permission to execute this command" + Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Missing arguments: {error}" + Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Not a valid image" + Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Discord error: {error}" + Fore.RESET)
    elif 'Cannot send an empty message' in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Couldnt send a empty message" + Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{error_str}" + Fore.RESET)


@ADG.event
async def on_message_edit(before, after):
    await ADG.process_commands(after)


@ADG.event
async def on_message(message):

    def GiveawayData():
        print(f"{Fore.WHITE} - CHANNEL: {Fore.CYAN}[{message.channel}]\n{Fore.WHITE} - SERVER: {Fore.CYAN}[{message.guild}]" + Fore.RESET)

    def SlotBotData():
        print(f"{Fore.WHITE} - CHANNEL: {Fore.CYAN}[{message.channel}]\n{Fore.WHITE} - SERVER: {Fore.CYAN}[{message.guild}]" + Fore.RESET)

    def NitroData(elapsed, code):
        print(f"{Fore.WHITE} - CHANNEL: {Fore.CYAN}[{message.channel}]\n{Fore.WHITE} - SERVER: {Fore.CYAN}[{message.guild}]\n{Fore.WHITE} - AUTHOR: {Fore.CYAN}[{message.author}]\n{Fore.WHITE} - ELAPSED: {Fore.CYAN}[{elapsed}]\n{Fore.WHITE} - CODE: {Fore.CYAN}{code}" + Fore.RESET)

    def PrivnoteData(code):
        print(f"{Fore.WHITE} - CHANNEL: {Fore.CYAN}[{message.channel}]\n{Fore.WHITE} - SERVER: {Fore.CYAN}[{message.guild}]\n{Fore.WHITE} - CONTENT: {Fore.CYAN}[The content can be found at Privnote/{code}.txt]" + Fore.RESET)

    time = datetime.datetime.now().strftime('%H:%M %p')
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search('discord.gift/(.*)', message.content).group(1)
            token = config.get('token')
            headers = {'Authorization': token}
            r = requests.post(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem",
              headers=headers).text
            elapsed = datetime.datetime.now() - start
            elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
            if 'This gift has been redeemed already.' in r:
                print(f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)
            elif 'subscription_plan' in r:
                print(f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)
            elif 'Unknown Gift Code' in r:
                print(f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                else:
                    print(f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                    SlotBotData()
        else:
            return
    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction('🎉')
                except discord.errors.Forbidden:
                    print(f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                else:
                    print(f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                    GiveawayData()
        else:
            return
    if f"Congratulations <@{ADG.user.id}>" in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                print(f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return
    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/' + code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                try:
                    print(e)
                finally:
                    e = None
                    del e

            else:
                with open(f"Privnote/{code}.txt", 'a+') as f:
                    print(f"\n{Fore.CYAN}[{time} - Privnote Sniped]" + Fore.RESET)
                    PrivnoteData(code)
                    f.write(note_text)
        else:
            return
    await ADG.process_commands(message)


@ADG.event
async def on_connect():
    Clear()
    if giveaway_sniper == True:
        giveaway = 'Active'
    else:
        giveaway = 'Disabled'
    if nitro_sniper == True:
        nitro = 'Active'
    else:
        nitro = 'Disabled'
    if slotbot_sniper == True:
        slotbot = 'Active'
    else:
        slotbot = 'Disabled'
    if privnote_sniper == True:
        privnote = 'Active'
    else:
        privnote = 'Disabled'
    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f"Project ADG  -  Logged in as {ADG.user.name}")


@ADG.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nﾠﾠ')


@ADG.command()
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices((ctx.guild.members), k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))


@ADG.command(aliases=['tokenfucker', 'disable', 'crash'])
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
        'name': "ADG",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
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
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
            else:
                break

@ADG.command()
async def lmgtfy(ctx, *, message):
    await ctx.message.delete()
    q = urlencode({'q': message})
    await ctx.send(f"<https://lmgtfy.com/?{q}>")


@ADG.command()
async def login(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = '\n            function login(token) {\n            setInterval(() => {\n            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n            }, 50);\n            setTimeout(() => {\n            location.reload();\n            }, 2500);\n            }   \n            '
    driver.get('https://discordapp.com/login')
    driver.execute_script(script + f'\nlogin("{_token}")')


@ADG.command()
async def botlogin(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = "\n    function login(token) {\n      ((i) => {\n        window.webpackJsonp.push([  \n          [i], {\n            [i]: (n, b, d) => {\n              let dispatcher;\n              for (let key in d.c) {\n                if (d.c[key].exports) {\n                  const module = d.c[key].exports.default || d.c[key].exports;\n                  if (typeof(module) === 'object') {\n                    if ('setToken' in module) {\n                      module.setToken(token);\n                      module.hideToken = () => {};\n                    }\n                    if ('dispatch' in module && '_subscriptions' in module) {\n                      dispatcher = module;\n                    }\n                    if ('AnalyticsActionHandlers' in module) {\n                      console.log('AnalyticsActionHandlers', module);\n                      module.AnalyticsActionHandlers.handleTrack = (track) => {};\n                    }\n                  } else if (typeof(module) === 'function' && 'prototype' in module) {\n                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);\n                    if ('_discoveryFailed' in descriptors) {\n                      const connect = module.prototype._connect;\n                      module.prototype._connect = function(url) {\n                        console.log('connect', url);\n                        const oldHandleIdentify = this.handleIdentify;\n                        this.handleIdentify = () => {\n                          const identifyData = oldHandleIdentify();\n                          identifyData.token = identifyData.token.split(' ').pop();\n                          return identifyData;\n                        };\n                        const oldHandleDispatch = this._handleDispatch;\n                        this._handleDispatch = function(data, type) {\n                          if (type === 'READY') {\n                            console.log(data);\n                            data.user.bot = false;\n                            data.user.email = 'ADG-Was-Here@Fuckyou.com';\n                            data.analytics_tokens = [];\n                            data.connected_accounts = [];\n                            data.consents = [];\n                            data.experiments = [];\n                            data.guild_experiments = [];\n                            data.relationships = [];\n                            data.user_guild_settings = [];\n                          }\n                          return oldHandleDispatch.call(this, data, type);\n                        }\n                        return connect.call(this, url);\n                      };\n                    }\n                  }\n                }\n              }\n              console.log(dispatcher);\n              if (dispatcher) {\n                dispatcher.dispatch({\n                  type: 'LOGIN_SUCCESS',\n                  token\n                });\n              }\n            },\n          },\n          [\n            [i],\n          ],\n        ]);\n      })(Math.random());\n    }\n    "
    driver.get('https://discordapp.com/login')
    driver.execute_script(script + f'\nlogin("Bot {_token}")')


@ADG.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=(discord.Color(12981782)))
    embed.set_image(url='https://cdn.discordapp.com/attachments/818733319117078578/826030950576160789/image0.gif')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/819302434744172555/819989884273033226/image0.gif')
    embed.add_field(name='GENERAL COMMANDS', value='**help, av, revav, whois, ping, guildicon, secret(msg), bold(msg), empty, ban(user), kick(user), hexcode(role)**')
    embed.add_field(name='STREAM COMMANDS', value='**stream, watching, game, listening, logout, spam(amt+msg), purge(amt), lenny, reverse(msg), fancy(msg), autoname, groupleaver**', inline=False)
    embed.add_field(name='FUN COMMANDS', value='**dick, hack, tinder, tweet, bomb, cums, 911, fox, dog, dick(user), 8ball, joke, tweet, slot, topic, wyr, feed(user), tickle(user), slap(user), hug(user), smug(user), pat(user), kiss(user)**', inline=False)
    embed.add_field(name='UTIL COMMANDS', value='**nitroon, msgsniper, tokinfo, nitrooff, banner, rainbow(role), tinyurl(url), clear, upper(msg), genname, speak(msg), abc, devowel, combine(msg + msg) fm(firstmsg)**', inline=False)
    embed.add_field(name='WIZZ COMMANDS', value='**cnuke, wizz, dmall(msg), massban, masskick, massunban, masschannel, massrole, delroles, delchannels, rc(name), servername(name), nickall(name)**', inline=False)
    embed.add_field(name='NSFW COMMANDS', value='**lesbian, lewdneko, blowjob, tits, boobs, hentai, feet, erofeet, anal**', inline=False)
    embed.add_field(name='MATH COMMANDS', value='**add <X Y>, subtract <X Y>, multiply <X Y>, divide <X Y>**', inline=False)
    embed.add_field(name='Credits: ', value='**icy x dakari**', inline=False)
    await ctx.send(embed=embed)
    embed = discord.Embed(color=(ctx.author.color), timestamp=(ctx.message.created_at))

@ADG.command()
async def masscon(ctx, _type, amount: int, *, name=None):
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json',
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5)
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@ADG.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=(ctx.guild.name))
    embed.set_image(url=(ctx.guild.banner_url))
    await ctx.send(embed=embed)


@ADG.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.User=None):
    await ctx.message.delete()
    embed = discord.Embed(author=(user.mention), color=(discord.Color(random.randint(0, 16777215))))
    embed.set_author(name=(str(user) + "'s pfp"))
    embed.set_image(url=(user.avatar_url))
    await ctx.send(embed=embed)


@ADG.command(name='tinder', aliases=['match'])
async def tinder(ctx):
    await ctx.message.delete()
    try:
        user1 = ctx.message.mentions[0].avatar_url_as(size=1024)
        user2 = ctx.message.mentions[1].avatar_url_as(size=1024)
    except IndexError:
        return await ctx.send('Mention two users to match :heart:')
    else:
        embed = discord.Embed(color=(discord.Color(16725342)))
        embed.set_image(url=f"https://useless-api--vierofernando.repl.co/tinder?image1={user1}&image2={user2}")
        await ctx.send(embed=embed)


@ADG.command(aliases=['nitrosniper', '6ixnitrosniper'])
async def nitroon(ctx, param=None):
    await ctx.message.delete()
    embed = discord.Embed(color=(discord.Color(12981782)))
    embed.add_field(name='Nitro Mode', value='**Nitro Mode On**', inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/819302434744172555/819623771585249341/image0.gif')
    embed.set_footer(text='', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=embed)
    SIX.nitro_sniper = False
    if str(param).lower() == 'true' or (str(param).lower() == 'on'):
        SIX.nitro_sniper = True

@ADG.command()
async def multiply(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a * b)


@ADG.command()
async def add(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a + b)


@ADG.command()
async def divide(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a / b)


@ADG.command()
async def subtract(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a - b)


@ADG.command(aliases=['nitro_sniper', '6ixnitro_sniper'])
async def nitrooff(ctx, param=None):
    await ctx.message.delete()
    embed = discord.Embed(color=(discord.Color(12981782)))
    embed.add_field(name='Nitro Mode Off', value='**Nitro Mode Off**', inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/819302434744172555/819623771585249341/image0.gif')
    embed.set_footer(text='', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=embed)


@ADG.command()
async def boost(ctx, param=None):
    await ctx.message.delete()
    embed = discord.Embed(color=(discord.Color(12632256)))
    embed.add_field(name='I Boosted Now Slide Perms :p', value='**You Have Succesfully Boosted 293 Times**', inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/819302434744172555/819623893853405214/a_21e1c50008797c36a3d6a7db0c873983.gif')
    embed.set_footer(text='', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=embed)


@ADG.command()
async def bomb(ctx):
    await ctx.message.edit(content=':bomb: ---------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------------ :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ----------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ---------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------ :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ----- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ---- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: - :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb:  :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':boom: ** BOOM!!! **')


@ADG.command()
async def fuckyou(ctx):
    await ctx.message.edit(content='F')
    time.sleep(0.1)
    await ctx.message.edit(content='FU')
    time.sleep(0.1)
    await ctx.message.edit(content='FUC')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK ')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK Y')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YO')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU ')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU N')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NI')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIG')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGG')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGGA')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGGA')


@ADG.command(aliases=['jerkoff', 'ejaculate', 'orgasm'])
async def cums(ctx):
    await ctx.message.delete()
    message = await ctx.send('\n            :ok_hand:            :smile:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:=D \n             :trumpet:      :eggplant:')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                      :ok_hand:            :smiley:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D \n             :trumpet:      :eggplant:  \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                      :ok_hand:            :grimacing:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:=D \n             :trumpet:      :eggplant:  \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                      :ok_hand:            :persevere:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D \n             :trumpet:      :eggplant:   \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                      :ok_hand:            :confounded:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:=D \n             :trumpet:      :eggplant: \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                       :ok_hand:            :tired_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D \n             :trumpet:      :eggplant:    \n             ')
    await asyncio.sleep(0.5)
    await message.edit(contnet='\n                       :ok_hand:            :weary:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:= D:sweat_drops:\n             :trumpet:      :eggplant:        \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                       :ok_hand:            :dizzy_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D :sweat_drops:\n             :trumpet:      :eggplant:                 :sweat_drops:\n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                       :ok_hand:            :drooling_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D :sweat_drops:\n             :trumpet:      :eggplant:                 :sweat_drops:\n     ')


@ADG.command(aliases=['9/11', '911', 'terrorist'])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ''
    message = await ctx.send(f"\n{invis}:man_wearing_turban::airplane:    :office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content=f"\n{invis} :man_wearing_turban::airplane:   :office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content=f"\n{invis}  :man_wearing_turban::airplane:  :office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content=f"\n{invis}   :man_wearing_turban::airplane: :office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content=f"\n{invis}    :man_wearing_turban::airplane::office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content='\n        :boom::boom::boom:    \n        ')


@ADG.command()
async def cnuke(ctx, amount=1):
    await ctx.channel.purge(limit=10000)
    await ctx.send('Channel nuked')
    await ctx.send('https://imgur.com/LIyGeCR')


@ADG.command()
async def address(ctx, *, text):
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while True:
        if i < 10:
            address_array.append(GenAddress(addy))
            i += 1

    final_str = '\n'.join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)


@ADG.command()
async def whois(ctx, *, user: discord.User=None):
    await ctx.message.delete()
    time.sleep(0.4)
    if user is None:
        user = ctx.author
    date_format = '%a, %d %b %Y %I:%M %p'
    em = discord.Embed(description=(user.mention))
    em.set_author(name=(str(user)), icon_url=(user.avatar_url))
    em.set_thumbnail(url=(user.avatar_url))
    em.add_field(name='Registered', value=(user.created_at.strftime(date_format)))
    em.set_footer(text=('ID: ' + str(user.id)))
    return await ctx.send(embed=em)


@ADG.command()
async def weather(ctx, *, city):
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.LIGHTBLACK_EX}[ERROR]: {Fore.RED}Weather API key has not been set in the config.json file" + Fore.RESET)
    else:
        try:
            req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}")
            r = req.json()
            temperature = round(float(r['main']['temp']) - 273.15, 1)
            lowest = round(float(r['main']['temp_min']) - 273.15, 1)
            highest = round(float(r['main']['temp_max']) - 273.15, 1)
            weather = r['weather'][0]['main']
            humidity = round(float(r['main']['humidity']), 1)
            wind_speed = round(float(r['wind']['speed']), 1)
            em = discord.Embed(description=f"\n            Temperature: `{temperature}`\n            Lowest: `{lowest}`\n            Highest: `{highest}`\n            Weather: `{weather}`\n            Humidity: `{humidity}`\n            Wind Speed: `{wind_speed}`\n            ")
            em.add_field(name='City', value=(city.capitalize()))
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f"\n                Temperature: {temperature}\n                Lowest: {lowest}\n                Highest: {highest}\n                Weather: {weather}\n                Humidity: {humidity}\n                Wind Speed: {wind_speed}\n                City: {city.capitalize()}\n                ")

        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{city} Is not a real city" + Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{req.text}" + Fore.RESET)


@ADG.command(aliases=['shorteen'])
async def bitly(ctx, *, link):
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Bitly API key has not been set in the config.json file" + Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}") as req:
                    r = await req.read()
                    r = json.loads(r)
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{req.text}" + Fore.RESET)


@ADG.command()
async def cuttly(ctx, *, link):
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Cutt.ly API key has not been set in the config.json file" + Fore.RESET)
    else:
        try:
            req = requests.get(f"https://cutt.ly/api/api.php?key={cuttly_key}&short={link}")
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)

        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{req.text}" + Fore.RESET)


@ADG.command()
async def cat(ctx):
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Cat API key has not been set in the config.json file" + Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=(str(r[0]['url'])))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]['url']))

        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{req.text}" + Fore.RESET)


@ADG.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get('https://dog.ceo/api/breeds/image/random').json()
    em = discord.Embed()
    em.set_image(url=(str(r['message'])))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))


@ADG.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title='Random fox image', color=16202876)
    em.set_image(url=(r['image']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])


@ADG.command()
async def encode(ctx, string):
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff) - 1]
    await ctx.send(encoded_stuff)


@ADG.command()
async def decode(ctx, string):
    await ctx.message.delete()
    strOne = string.encode('ascii')
    pad = len(strOne) % 4
    strOne += b'=' * pad
    encoded_stuff = codecs.decode(strOne.strip(), 'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff) - 1]
    await ctx.send(decoded_stuff)


@ADG.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int):
    await ctx.message.delete()
    start_time = datetime.datetime.now()

    def EbayViewer(url, views):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        for _i in range(views):
            requests.get(url, headers=headers)

    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)


@ADG.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str='1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
    geo = r.json()
    em = discord.Embed()
    fields = [
     {'name':'IP',
      'value':geo['query']},
     {'name':'ipType',
      'value':geo['ipType']},
     {'name':'Country',
      'value':geo['country']},
     {'name':'City',
      'value':geo['city']},
     {'name':'Continent',
      'value':geo['continent']},
     {'name':'Country',
      'value':geo['country']},
     {'name':'IPName',
      'value':geo['ipName']},
     {'name':'ISP',
      'value':geo['isp']},
     {'name':'Latitute',
      'value':geo['lat']},
     {'name':'Longitude',
      'value':geo['lon']},
     {'name':'Org',
      'value':geo['org']},
     {'name':'Region',
      'value':geo['region']},
     {'name':'Status',
      'value':geo['status']}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']), value=(field['value']), inline=True)
    else:
        return await ctx.send(embed=em)


@ADG.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            if r == 404:
                await ctx.send(f"Site is down, responded with a status code of {r}", delete_after=3)
            else:
                await ctx.send(f"Site is up, responded with a status code of {r}", delete_after=3)


@ADG.command()
async def tweet(ctx, username: str, *, message: str):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=(res['message']))
            await ctx.send(embed=em)


@ADG.command()
async def revav(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        try:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}" + Fore.RESET)
        finally:
            e = None
            del e


@ADG.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role):
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime('%d %b %Y %H:%M')
    created_on = '{} ({} days ago)'.format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == '#000000':
        colour = 'default'
        color = '#%06x' % random.randint(0, 16777215)
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}\nRole ID: {role.id}")
    em.add_field(name='Users', value=users)
    em.add_field(name='Mentionable', value=(role.mentionable))
    em.add_field(name='Hoist', value=(role.hoist))
    em.add_field(name='Position', value=(role.position))
    em.add_field(name='Managed', value=(role.managed))
    em.add_field(name='Colour', value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)



@ADG.command()
async def minesweeper(ctx, size: int=5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x if i[1] == y]
    message = '**Click to play**:\n'
    for y in range(size):
        for x in range(size):
            tile = '||{}||'.format(chr(11036))
            if has_bomb(x, y):
                tile = '||{}||'.format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod):
                        if has_bomb(x + xmod, y + ymod):
                            count += 1
                else:
                    if count != 0:
                        tile = '||{}||'.format(m_numbers[(count - 1)])

            message += tile
        else:
            message += '\n'

    else:
        await ctx.send(message)


@ADG.command()
async def combine(ctx, name1, name2):
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = ''.join([name1letters, name2letters])
    emb = discord.Embed(description=(f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)


@ADG.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3').replace('E', '3').replace('i', '!').replace('I', '!').replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f"`{text}`")


@ADG.command(aliases=['dvwl'])
async def devowel(ctx, *, text):
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '').replace('E', '').replace('i', '').replace('I', '').replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)


@ADG.command()
async def blank(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
            try:
                await ADG.user.edit(password=password, username='ٴٴٴٴ', avatar=(f.read()))
            except discord.HTTPException as e:
                try:
                    print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}" + Fore.RESET)
                finally:
                    e = None
                    del e

@ADG.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@ADG.command()
async def dm(ctx, user: discord.User=None, *, message):
    await ctx.message.delete()
    user = ADG.get_user(user.id)
    if ctx.author.id == ADG.user.id:
        return
    try:
        await user.send(message)
    except:
        pass


@ADG.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f"Showing Color: {str(color)}")
    em.set_image(url='attachment://color.png')
    await ctx.send(file=(discord.File(file, 'color.png')), embed=em)


@ADG.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f"http://tinyurl.com/api-create.php?url={link}").text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False)
    await ctx.send(embed=em)


@ADG.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get((ctx.guild.roles), name=role)
    while True:
        try:
            await role.edit(role=role, colour=(RandomColor()))
            await asyncio.sleep(10)
        except:
            pass


@ADG.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
     'That is a resounding no',
     'It is not looking likely',
     'Too hard to tell',
     'It is quite possible',
     'That is a definite yes!',
     'Maybe',
     'There is a good chance']
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name='Question', value=question, inline=False)
    embed.add_field(name='Answer', value=answer, inline=False)
    embed.set_thumbnail(url='https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png')
    embed.set_footer(text=(datetime.datetime.now()))
    await ctx.send(embed=embed)


@ADG.command(aliases=['slots', 'bet'])
async def slot(ctx):
    await ctx.message.delete()
    emojis = '🍎🍊🍐🍋🍉🍇🍓🍒'
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} All matchings, you won!"})))
    elif a == b or a == c or b == c:
        await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} 2 in a row, you won!"})))
    else:
        await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} No match, you lost"})))


@ADG.command()
async def joke(ctx):
    await ctx.message.delete()
    headers = {'Accept': 'application/json'}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://icanhazdadjoke.com', headers=headers) as req:
            r = await req.json()
    await ctx.send(r['joke'])


@ADG.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid):
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1
            channel = ADG.get_channel(int(channelid))
            await channel.send('!d bump')
            print(f"{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent" + Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}" + Fore.RESET)
            finally:
                e = None
                del e


@ADG.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=(discord.File(buff, f"{message}.wav")))


@ADG.command()
async def upper(ctx, *, message):
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)


@ADG.command(aliases=['guildpfp'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=(ctx.guild.name))
    em.set_image(url=(ctx.guild.icon_url))
    await ctx.send(embed=em)


@ADG.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx):
    await ctx.message.delete()
    for friend in ADG.user.friends:
        friendlist = friend.name + '#' + friend.discriminator
        with open('Backup/Friends.txt', 'a+') as f:
            f.write(friendlist + '\n')
    else:
        for block in ADG.user.blocked:
            blocklist = block.name + '#' + block.discriminator
            with open('Backup/Blocked.txt', 'a+') as f:
                f.write(blocklist + '\n')


@ADG.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel=None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=(first_message.content))
    embed.add_field(name='First Message', value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)


@ADG.command()
async def mac(ctx, mac):
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=(r.text), colour=14593471)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)


@ADG.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)


@ADG.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`")
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@ADG.command(aliases=['ethereum'])
async def eth(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`")
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)


@ADG.command()
async def topic(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id='random').text
    await ctx.send(topic)


@ADG.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f"{qa}\n{qor}\n{qb}")
    await ctx.send(embed=em)


@ADG.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post('https://hastebin.com/documents', data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")


@ADG.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")


@ADG.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/anal')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def erofeet(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/erofeet')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/feetg')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/Random_hentai_gif')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/boobs')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def tits(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/tits')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/blowjob')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/nsfw_neko_gif')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/les')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def feed(ctx, user: discord.User=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/feed')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def tickle(ctx, user: discord.User=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/tickle')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def slap(ctx, user: discord.User=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/slap')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def hug(ctx, user: discord.User=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/hug')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def smug(ctx, user: discord.User=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/smug')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def pat(ctx, user: discord.User=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/pat')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command()
async def kiss(ctx, user: discord.User=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/kiss')
    res = r.json()
    em = discord.Embed(description=(user.mention))
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)


@ADG.command(aliases=['proxy'])
async def proxies(ctx):
    await ctx.message.delete()
    file = open('Data/Http-proxies.txt', 'a+')
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)

    for p in proxies:
        file.write(p + '\n')
    else:
        file = open('Data/Https-proxies.txt', 'a+')
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)

        for p in proxies:
            file.write(p + '\n')
        else:
            file = open('Data/Socks4-proxies.txt', 'a+')
            res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
            proxies = []
            for proxy in res.text.split('\n'):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)

            for p in proxies:
                file.write(p + '\n')
            else:
                file = open('Data/Socks5-proxies.txt', 'a+')
                res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
                proxies = []
                for proxy in res.text.split('\n'):
                    proxy = proxy.strip()
                    if proxy:
                        proxies.append(proxy)
                else:
                    for p in proxies:
                        file.write(p + '\n')


@ADG.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send('`' + uptime + '`')

@ADG.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in ADG.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()


@ADG.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message,
      url=stream_url)
    await ADG.change_presence(activity=stream)


@ADG.command(name='soff', aliases=['status-off', 'Soff'])
async def statusoff(ctx):
    await SIX.change_presence(status=(discord.Status.online))
    await ctx.message.delete()


@ADG.command()
async def game(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await ADG.change_presence(activity=game)


@ADG.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await ADG.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening),
      name=message))


@ADG.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await ADG.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching),
      name=message))


@ADG.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in ADG.guilds:
        await guild.ack()


@ADG.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@ADG.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = '¯\\_(ツ)_/¯'
    await ctx.send(shrug)


@ADG.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@ADG.command()
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@ADG.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)


@ADG.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@ADG.command()
async def secret(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')

@ADG.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == ADG.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass


@ADG.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")


@ADG.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx):
    await ctx.message.delete()
    print(f"HWID: {Fore.CYAN}{hwid}" + Fore.RESET)


@ADG.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))


@ADG.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')


@ADG.command()
async def logout(ctx):
    await ctx.message.delete()
    await ADG.logout()


@ADG.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):
    await ctx.message.delete()
    btc_status.start()


@ADG.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx):
    await ctx.message.delete()
    Dump(ctx)


@ADG.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):
    await ctx.message.delete()
    Clear()
    startprint()


@ADG.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())


@ADG.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
    await ctx.message.delete()
    GmailBomber()


@ADG.command(aliases=["nuke", "wizz"])
async def destroy(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="ADG Runs You",
            description="ADG Was here LOL",
            reason="ADG On Top Pussy",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="ADG Was Here")
    for _i in range(250):
        await ctx.guild.create_role(name="ADG On Top Pussy", color=RandomColor())


@ADG.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)
            await user.send(message)
        except:
            pass

@ADG.command()
async def massban(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

@ADG.command()
async def masskick(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass

@ADG.command()
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return

@ADG.command()
async def masschannel(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@ADG.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@ADG.command()
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@ADG.command()
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@ADG.command()
async def hack(ctx, user: discord.User = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}\nHacked by: ADG```\n")


@ADG.command(aliases=['tokinfo', 'tdox'])
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
            await ctx.send("**Invalid token :c **")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
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



@ADG.command(aliases=["msniper"])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        ADG.msgsniper = True
        await ctx.send('`Message-Sniper is now` *on*')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        ADG.msgsniper = False
        await ctx.send('`Message-Sniper is now` *off*')


@ADG.event
async def on_message_delete(message):
    if message.author.id == ADG.user.id:
        return
    if ADG.msgsniper:
        if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "**" + str(discord.utils.escape_markdown(str(message.author))) + "**: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "**" + str(
                    discord.utils.escape_markdown(str(message.author))) + "**: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(ADG.sniped_message_dict) > 1000:
        ADG.sniped_message_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "**" + str(discord.utils.escape_markdown(str(message.author))) + "**: " + str(
            message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        ADG.sniped_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "**" + str(
            discord.utils.escape_markdown(str(message.author))) + "**: " + discord.utils.escape_mentions(
            message.content) + "\n\n**Attachments:**\n" + links
        ADG.sniped_message_dict.update({channel_id: message_content})


@ADG.event
async def on_message_edit(before, after):
    if before.author.id == ADG.user.id:
        return
    if ADG.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "**" + str(
                    discord.utils.escape_markdown(str(before.author))) + "**: \n*BEFORE*\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n*LATER*\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "**" + str(
                    discord.utils.escape_markdown(str(before.author))) + "**: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(ADG.sniped_edited_message_dict) > 1000:
        ADG.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "**" + str(discord.utils.escape_markdown(str(before.author))) + "**: \n*BEFORE*\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n*LATER*\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        ADG.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "**" + str(
            discord.utils.escape_markdown(str(before.author))) + "**: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        ADG.sniped_edited_message_dict.update({channel_id: message_content})


@ADG.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in ADG.sniped_message_dict:
        await ctx.send(ADG.sniped_message_dict[currentChannel])
    else:
        await ctx.send("**No message to snipe goofy!**")


@ADG.command(aliases=["esnipe"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in ADG.sniped_edited_message_dict:
        await ctx.send(ADG.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("**No message to snipe gooofy!**")


@ADG.command()
async def ogav(ctx, *, user: discord.User = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))



if __name__ == '__main__':
    Init()





