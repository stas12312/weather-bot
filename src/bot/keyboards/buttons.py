"""
Клавиши для клавиатур
"""
from aiogram.utils.keyboard import KeyboardButton

ADD_WIDGET = KeyboardButton(text='✏ Добавить виджет')
MY_WIDGET = KeyboardButton(text='🌦 Мои виджеты')
WEATHER = KeyboardButton(text='🌤 Погода')

SEND_LOCATION = KeyboardButton(text='📍 Отправить геопозицию', request_location=True)
