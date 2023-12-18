import nextcord
from nextcord import Embed
from nextcord.ext import commands
from emoji import *
from datetime import datetime, timedelta, timezone

intents = nextcord.Intents.default()
intents.messages = True

class logger(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        
        user = message.author
        channel_raw = message.channel.id
        channel_del = self.client.get_channel(channel_raw)
        
        embed_del = Embed(title=f"{failed_emoji} Usunięcie wiadomości", timestamp=message.created_at, color=0xff0000)
        embed_del.add_field(
            name=f"Autor wiadomości: {user.display_name}",
                        value=f"- Kanał: {channel_del.name}\n- Treść: {message.content}",
                        inline=False
        )
        embed_del.set_thumbnail(url=user.avatar.url)
        
        channel_id = 1186019315934314596
        channel = self.client.get_channel(channel_id)
        
        if channel:
            await channel.send(embed=embed_del)
        else:
            print(f"Nie znaleziono kanału o tym ID {channel_id}")
            
        
def setup(client):
    client.add_cog(logger(client))