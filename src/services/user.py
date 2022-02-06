from . import models
from .repo import Repository


async def create_user(
        repo: Repository,
        user_id: int,
        first_name: str,
        last_name: str | None,
        username: str | None,
) -> models.User:
    """
    Добавление пользователя
    :param repo:
    :param user_id:
    :param first_name:
    :param last_name:
    :param username:
    :return:
    """

    user = await repo.create_user(
        user_id,
        first_name,
        last_name,
        username
    )
    return user
