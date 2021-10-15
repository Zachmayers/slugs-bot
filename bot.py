import discord
from consts import *
import os

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')



client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content[0] == '!':

        content = message.content[1:]
        print(content)

        name = message.author.name

        if content == 'generate':
            gen = 'test for now!'
            response = f'it works! {gen}'

            print(response)
            await message.channel.send(response)

client.run(TOKEN)
