import asyncio
import time

import discord
import requests
import schedule
from bs4 import BeautifulSoup

client = discord.Client()


def get_info(forum_url, list_name):
    r = requests.get(forum_url)
    soup = BeautifulSoup(r.text, "lxml")
    tags = soup.find_all("a", class_="title raw-link raw-topic-link")
    for tag in tags:
        item_url = tag.get("href")
        item_text = tag.text
        list_name.append(item_text)
        list_name.append(item_url)
    return list_name


def compare(forum_url):
    state1_list, state2_list, final_list = [], [], []
    list1 = get_info(forum_url, state1_list)
    time.sleep(120)
    list2 = get_info(forum_url, state2_list)

    if list1[2] != list2[2]:
        final1 = list2[2:4].copy()
        # print(list2[2], "\n ")
        # print(list2[3], "\n ")
        return final1
    state1_list.clear()
    state2_list.clear()


def compare_on_time(forum_url):
    schedule.every(1).seconds.do(compare, forum_url)
    while True:
        schedule.run_pending()


# data = compare_on_time("https://forums.eveonline.com/c/marketplace/sales-ads/")


@client.event
async def on_message(message):
    if message.content.startswith("!start"):
        while True:
            data = compare("https://forums.eveonline.com/c/marketplace/sales-ads/")
            for line in data:
                await message.channel.send(line)
            data.clear()


client.run("OTM5OTczOTMwNjA3ODQxMzMw.YgAo8A.dGT5T5oG68DTKUcEPhY4Gb6q9Fs")
