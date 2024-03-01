# import nextcord
# from nextcord import Interaction, Member, Embed, SlashOption
# from nextcord.ext import commands
# import asyncio
# from serwerID import *
# import json

# class Economy(commands.Cog):
#     def __init__(self, client):
#         self.client = client
#         self.data_file = "economy_data.json"  # JSON file to store data
#         self.data = self.load_data()

#     def load_data(self):
#         try:
#             with open(self.data_file, "r") as f:
#                 return json.load(f)
#         except FileNotFoundError:
#             return {}

#     def save_data(self):
#         with open(self.data_file, "w") as f:
#             json.dump(self.data, f, indent=4)

#     def create_balance(self, user):
#         user_id = str(user.id)
#         if user_id not in self.data:
#             self.data[user_id] = {"wallet": 0, "bank": 100, "maxbank": 10000000}
#             self.save_data()

#     def get_balance(self, user):
#         user_id = str(user.id)
#         if user_id not in self.data:
#             self.create_balance(user)
#         return (
#             self.data[user_id]["wallet"],
#             self.data[user_id]["bank"],
#             self.data[user_id]["maxbank"],
#         )

#     def update_wallet(self, user, amount: int):
#         user_id = str(user.id)
#         if user_id not in self.data:
#             self.create_balance(user)
#         self.data[user_id]["wallet"] += amount
#         self.save_data()

#     @commands.Cog.listener()
#     async def on_ready(self):
#         await asyncio.sleep(3)
#         print("Baza danych gotowa!")

#     @nextcord.slash_command(name="konto", description="Sprawdź swój stan konta", guild_ids=[ServerID])
#     async def konto(self, interaction: Interaction, user:nextcord.User = None):
#         if not user:
#             user = interaction.user
#         wallet, bank, maxbank = self.get_balance(user)
#         em = nextcord.Embed(title=f'Stan konta użytkownika {user.display_name}', color=0x9be024)
#         em.add_field(name="Wallet", value=str(wallet))
#         em.add_field(name="Bank", value=f"{bank}/{maxbank}")
#         em.set_thumbnail(url=user.display_avatar.url)
#         await interaction.response.send_message(embed=em)

# def setup(client):
#     client.add_cog(Economy(client))