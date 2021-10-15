import discord
from consts import *
import os

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = '681609827801366591'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    


        content = message.content[1:].lower()
        print(content)

        name = message.author.name
        if message.content[0] == '!':
            if message.channel != CHANNEL:
                response = f'Hello {name}, please only contact me in bot commands from now on. Thank you'
                print(response)

            await message.channel.send(response)
        if content == 'hey' or content == 'hello' or content == 'hi':
            response = f'Hello {name}'
            print(response)

            await message.channel.send(response)

        if content == 'generate':
            gen = 'test for now!'
            response = f'it works! {gen}'

            print(response)
            await message.channel.send(response)

client.run(TOKEN)

