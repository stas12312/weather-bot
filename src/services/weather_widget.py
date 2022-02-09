"""
Модуль для реализации погодного виджета
"""
from open_weather_map.models import OneCall
from datetime import datetime, time

TIME_FORMAT = '%H:%M'


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
        msg_parts = [
            f'ПОГОДА НА СЕГОДНЯ',
            f'🌡 Температура: {current_weather.temp} [{current_weather.feels_like}]',
            f'Описание: {current_weather.weather[0].description}',
            f'Восход: {datetime.fromtimestamp(current_weather.sunrise).strftime(TIME_FORMAT)}',
            f'Закат: {datetime.fromtimestamp(current_weather.sunset).strftime(TIME_FORMAT)}',
        ]

        return '\n'.join(msg_parts)
