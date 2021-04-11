import os, json, time, datetime, re, aiohttp, discord, asyncio, requests, pypresence

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

os.system('cls & title [Seraph Sniper] - Loading & mode 70,20')

try:
    RPC = Presence("802317564679946311") 
    RPC.connect()

    RPC.update(details="Main Menu", large_image="seraph", small_image="seraph", large_text="Seraph Sniper", start=time.time())
except:
    pass

with open('config.json') as f:
    config = json.load(f)

token = config.get('Token')
nitroSniper = config.get('Nitro-Sniper')
giveawaySniper = config.get('Giveaway-Sniper')

async def SendWebhook(embed):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(config.get('Webhook'), adapter=AsyncWebhookAdapter(session))
        try:
            await webhook.send(embed=embed, username="Seraph Sniper", avatar_url="https://media.discordapp.net/attachments/765924004829331466/796485783720165406/SeraphYELLOW.png")
        except:
            pass

client = discord.Client()

if nitroSniper == True:
    NitroSniperCheck = "Enabled"
else:
    NitroSniperCheck = "Disabled"

if giveawaySniper == True:
    GiveawaySniperCheck = "Enabled"
else:
    GiveawaySniperCheck = "Disabled"

@client.event
async def on_connect():
    guilds = len(client.guilds)
    os.system(f'cls & mode 70,20 & title [Seraph Sniper] - Connected')
    print(f'''
                  \x1b[38;5;185m╔═╗   ╔═╗   ╦═╗   ╔═╗   ╔═╗   ╦ ╦\033[37m
                  \033[90m╚═╗   ║╣    ╠╦╝   ╠═╣   ╠═╝   ╠═╣\033[37m
                  \033[37m╚═╝   ╚═╝   ╩╚═   ╩ ╩   ╩     ╩ ╩\033[37m

                  \x1b[38;5;185m═════════════════════════════════\033[37m
                    Connected       \x1b[38;5;185m[\033[37m{client.user}\x1b[38;5;185m]\033[37m
                    Guilds          \x1b[38;5;185m[\033[37m{guilds}\x1b[38;5;185m]\033[37m
                    Nitro Sniper    \x1b[38;5;185m[\033[37m{NitroSniperCheck}\x1b[38;5;185m]\033[37m
                    Giveaway Sniper \x1b[38;5;185m[\033[37m{GiveawaySniperCheck}\x1b[38;5;185m]\033[37m
                  \x1b[38;5;185m═════════════════════════════════\033[37m
    ''')

