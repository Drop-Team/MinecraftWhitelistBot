from typing import Optional

from aiogram import types

from .base import BaseState
from ..callback_data import change_nickname_cb, delete_nickname_cb, go_to_nicknames_list_cb


class NicknameState(BaseState):
    author_telegram_id: int
    page: int

    def __init__(self, author_telegram_id: int, nickname):
        self.nickname = nickname
        self.author_telegram_id = author_telegram_id

    def get_message_text(self) -> str:
        text = f"Selected nickname: <b>{self.nickname}</b>\n" \
               f"What do you want to do with it?"
        return text

    def get_message_keyboard(self) -> Optional[types.InlineKeyboardMarkup]:
        markup = types.InlineKeyboardMarkup()
        markup.insert(types.InlineKeyboardButton(
            text="Change nickname",
            callback_data=change_nickname_cb.new(self.nickname)
        ))
        markup.insert(types.InlineKeyboardButton(
            text="Delete nickname",
            callback_data=delete_nickname_cb.new(self.nickname)
        ))
        markup.add(types.InlineKeyboardButton(
            text="<< Back to nicknames",
            callback_data=go_to_nicknames_list_cb.new(self.author_telegram_id)
        ))

        return markup
