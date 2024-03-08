import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Guild
import os

class automod(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    commands.Cog.listener()
    async def on_message(self, message):
        
        guild_id = 1038037955836661840
        if message.guild.id != guild_id:
            return
        
        