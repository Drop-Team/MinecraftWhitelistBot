from abc import ABC, abstractmethod

from aiogram import types


class BaseState(ABC):
    @abstractmethod
    def get_message_text(self) -> str:
        pass

    @abstractmethod
    def get_message_keyboard(self) -> types.InlineKeyboardMarkup:
        pass
