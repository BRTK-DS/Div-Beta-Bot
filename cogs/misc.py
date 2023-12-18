import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member
from serwerID import *
import random

class misc(commands.Cog):

    def __init__(self, client):
        self.client = client     
        
    @nextcord.slash_command(name="dmuchnij", description="Dmuchnij w alkomat", guild_ids=[ServerID])
    async def dmuchnij(self, interaction:Interaction, member: nextcord.Member):
        # Ustawiam zmienne z funkcją random
        first = random.randrange(0, 3)
        scnd = random.randrange(10, 19)
        await interaction.response.send_message(f'Użytkownik {member.mention} dmuchnął. Alkomat wykazuje ' + str(first) + "." + str(scnd) + "!")

def setup(client):
    client.add_cog(misc(client))