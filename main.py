import os
import discord
from dotenv import load_dotenv
try:
    load_dotenv()
except:  # noqa
    pass

# 環境変数を参照
TOKEN = os.getenv('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in!')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/hello':
        await message.channel.send('Hello World!!')


@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.author.bot:
        await reaction.message.channel.send('Reaction added!!')
    else:
        pass


# Botの起動
client.run(TOKEN)
