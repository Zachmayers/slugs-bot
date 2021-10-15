from random import choice
from json import load

with open("promptsList.json", "r") as file:
    masterPool = dict(load(file))

def slugline():
    pool = masterPool['slugline']
    interior = choice(pool['interior'])
    location = choice(pool['location'])
    time = choice(pool['time'])

    return f'{interior} {location} - {time}'

print(slugline())