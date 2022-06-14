from aiogram import Dispatcher

from .logs import LogsMiddleware
from .metrics import MetricsMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(MetricsMiddleware())
    dp.middleware.setup(LogsMiddleware())
