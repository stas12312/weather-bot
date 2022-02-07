from typing import Callable, Any, Awaitable

import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import Message

from services.repo import Repository


class DBMiddleware(BaseMiddleware):
    def __init__(self, pool: asyncpg.Pool) -> None:
        self.pool = pool

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        # Берем соединение из пула и на основе
        # него создаём репозиторий для взаимодействия с БД
        conn: asyncpg.Connection = await self.pool.acquire()
        repo = Repository(conn)
        data['repo'] = repo
        await handler(event, data)

        # Закрываем соединение
        del data['repo']
        await conn.close()
