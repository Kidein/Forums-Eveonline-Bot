import discord

import main
from bot_token import BOT_TOKEN  # noqa

client = discord.Client()

"""
we use discord library to send messages
on_message()

if user message starts with !Sales_ads_all_updates it will start working
"""


@client.event
async def on_message(message):
    if message.content.startswith("!Sales_ads_all_updates"):
        while True:
            data = main.compare("https://forums.eveonline.com/c/marketplace/sales-ads/")
            for line in data:
                await message.channel.send(line)
            data.clear()
    if message.content.startswith("!Sales_ads_new_topics"):
        while True:
            data = main.compare_for_new_topics(
                "https://forums.eveonline.com/c/marketplace/sales-ads/"
            )
            for line in data:
                await message.channel.send(line)
            data.clear()


client.run(BOT_TOKEN)
