"""
this is how bot works
"""
import asyncio

import discord

import main
from bot_token import BOT_TOKEN  # pylint: disable=C0411,E0401

client = discord.Client()

task_storage = {}
lock = asyncio.Lock()


async def sales_ads_all_updates(message):
    while True:
        data = await main.compare(
            "https://forums.eveonline.com/c/marketplace/sales-ads/"
        )
        for line in data:
            await message.channel.send(line)
        data.clear()


async def sales_ads_new_topics(message):
    while True:
        data = await main.compare_for_new_topics(
            "https://forums.eveonline.com/c/marketplace/sales-ads/"
        )
        for line in data:
            await message.channel.send(line)
        data.clear()


@client.event
async def on_message(message):
    """
    we use discord library to send messages
    on_message()
    if user message starts with !Sales_ads_all_updates it will start working
    """
    async with lock:
        channel_id = message.channel.id
        if (
            message.content.startswith("!Sales_ads_all_updates")
            and task_storage.get(channel_id) is None
        ):
            t = asyncio.create_task(sales_ads_all_updates(message))
            task_storage[channel_id] = t
        elif (
            message.content.startswith("!Sales_ads_new_topics")
            and task_storage.get(channel_id) is None
        ):
            t = asyncio.create_task(sales_ads_new_topics(message))
            task_storage[channel_id] = t
        elif (
            message.content.startswith("!stop") and task_storage.get(channel_id) is None
        ):
            t = task_storage.get(channel_id)
            if t is not None:  # there is a background task
                t.cancel()  # cancel task
                task_storage.pop(channel_id)  # remove the task since it is canceled
        else:
            pass


client.run(BOT_TOKEN)
