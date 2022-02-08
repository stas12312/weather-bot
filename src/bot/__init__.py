import asyncpg
from aiogram import Dispatcher, Router

from config import Config
from middleware.client import ClientMiddleware
from middleware.db import DBMiddleware
from open_weather_map import OpenWeatherMapClient
from .handlers.user import register_handlers as user_register
from .handlers.weather import register_handlers as weather_register


def setup_dispatcher(config: Config, pool: asyncpg.Pool) -> Dispatcher:
    """
    Настройки клиента для работы с Telegram
    :param config: Конфигурация
    :param pool: Репозиторий
    :return:
    """
    weather_client = OpenWeatherMapClient(api_key=config.open_weather.api_key)

    router = Router()
    router.message.middleware(DBMiddleware(pool))
    router.message.middleware(ClientMiddleware(weather_client))

    user_register(router)
    weather_register(router)

    dp = Dispatcher()
    dp.include_router(router)
    return dp
