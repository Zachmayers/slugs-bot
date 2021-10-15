import discord
from consts import *
import os
import prompt

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = '681609827801366591'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0] == '!':


        content = message.content[1:].lower()
        print(content)

        name = message.author.name

        if content == 'hey' or content == 'hello' or content == 'hi':
            response = f'Hello {name}'
            print(response)

            await message.channel.send(response)

        if content == 'slugline':
            response = f'''
            Here's a slugline to get you started:
`{prompt.slugline()}`'''
            
            print(response)
            await message.channel.send(response)

        if content == 'character':
            response = f'''
            Here's a character you could write about:
`{prompt.character()}`'''

            print(response)
            await message.channel.send(response)

client.run(TOKEN)

