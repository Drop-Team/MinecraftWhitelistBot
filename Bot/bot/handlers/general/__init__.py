from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .authorization import authorize_command, is_not_authorized_error
from .help import help_command
from .start import start_command


def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, CommandStart())
    dp.register_message_handler(help_command, CommandHelp())
    dp.register_message_handler(authorize_command, commands="auth")
    dp.register_message_handler(is_not_authorized_error, content_types=["any"], is_authorized=False)
