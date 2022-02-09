import logging
from typing import Any

import aiohttp
from .consts import BASE_URL, VERSION


class ApiService:
    """
    Сервис для работы с API
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = self.make_session()

    @classmethod
    def make_session(cls) -> aiohttp.ClientSession:
        """
        Создание сессии
        :return: Сессия
        """

        session = aiohttp.ClientSession()
        return session

    async def api_request(
            self,
            api_service: str,
            api_method: str,
            params: dict[str, str | float | int],
    ) -> dict[str, Any]:
        """
        Выполнение запроса к openweathermap.org
        :param api_service: API сервис
        :param api_method: API метод
        :param params: GET параметры запроса
        :return: Результат запроса
        """
        url = self.make_url(api_service, api_method)
        params['appid'] = self.api_key
        params['units'] = 'metric'
        params['lang'] = 'ru'
        result = await self.raw_request(url, params)
        return result

    async def raw_request(
            self,
            url: str,
            params: dict
    ) -> dict:
        """
        Выполнение запроса
        :param url: URL запроса,
        :param params: GET параметры запроса
        :return:
        """
        response = await self.session.get(url, params=params)
        data = await response.json()
        logging.info(response.url)
        return data

    @classmethod
    def make_url(
            cls,
            api_service: str,
            api_method: str,
    ) -> str:
        """
        Формирование полного URL для запроса
        :param api_service: API сервис
        :param api_method: API метод
        :return: URL для запроса
        """
        return f'{BASE_URL}/{api_service}/{api_method}'
