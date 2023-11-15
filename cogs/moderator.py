import nextcord
from nextcord.ext import commands
from nextcord import Member
from nextcord import Interaction
from nextcord.ext.application_checks import has_role, ApplicationMissingRole
from emoji import *

class moderator(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command()
    @has_role(1170518127369519124)
    async def kick(self, interaction: Interaction, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await interaction.response.send_message(f'{success_emoji}Użytkownik {member.mention} został wyrzucony.')

    @kick.error
    async def kick_error(self, interaction: Interaction, error):
        if isinstance(error, ApplicationMissingRole):
            await interaction.response.send_message(f"{failed_emoji}Nie masz odpowiednich uprawnień do tej komendy!")

    @nextcord.slash_command()
    @has_role(1170518127369519124)
    async def ban(self, interaction: Interaction, member: nextcord.Member, *, reason=None):
        try:
            appeal_message = f'Zostałeś zbanowany na serwerze za "{reason}". Jeśli chcesz odwołać się od bana, możesz to zrobić poprzez formularz: https://forms.gle/VbYGVJCmgMYsVg9U7'
            await member.send(appeal_message)
        except nextcord.HTTPException:
            pass
        await member.ban(reason=reason)    
        await interaction.response.send_message(f'{success_emoji}Użytkownik {member.mention} został zbanowany.')

    @ban.error
    async def ban_error(self, interaction: Interaction, error):
        if isinstance(error, ApplicationMissingRole):
            await interaction.response.send_message(f"{failed_emoji}Nie masz odpowiednich uprawnień do tej komendy!")
            
def setup(client):
    client.add_cog(moderator(client))