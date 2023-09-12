# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
import config


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in config.BOT_ADMIN
