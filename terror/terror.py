import requests 
import os 
import threading 
import time 
import subprocess 
import hashlib 
import sys 
from random import choice 
from time import strftime ,gmtime 
import subprocess ,requests ,time ,os 

tokens =[]
proxies =[]
lock =threading .Lock ()
class Fore ():
    BLACK =
    RED =
    GREEN =
    YELLOW =
    BLUE =
    MAGENTA =
    CYAN =
    WHITE =
    RESET =
    LIGHTBLACK_EX =
    LIGHTRED_EX =
    LIGHTGREEN_EX =
    LIGHTYELLOW_EX = 
    LIGHTBLUE_EX =
    LIGHTMAGENTA_EX =
    LIGHTCYAN_EX =
    LIGHTWHITE_EX =
class Proxyless :
    def ChangeName (O00O0OOOOOOO0OOOO ,OO0OO0OOO0OOO00O0 ,OO0O0000O000O0O00 ):
        O0O0O0OO0OO000OO0 =requests .patch (f'https://discordapp.com/api/v8/guilds/{OO0OO0OOO0OOO00O0}/members/%40me/nick',headers ={'Authorization':O00O0OOOOOOO0OOOO },json ={'nick':OO0O0000O000O0O00 }).text 
        if OO0O0000O000O0O00 in O0O0O0OO0OO000OO0 :
            print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Changed Username.')
        elif 'You are being rate limited.'in O0O0O0OO0OO000OO0 :
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')
        else ::66
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O0O0O0OO0OO000OO0}'):
    def JoinServer (OO0OOOOOO0O000O00 ,O0O0OOO0OOO0O00OO ):
        O0OO0O00O000O0OOO =requests .post (f'https://discordapp.com/api/v8/invites/{O0O0OOO0OOO0O00OO}',headers ={'Authorization':OO0OOOOOO0O000O00 }).text 
        if 'You need to verify your account'in O0OO0O00O000O0OOO :
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {OO0OOOOOO0O000O00}')
        elif 'Unauthorized'in O0OO0O00O000O0OOO :
            print (f'[\033[94m{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {OO0OOOOOO0O000O00}')
        elif 'banned from this guild'in O0OO0O00O000O0OOO :
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Banned From Server.')
        elif 'Maximum number of guilds reached'in O0OO0O00O000O0OOO :
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] User Already In 100 Servers.')
        elif 'vanity_url_code'in O0OO0O00O000O0OOO :
            print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Joined Server.')
        elif 'You are being rate limited.'in O0OO0O00O000O0OOO :
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')
        else :
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O0OO0O00O000O0OOO}')
    def LeaveServer (O0000OO0O0O0OOOOO ,O0OOO0OOOOO000O00 ):
        O0OOOO000000OO0O0 =requests .delete (f'https://discordapp.com/api/v8/users/@me/guilds/{O0OOO0OOOOO000O00}',headers ={'Authorization':O0000OO0O0O0OOOOO })
        if O0OOOO000000OO0O0 .status_code ==204 :
            print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Left Server.')
        elif 'Unauthorized'in O0OOOO000000OO0O0 .text :
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O0000OO0O0O0OOOOO}')
        elif 'You need to verify your account'in O0OOOO000000OO0O0 .text :
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O0000OO0O0O0OOOOO}')
        elif 'You are being rate limited.'in O0OOOO000000OO0O0 .text :
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')
        else :
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O0OOOO000000OO0O0.text}')
    def SendMessage (OOO0OO000OOO0OOOO ,O000OOOO000OO00OO ,OO0O00OOOO0000O00 ):
        OOOOOOOO0O00O0OOO =requests .post (f'https://discordapp.com/api/v8/channels/{O000OOOO000OO00OO}/messages',headers ={'Authorization':OOO0OO000OOO0OOOO },json ={'content':OO0O00OOOO0000O00 }).text 
        if 'content'in OOOOOOOO0O00O0OOO :
            print (f'[\033[94m{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Sent Message.')
        elif 'You need to verify your account'in OOOOOOOO0O00O0OOO :
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {OOO0OO000OOO0OOOO}')
        elif 'Unauthorized'in OOOOOOOO0O00O0OOO :
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {OOO0OO000OOO0OOOO}')#line:103
        elif 'Missing Access'in OOOOOOOO0O00O0OOO :#line:104
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Missing Permissions.')#line:105
        elif 'You are being rate limited.'in OOOOOOOO0O00O0OOO :#line:106
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:107
        else :#line:108
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {OOOOOOOO0O00O0OOO}')#line:109
    def SendDirectMessage (O00O0OO00OO0O0000 ,OOOOO0OOOOO0O00OO ,OOO00OOOO00OOO0OO ):#line:110
        O0OOOO0O00OO0OO0O =requests .post ('https://discordapp.com/api/v8/users/@me/channels',headers ={'Authorization':O00O0OO00OO0O0000 },json ={"recipient_id":OOOOO0OOOOO0O00OO })#line:111
        if 'id'in O0OOOO0O00OO0OO0O .text :#line:112
            O00O0OO0OO00OOOO0 =O0OOOO0O00OO0OO0O .json ()['id']#line:113
            O0O0O000000O0OO00 =requests .post (f'https://discordapp.com/api/v8/channels/{O00O0OO0OO00OOOO0}/messages',headers ={'Authorization':O00O0OO00OO0O0000 },json ={'content':OOO00OOOO00OOO0OO }).text 
            if 'content'in O0O0O000000O0OO00 .text :#line:115
                print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Sent Direct Message.')#line:116
            elif 'Missing Access'in O0O0O000000O0OO00 .text :#line:117
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Unable To Send Direct Message.')#line:118
            elif 'You are being rate limited.'in O0O0O000000O0OO00 .text :#line:119
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:120
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O0O0O000000O0OO00.text}')#line:121
        elif 'Unauthorized'in O0OOOO0O00OO0OO0O .text :#line:122
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O00O0OO00OO0O0000}')#line:123
        elif 'You need to verify your account'in O0OOOO0O00OO0OO0O .text :#line:124
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O00O0OO00OO0O0000}')#line:125
        elif 'You are being rate limited.'in O0OOOO0O00OO0OO0O .text :#line:126
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:127
        else :#line:128
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O0OOOO0O00OO0OO0O.text}')#line:129
    def SendFriendRequest (OOO000OOO000O00O0 ,OOOO0O000O00O0OO0 ):#line:130
        OOO0OO00O000OO00O =requests .put (f'https://discordapp.com/api/v8/users/@me/relationships/{OOOO0O000O00O0OO0}',headers ={'Authorization':OOO000OOO000O00O0 },json ={})#line:131
        if OOO0OO00O000OO00O .status_code ==204 :#line:132
            print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Sent Friend Request.')#line:133
        elif 'Cannot send friend request to self'in OOO0OO00O000OO00O .text :#line:134
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] You Cannot Add Yourself.')#line:135
        elif 'Unauthorized'in OOO0OO00O000OO00O .text :#line:136
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {OOO000OOO000O00O0}')#line:137
        elif 'You need to verify your account'in OOO0OO00O000OO00O .text :#line:138
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {OOO000OOO000O00O0}')#line:139
        elif 'You are being rate limited.'in OOO0OO00O000OO00O .text :#line:140
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:141
        else :#line:142
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {OOO0OO00O000OO00O.text}')#line:143
    def RemoveFriendRequest (O00O0OOOO0O0OOOOO ,OO000O00OO00O0000 ):#line:144
        O00OOO0000OOOOO0O =requests .delete (f'https://discordapp.com/api/v8/users/@me/relationships/{OO000O00OO00O0000}',headers ={'Authorization':O00O0OOOO0O0OOOOO })#line:145
        if O00OOO0000OOOOO0O .status_code ==204 :#line:146
            print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Removed Friend Request.')#line:147
        elif 'Unauthorized'in O00OOO0000OOOOO0O .text :#line:148
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O00O0OOOO0O0OOOOO}')#line:149
        elif 'You need to verify your account'in O00OOO0000OOOOO0O .text :#line:150
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O00O0OOOO0O0OOOOO}')#line:151
        elif 'You are being rate limited.'in O00OOO0000OOOOO0O .text :#line:152
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:153
        else :#line:154
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O00OOO0000OOOOO0O.text}')#line:155
    def ReactToMessage (O00OO0OO0O0OOOO0O ,O0O00OOO0O0O000OO ):#line:156
        OOO0O0O00000OO0OO =requests .put (O0O00OOO0O0O000OO ,headers ={'Authorization':O00OO0OO0O0OOOO0O })#line:157
        if OOO0O0O00000OO0OO .status_code ==204 :#line:158
            print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Reacted To Message.')#line:159
        elif 'Unauthorized'in OOO0O0O00000OO0OO .text :#line:160
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O00OO0OO0O0OOOO0O}')#line:161
        elif 'You need to verify your account'in OOO0O0O00000OO0OO .text :#line:162
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O00OO0OO0O0OOOO0O}')#line:163
        elif 'You are being rate limited.'in OOO0O0O00000OO0OO .text :#line:164
            print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:165
        else :#line:166
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {OOO0O0O00000OO0OO.text}')#line:167
    def CheckToken (OO0O0O0OO0000OOOO ):#line:168
        OOOO00O0OO00O0OO0 =requests .get ('https://discordapp.com/api/v8/users/@me',headers ={'Authorization':OO0O0O0OO0000OOOO })#line:169
        if "id"in OOOO00O0OO00O0OO0 .text :#line:170
            OO0OOO0000OOO0OO0 =OOOO00O0OO00O0OO0 .json ()['verified']#line:171
            if OO0OOO0000OOO0OO0 ==False :#line:172
                O000O000O0OOO0O0O ='Unverified'#line:173
            if OO0OOO0000OOO0OO0 ==True :#line:174
                O000O000O0OOO0O0O ='Verified'#line:175
            try :#line:176
                O0OOO00OO0O0O0O0O =OOOO00O0OO00O0OO0 .json ()['premium_type']#line:177
                if O0OOO00OO0O0O0O0O ==1 :#line:178
                    OOO0O00O00OOO0O0O ='Nitro Classic'#line:179
                if O0OOO00OO0O0O0O0O ==2 :#line:180
                    OOO0O00O00OOO0O0O ='Nitro Boost'#line:181
            except :#line:182
                OOO0O00O00OOO0O0O ='No Subscription'#line:183
            with open ('Valid.txt','a+')as OOO0OO00O00000000 :#line:184
                OOO0OO00O00000000 .write (f'{OO0O0O0OO0000OOOO} - {O000O000O0OOO0O0O} - {OOO0O00O00OOO0O0O}\n')#line:185
                OOO0OO00O00000000 .close ()#line:186
                if O000O000O0OOO0O0O =='Unverified':#line:187
                    print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] {O000O000O0OOO0O0O}     {Fore.GREEN}|{Fore.RESET} {OO0O0O0OO0000OOOO}')#line:188
                else :#line:189
                    print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] {O000O000O0OOO0O0O}       {Fore.GREEN}|{Fore.RESET} {OO0O0O0OO0000OOOO}')#line:190
        elif 'Unauthorized'in OOOO00O0OO00O0OO0 .text :#line:191
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token. {Fore.RED}|{Fore.RESET} {OO0O0O0OO0000OOOO}')#line:192
        else :#line:193
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR          {Fore.RED}|{Fore.RESET} {OOOO00O0OO00O0OO0.text}')#line:194
    def TokenInformation (OOO0O0000O0OO00O0 ):#line:195
        OOO000O0O000OO0O0 =requests .get ('https://discordapp.com/api/v8/users/@me',headers ={'Authorization':OOO0O0000O0OO00O0 })#line:196
        if OOO000O0O000OO0O0 .status_code ==200 :#line:197
            O0O00OOO0O0OO000O =OOO000O0O000OO0O0 .json ()['username']+'#'+OOO000O0O000OO0O0 .json ()['discriminator']#line:198
            O000O0OOOO0O00OO0 =OOO000O0O000OO0O0 .json ()['id']#line:199
            O0O00OOO0O0O0OO0O =OOO000O0O000OO0O0 .json ()['phone']#line:200
            O0O0OOO0O000OO000 =OOO000O0O000OO0O0 .json ()['email']#line:201
            OOO0O0OO0OOO0OOOO =OOO000O0O000OO0O0 .json ()['mfa_enabled']#line:202
            print (f'''
[\033[94mUser ID{Fore.RESET}]         {O000O0OOOO0O00OO0}
[\033[94mUser Name{Fore.RESET}]       {O0O00OOO0O0OO000O}
[\033[94m2 Factor{Fore.RESET}]        {OOO0O0OO0OOO0OOOO}

[\033[94mEmail{Fore.RESET}]           {O0O0OOO0O000OO000}
[\033[94mPhone number{Fore.RESET}]    {O0O00OOO0O0O0OO0O if O0O00OOO0O0O0OO0O else "No Phone Number."}
[\033[94mToken{Fore.RESET}]           {OOO0O0000O0OO00O0}''')#line:210
        else :#line:211
            print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {OOO0O0000O0OO00O0}')#line:212
