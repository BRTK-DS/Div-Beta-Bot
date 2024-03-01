import nextcord
import os
from nextcord.ext import commands
from googleapiclient.discovery import build
from emoji import *

class youtube(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    async def video_check(self, message):
        if message.channel.id == self.client.target_channel_id:
            youtube = build("youtube", "v3", dedveloperKey=self.client.youtube_api_key)
            
            channel_id = "WSTAW TUTAJ ID"
            
            request = youtube.search().list(parts="id", channelId=channel_id, order="date", type="video", maxResults=1)
            response = request.execute()
            latest_video_id = response["items"][0]["id"]["videoId"]
            
            ancmnt_chan = 1153075658331795508
            stored_video_id = self.client.data.get("latest_video_id")
            if latest_video_id != stored_video_id:
                channel = self.client.get_channel(ancmnt_chan)
                await channel.send(f"{excited_emoji}  Zapraszamy na obejrzenie nowego filmu!\n@everyone\nhttps://www.youtube.com/watch?v={latest_video_id}")
                
                self.client.data["latest_video_id"] = latest_video_id
                self.client.save_data()
                
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        await self.check_for_new_video(message)
        
def setup(client):
    client.add_cog(youtube(client))