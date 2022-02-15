from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from . import buttons as btn


def get_main_menu(
        is_set_location: bool
) -> ReplyKeyboardMarkup:
    """
    Получение главного меню
    :param is_set_location: Настроена локация
    :return:
    """
    keyboard = []
    if is_set_location:
        keyboard.append([btn.WEATHER])

    keyboard.append([btn.SETTING_WEATHER])

    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
    return keyboard


def send_geo_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [btn.SEND_LOCATION],
        ],
        resize_keyboard=True,
    )
    return keyboard
