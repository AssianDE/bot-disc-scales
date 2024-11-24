import discord
from discord.ext import commands
import Lancer

class LancerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lanceur = Lancer.Lancer()

    def afficher_le_lancer(self, ctx, carac=1, comp=0, mana=1):
        total_des = carac + comp
        resultat = self.lanceur.lancer_de_des(carac, comp, mana)
        roll_affichable = " , ".join([i[0] for i in resultat[0]])
        
       # face_url = f"https://cdn.discordapp.com/attachments/833174207818498068/835588918464348160/Dice4BotDiscord-{min(resultat[2], 9)}.png"

        embed = discord.Embed(
            description=f"{total_des}g**{carac}** ({mana}dMana)\n{roll_affichable}",
            color=0x66c0c6
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        # embed.set_thumbnail(url=face_url)
        embed.add_field(name="Seuil", value=f"{resultat[1]}", inline=True)
        embed.add_field(name="Qualité", value=f"{resultat[2]}", inline=True)

        return embed

    @commands.command(aliases=["d", "dés", "roll", "r"], description="Lance des dés.")
    async def dice(self, ctx, carac: int = 1, comp: int = 0, mana: int = 1):
        embed = self.afficher_le_lancer(ctx, carac, comp, mana)
        await ctx.send(embed=embed)

    @commands.command(aliases=["di", "init"], description="Lancer une initiative.")
    async def init_dice(self, ctx, reflex: int):
        resultat = self.lanceur.lancer_init(reflex)
        embed = discord.Embed(
            color=0x66c0c6
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        embed.add_field(name="Initiative", value=f"{resultat}", inline=True)
        await ctx.send(embed=embed)

# Fonction setup pour charger le Cog
async def setup(bot):
    await bot.add_cog(LancerCog(bot))
