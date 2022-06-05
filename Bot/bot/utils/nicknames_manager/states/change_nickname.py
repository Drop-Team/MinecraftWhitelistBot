from aiogram import types

from .base import BaseState


class ChangeNicknameState(BaseState):
    author_telegram_id: int
    old_nickname: str

    def __init__(self, author_telegram_id: int, old_nickname: str):
        self.author_telegram_id = author_telegram_id
        self.old_nickname = old_nickname

    def get_message_text(self) -> str:
        text = f"Enter new nickname. Old nickname <b>{self.old_nickname}</b> will be removed."
        return text

    def get_message_keyboard(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup()
        return markup
