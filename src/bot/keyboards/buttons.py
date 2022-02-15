"""
Клавиши для клавиатур
"""
from aiogram.utils.keyboard import KeyboardButton

ADD_WIDGET = KeyboardButton(text='✏ Добавить виджет')
MY_WIDGET = KeyboardButton(text='🌦 Мои виджеты')
SETTING_WEATHER = KeyboardButton(text='⚙ Настроить погоду')
WEATHER = KeyboardButton(text='🌤 Погода')

SEND_LOCATION = KeyboardButton(text='📍 Отправить местоположение', request_location=True)