class Proxies :#line:213
    def ChangeName (O00O0O000000OOO00 ,O0OO000OOOOO0O0OO ,OOO00OO0OOO0OOO0O ,OO0OO0OO00O00O00O ):#line:214
        try :#line:215
            OO0O0O00O0O00O0OO =requests .patch (f'https://discordapp.com/api/v8/guilds/{OOO00OO0OOO0OOO0O}/members/%40me/nick',headers ={'Authorization':O0OO000OOOOO0O0OO },json ={'nick':OO0OO0OO00O00O00O },proxies ={'http':'%s://%s'%(O00O0O000000OOO00 .lower (),choice (proxies ))},timeout =5 ).text #line:216
            if OO0OO0OO00O00O00O in OO0O0O00O0O00O0OO :#line:217
                print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Changed Username.')#line:218
            elif 'You are being rate limited.'in OO0O0O00O0O00O0OO :#line:219
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:220
            else :#line:221
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {OO0O0O00O0O00O0OO}')#line:222
        except :#line:223
            Proxies .ChangeName (O00O0O000000OOO00 ,O0OO000OOOOO0O0OO ,OOO00OO0OOO0OOO0O ,OO0OO0OO00O00O00O )#line:224
    def JoinServer (O0O0O0O0OO00OO000 ,O0O00OO00OOOOO0O0 ,OO0000O0OO0OO0O00 ):#line:225
        try :#line:226
            OOOO0O0OO0000O00O =requests .post (f'https://discordapp.com/api/v8/invites/{OO0000O0OO0OO0O00}',headers ={'Authorization':O0O00OO00OOOOO0O0 },proxies ={'http':'%s://%s'%(O0O0O0O0OO00OO000 .lower (),choice (proxies ))},timeout =5 ).text #line:227
            if 'You need to verify your account'in OOOO0O0OO0000O00O :#line:228
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O0O00OO00OOOOO0O0}')#line:229
            elif 'Unauthorized'in OOOO0O0OO0000O00O :#line:230
                print (f'[\033[94m{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O0O00OO00OOOOO0O0}')#line:231
            elif 'banned from this guild'in OOOO0O0OO0000O00O :#line:232
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Banned From Server.')#line:233
            elif 'Maximum number of guilds reached'in OOOO0O0OO0000O00O :#line:234
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] User Already In 100 Servers.')#line:235
            elif 'vanity_url_code'in OOOO0O0OO0000O00O :#line:236
                print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Joined Server.')#line:237
            elif 'You are being rate limited.'in OOOO0O0OO0000O00O :#line:238
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:239
            else :#line:240
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {OOOO0O0OO0000O00O}')#line:241
        except :#line:242
            Proxies .JoinServer (O0O0O0O0OO00OO000 ,O0O00OO00OOOOO0O0 ,OO0000O0OO0OO0O00 )#line:243
    def LeaveServer (O00O0O0000OOOO0OO ,OO0000000OO000O0O ,O0OOOO0OOOOOOOOO0 ):#line:244
        try :#line:245
            O00OOOO0000000OOO =requests .delete (f'https://discordapp.com/api/v8/users/@me/guilds/{O0OOOO0OOOOOOOOO0}',headers ={'Authorization':OO0000000OO000O0O },proxies ={'http':'%s://%s'%(O00O0O0000OOOO0OO .lower (),choice (proxies ))},timeout =5 )#line:246
            if O00OOOO0000000OOO .status_code ==204 :#line:247
                print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Left Server.')#line:248
            elif 'Unauthorized'in O00OOOO0000000OOO .text :#line:249
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {OO0000000OO000O0O}')#line:250
            elif 'You need to verify your account'in O00OOOO0000000OOO .text :#line:251
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {OO0000000OO000O0O}')#line:252
            elif 'You are being rate limited.'in O00OOOO0000000OOO .text :#line:253
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:254
            else :#line:255
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O00OOOO0000000OOO.text}')#line:256
        except :#line:257
            Proxies .LeaveServer (O00O0O0000OOOO0OO ,OO0000000OO000O0O ,O0OOOO0OOOOOOOOO0 )#line:258
    def SendMessage (OOO0OO0000OO00O0O ,O0OO0000OOO0OO00O ,OOO0000O00O0OO000 ,O0O00O0OOO0O0000O ):#line:259
        try :#line:260
            O00O000O0O0O0000O =requests .post (f'https://discordapp.com/api/v8/channels/{OOO0000O00O0OO000}/messages',headers ={'Authorization':O0OO0000OOO0OO00O },json ={'content':O0O00O0OOO0O0000O },proxies ={'http':'%s://%s'%(OOO0OO0000OO00O0O .lower (),proxy )},timeout =5 ).text #line:261
            if 'content'in O00O000O0O0O0000O :#line:262
                print (f'[\033[94m{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Sent Message.')#line:263
            elif 'You need to verify your account'in O00O000O0O0O0000O :#line:264
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O0OO0000OOO0OO00O}')#line:265
            elif 'Unauthorized'in O00O000O0O0O0000O :#line:266
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O0OO0000OOO0OO00O}')#line:267
            elif 'Missing Access'in O00O000O0O0O0000O :#line:268
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Missing Permissions.')#line:269
            elif 'You are being rate limited.'in O00O000O0O0O0000O :#line:270
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:271
            else :#line:272
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O00O000O0O0O0000O}')#line:273
        except :#line:274
            Proxies .SendMessage (OOO0OO0000OO00O0O ,O0OO0000OOO0OO00O ,OOO0000O00O0OO000 ,O0O00O0OOO0O0000O )#line:275
    def SendDirectMessage (OO0O000OO0O00O0O0 ,O0O0OOOOOOOO0OO0O ,O00OOO0O00OO0OOOO ,O0OO0OO0O0O0OO00O ):#line:276
        try :#line:277
            O00O00OO000O000OO =requests .post ('https://discordapp.com/api/v8/users/@me/channels',headers ={'Authorization':O0O0OOOOOOOO0OO0O },json ={"recipient_id":O00OOO0O00OO0OOOO },proxies ={'http':'%s://%s'%(OO0O000OO0O00O0O0 .lower (),choice (proxies ))},timeout =5 )#line:278
            if 'id'in O00O00OO000O000OO .text :#line:279
                OOOOO00OOO0000O0O =O00O00OO000O000OO .json ()['id']#line:280
                O0O00OO000OO0OO00 =requests .post (f'https://discordapp.com/api/v8/channels/{OOOOO00OOO0000O0O}/messages',headers ={'Authorization':O0O0OOOOOOOO0OO0O },json ={'content':O0OO0OO0O0O0OO00O },proxies ={'http':'%s://%s'%(OO0O000OO0O00O0O0 .lower (),choice (proxies ))},timeout =5 ).text #line:281
                if 'content'in O0O00OO000OO0OO00 .text :#line:282
                    print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Sent Direct Message.')#line:283
                elif 'Missing Access'in O0O00OO000OO0OO00 .text :#line:284
                    print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Unable To Send Direct Message.')#line:285
                elif 'You are being rate limited.'in O0O00OO000OO0OO00 .text :#line:286
                    print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:287
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O0O00OO000OO0OO00.text}')#line:288
            elif 'Unauthorized'in O00O00OO000O000OO .text :#line:289
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O0O0OOOOOOOO0OO0O}')#line:290
            elif 'You need to verify your account'in O00O00OO000O000OO .text :#line:291
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O0O0OOOOOOOO0OO0O}')#line:292
            elif 'You are being rate limited.'in O00O00OO000O000OO .text :#line:293
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:294
            else :#line:295
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O00O00OO000O000OO.text}')#line:296
        except :#line:297
            Proxies .SendDirectMessage (OO0O000OO0O00O0O0 ,O0O0OOOOOOOO0OO0O ,O00OOO0O00OO0OOOO ,O0OO0OO0O0O0OO00O )#line:298
    def SendFriendRequest (O0OO000O0O00OO0O0 ,O00OOO000O00000OO ,O00O00000O0O00OO0 ):#line:299
        try :#line:300
            O0O0OO0O0OO0OO0O0 =requests .put (f'https://discordapp.com/api/v8/users/@me/relationships/{O00O00000O0O00OO0}',headers ={'Authorization':O00OOO000O00000OO },json ={},proxies ={'http':'%s://%s'%(O0OO000O0O00OO0O0 .lower (),choice (proxies ))},timeout =5 )#line:301
            if O0O0OO0O0OO0OO0O0 .status_code ==204 :#line:302
                print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Sent Friend Request.')#line:303
            elif 'Cannot send friend request to self'in O0O0OO0O0OO0OO0O0 .text :#line:304
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] You Cannot Add Yourself.')#line:305
            elif 'Unauthorized'in O0O0OO0O0OO0OO0O0 .text :#line:306
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O00OOO000O00000OO}')#line:307
            elif 'You need to verify your account'in O0O0OO0O0OO0OO0O0 .text :#line:308
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O00OOO000O00000OO}')#line:309
            elif 'You are being rate limited.'in O0O0OO0O0OO0OO0O0 .text :#line:310
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:311
            else :#line:312
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O0O0OO0O0OO0OO0O0.text}')#line:313
        except :#line:314
            Proxies .SendFriendRequest (O0OO000O0O00OO0O0 ,O00OOO000O00000OO ,O00O00000O0O00OO0 )#line:315
    def RemoveFriendRequest (OO0O00O0OO0OO0O0O ,OOO0O0O00O0OO0000 ,OOOOO0OOOOO00O0OO ):#line:316
        try :#line:317
            OO0000O0O000O0OO0 =requests .delete (f'https://discordapp.com/api/v8/users/@me/relationships/{OOOOO0OOOOO00O0OO}',headers ={'Authorization':OOO0O0O00O0OO0000 },proxies ={'http':'%s://%s'%(OO0O00O0OO0OO0O0O .lower (),choice (proxies ))},timeout =5 )
            if OO0000O0O000O0OO0 .status_code ==204 :#line:319
                print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Removed Friend Request.')#line:320
            elif 'Unauthorized'in OO0000O0O000O0OO0 .text :#line:321
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {OOO0O0O00O0OO0000}')#line:322
            elif 'You need to verify your account'in OO0000O0O000O0OO0 .text :#line:323
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {OOO0O0O00O0OO0000}')#line:324
            elif 'You are being rate limited.'in OO0000O0O000O0OO0 .text :#line:325
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:326
            else :#line:327
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {OO0000O0O000O0OO0.text}')#line:328
        except :#line:329
            Proxies .RemoveFriendRequest (OO0O00O0OO0OO0O0O ,OOO0O0O00O0OO0000 ,OOOOO0OOOOO00O0OO )#line:330
    def ReactToMessage (O0O0O00OO0OO0O0OO ,O0000O0OO0OO000O0 ,OOO00OOO0OO0O0000 ):#line:331
        try :#line:332
            O0O0O0OOOO00OO000 =requests .put (OOO00OOO0OO0O0000 ,headers ={'Authorization':O0000O0OO0OO000O0 },proxies ={'http':'%s://%s'%(O0O0O00OO0OO0O0OO .lower (),choice (proxies ))},timeout =5 )
            if O0O0O0OOOO00OO000 .status_code ==204 :#line:334
                print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Reacted To Message.')#line:335
            elif 'Unauthorized'in O0O0O0OOOO00OO000 .text :#line:336
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {O0000O0OO0OO000O0}')#line:337
            elif 'You need to verify your account'in O0O0O0OOOO00OO000 .text :#line:338
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Account Not Verified. {Fore.YELLOW}|{Fore.RESET} {O0000O0OO0OO000O0}')#line:339
            elif 'You are being rate limited.'in O0O0O0OOOO00OO000 .text :#line:340
                print (f'[{Fore.YELLOW}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Ratelimited.')#line:341
            else :#line:342
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR                 {Fore.RED}|{Fore.RESET} {O0O0O0OOOO00OO000.text}')#line:343
        except :#line:344
            Proxies .ReactToMessage (O0O0O00OO0OO0O0OO ,O0000O0OO0OO000O0 ,OOO00OOO0OO0O0000 )#line:345
    def CheckToken (OO000OO0O0O0OO0O0 ,OO0OO0OO0OO0000OO ):#line:346
        try :#line:347
            OOOOO000OO0O0OO0O =requests .get ('https://discordapp.com/api/v8/users/@me',headers ={'Authorization':OO0OO0OO0OO0000OO },proxies ={'http':'%s://%s'%(OO000OO0O0O0OO0O0 .lower (),choice (proxies ))},timeout =5 )
            if "id"in OOOOO000OO0O0OO0O .text :#line:349
                O00O0O00OO0O00OOO =OOOOO000OO0O0OO0O .json ()['verified']#line:350
                if O00O0O00OO0O00OOO ==False :#line:351
                    OOO0OOO0OO0OOOOOO ='Unverified'#line:352
                if O00O0O00OO0O00OOO ==True :#line:353
                    OOO0OOO0OO0OOOOOO ='Verified'#line:354
                try :#line:355
                    O00OO0OO0OO0O00OO =OOOOO000OO0O0OO0O .json ()['premium_type']#line:356
                    if O00OO0OO0OO0O00OO ==1 :#line:357
                        OOOOOOOO0OOO0O000 ='Nitro Classic'#line:358
                    if O00OO0OO0OO0O00OO ==2 :#line:359
                        OOOOOOOO0OOO0O000 ='Nitro Boost'#line:360
                except :#line:361
                    OOOOOOOO0OOO0O000 ='No Subscription'#line:362
                with open ('Valid.txt','a+')as O000000O0OO0O0O0O :#line:363
                    O000000O0OO0O0O0O .write (f'{OO0OO0OO0OO0000OO} - {OOO0OOO0OO0OOOOOO} - {OOOOOOOO0OOO0O000}\n')#line:364
                    O000000O0OO0O0O0O .close ()#line:365
                    if OOO0OOO0OO0OOOOOO =='Unverified':#line:366
                        print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] {OOO0OOO0OO0OOOOOO}     {Fore.GREEN}|{Fore.RESET} {OO0OO0OO0OO0000OO}')#line:367
                    else :#line:368
                        print (f'[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] {OOO0OOO0OO0OOOOOO}       {Fore.GREEN}|{Fore.RESET} {OO0OO0OO0OO0000OO}')#line:369
            elif 'Unauthorized'in OOOOO000OO0O0OO0O .text :#line:370
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token. {Fore.RED}|{Fore.RESET} {OO0OO0OO0OO0000OO}')#line:371
            else :#line:372
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] ERROR          {Fore.RED}|{Fore.RESET} {OOOOO000OO0O0OO0O.text}')#line:373
        except :#line:374
            Proxies .CheckToken (OO000OO0O0O0OO0O0 ,OO0OO0OO0OO0000OO )#line:375
    def TokenInformation (O00OO0OOO0O0OOOOO ,OO0O00000OO000O00 ):#line:376
        try :#line:377
            O0OO00000000OOO00 =requests .get ('https://discordapp.com/api/v8/users/@me',headers ={'Authorization':OO0O00000OO000O00 },proxies ={'http':'%s://%s'%(O00OO0OOO0O0OOOOO .lower (),choice (proxies ))},timeout =5 )
            if O0OO00000000OOO00 .status_code ==200 :#line:379
                O00O00OOO00OOOOOO =O0OO00000000OOO00 .json ()['username']+'#'+O0OO00000000OOO00 .json ()['discriminator']#line:380
                O0O0O0OO0OO00000O =O0OO00000000OOO00 .json ()['id']#line:381
                OO00OOOO000O0O0OO =O0OO00000000OOO00 .json ()['phone']#line:382
                OOOO000O0OOO0OO00 =O0OO00000000OOO00 .json ()['email']#line:383
                O00O0O00000O0O0O0 =O0OO00000000OOO00 .json ()['mfa_enabled']#line:384
                print (f'''
[{Fore.MAGENTA}User ID{Fore.RESET}]         {O0O0O0OO0OO00000O}
[{Fore.MAGENTA}User Name{Fore.RESET}]       {O00O00OOO00OOOOOO}
[{Fore.MAGENTA}2 Factor{Fore.RESET}]        {O00O0O00000O0O0O0}

[{Fore.MAGENTA}{Fore.RESET}]           {OOOO000O0OOO0OO00}
[{Fore.MAGENTA}Phone number{Fore.RESET}]    {OO00OOOO000O0O0OO if OO00OOOO000O0O0OO else "No Phone Number."}
[{Fore.MAGENTA}Token{Fore.RESET}]           {OO0O00000OO000O00}''')#line:392
            else :#line:393
                print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token.        {Fore.RED}|{Fore.RESET} {OO0O00000OO000O00}')#line:394
        except :#line:395
            Proxies .TokenInformation (O00OO0OOO0O0OOOOO ,OO0O00000OO000O00 )#line:396
