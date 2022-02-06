"""
Получение конфигурации приложения
"""
import configparser
from pydantic import BaseModel


class OpenWeatherConfig(BaseModel):
    """Конфигурация работы с  OpenWeatherMap API"""
    api_key: str


class BotConfig(BaseModel):
    """Конфигурация работы с  Telegram Bot API"""
    api_key: str


class DatabaseConfig(BaseModel):
    """Конфигурация подключения к БД"""
    database: str
    user: str
    password: str
    host: str
    port: int


class Config(BaseModel):
    """Конфигурация приложения"""
    open_weather: OpenWeatherConfig
    tg_bot: BotConfig
    db: DatabaseConfig


def load_from_file(path: str) -> Config:
    config_values = configparser.ConfigParser()
    config_values.read(path)
    return load_config(config_values)


def load_config(values: dict[str, dict | str]) -> Config:
    """
    Получение конфигурации из переменных окружения
    :return: Конфигурация приложения
    """

    open_weather = values['open_weather']
    tg_bot = values['tg_bot']
    db = values['db']

    return Config(
        open_weather=OpenWeatherConfig(**open_weather),
        tg_bot=BotConfig(**tg_bot),
        db=DatabaseConfig(**db)
    )
