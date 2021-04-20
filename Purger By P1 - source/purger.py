import discord, asyncio
from os import system
import shutil, subprocess, socket, sys, discord, base64, mysql.connector, threading, requests
from tpblite import TPB
from sys import argv
import psutil, logging
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system
import json
init()
system('@echo off')
system('cls')
system('mode con: cols=105 lines=30')
system('title @p1_loll')

def logo():
    try:
        print(Fore.LIGHTYELLOW_EX)
        msg = '\n ██▓███   █    ██  ██▀███    ▄████ ▓█████  ██▀███  \n▓██░  ██▒ ██  ▓██▒▓██ ▒ ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒\n▓██░ ██▓▒▓██  ▒██░▓██ ░▄█ ▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒\n▒██▄█▓▒ ▒▓▓█  ░██░▒██▀▀█▄  ░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  \n▒██▒ ░  ░▒▒█████▓ ░██▓ ▒██▒░▒▓███▀▒░▒████▒░██▓ ▒██▒\n▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░\n░▒ ░     ░░▒░ ░ ░   ░▒ ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░\n░░        ░░░ ░ ░   ░░   ░ ░ ░   ░    ░     ░░   ░ \n            ░        ░           ░    ░  ░   ░\n\n        '
        for l in msg:
            print(l, end='')

    except KeyboardInterrupt:
        sys.exit()


logo()
print(Fore.RESET)
print('  ')
print('{}╔═════ Commands ═══════════════════════════════╗{}'.format(Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX))
print('{}║ [1] glee :{} (purges your msgs)'.format(Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX))
print('{}║ [2] gleegc :{} (leaves all the groups ur in))'.format(Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX))
print('{}╚══════════════════════════════════════════════╝{}'.format(Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX))
print('  ')
client = discord.Client()
with open('config.json') as f:
    config = json.load(f)
    token = config.get('token')

def murder(cmd):
    subprocess.call(cmd, shell=True)


@client.event
async def on_ready():
    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print('PurgerW')
        print('P1 Made This')
        print()
        print('Logged in as: {0}'.format(client.user))
        print()

    ui()


@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == ' ':
                commands.append(message.content[z:index])
                z = index + 1
        else:
            commands.append(message.content[z:])
            channel = message.channel
            if commands[0] == 'glee':
                if len(commands) == 1:
                    async for msg in channel.history(limit=9999):
                        if msg.author == client.user:
                            try:
                                await msg.delete()
                            except Exception as x:
                                try:
                                    pass
                                finally:
                                    x = None
                                    del x

        if commands[0] == 'gleegc':
            await message.delete()
            count = 0
            for channel in client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if channel.id != message.channel.id:
                        count = count + 1
                        await channel.leave()


client.run(token, bot=False)