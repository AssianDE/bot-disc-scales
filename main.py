import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import MyHelp

# Récupération du token
load_dotenv(dotenv_path="config")

# Configuration des intents
default_intents = discord.Intents.all()

# Création du bot
bot = commands.Bot(
    command_prefix="!",
    intents=default_intents,
    help_command=MyHelp.MyHelp()
)

@bot.event
async def on_ready():
    print(f"Le Bot **{bot.user.display_name}** est prêt")
    print(f"Logged in as {bot.user} ({bot.user.id})")
    print("------")

# Chargement des extensions (Cogs)
async def load_extensions():
    # Ajoutez ici tous vos fichiers de cog
    for extension in ["LancerCog", "BoobsCog"]:
        try:
            await bot.load_extension(extension)
            print(f"Loaded extension '{extension}'")
        except Exception as e:
            print(f"Failed to load extension '{extension}': {e}")

# Fonction principale pour démarrer le bot
async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.getenv("TOKEN"))

# Lancement du bot
import asyncio
asyncio.run(main())
