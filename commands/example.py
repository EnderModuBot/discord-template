from discord import Interaction
from ModuBotDiscord import ModuBotDiscord
from ModuBotDiscord.commands import (
    BaseCommand,
    check_bot_owner,
    check_bot_permission,
    check_guild_owner,
    check_permission,
    send_message,
)
from ModuBotDiscord.enums import PermissionEnum


class ExampleCommand(BaseCommand):
    async def register(self, bot: ModuBotDiscord):
        @bot.tree.command(
            name="check_bot_permission_example",
            description="Example for `@check_bot_permission`",
        )
        @check_bot_permission(PermissionEnum.ADMINISTRATOR)
        async def check_bot_permission_example(interaction: Interaction):
            await send_message(
                interaction,
                f"Bot has the Permission: `{PermissionEnum.ADMINISTRATOR}`",
                ephemeral=True,
            )

        @bot.tree.command(
            name="check_bot_permission2_example",
            description="Example for `@check_bot_permission`",
        )
        @check_bot_permission(PermissionEnum.KICK_MEMBERS, PermissionEnum.BAN_MEMBERS)
        async def check_bot_permission_multiple_example(interaction: Interaction):
            await send_message(
                interaction,
                f"Bot has the Permissions: `{PermissionEnum.KICK_MEMBERS}`, `{PermissionEnum.BAN_MEMBERS}`",
                ephemeral=True,
            )

        @bot.tree.command(
            name="check_permission_example",
            description="Example for `@check_permission`",
        )
        @check_permission(PermissionEnum.ADMINISTRATOR)
        async def check_permission_example(interaction: Interaction):
            await send_message(
                interaction,
                f"You have the Permission: `{PermissionEnum.ADMINISTRATOR}`",
                ephemeral=True,
            )

        @bot.tree.command(
            name="check_permission2_example",
            description="Example for `@check_permission`",
        )
        @check_permission(PermissionEnum.KICK_MEMBERS, PermissionEnum.BAN_MEMBERS)
        async def check_permission_multiple_example(interaction: Interaction):
            await send_message(
                interaction,
                f"You have the Permissions: `{PermissionEnum.KICK_MEMBERS}`, `{PermissionEnum.BAN_MEMBERS}`",
                ephemeral=True,
            )

        @bot.tree.command(
            name="check_bot_owner_example", description="Example for `@check_bot_owner`"
        )
        @check_bot_owner()
        async def check_bot_owner_example(interaction: Interaction):
            await send_message(interaction, "You are the Owner of the Bot!")

        @bot.tree.command(
            name="check_guild_owner_example",
            description="Example for `@check_guild_owner`",
        )
        @check_guild_owner()
        async def check_guild_owner_example(interaction: Interaction):
            await send_message(interaction, "You are the Owner of the Guild!")
