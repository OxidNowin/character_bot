# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

choose_person_ikb = ReplyKeyboardMarkup(resize_keyboard=True)
choose_person_ikb.add(KeyboardButton('Выбрать персонажа',
                                     web_app=WebAppInfo(url='https://oxidnowin.github.io/')))
