from services.models import WeatherWidget
from services.repo import Repository


async def create_widget(
        repo: Repository,
        user_id: int,
        name: str,
        timezone_offset: int,
        latitude: float,
        longitude: float,
        city_name: str | None,
        settings: dict,
        is_default: bool,
) -> None:
    """
    Добавление виджета
    :param repo: Репозитория
    :param user_id:
    :param name:
    :param timezone_offset:
    :param latitude:
    :param longitude:
    :param city_name:
    :param settings:
    :param is_default:
    :return:
    """
    await repo.create_widget(
        user_id=user_id,
        name=name,
        timezone_offset=timezone_offset,
        latitude=latitude,
        longitude=longitude,
        city_name=city_name,
        settings=settings,
        is_default=is_default,
    )


async def get_default_widget(
        repo: Repository,
        user_id: int,
) -> WeatherWidget:
    """
    Получение виджета по умолчанию
    :param repo:
    :param user_id:
    :return:
    """

    widget_data = await repo.get_default_widget(
        user_id=user_id
    )
    return widget_data
