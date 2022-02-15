"""
Модуль для реализации погодного виджета
"""
from datetime import datetime, timedelta

from open_weather_map.models import OneCall

TIME_FORMAT = '%H:%M'
DATE_FORMAT = '%m.%d.%Y'


class WeatherWidget:

    def __init__(self, weather: OneCall, widget_config: dict):
        """
        Конструктор класса
        :param weather: Информация о погоде
        :param widget_config: Конфигурация виджета
        """
        self.weather = weather
        self.config = widget_config

    def as_text(self) -> str:
        """
        Получение виджета в текстовом представлении
        :return: Текстовое представление виджета
        """
        current_weather = self.weather.current
        offset = self.weather.timezone_offset
        current_datetime = local_time_to_global(current_weather.dt, offset)
        today_weather = self.weather.daily[0]

        msg_parts = [
            f'ПОГОДА НА СЕГОДНЯ <b>({current_datetime.strftime(DATE_FORMAT)})</b>',
            f'🌡 Температура: {r_temp(current_weather.temp)} ({current_weather.weather[0].description})',
            f'🌡 Ощущается как {r_temp(current_weather.feels_like)}',
            f'💨 Ветер {current_weather.wind_speed} м/c',
            f'🌅 Восход: {local_time_to_global(current_weather.sunrise, offset).strftime(TIME_FORMAT)}',
            f'🌆 Закат: {local_time_to_global(current_weather.sunset, offset).strftime(TIME_FORMAT)}',
            f'',
            f'🌡 Утро <b>{r_temp(today_weather.temp.morn)}</b> '
            f'(Ощущается как {r_temp(today_weather.feels_like.morn)})',
            f'🌡 День <b>{r_temp(today_weather.temp.day)}</b> '
            f'(Ощущается как {r_temp(today_weather.feels_like.day)})',
            f'🌡 Вечер <b>{r_temp(today_weather.temp.eve)}</b> '
            f'(Ощущается как {r_temp(today_weather.feels_like.eve)})',
            f'🌡 Ночь <b>{r_temp(today_weather.temp.night)}</b> '
            f'(Ощущается как {r_temp(today_weather.feels_like.night)})',
            f'Максимальная температура: {r_temp(today_weather.temp.max)}',
            f'Минимальная температура: {r_temp(today_weather.temp.min)}',
        ]

        return '\n'.join(msg_parts)


def local_time_to_global(
        timestamp: int,
        timezone_offset: int,
) -> datetime:
    """
    Преобразование локального времени в глобальное
    :param timestamp: Временная отметка
    :param timezone_offset: Временной сдвиг
    :return:
    """

    timestamp_datetime = datetime.utcfromtimestamp(timestamp)
    local_timestamp_datetime = timestamp_datetime + timedelta(seconds=timezone_offset)
    return local_timestamp_datetime


def r_temp(
        temp: float
) -> float:
    """
    Округление температуры
    :param temp: Температура
    :return:
    """
    return round(temp, 1)
