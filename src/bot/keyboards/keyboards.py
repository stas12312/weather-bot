from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from . import buttons


def get_main_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [buttons.WEATHER, buttons.MY_WIDGET],
            [buttons.ADD_WIDGET],
        ],
        resize_keyboard=True,
    )
    return keyboard


def send_geo_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [buttons.SEND_LOCATION],
        ],
        resize_keyboard=True,
    )
    return keyboard