@client.event
async def on_message(message):

    time = datetime.datetime.now().strftime("%H:%M")

    if 'discord.gift/' in message.content:
        if nitroSniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            headers = {'Authorization': token}
            link = requests.post(f'https://discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem', headers=headers).text
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in link:
                print(
                 f"\033[37m[\033[91m{time} \033[37m- \033[91mNitro Already Redeemed\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mServer\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.guild}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mChannel\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{message.channel}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mAuthor\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.author}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mElapsed\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{elapsed}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mCode\x1b[38;5;185m:    \033[37m[\x1b[38;5;185m{code}\033[37m]\n"
                )
                embed = discord.Embed(color=0x2f3136, title = "Nitro Sniped", description=f'''```
• Server        | {message.guild}
• Channel       | {message.channel}
• Author        | {message.author}
• Elapsed       | {elapsed}
• Code          | {code}
• Status        | Already Redeemed
```''')
                embed.set_footer(text='Seraph Sniper', icon_url='https://media.discordapp.net/attachments/765924004829331466/796485783720165406/SeraphYELLOW.png')
                try:
                    await SendWebhook(embed)
                except:
                    pass
            elif 'subscription_plan' in link:
                print(
                 f"\033[37m[\033[92m{time} \033[37m- \033[92mNitro Sniped\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mServer\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.guild}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mChannel\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{message.channel}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mAuthor\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.author}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mElapsed\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{elapsed}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mCode\x1b[38;5;185m:    \033[37m[\x1b[38;5;185m{code}\033[37m]\n"
                )
                embed = discord.Embed(color=0x2f3136, title = "Nitro Sniped", description=f'''```
• Server        | {message.guild}
• Channel       | {message.channel}
• Author        | {message.author}
• Elapsed       | {elapsed}
• Code          | {code}
• Status        | Valid
```''')
                embed.set_footer(text='Seraph Sniper', icon_url='https://media.discordapp.net/attachments/765924004829331466/796485783720165406/SeraphYELLOW.png')
                try:
                    await SendWebhook(embed)
                except:
                    pass
            elif 'Unknown Gift Code' in link:
                print(
                 f"\033[37m[\033[91m{time} \033[37m- \033[91mInvalid Nitro\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mServer\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.guild}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mChannel\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{message.channel}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mAuthor\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.author}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mElapsed\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{elapsed}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mCode\x1b[38;5;185m:    \033[37m[\x1b[38;5;185m{code}\033[37m]\n"
                )
                embed = discord.Embed(color=0x2f3136, title = "Nitro Sniped", description=f'''```
• Server        | {message.guild}
• Channel       | {message.channel}
• Author        | {message.author}
• Elapsed       | {elapsed}
• Code          | {code}
• Status        | Invalid
```''')
                embed.set_footer(text='Seraph Sniper', icon_url='https://media.discordapp.net/attachments/765924004829331466/796485783720165406/SeraphYELLOW.png')
                try:
                    await SendWebhook(embed)
                except:
                    pass
        else:
            return

    words = ['GIVEAWAY', 'Giveaway', 'giveaway', 'give-away', 'GIVE-AWAY', 'Give-away']
    for word in words:
        if f'{word}' in message.content and message.author.bot == True:
            start = datetime.datetime.now()
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'
            if giveawaySniper == True:
                try:
                    await message.add_reaction("🎉")
                    print(
                     f"\033[37m[\033[92m{time} \033[37m- \033[92mGiveaway Sniped\033[37m]\n"
                     f" \x1b[38;5;185m- \033[37mServer\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.guild}\033[37m]\n"
                     f" \x1b[38;5;185m- \033[37mChannel\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{message.channel}\033[37m]\n"
                     f" \x1b[38;5;185m- \033[37mElapsed\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{elapsed}\033[37m]\n"
                    )
                    embed = discord.Embed(color=0x2f3136, title = "Giveaway Sniped", description=f'''```
• Server        | {message.guild}
• Channel       | {message.channel}
• Author        | {message.author}
• Elapsed       | {elapsed}
```''')
                    embed.set_footer(text='Seraph Sniper', icon_url='https://media.discordapp.net/attachments/765924004829331466/796485783720165406/SeraphYELLOW.png')
                    try:
                        await SendWebhook(embed)
                    except:
                        pass
                except discord.errors.Forbidden:
                    print(
                     f"\033[37m[\033[91m{time} \033[37m- \033[91mGiveaway Couldn't React\033[37m]\n"
                     f" \x1b[38;5;185m- \033[37mServer\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.guild}\033[37m]\n"
                     f" \x1b[38;5;185m- \033[37mChannel\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{message.channel}\033[37m]\n"
                    )
            else:
                return
    words2 = ['Congratulations', 'CONGRATULATIONS', 'congratulations', 'Congrats', 'congrats', 'CONGRATS']
    for word in words2:
        if word in message.content and client.user in message.mentions and message.author.bot == True:
            if giveawaySniper == True:
                print(
                 f"\033[37m[\033[92m{time} \033[37m- \033[92mGiveaway Won\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mChannel\x1b[38;5;185m: \033[37m[\x1b[38;5;185m{message.channel}\033[37m]\n"
                 f" \x1b[38;5;185m- \033[37mServer\x1b[38;5;185m:  \033[37m[\x1b[38;5;185m{message.guild}\033[37m]\n"
                )
                embed = discord.Embed(color=0x2f3136, title = "Giveaway Won", description=f'''```
• Server        | {message.guild}
• Channel       | {message.channel}
• Author        | {message.author}
```''')
                embed.set_footer(text='Seraph Sniper', icon_url='https://media.discordapp.net/attachments/765924004829331466/796485783720165406/SeraphYELLOW.png')
                try:
                    await SendWebhook(embed)
                except:
                    pass
            else:
                return

client.run(token, bot=False, reconnect=True)
