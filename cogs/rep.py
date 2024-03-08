import nextcord
import json
from nextcord import Interaction, User
from nextcord.ext import commands
import os
import time
from emoji import *

class rep(commands.Cog):
    user_profiles_file = 'user_profiles.json'
    
    def __init__(self, client):
        self.client = client
        
    async def load_user_profiles(self):
        with open(self.user_profiles_file, 'r') as file:
            user_profiles = json.load(file)
        return user_profiles
        
    @nextcord.slash_command(name='rep', description='Przydziel innemu użytkownikowi punkt Rep')
    async def rep(self, interaction: Interaction, user: User):
        if interaction.user.id == user.id:
            await interaction.response.send_message("**S e r i o ?**")
            return
        
        user_profiles = await self.load_user_profiles()
        
        user_id = str(interaction.user.id)
        
        if user_id in user_profiles and "last_rep_timestamp" in user_profiles[user_id]:
            last_rep_timestamp = user_profiles[user_id]["last_rep_timestamp"]
            if time.time() - last_rep_timestamp < 24 * 3600:
                await interaction.response.send_message(f"{failed_emoji} Możesz przydzielić punkty tylko raz na 24h.")
                return
        
        user_id_given = str(user.id)
        if user_id_given in user_profiles:
            if "rep_points" in user_profiles[user_id_given]:
                user_profiles[user_id_given]["rep_points"] += 1
            else:
                user_profiles[user_id_given]["rep_points"] = 1
        else:
            user_profiles[user_id_given] = {"rep_points": 1}
            
        user_profiles[user_id]["last_rep_timestamp"] = time.time()
        
        with open(rep.user_profiles_file, 'w') as file:
            json.dump(user_profiles, file, indent=4)
        
        await interaction.response.send_message(f"{pzmrep} Przydzielono punkt Rep {user.mention}")
        
    async def load_rep_profiles(self):
        with open(self.user_profiles_file, 'r') as file:
            user_profiles = json.load(file)
        return user_profiles
    
def setup(client):
    client.add_cog(rep(client))