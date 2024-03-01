import nextcord
from nextcord import Embed
from nextcord.ext import commands
from emoji import *
from datetime import datetime, timezone, timedelta

intents = nextcord.Intents.default()
intents.messages = True
intents.members = True

class logger(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        
        user = message.author
        channel_raw = message.channel.id
        channel_del = self.client.get_channel(channel_raw)
        
        guild_id = 1038037955836661840
        
        if message.author.bot or not message.guild:
            return
        
        if message.guild.id != guild_id:
            return   
        
        embed_del = Embed(title=f"{failed_emoji} Usunięcie wiadomości", timestamp=message.created_at, color=0xff0000)
        embed_del.add_field(
            name=f"- Autor wiadomości: {user.display_name}",
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
            
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        
        user = after.author
        channel_raw = after.channel.id
        channel_upd = self.client.get_channel(channel_raw)
        
        guild_id = 1038037955836661840
        
        if after.author.bot or not after.guild:
            return
        
        if after.guild.id != guild_id:
            return   
        
        old_msg = before.content
        new_msg = after.content
        
        embed_upd = Embed(title=f"{edit_emoji} Zmiana wiadomości", timestamp=after.edited_at, color=0xffff00)
        embed_upd.add_field(
            name=f"- Autor wiadomości: {user.display_name}",
            value=f"- Kanał: {channel_upd.name}\n- Oryginalna treść: {old_msg}\n- Nowa treść: {new_msg}",
            inline=False
        )
        embed_upd.set_thumbnail(url=user.avatar.url)
        
        channel_id = 1186019315934314596
        channel = self.client.get_channel(channel_id)
        
        if channel:
            await channel.send(embed=embed_upd)
        else:
            print(f"Nie znaleziono kanału o tym ID {channel_id}")
            
            
    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        embed_join = Embed(title=f"{join_emoji} Użytkownik dołączył do serwera", timestamp=member.joined_at, color=0x00ff00)
        embed_join.add_field(
            name=f"- Nazwa użytkownika: {member.display_name}",
            value="- Witamy na serwerze!",
            inline=False
        )
        embed_join.set_thumbnail(url='https://cdn.discordapp.com/attachments/1155238879041962047/1186250892727558255/019ba383ab09d50ff38b73de0952aad3.png?ex=6592913c&is=65801c3c&hm=5c04d4dab8e5f1c92e1295a9b9054d8965a02281bba087e603437dbf7fd25140&')
        
        channel_id = 1186019315934314596
        channel = self.client.get_channel(channel_id)
        
        if channel:
            await channel.send(embed=embed_join)
        else:
            print(f"Nie znaleziono kanału o tym ID {channel_id}")
            
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        
        tz_poland = timezone(timedelta(hours=1))
        leave_time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz_poland)
        time_format = "%d/%m/%Y %H:%M"
        leave_now = leave_time.strftime(time_format)
        
        embed_leave = Embed(title=f"{leave_emoji} Użytkownik wyszedł z serwera", color=0xff0000)
        embed_leave.add_field(
            name=f"- Nazwa użytkownika: {member.display_name}",
            value="- Żegnamy! :(",
            inline=False
        )
        embed_leave.set_thumbnail(url='https://cdn.discordapp.com/attachments/1155238879041962047/1186250892727558255/019ba383ab09d50ff38b73de0952aad3.png?ex=6592913c&is=65801c3c&hm=5c04d4dab8e5f1c92e1295a9b9054d8965a02281bba087e603437dbf7fd25140&')
        embed_leave.set_footer(text=leave_now)
        
        channel_id = 1186019315934314596
        channel = self.client.get_channel(channel_id)
        
        if channel:
            await channel.send(embed=embed_leave)
        else:
            print(f"Nie znaleziono kanału o tym ID {channel_id}")
        
def setup(client):
    client.add_cog(logger(client))