"""
Работы с таблицей Пользователи
"""
import json

from asyncpg import Connection
from .models import User, WeatherWidget


class Repository:

    def __init__(self, conn: Connection):
        self.conn = conn

    async def get_user_by_id(
            self,
            user_id: int
    ) -> User:
        """
        Получение пользователя по идентификатору
        :param user_id: Идентификатор пользователя
        :return: Пользователь
        """
        user = await self.conn.fetchrow(
            """SELECT * FROM tg_user WHERE user_id=$1""",
            user_id
        )
        return User(**user)

    async def create_user(
            self,
            user_id: int,
            first_name: str,
            last_name: str | None,
            username: str | None,
    ) -> User:
        """
        Создание пользователя
        :param user_id: Идентификатор пользователя
        :param first_name: Имя
        :param last_name: Фамилия
        :param username: Пользовательское имя
        :return: Пользователь
        """
        user = await self.conn.fetchrow(
            """
            INSERT INTO tg_user(user_id, first_name, last_name, username)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (user_id) DO UPDATE 
            SET first_name=$2, last_name=$3, username=$4
            RETURNING *
            """,
            user_id, first_name, last_name, username,
        )

        return User(**user)

    async def create_widget(
            self,
            user_id: int,
            name: str,
            timezone_offset: int,
            latitude: float,
            longitude: float,
            city_name: str,
            settings: dict,
            is_default: bool,
    ) -> WeatherWidget:
        """
        Создание виджета
        :param user_id: Идентификатор пользователя
        :param name: Название виджета
        :param timezone_offset: Временной сдвиг
        :param latitude: Широта
        :param longitude: Долгота
        :param city_name: Название города
        :param settings: Настройки виджета
        :param is_default: Виджет по умолчанию
        :return:
        """

        result = await self.conn.fetchrow(
            """
        INSERT INTO user_weather_widget 
        (user_id, name, timezone_offset, latitude, longitude, city_name, settings, is_default)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        RETURNING *
        """,
            user_id,
            name,
            timezone_offset,
            latitude,
            longitude,
            city_name,
            json.dumps(settings),
            is_default,
        )
        return WeatherWidget(**result)

    async def get_default_widget(
            self,
            user_id: int,
    ) -> WeatherWidget:
        """

        :param user_id:
        :return:
        """
        result = await self.conn.fetchrow(
            """
            SELECT * FROM user_weather_widget WHERE user_id=$1 AND is_default=true
            """,
            user_id
        )
        return WeatherWidget(**result)
