from random import choice, randrange
from numpy.random import normal as norm
from math import floor
from json import load

with open("promptsList.json", "r") as file:
    masterPool = dict(load(file))

def slugline():
    pool = masterPool['slugline']
    interior = choice(pool['interior'])
    location = choice(pool['location'])
    time = choice(pool['time'])

    return f'{interior} {location} - {time}'

def character():
    name = choice(masterPool["name"]).upper()
    adj1 = choice(masterPool["adjective"])
    adj2 = choice(masterPool["adjective"])
    age = ""
    num = floor(norm(loc=30, scale=15))
    if num < 19:
        age = str(num)
    else:
        age = f"{(round(num/10))*10}s"
    
    return f'{name} ({age}, {adj1}, {adj2})'

print(character())