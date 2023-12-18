import nextcord
from nextcord.ext import commands
import os

from chybacbposralo import *

intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='/', intents=nextcord.Intents.all(), max_messages=3000)

@client.event
async def on_ready():
    print("Div jest gotowy.")
    print("-----------------------------")
    
initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

client.run(TKN)