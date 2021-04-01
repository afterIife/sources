import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import discord
import os
import colorama
from colorama import Fore, Style
import requests
import time
from colorama import Fore
import time, datetime
import json
def sbammah():
    webhook = input(f"[>]Enter The Webhook Link:")
    message = input(f"[>]Enter The Message: ")
    delay = float(input(f"[>]Enter The Delay:"))
    print(Fore.RESET + '')

    while True:

        print(Fore.CYAN + "Sending.. " + message)
        print(Fore.RESET + " ")
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.CYAN + "Sent -> " + message) 
        except:
            print("Something Happend! | Probably Broken Webhook -> " + webhook)
            time.sleep(5)
            exit()

x = 5
while x == 5:
    sbammah()