class ProxyEngine :#line:397
    def ChangeNickname (OOOO0OO0O000OO0O0 ,O00OOOO0O0O0OO00O ):#line:398
        OO0OOOOO00O0OOOOO =0 #line:399
        O0OOO0O0O00O00O00 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:400
        if O0OOO0O0O00O00O00 =='HTTP'or O0OOO0O0O00O00O00 =='SOCKS4'or O0OOO0O0O00O00O00 =='SOCKS5':#line:401
            OOOOOO0000OO00O00 =len (tokens )#line:402
            while True :#line:403
                try :#line:404
                    if threading .active_count ()<OOOOOO0000OO00O00 :#line:405
                        threading .Thread (target =Proxies .ChangeName ,args =(O0OOO0O0O00O00O00 ,tokens [OO0OOOOO00O0OOOOO ],OOOO0OO0O000OO0O0 ,O00OOOO0O0O0OO00O ,)).start ()#line:406
                        OO0OOOOO00O0OOOOO +=1 #line:407
                except IndexError :#line:408
                    break #line:409
        else :#line:410
            Menu ()#line:411
    def JoinServer (OOOO000O00000O000 ):#line:412
        O000000O0O00O00O0 =0 #line:413
        O000O0OOO0O00OO00 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:414
        if O000O0OOO0O00OO00 =='HTTP'or O000O0OOO0O00OO00 =='SOCKS4'or O000O0OOO0O00OO00 =='SOCKS5':#line:415
            OOO0OO000000O00OO =len (tokens )#line:416
            while True :#line:417
                try :#line:418
                    if threading .active_count ()<OOO0OO000000O00OO :#line:419
                        threading .Thread (target =Proxies .JoinServer ,args =(O000O0OOO0O00OO00 ,tokens [O000000O0O00O00O0 ],OOOO000O00000O000 ,)).start ()#line:420
                        O000000O0O00O00O0 +=1 #line:421
                except IndexError :#line:422
                    break #line:423
        else :#line:424
            Menu ()#line:425
    def LeaveServer (O000O000OO0OOOO0O ):#line:426
        O00OOOO0OOOO0O0OO =0 #line:427
        OO0OO0OO0O0OOO00O =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:428
        if OO0OO0OO0O0OOO00O =='HTTP'or OO0OO0OO0O0OOO00O =='SOCKS4'or OO0OO0OO0O0OOO00O =='SOCKS5':#line:429
            O0O000OO0O0O00OOO =len (tokens )#line:430
            while True :#line:431
                try :#line:432
                    if threading .active_count ()<O0O000OO0O0O00OOO :#line:433
                        threading .Thread (target =Proxies .LeaveServer ,args =(OO0OO0OO0O0OOO00O ,tokens [O00OOOO0OOOO0O0OO ],O000O000OO0OOOO0O ,)).start ()#line:434
                        O00OOOO0OOOO0O0OO +=1 #line:435
                except IndexError :#line:436
                    break #line:437
        else :#line:438
            Menu ()#line:439
    def SendMessage (O00OO0000OO00OO0O ,O0000OOOO000000O0 ):#line:440
        OO0OO00000OO0OO00 =0 #line:441
        O00O0O0OOOOOO0OOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:442
        if O00O0O0OOOOOO0OOO =='HTTP'or O00O0O0OOOOOO0OOO =='SOCKS4'or O00O0O0OOOOOO0OOO =='SOCKS5':#line:443
            O00O0OO0OO00OO0OO =len (tokens )#line:444
            while True :#line:445
                try :#line:446
                    if threading .active_count ()<O00O0OO0OO00OO0OO :#line:447
                        threading .Thread (target =Proxies .SendMessage ,args =(O00O0O0OOOOOO0OOO ,tokens [OO0OO00000OO0OO00 ],O00OO0000OO00OO0O ,O0000OOOO000000O0 ,)).start ()#line:448
                        OO0OO00000OO0OO00 +=1 #line:449
                except IndexError :#line:450
                    OO0OO00000OO0OO00 =0 #line:451
        else :#line:452
            Menu ()#line:453
    def SendDirectMessage (O0000O0000O0O0OOO ,O00OOO000O0O0O000 ):#line:454
        OOOOO0000000OOO0O =0 #line:455
        OO0O000OOO0OOOOO0 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:456
        if OO0O000OOO0OOOOO0 =='HTTP'or OO0O000OOO0OOOOO0 =='SOCKS4'or OO0O000OOO0OOOOO0 =='SOCKS5':#line:457
            O0O00OOOO0000O0OO =len (tokens )#line:458
            while True :#line:459
                try :#line:460
                    if threading .active_count ()<O0O00OOOO0000O0OO :#line:461
                        threading .Thread (target =Proxies .SendDirectMessage ,args =(OO0O000OOO0OOOOO0 ,tokens [OOOOO0000000OOO0O ],O0000O0000O0O0OOO ,O00OOO000O0O0O000 ,)).start ()#line:462
                        OOOOO0000000OOO0O +=1 #line:463
                except IndexError :#line:464
                    break #line:465
        else :#line:466
            Menu ()#line:467
    def SendFriendRequest (OO00O00OO0O0O000O ):#line:468
        OOO00OO00OO00O0OO =0 #line:469
        O000O000OOO0OOO00 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:470
        if O000O000OOO0OOO00 =='HTTP'or O000O000OOO0OOO00 =='SOCKS4'or O000O000OOO0OOO00 =='SOCKS5':#line:471
            O0O0O00O0OOOO00OO =len (tokens )#line:472
            while True :#line:473
                try :#line:474
                    if threading .active_count ()<O0O0O00O0OOOO00OO :#line:475
                        threading .Thread (target =Proxies .SendFriendRequest ,args =(O000O000OOO0OOO00 ,tokens [OOO00OO00OO00O0OO ],OO00O00OO0O0O000O ,)).start ()#line:476
                        OOO00OO00OO00O0OO +=1 #line:477
                except IndexError :#line:478
                    break #line:479
        else :#line:480
            Menu ()#line:481
    def RemoveFriendRequest (O0OO0OO0OOO00O00O ):#line:482
        O0O000OOOOOO00OOO =0 #line:483
        OOO00OO00O000OOO0 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:484
        if OOO00OO00O000OOO0 =='HTTP'or OOO00OO00O000OOO0 =='SOCKS4'or OOO00OO00O000OOO0 =='SOCKS5':#line:485
            O00000OO0OOOOO0O0 =len (tokens )#line:486
            while True :#line:487
                try :#line:488
                    if threading .active_count ()<O00000OO0OOOOO0O0 :#line:489
                        threading .Thread (target =Proxies .RemoveFriendRequest ,args =(OOO00OO00O000OOO0 ,tokens [O0O000OOOOOO00OOO ],O0OO0OO0OOO00O00O ,)).start ()#line:490
                        O0O000OOOOOO00OOO +=1 #line:491
                except IndexError :#line:492
                    break #line:493
        else :#line:494
            Menu ()#line:495
    def ReactToMessage (OO0O000OO0O0000OO ):#line:496
        O000O00O0OO0O0O00 =0 #line:497
        OOO0O00O0O00OO0O0 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:498
        if OOO0O00O0O00OO0O0 =='HTTP'or OOO0O00O0O00OO0O0 =='SOCKS4'or OOO0O00O0O00OO0O0 =='SOCKS5':#line:499
            O0O0O00OOO0O00O0O =len (tokens )#line:500
            while True :#line:501
                try :#line:502
                    if threading .active_count ()<O0O0O00OOO0O00O0O :#line:503
                        threading .Thread (target =Proxies .ReactToMessage ,args =(OOO0O00O0O00OO0O0 ,tokens [O000O00O0OO0O0O00 ],OO0O000OO0O0000OO ,)).start ()#line:504
                        O000O00O0OO0O0O00 +=1 #line:505
                except IndexError :#line:506
                    break #line:507
        else :#line:508
            Menu ()#line:509
    def CheckToken ():#line:510
        OO0OOOO0OOO0000O0 =0 #line:511
        OOO000OOOO00000OO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:512
        if OOO000OOOO00000OO =='HTTP'or OOO000OOOO00000OO =='SOCKS4'or OOO000OOOO00000OO =='SOCKS5':#line:513
            OO000OOO00O00OOO0 =len (tokens )#line:514
            while True :#line:515
                try :#line:516
                    if threading .active_count ()<OO000OOO00O00OOO0 :#line:517
                        threading .Thread (target =Proxies .CheckToken ,args =(OOO000OOOO00000OO ,tokens [OO0OOOO0OOO0000O0 ],)).start ()#line:518
                        OO0OOOO0OOO0000O0 +=1 #line:519
                except IndexError :#line:520
                    break #line:521
        else :#line:522
            Menu ()#line:523
    def TokenInformation (O0O0000OOOO0O0O0O ):#line:524
        OOO0O0OOO00OOOO0O =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxy Type (HTTP, SOCKS4, SOCKS5): ')#line:525
        if OOO0O0OOO00OOOO0O =='HTTP'or OOO0O0OOO00OOOO0O =='SOCKS4'or OOO0O0OOO00OOOO0O =='SOCKS5':#line:526
            Proxies .TokenInformation (OOO0O0OOO00OOOO0O ,O0O0000OOOO0O0O0O )#line:527
        else :#line:528
            Menu ()#line:529
