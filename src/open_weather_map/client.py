from .api import ApiService
from . import consts
from . import models


class OpenWeatherMapClient:
    """
    Клиент для работы с API openweathermap.org
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_service = ApiService(self.api_key)

    async def one_call(
            self,
            lat: float,
            lon: float,
            exclude_parts: list[str],
    ) -> models.OneCall:
        """
        Получение информации о погоде
        :param lat: Широта
        :param lon: Долгота
        :param exclude_parts: Исключаемая информация
        :return: Данные о погоде
        """
        params = {
            'lat': lat,
            'lon': lon,
            'part': ','.join(exclude_parts),
        }

        result = await self.api_service.api_request(
            api_service=consts.APIService.DATA,
            api_method=consts.DataAPIMethod.ONE_CALL,
            params=params,
        )
        return models.OneCall(**result)
