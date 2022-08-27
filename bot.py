import os
from urllib.parse import quote
import discord
from discord.ext import commands

description = 'A bot that lets you generate Let Me Google That For You links'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('------')

@bot.command()
async def lmgt(ctx, *args):
    arg = ' '.join(args)
    link = 'https://letmegooglethat.com/?q=' + quote(arg)
    await ctx.send(f'Here, let me google that: {link}')

bot.run(os.environ.get('TOKEN'))