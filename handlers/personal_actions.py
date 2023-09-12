# - *- coding: utf- 8 - *-
from aiogram import types

from dispatcher import dp
from keyboards import *
from utils import is_user, add_user, get_hello_message, set_dialog, get_dialog_name
from utils.openai_api import get_response


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ans = f"Привет, {message.from_user.first_name.title()}\n"
    if not await is_user(message.from_user.id):
        await add_user(message.from_user.id, message.from_user.username)
        await set_dialog(message.from_user.id)
        ans += "Я бот для генерации диалогов с различными личностями на основе AI!"
    else:
        ans += 'Рады снова тебя видеть!'

    await message.bot.send_message(message.chat.id, ans, reply_markup=choose_person_ikb)


@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    await message.bot.send_message(message.chat.id, "Главное меню:", reply_markup=choose_person_ikb)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    character = message.web_app_data.data
    hello_message = await get_hello_message(message.from_user.id, character)
    await message.bot.send_message(message.chat.id, hello_message, reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler()
async def send_msg(message: types.Message):
    dialog_name = await get_dialog_name(message.from_user.id)

    if dialog_name:
        reply_msg = await get_response(dialog_name[0], message.text)
    else:
        reply_msg = 'Для начала диалога выберите персонажа, кликнув по кнопке клавиатуры'

    await message.bot.send_message(message.chat.id, reply_msg)
