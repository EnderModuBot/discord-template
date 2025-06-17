from discord import Interaction
from ModuBotDiscord import ModuBotDiscord
from ModuBotDiscord.commands import BaseCommand


class PingCommand(BaseCommand):
    async def register(self, bot: ModuBotDiscord):
        @bot.tree.command(name="ping", description="Responds with Pong!")
        async def ping(interaction: Interaction):
            await interaction.response.send_message("Pong!", ephemeral=True)
