import discord
from discord.ext import commands

class Boobs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Des Boobs pour Alfrida")
    async def boobs(self, ctx):
        # Mention de l'auteur de la commande
        await ctx.send(ctx.author.mention)

        # Récupération du membre par ID
        frifri_id = 243135257946095617
        frifri = ctx.guild.get_member(frifri_id)

        # Vérification si le membre est trouvé
        if frifri:
            await ctx.send(f"{frifri.mention}, arrête de jouer avec les boobs du Bot !!!")
        else:
            await ctx.send("Je n'ai pas pu trouver Alfrida dans cette guilde !")

# Fonction setup pour charger le Cog
async def setup(bot):
    await bot.add_cog(Boobs(bot))