class Engine :#line:530
    def ChangeNickname (OOOO0O0O0O00O0OO0 ,OOOO0OOO0O0OOO00O ):#line:531
        OO0000O00O000OOO0 =0 #line:532
        O0O00OO0O0O000000 =len (tokens )#line:533
        while True :#line:534
            try :#line:535
                if threading .active_count ()<O0O00OO0O0O000000 :#line:536
                    threading .Thread (target =Proxyless .ChangeName ,args =(tokens [OO0000O00O000OOO0 ],OOOO0O0O0O00O0OO0 ,OOOO0OOO0O0OOO00O ,)).start ()#line:537
                    OO0000O00O000OOO0 +=1 #line:538
            except IndexError :#line:539
                break #line:540
    def JoinServer (OO00000O00O0O0O0O ):#line:541
        O0O00O0O0O0OO00OO =0 #line:542
        O0O0OO0000OO0O00O =len (tokens )#line:543
        while True :#line:544
            try :#line:545
                if threading .active_count ()<O0O0OO0000OO0O00O :#line:546
                    threading .Thread (target =Proxyless .JoinServer ,args =(tokens [O0O00O0O0O0OO00OO ],OO00000O00O0O0O0O ,)).start ()#line:547
                    O0O00O0O0O0OO00OO +=1 #line:548
            except IndexError :#line:549
                break #line:550
    def LeaveServer (OO0OO0O0O00OO0OOO ):#line:551
        O0OO0O00OOOO0O00O =0 #line:552
        O000OOO00O0O0O0OO =len (tokens )#line:553
        while True :#line:554
            try :#line:555
                if threading .active_count ()<O000OOO00O0O0O0OO :#line:556
                    threading .Thread (target =Proxyless .LeaveServer ,args =(tokens [O0OO0O00OOOO0O00O ],OO0OO0O0O00OO0OOO ,)).start ()#line:557
                    O0OO0O00OOOO0O00O +=1 #line:558
            except IndexError :#line:559
                break #line:560
    def SendMessage (O0000O0OOO000OO00 ,OOOO0000O0O0O00OO ):#line:561
        O00OO0O000OOO00OO =0 #line:562
        OO000OO0O00000OOO =len (tokens )#line:563
        while True :#line:564
            try :#line:565
                if threading .active_count ()<OO000OO0O00000OOO :#line:566
                    threading .Thread (target =Proxyless .SendMessage ,args =(tokens [O00OO0O000OOO00OO ],O0000O0OOO000OO00 ,OOOO0000O0O0O00OO ,)).start ()#line:567
                    O00OO0O000OOO00OO +=1 #line:568
            except IndexError :#line:569
                O00OO0O000OOO00OO =0 #line:570
    def SendDirectMessage (OO000OOOO000000O0 ,OO0OO00O0OOO000OO ):#line:571
        O0OOOO0OO0O000O00 =0 #line:572
        OOO00OOO0OO000OO0 =len (tokens )#line:573
        while True :#line:574
            try :#line:575
                if threading .active_count ()<OOO00OOO0OO000OO0 :#line:576
                    threading .Thread (target =Proxyless .SendDirectMessage ,args =(tokens [O0OOOO0OO0O000O00 ],OO000OOOO000000O0 ,OO0OO00O0OOO000OO ,)).start ()#line:577
                    O0OOOO0OO0O000O00 +=1 #line:578
            except IndexError :#line:579
                break #line:580
    def SendFriendRequest (OOOOOOOOO0O000O0O ):#line:581
        OOOO000OO0O00O00O =0 #line:582
        OOO0O0OO000O0O0O0 =len (tokens )#line:583
        while True :#line:584
            try :#line:585
                if threading .active_count ()<OOO0O0OO000O0O0O0 :#line:586
                    threading .Thread (target =Proxyless .SendFriendRequest ,args =(tokens [OOOO000OO0O00O00O ],OOOOOOOOO0O000O0O ,)).start ()#line:587
                    OOOO000OO0O00O00O +=1 #line:588
            except IndexError :#line:589
                break #line:590
    def RemoveFriendRequest (O00OOOO0000OOO00O ):#line:591
        O0OO00O0OO000OOOO =0 #line:592
        OO0O00OO0OOO00O0O =len (tokens )#line:593
        while True :#line:594
            try :#line:595
                if threading .active_count ()<OO0O00OO0OOO00O0O :#line:596
                    threading .Thread (target =Proxyless .RemoveFriendRequest ,args =(tokens [O0OO00O0OO000OOOO ],O00OOOO0000OOO00O ,)).start ()#line:597
                    O0OO00O0OO000OOOO +=1 #line:598
            except IndexError :#line:599
                break #line:600
    def ReactToMessage (O0O00OOOOO00O0O00 ):#line:601
        OO00OO00O0OO0OO00 =0 #line:602
        OOO0O00O00OOOO0O0 =len (tokens )#line:603
        while True :#line:604
            try :#line:605
                if threading .active_count ()<OOO0O00O00OOOO0O0 :#line:606
                    threading .Thread (target =Proxyless .ReactToMessage ,args =(tokens [OO00OO00O0OO0OO00 ],O0O00OOOOO00O0O00 ,)).start ()#line:607
                    OO00OO00O0OO0OO00 +=1 #line:608
            except IndexError :#line:609
                break #line:610
    def CheckToken ():#line:611
        OO0O0O000O000O0OO =0 #line:612
        O0000OO00000O00OO =len (tokens )#line:613
        while True :#line:614
            try :#line:615
                if threading .active_count ()<O0000OO00000O00OO :#line:616
                    threading .Thread (target =Proxyless .CheckToken ,args =(tokens [OO0O0O000O000O0OO ],)).start ()#line:617
                    OO0O0O000O000O0OO +=1 #line:618
            except IndexError :#line:619
                break #line:620
    def TokenInformation (OOOO0O0000O00OOOO ):#line:621
        Proxyless .TokenInformation (OOOO0O0000O00OOOO )#line:622
