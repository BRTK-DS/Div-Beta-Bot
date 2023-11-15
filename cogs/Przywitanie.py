import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member
from serwerID import *
import random

class Przywitanie(commands.Cog):

    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name = "hej", description = "Powiedz cześć Divowi :)", guild_ids=[ServerID])
    async def hej(self, interaction: Interaction):
        await interaction.response.send_message("Hejka! :D")
        
        
    @nextcord.slash_command(name="dmuchnij", description="Dmuchnij w alkomat", guild_ids=[ServerID])
    async def dmuchnij(self, interaction:Interaction, member: nextcord.Member):
        # Ustawiam zmienne z funkcją random
        first = random.randrange(0, 3)
        scnd = random.randrange(10, 19)
        await interaction.response.send_message(f'Użytkownik {member.mention} dmuchnął. Alkomat wykazuje ' + str(first) + "." + str(scnd) + "!")
    
    # event
    @commands.Cog.listener()
    async def on_member_join(member):
        channel = nextcord.Client.get_channel(1155238879041962047)
        await channel.send("Witaj")

    @commands.Cog.listener()
    async def on_member_remove(member):
        channel = nextcord.Client.get_channel(1155238879041962047)
        await channel.send("Żegnaj :(")

def setup(client):
    client.add_cog(Przywitanie(client))