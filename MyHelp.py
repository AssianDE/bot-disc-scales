import ast
import discord
from discord.ext import commands

class MyHelp(commands.HelpCommand):
    # !help
    async def send_bot_help(self, mapping):
        affich_dict = {}

        for cog, commandes in mapping.items():
            if commandes:
                for commande in commandes:
                    affich_dict[commande.name] = [commande.aliases, commande.description]
                    if commande.usage:
                        affich_dict[commande.name].append(ast.literal_eval(commande.usage))
                    else:
                        affich_dict[commande.name].append({})

        embed_help = discord.Embed(title="Help", color=discord.Color.blue())

        for nom_commande, signature_commandes in affich_dict.items():
            affich_commande = ""

            # Alias
            if signature_commandes[0]:
                affich_commande = f"*alias* : {' | '.join(signature_commandes[0])}\n"

            # Description
            if signature_commandes[1]:
                affich_commande += f"{signature_commandes[1]}\n"

            # Usage
            affich_commande += "\n*usages* :"
            if signature_commandes[2]:
                for usage, description_usage in signature_commandes[2].items():
                    affich_commande += f"\n{self.context.clean_prefix}{nom_commande} {usage}\n{description_usage}\n"
            else:
                affich_commande += f"\n{self.context.clean_prefix}{nom_commande}\n"

            affich_commande += "\n--------------------\n\n\n"

            embed_help.add_field(name=nom_commande, value=affich_commande, inline=False)

        await self.context.send(embed=embed_help)

    # !help <command>
    async def send_command_help(self, command):
        embed_help = discord.Embed(title=f"Help for {command.name}", color=discord.Color.green())

        affich_commande = ""

        # Alias
        if command.aliases:
            affich_commande += f"*alias* : {' | '.join(command.aliases)}\n"

        # Description
        if command.description:
            affich_commande += f"{command.description}\n"

        # Usage
        affich_commande += "\n*usages* :"
        if command.usage:
            for usage, description_usage in ast.literal_eval(command.usage).items():
                affich_commande += f"\n{self.context.clean_prefix}{command.name} {usage}\n{description_usage}\n"
        else:
            affich_commande += f"\n{self.context.clean_prefix}{command.name}\n"

        embed_help.add_field(name=command.name, value=affich_commande, inline=False)

        await self.context.send(embed=embed_help)

