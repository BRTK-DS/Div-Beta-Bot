import nextcord
from nextcord.ext import commands
    
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
                muted_role = nextcord.utils.get(message.guild.roles, name='Muted')
                
                await message.author.add_roles(muted_role)
                await message.channel.send(f"{message.author.mention} został wyciszony")
                break
            
def setup(client):
    client.add_cog(automod(client))