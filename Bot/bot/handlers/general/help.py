from aiogram import types


async def help_command(msg: types.Message):
    """Send bot commands and all useful information"""

    text = "InnoMinecraftBot is a bot for managing your nicknames on the minecraft server of InnoMC club.\n" \
           "It uses InnoID to confirm that you are a student or an employee of Innopolis University.\n" \
           "/help - Shows this message\n" \
           "/auth - Get instruction for authorization\n\n" \
           "/add_nickname - Add your nickname to whitelist\n" \
           "/my_nicknames - Manage your nicknames in whitelist\n\n" \
           "Developers & Support: @DropTeamDev\n" \
           "In case of problems, write to @blinikar or @KeepError\n\n" \
           "Our products are open source, so you can find repository on GitHub: " \
           "https://github.com/Drop-Team/MinecraftWhitelistBot\n" \
           "Star if you liked it :)"

    await msg.answer(text, disable_web_page_preview=True)