def Menu ():#line:623
    O00000O000O000O0O =0 #line:624
    os .system ('cls & title [Jelly Multitool] Made by Xelly and Clheyo ^')#line:625
    print (f'''
                                                  {Fore.LIGHTWHITE_EX} ╔╗╔═╗╔╗ ╔╗ ╔═╦╗
                                                 {Fore.WHITE}  ║║║╦╝║║ ║║ ╚╗║║
                                                  ╔╣║║╩╗║╚╗║╚╗╔╩╗║
                                                {Fore.MAGENTA}  ╚═╝╚═╝╚═╝╚═╝╚══╝
     
        {Fore.MAGENTA}╔═════════════════════════════════╗╔═════════════════════════════════╗╔═════════════════════════════════╗
        {Fore.MAGENTA}║ {Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}] Join Server                 {Fore.MAGENTA}║║ {Fore.RESET}[{Fore.MAGENTA}5{Fore.RESET}] Friend Requester            {Fore.MAGENTA}║║ {Fore.RESET}[{Fore.MAGENTA}9{Fore.RESET}] Direct Message Spammer      {Fore.MAGENTA}║
        {Fore.MAGENTA}║ {Fore.RESET}[{Fore.MAGENTA}2{Fore.RESET}] Leave Server                {Fore.MAGENTA}║║ {Fore.RESET}[{Fore.MAGENTA}6{Fore.RESET}] Friend Remover              {Fore.MAGENTA}║║ {Fore.RESET}[{Fore.MAGENTA}10{Fore.RESET}] Nickname Changer           {Fore.MAGENTA}║
        {Fore.MAGENTA}║ {Fore.RESET}[{Fore.MAGENTA}3{Fore.RESET}] Message Spammer             {Fore.MAGENTA}║║ {Fore.RESET}[{Fore.MAGENTA}7{Fore.RESET}] Token Check                 {Fore.MAGENTA}║║ {Fore.RESET}[{Fore.MAGENTA}11{Fore.RESET}] Credits                    {Fore.MAGENTA}║
        {Fore.MAGENTA}║ {Fore.RESET}[{Fore.MAGENTA}4{Fore.RESET}] React To Message            {Fore.MAGENTA}║║ {Fore.RESET}[{Fore.MAGENTA}8{Fore.RESET}] Token Infomation            {Fore.MAGENTA}║║ {Fore.RESET}[{Fore.MAGENTA}12{Fore.RESET}] Exit                       {Fore.MAGENTA}║
        {Fore.MAGENTA}╚═════════════════════════════════╝╚═════════════════════════════════╝╚═════════════════════════════════╝''')#line:636
    O00O0O0OOO0OOO0OO =input (f'\n{Fore.RESET}[{Fore.MAGENTA}?{Fore.RESET}] ')#line:637
    if O00O0O0OOO0OOO0OO =='1':#line:638
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:639
        if OOO0OO00OO0OOOOOO =='Yes':#line:640
            OOOO000O00O00OOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Invite{Fore.MAGENTA}:{Fore.RESET} discord.gg/')#line:641
            print ()#line:642
            ProxyEngine .JoinServer (OOOO000O00O00OOOO )#line:643
            time .sleep (5 )#line:644
            Menu ()#line:645
        elif OOO0OO00OO0OOOOOO =='No':#line:646
            OOOO000O00O00OOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Invite{Fore.MAGENTA}:{Fore.RESET} discord.gg/')#line:647
            print ()#line:648
            Engine .JoinServer (OOOO000O00O00OOOO )#line:649
            time .sleep (5 )#line:650
            Menu ()#line:651
        else :#line:652
            Menu ()#line:653
    elif O00O0O0OOO0OOO0OO =='2':#line:654
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:655
        O0000O00OO0OOO00O =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Server ID{Fore.MAGENTA}:{Fore.RESET} ')#line:656
        print ()#line:657
        if OOO0OO00OO0OOOOOO =='Yes':#line:658
            ProxyEngine .LeaveServer (O0000O00OO0OOO00O )#line:659
            time .sleep (5 )#line:660
            Menu ()#line:661
        elif OOO0OO00OO0OOOOOO =='No':#line:662
            Engine .LeaveServer (O0000O00OO0OOO00O )#line:663
            time .sleep (5 )#line:664
            Menu ()#line:665
        else :#line:666
            Menu ()#line:667
    elif O00O0O0OOO0OOO0OO =='3':#line:668
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:669
        OO0OOOOO00O0OO0OO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Channel ID{Fore.MAGENTA}:{Fore.RESET} ')#line:670
        OOOOO0000OO00OOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Message{Fore.MAGENTA}:{Fore.RESET} ')#line:671
        print ()#line:672
        if OOO0OO00OO0OOOOOO =='Yes':#line:673
            ProxyEngine .SendMessage (OO0OOOOO00O0OO0OO ,OOOOO0000OO00OOOO )#line:674
            time .sleep (5 )#line:675
            Menu ()#line:676
        elif OOO0OO00OO0OOOOOO =='No':#line:677
            Engine .SendMessage (OO0OOOOO00O0OO0OO ,OOOOO0000OO00OOOO )#line:678
            time .sleep (5 )#line:679
            Menu ()#line:680
        else :#line:681
            Menu ()#line:682
    elif O00O0O0OOO0OOO0OO =='4':#line:683
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:684
        OO0000O00O0O00OO0 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Link{Fore.MAGENTA}:{Fore.RESET} ')#line:685
        print ()#line:686
        if OOO0OO00OO0OOOOOO =='No':#line:687
            Engine .ReactToMessage (OO0000O00O0O00OO0 )#line:688
            time .sleep (5 )#line:689
            Menu ()#line:690
        elif OOO0OO00OO0OOOOOO =='Yes':#line:691
            ProxyEngine .ReactToMessage (OO0000O00O0O00OO0 )#line:692
            time .sleep (5 )#line:693
            Menu ()#line:694
        else :#line:695
            Menu ()#line:696
    elif O00O0O0OOO0OOO0OO =='5':#line:697
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:698
        O0O0O0OO000000000 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] User ID{Fore.MAGENTA}:{Fore.RESET} ')#line:699
        print ()#line:700
        if OOO0OO00OO0OOOOOO =='No':#line:701
            Engine .SendFriendRequest (O0O0O0OO000000000 )#line:702
            time .sleep (5 )#line:703
            Menu ()#line:704
        elif OOO0OO00OO0OOOOOO =='Yes':#line:705
            ProxyEngine .SendFriendRequest (O0O0O0OO000000000 )#line:706
            time .sleep (5 )#line:707
            Menu ()#line:708
        else :#line:709
            Menu ()#line:710
    elif O00O0O0OOO0OOO0OO =='6':#line:711
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:712
        O0O0O0OO000000000 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] User ID{Fore.MAGENTA}:{Fore.RESET} ')#line:713
        print ()#line:714
        if OOO0OO00OO0OOOOOO =='No':#line:715
            Engine .RemoveFriendRequest (O0O0O0OO000000000 )#line:716
            time .sleep (5 )#line:717
            Menu ()#line:718
        elif OOO0OO00OO0OOOOOO =='Yes':#line:719
            ProxyEngine .RemoveFriendRequest (O0O0O0OO000000000 )#line:720
            time .sleep (5 )#line:721
            Menu ()#line:722
        else :#line:723
            Menu ()#line:724
    elif O00O0O0OOO0OOO0OO =='7':#line:725
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:726
        if OOO0OO00OO0OOOOOO =='No':#line:727
            Engine .CheckToken ()#line:728
            time .sleep (5 )#line:729
            Menu ()#line:730
        elif OOO0OO00OO0OOOOOO =='Yes':#line:731
            ProxyEngine .CheckToken ()#line:732
            time .sleep (5 )#line:733
            Menu ()#line:734
        else :#line:735
            Menu ()#line:736
    elif O00O0O0OOO0OOO0OO =='8':#line:737
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:738
        O00OO0000OOO0OOO0 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Token{Fore.MAGENTA}:{Fore.RESET} ')#line:739
        print ()#line:740
        if OOO0OO00OO0OOOOOO =='No':#line:741
            Engine .TokenInformation (O00OO0000OOO0OOO0 )#line:742
            time .sleep (5 )#line:743
            Menu ()#line:744
        elif OOO0OO00OO0OOOOOO =='Yes':#line:745
            ProxyEngine .TokenInformation (O00OO0000OOO0OOO0 )#line:746
            time .sleep (5 )#line:747
            Menu ()#line:748
        else :#line:749
            Menu ()#line:750
    elif O00O0O0OOO0OOO0OO =='9':#line:751
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:752
        O0O0O0OO000000000 =input (f'[{Fore.MAGENTA}?{Fore.RESET}] User ID{Fore.MAGENTA}:{Fore.RESET} ')#line:753
        OOOOO0000OO00OOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Message{Fore.MAGENTA}:{Fore.RESET} ')#line:754
        if OOO0OO00OO0OOOOOO =='No':#line:755
            Engine .SendDirectMessage (O0O0O0OO000000000 ,OOOOO0000OO00OOOO )#line:756
            time .sleep (5 )#line:757
            Menu ()#line:758
        elif OOO0OO00OO0OOOOOO =='Yes':#line:759
            ProxyEngine .SendDirectMessage (O0O0O0OO000000000 ,OOOOO0000OO00OOOO )#line:760
            time .sleep (5 )#line:761
            Menu ()#line:762
        else :#line:763
            Menu ()#line:764
    elif O00O0O0OOO0OOO0OO =='10':#line:765
        OOO0OO00OO0OOOOOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Proxys? Yes/No{Fore.MAGENTA}:{Fore.RESET} ')#line:766
        OOO000OOOO0O00O0O =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Guild ID{Fore.MAGENTA}:{Fore.RESET} ')#line:767
        O0000OOO0000O0OOO =input (f'[{Fore.MAGENTA}?{Fore.RESET}] Username{Fore.MAGENTA}:{Fore.RESET} ')#line:768
        if OOO0OO00OO0OOOOOO =='No':#line:769
            Engine .ChangeNickname (OOO000OOOO0O00O0O ,O0000OOO0000O0OOO )#line:770
            time .sleep (5 )#line:771
            Menu ()#line:772
        elif OOO0OO00OO0OOOOOO =='Yes':#line:773
            ProxyEngine .ChangeNickname (OOO000OOOO0O00O0O ,O0000OOO0000O0OOO )#line:774
            time .sleep (5 )#line:775
            Menu ()#line:776
    elif O00O0O0OOO0OOO0OO =='11':#line:777
        print (f'{Fore.WHITE}Creators: {Fore.MAGENTA}Clheyo#{Fore.RESET}0009, {Fore.MAGENTA}Xelly#{Fore.RESET}0001')#line:778
        time .sleep (5 )
        Menu ()#line:779
    elif O00O0O0OOO0OOO0OO =='12':#line:780
        os ._exit (0 )#line:781
    else :#line:782
        print ()#line:783
        print (f'[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Option.')#line:784
        time .sleep (2 )#line:785
        Menu ()#line:786
if __name__ =="__main__":#line:787
    if os .path .exists ('Tokens.txt'):#line:788
        with open ('Tokens.txt','r',encoding ='UTF-8')as f :#line:789
            for line in f .readlines ():#line:790
                line =line .split ('\n')[0 ]#line:791
                try :#line:792
                    tokens .append (line )#line:793
                except :#line:794
                    pass #line:795
    if os .path .exists ('Proxies.txt'):#line:796
        with open ('Proxies.txt','r',encoding ='UTF-8')as f :
            for line in f .readlines ():#line:798
                line =line .split ('\n')[0 ]
                try :
                    proxies .append (line )
                except :
                    pass 
    Menu ()
