import discord
from consts import *
import os
import prompt, spdefs

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
        
        if content == 'prompt' or content == "i'm stuck":

            response =f'''
            Here are some ideas for you! See if these help you out!

Character: `{prompt.character()}`

Scene: `{prompt.slugline()}`
            '''

            print(response)
            await message.channel.send(response)
            # embed = discord.Embed(title="Story Prompts", colour=discord.Colour(0xba9b37), description="Here are a few writing ideas you can hopefully use to kickstart some creativity. Hopefully they help!\n\n-Slugsy\n", timestamp=datetime.datetime.utcfromtimestamp(1634276062))

            # embed.set_image(url="https://imgur.com/m3kkq9I")
            # embed.set_footer(text="Slugsy: the TSC@UCF Writing Helper", icon_url="https://imgur.com/m3kkq9I")

            # embed.add_field(name="Slugline", value=f"`{prompt.slugline()}`")
            # embed.add_field(name="Character", value=f"`{prompt.character()}`")

            # await message.channel.send(content="Here's your slugline, straight from your favorite slug!", embed=embed)

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
        
        if content[:5] == 'guide':
            if len(content) == 5:
                response = spdefs.toc
            else:
                if content[6:19] == 'parenthetical':
                    if content[-2:] == 'al':
                        response = spdefs.parenBase
                    else:
                        respose = spdefs.parentheticals[str(content[-1])]
            print(response)
            await message.channel.send(response)

client.run(TOKEN)

