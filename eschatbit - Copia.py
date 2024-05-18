import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='|', intents=intents)
count=0
mess=[]

@bot.event
async def on_ready():
    print(f"Hai fatto l'accesso come {bot.user}")

@bot.event
async def on_message(message):
    count+=1
    mess.append(message.content)

@bot.command()
async def quota(ctx):
    count=0
    mess.clear()

@bot.command()
async def somma(ctx):
    count=0
    mess.clear()

@bot.command()
async def risulta(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


import random

@bot.command()
async def emoji(ctx, count = 1):
    await ctx.send("BiBu" * count)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


import os

@bot.command()
async def mem(ctx, name=None):
    folder = "images"
    memes = os.listdir(folder)
    
    if name is None or name not in memes:
        name = random.choice(memes)

    with open(f'{folder}/{name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

from requests import requests

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")