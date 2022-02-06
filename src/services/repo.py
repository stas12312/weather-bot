"""
Работы с таблицей Пользователи
"""
from asyncpg import Connection
from .models import User


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
