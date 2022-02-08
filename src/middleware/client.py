from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from config import Config
from open_weather_map import OpenWeatherMapClient


class ClientMiddleware(BaseMiddleware):
    def __init__(self, weather_client: OpenWeatherMapClient) -> None:
        self.weather_client = weather_client

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        data['weather_client'] = self.weather_client
        await handler(event, data)
