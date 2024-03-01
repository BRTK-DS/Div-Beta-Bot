# import nextcord
# from nextcord.ext import commands
# from nextcord import Interaction
# import wavelink

# class music(commands.Cog):
#     def __init__(self, client):
#         self.client = client
#         self.wavelink = wavelink
        
#         self.host = 'lavalink-v4.teramont.net'
#         self.port = 443
#         self.password = 'eHKuFcz67k4lBS64'
        
#         self.client.loop.create_task(self.setup_lavalink())
        
#     async def setup_lavalink(self):
#         self.wavelink_client = self.wavelink.Client(client=self.client)
        
#         await self.client.wait_until_ready()
#         await self.wavelink_client.initiate_node(
#             host=self.host,
#             port=self.port,
#             rest_uri=f'https://{self.host}:{self.port}',
#             password=self.password,
#             identifier='MAIN',
#             region='eu_west'
#         )
        
#     async def connect_to_voice(self, interaction: Interaction):
#         if not interaction.user.voice.channel:
#             await interaction.response.send_message("Musisz być na kanale żeby użyć tej komendy!")
#             return False
        
#         voice_channel = interaction.user.voice.channel
#         await voice_channel.connect()
#         return True
    
#     @nextcord.slash_command()
#     async def graj(self, interaction: Interaction, *, query: str):
#         if not await self.connect_to_voice(interaction):
#             return
        
#         player = self.wavelink.Player(interaction.guild)
        
#         try:
#             await player.connect()
#         except Exception as e:
#             await interaction.response.send_message(f"Nie udało się dołączyć do kanału: {e}", ephemeral=True)
#             return
        
#         tracks = await self.wavelink.YouTubeMusicTrack.search(query)
        
#         if not tracks:
#             await interaction.response.send_message("Nie znaleziono utworu.", ephemeral=True)
#             return
        
#         await player.play(tracks[0])
#         await interaction.response.send_message(f"Włączono: {tracks[0].title}")
        
# def setup(client):
#     client.add_cog(music(client))