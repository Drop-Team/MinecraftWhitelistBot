from aiogram import Bot
from aiogram import types

from . import states


class NicknamesManager:
    message: types.Message
    state: states.BaseState
    author_id: int

    def __init__(self, author_id: int = None, message: types.Message = None):
        self.chat_id = author_id
        self.message = message
        self.state = states.NicknamesListState(author_id)

    async def update_message(self):
        await self.message.edit_text(
            text=self.state.get_message_text(),
            reply_markup=self.state.get_message_keyboard(),
            parse_mode=types.ParseMode.HTML
        )

    async def send_message(self, bot: Bot, chat_id: int):
        self.message = await bot.send_message(
            chat_id=chat_id,
            text=self.state.get_message_text(),
            reply_markup=self.state.get_message_keyboard(),
            parse_mode=types.ParseMode.HTML
        )
