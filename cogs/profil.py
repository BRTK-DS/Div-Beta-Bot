import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Embed, PartialEmoji
from serwerID import *
from emoji import *
from datetime import datetime
import json
import os
from nextcord.ext.application_checks import has_role, ApplicationMissingRole
from cogs.levels import levels

class profil(commands.Cog):
    user_profiles_file = 'user_profiles.json'
    badge_data_file = 'badge_data.json'

    def __init__(self, client):
        self.client = client
        self.initialize_profiles()
        self.initialize_badges()
        self.levels_cog = levels(client)

    def initialize_profiles(self):
        if not os.path.exists(profil.user_profiles_file):
            with open(profil.user_profiles_file, 'w') as file:
                initial_data = {}
                json.dump(initial_data, file)

    def initialize_badges(self):
        if not os.path.exists(profil.badge_data_file):
            with open(profil.badge_data_file, 'w') as file:
                initial_data = {}
                json.dump(initial_data, file)

    @nextcord.slash_command(name="profil", description="Twój profil na serwerze", guild_ids=[ServerID])
    async def profil(self, interaction: Interaction, user: nextcord.User = None):
        if not user:
            user = interaction.user

        # Czyta dane z pliku JSON
        with open(self.user_profiles_file, 'r') as file:
            user_profiles = json.load(file)

        user_id = str(user.id)
        level_info = self.levels_cog.get_user_level_info(user.id)

        if user_id in user_profiles:
            profile_data = user_profiles[user_id]
            date_of_birth = profile_data.get("date_of_birth")
            badges = profile_data.get("badges", [])
        else:
            date_of_birth = None
            badges = []

        embed = Embed(title=f"{profil_emoji}Profil użytkownika @{user.display_name}", color=0xa751ed)

        badge_1 = puste_odzn
        badge_2 = puste_odzn
        badge_3 = puste_odzn
        badge_4 = puste_odzn
        badge_5 = puste_odzn
        badge_6 = puste_odzn
        badge_7 = puste_odzn
        badge_8 = puste_odzn
        badge_9 = puste_odzn
        badge_10 = puste_odzn
        badge_11 = puste_odzn
        badge_12 = puste_odzn
        badge_13 = puste_odzn
        badge_14 = puste_odzn
        badge_15 = puste_odzn
        badge_16 = puste_odzn
        badge_17 = puste_odzn
        badge_18 = puste_odzn

        if date_of_birth:
            embed.add_field(name="DANE UŻYTKOWNIKA:",
                    value=f"{nkname}Nickname: {user.mention}\n"
                          f"{urodziny}Data urodzin: {date_of_birth}\n"
                          f"{wiek}Wiek: {self.calculate_age(date_of_birth)}",
                    inline=False
                    )
        else:
            embed.add_field(name="DANE UŻYTKOWNIKA:",
                    value=f"{nkname}Nickname: {user.mention}\n"
                          f"{urodziny}Data urodzin: Brak\n"
                          f"{wiek}Wiek: Brak",
                    inline=False
                    )

        embed.add_field(name="BANK: ",
                value=f"{monety_emoji}Portfel: Work In Progress",
                inline=False
                )
        
        level = level_info['level']
        
        embed.add_field(name="POZIOM: ",
                value=f"{poziom_emoji}Poziom: {level}\n" 
                      f"{pzmrep}Rep Level: Work In Progress\n",
                inline=False
                ) 

        if badges:
            for i, badge in enumerate(badges):
                if i == 0:  # First badge slot
                    badge_1 = str(badge)
                elif i == 1:  # Second badge slot
                    badge_2 = str(badge)
                elif i == 2:
                    badge_3 = str(badge)
                elif i == 3:
                    badge_4 = str(badge)
                elif i == 4:
                    badge_5 = str(badge)
                elif i == 5:
                    badge_6 = str(badge)
                elif i == 6:
                    badge_7 = str(badge)
                elif i == 7:
                    badge_8 = str(badge)
                elif i == 8:  
                    badge_9 = str(badge)
                elif i == 9:  
                    badge_10 = str(badge)
                elif i == 10:
                    badge_11 = str(badge)
                elif i == 11:
                    badge_12 = str(badge)
                elif i == 12:
                    badge_13 = str(badge)
                elif i == 13:
                    badge_14 = str(badge)
                elif i == 14:
                    badge_15 = str(badge)
                elif i == 15:
                    badge_16 = str(badge)

        badge_field_value = f"{badge_1} {badge_2} {badge_3} {badge_4} {badge_5} {badge_6}\n{badge_7} {badge_8} {badge_9} {badge_10} {badge_11} {badge_12}\n{badge_13} {badge_14} {badge_15} {badge_16} {badge_17} {badge_18}"

        embed.add_field(name="ODZNAKI: ", value=badge_field_value, inline=False)

        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_image(url=user.display_avatar.url)

        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="odznaka", description="Przypisz odznakę użytkownikowi")
    @has_role(1170518127369519124)
    async def odznaka(self, interaction: Interaction, user: nextcord.User, badge_name: str):

        with open(self.user_profiles_file, 'r') as file:
            user_profiles = json.load(file)

        user_id = str(user.id)

        if user_id not in user_profiles:
            user_profiles[user_id] = {"badges": [badge_name]}
            await interaction.response.send_message(f"{success_emoji}Przypisano odznakę '{badge_name}' użytkownikowi {user.mention}.")
        else:
            if "badges" not in user_profiles[user_id]:
                user_profiles[user_id]["badges"] = [badge_name]
                await interaction.response.send_message(f"{success_emoji}Przypisano odznakę '{badge_name}' użytkownikowi {user.mention}.")
            elif badge_name not in user_profiles[user_id]["badges"]:
                user_profiles[user_id]["badges"].append(badge_name)
                await interaction.response.send_message(f"{success_emoji}Przypisano odznakę '{badge_name}' użytkownikowi {user.mention}.")
            else:
                await interaction.response.send_message(f"{user.mention} już posiada odznakę '{badge_name}'.")

        with open(self.user_profiles_file, 'w') as file:
            json.dump(user_profiles, file, indent=4)

    async def update_badges(self, user_id, badges):
        pass
    
    @odznaka.error
    async def odznaka_error(self, interaction: Interaction, error):
        if isinstance(error, ApplicationMissingRole):
            await interaction.response.send_message(f"{failed_emoji}Nie masz odpowiednich uprawnień do tej komendy!")

    def calculate_age(self, date_of_birth):
        from datetime import datetime
        birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    
    @nextcord.slash_command(name="data_urodzin", description="Aktualizuj datę urodzin. Format RRRR-MM-DD.", guild_ids=[ServerID])
    async def data_urodzin(self, interaction: Interaction, date_of_birth: str):
        try:
            birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        except ValueError:
            await interaction.response.send_message(f"{failed_emoji}Nieprawidłowy format daty. Użyj formatu RRRR-MM-DD.")
            return

        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        user_id = str(interaction.user.id)

        with open('user_profiles.json', 'r') as file:
            user_profiles = json.load(file)

        if user_id in user_profiles:
            user_profiles[user_id]["date_of_birth"] = date_of_birth
        else:
            user_profiles[user_id] = {"date_of_birth": date_of_birth}

        with open('user_profiles.json', 'w') as file:
            json.dump(user_profiles, file, indent=4)

        await interaction.response.send_message(f"{success_emoji}Pomyślnie zaktualizowano profil.")
        
    @nextcord.slash_command(name="dodaj_odznake", description="Dodaj emoji jako odznakę")
    @has_role(1170518127369519124)
    async def dodaj_odznake(self, interaction: Interaction, emoji: str, badge_name: str):

        if not emoji:
            await interaction.response.send_message(f"{failed_emoji}Nieprawidłowy emoji.")
            return

        parsed_emoji = PartialEmoji.from_str(emoji)

        if parsed_emoji is None:
            await interaction.response.send_message(f"{failed_emoji}Nieprawidłowy format emoji.")
            return

        with open(profil.badge_data_file, 'r') as file:
            badge_data = json.load(file)

        emoji_name = badge_name

        if emoji_name in badge_data:
            await interaction.response.send_message(f"{failed_emoji}Ta odznaka już istnieje.")
            return

        badge_data[emoji_name] = {
            "emoji_id": parsed_emoji.id,
            "emoji_name": str(parsed_emoji)
        }

        with open(profil.badge_data_file, 'w') as file:
            json.dump(badge_data, file, indent=4)

        await interaction.response.send_message(f"{success_emoji}Dodano emoji jako odznakę: {str(parsed_emoji)}")
        
    @dodaj_odznake.error
    async def dodaj_odznake_error(self, interaction: Interaction, error):
        if isinstance(error, ApplicationMissingRole):
            await interaction.response.send_message(f"{failed_emoji}Nie masz odpowiednich uprawnień do tej komendy!")

def setup(client):
    client.add_cog(profil(client))