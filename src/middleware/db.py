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
        conn: asyncpg.Connection = await self.pool.acquire()
        repo = Repository(conn)
        data['repo'] = repo
        await handler(event, data)
        
        del data['repo']
        await conn.close()
