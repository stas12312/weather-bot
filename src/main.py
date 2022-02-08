import asyncio
import logging

import asyncpg
from aiogram import Bot

from bot import setup_dispatcher
from config import load_from_file, Config
from logger import app_logger
from open_weather_map import OpenWeatherMapClient

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

app_config = load_from_file('../config.ini')


async def create_pool(config: Config) -> asyncpg.Pool:
    return await asyncpg.create_pool(
        database=config.db.database,
        user=config.db.user,
        password=config.db.password,
    )


async def main():
    pool = await create_pool(app_config)
    dp = setup_dispatcher(app_config, pool)
    bot = Bot(app_config.tg_bot.api_key)
    app_logger.info('Запуск бота')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
