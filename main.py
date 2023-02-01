import discord
from discord.ext import commands
from functions import *

TOKEN: str = ''
CHANNEL_ID: int = 0
client = commands.Bot(command_prefix = '.', intents = discord.Intents.all())

@client.event
async def on_ready(): print('cum')

@client.event
async def on_message(message):
    message_content: str = str(message.content)
    channel = message.channel.id
    if channel != CHANNEL_ID: return
    try:
        int(message_content)
    except ValueError:
        await message.delete()
        return
    if int(message_content) - 1 == get_number("data") and str(message.author) != get_user("data"):
        update_data("data", get_number("data"), str(message.author))
    else:
        await message.delete()

client.run(TOKEN)