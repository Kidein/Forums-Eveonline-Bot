import time
from asyncore import write

import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()


def write_to_file():
    r = requests.get("https://forums.eveonline.com/c/marketplace/sales-ads/")
    stuff_list = []
    soup = BeautifulSoup(r.text, "lxml")
    tags = soup("a", class_="title raw-link raw-topic-link")
    for tag in tags:
        item_url = tag.get("href")
        item_text = tag.text
        stuff_list.append(item_text)
        stuff_list.append(item_url)
    return stuff_list


data = write_to_file()
# for line in data:
# print(line.strip())


@client.event
async def on_message(message):
    if message.content.startswith(
        "!start"
    ):  # the command you want to use e.g if you want to use .ff DRSP set to .ff
        for line in data:
            await message.channel.send(line.strip())
    elif message.content.startswith("hello"):
        await message.channel.send("hi,i am a bot")
    else:
        return


client.run("OTM5OTczOTMwNjA3ODQxMzMw.YgAo8A.dGT5T5oG68DTKUcEPhY4Gb6q9Fs")
