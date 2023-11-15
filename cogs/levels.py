import nextcord
from nextcord.ext import commands, tasks
from nextcord import Interaction, Embed
import json
import random
from nextcord.ext.application_checks import has_role, ApplicationMissingRole
from emoji import *

intents = nextcord.Intents.default()
intents.typing = False
intents.presences = False

# Ładuje dane usera z JSON'a (XP)
try:
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
except FileNotFoundError:
    user_data = {}

# Funkcja do zapisu danych usera na JSON
def save_user_data():
    with open('user_data.json', 'w') as f:
        json.dump(user_data, f, indent=4)

class levels(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cooldown_users = set()
        self.xp_task.start()  # Zacznij task dla XP

    def get_user_level_info(self, user_id):
        user_id = str(user_id)
        if user_id in user_data:
            return user_data[user_id]
        else:
            return {'level': 1, 'xp': 0} # Lepsza integracja dla Profilu

    def cog_unload(self):
        self.xp_task.cancel()  # Anuluj przyznawanie XP gdy Cog się unload'uje

    @tasks.loop(seconds=30)
    async def xp_task(self):
        # Zadanie w tle, przydziela XP okresowo
        for user_id in self.cooldown_users.copy():
            self.cooldown_users.remove(user_id)

    @xp_task.before_loop
    async def before_xp_task(self):
        await self.client.wait_until_ready()
        
    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignoruj wiadomości bota
        if message.author.bot:
            return

        user_id = str(message.author.id)

        # Sprawdź czy user ma cooldown
        if user_id in self.cooldown_users:
            return

        # Tworzy nowego użytkownika jeśli nie znajdzie w bazie
        if user_id not in user_data:
            user_data[user_id] = {'xp': 0, 'level': 1}

        # Przydziela XP za wiadomość
        user_data[user_id]['xp'] += random.randrange(5, 26)

        # Sprawdzenie czy użytkownik wbił nowy poziom
        if user_data[user_id]['xp'] >= user_data[user_id]['level'] * 100:
            user_data[user_id]['level'] += 1
            level = user_data[user_id]['level']

            # Przydzielanie rang za poziom
            if level >= 5:
                role_id = 1170487875016609923
                role = message.guild.get_role(role_id)
                await message.author.add_roles(role)
                
            if level >= 15:
                role_id = 1170487922512896041
                role = message.guild.get_role(role_id)
                await message.author.add_roles(role)
                
            if level >= 30:
                role_id = 1170487960655888444
                role = message.guild.get_role(role_id)
                await message.author.add_roles(role)
                
            if level >= 50:
                role_id = 1170487988254429234
                role = message.guild.get_role(role_id)
                await message.author.add_roles(role)

            user_data[user_id]['xp'] = 0
            await message.channel.send(f'{message.author.mention} Gratuluję zdobycia {level} poziomu!')

        # Zapisanie danych użytkownika
        save_user_data()

        # Dodaj użytkownika do listy z cooldownem
        self.cooldown_users.add(user_id)


    @nextcord.slash_command()
    async def level(self, interaction: Interaction, user: nextcord.User = None):
        user = user or interaction.user
        user_id = str(user.id)

        if user_id in user_data:
            level = user_data[user_id]['level']
            xp = user_data[user_id]['xp']
            xp_needed = level * 100
            progress = xp / xp_needed

        # Stworzenie belki postępu
            progress_bar = "["
            filled = int(20 * progress)
            progress_bar += "█" * filled
            progress_bar += " " * (20 - filled)
            progress_bar += f"] {int(progress * 100)}%"

        # Kod na embed
            xp_emoji = nextcord.PartialEmoji(animated=True, name="xp", id="1170497037339476018")
            level_emoji = nextcord.PartialEmoji(animated=True, name='lvl', id='1170499855068696717')
            progress_emoji = nextcord.PartialEmoji(animated=True, name='prg', id='1170499275306827826')
            embed = Embed(
                title=f'Karta postępu użytkownika @{user.display_name}',
                color=0xa751ed
            )
            embed.add_field(name=f'{level_emoji} Poziom:', value=level, inline=True)
            embed.add_field(name=f'{xp_emoji} XP:', value=f'{xp}/{xp_needed}', inline=True)
            embed.add_field(name=f'{progress_emoji} Postęp:', value=progress_bar, inline=False)
            embed.set_thumbnail(url=user.display_avatar.url)

            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message('Użytkownik nie został znaleziony w bazie.')


    @nextcord.slash_command()
    async def leaderboard(self, interaction: Interaction):
        sorted_users = sorted(user_data.items(), key=lambda x: x[1]['level'], reverse=True)
        
        xp_emoji = nextcord.PartialEmoji(animated=True, name="xp", id="1170497037339476018")
        lb_emoji = nextcord.PartialEmoji(animated=True, name="troph1", id='1170686245576392814')
        level_emoji = nextcord.PartialEmoji(animated=True, name='lvl', id='1170499855068696717')
        position_emoji = nextcord.PartialEmoji(animated=True, name="qmark", id="1170695514854006874")
        embed = Embed(title=f"{lb_emoji} Leaderboard:", color=0xffe45c)
    
        for index, (user_id, data) in enumerate(sorted_users[:10], start=1):
            user = self.client.get_user(int(user_id))
            embed.add_field(
                name=f"{index}. {user.display_name}",
                value=f"{level_emoji}Level: {data['level']}\n"
                f"{xp_emoji}XP: {data['xp']}",
                inline=False
                )

        embed.add_field(
                name="========================================",
                value="",
                inline=False
            )
        
        author_id = str(interaction.user.id)
        author_position = next((index for index, (user_id, _) in enumerate(sorted_users) if user_id == author_id), None)
        if author_position is not None:
            embed.add_field(
                name=f"{position_emoji}Twoja pozycja: " + f"{author_position + 1}.",
                value="",
                inline=False
            )
        
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1155238879041962047/1170684183836897362/image.png?ex=6559ef9b&is=65477a9b&hm=0a3d0aec66ffe074ffa819d15e6e5d0beb2778d089ea180fdf54b6ba427821b3&")

        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command()
    @has_role(1170518127369519124)
    async def przydziel_xp(self, interaction: Interaction, user: nextcord.User, xp_amount: int):
 
        user_id = str(user.id)
        if user_id in user_data:
            user_data[user_id]['xp'] += xp_amount
            save_user_data()
            await interaction.response.send_message(f"{success_emoji}Dodano {xp_amount} XP użytkownikowi {user.mention}")
        else:
            await interaction.response.send_message(f"{failed_emoji}Użytkownik nie został znaleziony w bazie.")
            
    @przydziel_xp.error
    async def przydziel_xp_error(self, interaction: Interaction, error):
        if isinstance(error, ApplicationMissingRole):
            await interaction.response.send_message(f"{failed_emoji}Nie masz odpowiednich uprawnień do tej komendy!")
            
    @nextcord.slash_command()
    @has_role(1170518127369519124)
    async def ustaw_poziom(self, interaction: Interaction, user: nextcord.User, new_level: int):
        
        user_id = str(user.id)
        if user_id in user_data:
            user_data[user_id]['level'] = new_level
            save_user_data()
            await interaction.response.send_message(f"{success_emoji}Ustawiono {new_level} poziom użytkownikowi {user.mention}")
        else:
            await interaction.response.send_message(f"{failed_emoji}Użytkownik nie został znaleziony w bazie.")
            
    @ustaw_poziom.error
    async def ustaw_poziom_error(self, interaction: Interaction, error):
        if isinstance(error, ApplicationMissingRole):
            await interaction.response.send_message(f"{failed_emoji}Nie masz odpowiednich uprawnień do tej komendy!")

def setup(client):
    client.add_cog(levels(client))