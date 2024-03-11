import nextcord
from nextcord.ext import commands
from nextcord import Guild
import os
from emoji import *
    
class automod(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        with open('banned_words.txt', 'r') as file:
            self.banned_words = [word.strip().lower() for word in file.readlines()]
        
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author.bot:
            return
        
        content_lower = message.content.lower()
        for word in self.banned_words:
            if word in content_lower:
                muted_role = message.guild.get_role(1216727135142805585)
                role_id = message.guild.get_role(1038194522422775878)
                
                try:
                    appeal_message = f'{failed_emoji} Zostałeś wyciszony na serwerze za użycie niedozwolonych wyrazów. Jeśli chcesz odwołać się od wyciszenia, możesz to zrobić na odpowiednim kanale.'
                    await message.author.send(appeal_message)
                except nextcord.HTTPException:
                    pass
                await message.author.add_roles(muted_role)
                await message.author.remove_roles(role_id)
                await message.channel.send(f"{failed_emoji} {message.author.mention} został wyciszony.")
                
                break
            
def setup(client):
    client.add_cog(automod(client))