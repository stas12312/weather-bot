import asyncio

from config import load_from_file
from open_weather_map.client import OpenWeatherMapClient

config = load_from_file('../config.ini')


async def main():
    client = OpenWeatherMapClient(
        api_key=config.open_weather.api_key,
    )


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
