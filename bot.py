import discord

import main
from bot_token import BOT_TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    if message.content.startswith("!start"):
        while True:
            data = main.compare("https://forums.eveonline.com/c/marketplace/sales-ads/")
            for line in data:
                await message.channel.send(line)
            data.clear()


client.run(BOT_TOKEN)

