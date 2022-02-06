import asyncpg
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import Message
from config import Config
from services.repo import Repository
from middleware.db import DBMiddleware
from .handlers.user import register_handlers


def setup_dispatcher(config: Config, pool: asyncpg.Pool) -> Dispatcher:
    """
    Настройки клиента для работы с Telegram
    :param config: Конфигурация
    :param pool: Репозиторий
    :return:
    """

    router = Router()
    router.message.middleware(DBMiddleware(pool))
    register_handlers(router)

    dp = Dispatcher()
    dp.include_router(router)
    return dp
