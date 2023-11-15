import nextcord
from nextcord.ext import commands
from nextcord import Member
from nextcord import Interaction
from nextcord.ext.commands import has_permissions, MissingPermissions

class moderator(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command()
    @has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await interaction.response.send_message(f'Użytkownik {member.mention} został wyrzucony.')

    @kick.error
    async def kick_error(self, interaction: Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("Nie masz odpowiednich uprawnień do tej komendy!")

    @nextcord.slash_command()
    @has_permissions(ban_members=True)
    async def ban(self, interaction: Interaction, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await interaction.response.send_message(f'Użytkownik {member.mention} został zbanowany.')

    @ban.error
    async def ban_error(self, interaction: Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("Nie masz odpowiednich uprawnień do tej komendy!")
            
def setup(client):
    client.add_cog(moderator(client))