from aiogram import types, Router
from aiogram.dispatcher.fsm.context import FSMContext
from magic_filter import F

from open_weather_map import OpenWeatherMapClient
from services import weather
from services.repo import Repository
from services.weather_widget import WeatherWidget
from ..keyboards import buttons, keyboards
from ..states import AddWidget


async def start_add_widget(message: types.Message, state: FSMContext) -> None:
    """
    Начало процесса добавления виджета
    :param message:
    :param state:
    :return:
    """
    await message.answer(
        text='Укажите местоположение',
        reply_markup=keyboards.send_geo_keyboard(),
    )
    await state.set_state(AddWidget.location)


async def set_widget_name(
        message: types.Message,
        state: FSMContext,
) -> None:
    """
    Сохранение названия виджета
    :param message: Сообщение
    :param state: FSM
    :return:
    """
    name = message.text
    await state.update_data(name=name)
    await state.set_state(AddWidget.location)
    await message.answer(
        text='Отправьте местоположение для определения погоды',
        reply_markup=keyboards.send_geo_keyboard(),
    )


async def create_widget(
        message: types.Message,
        repo: Repository,
        state: FSMContext,
        weather_client: OpenWeatherMapClient,
) -> None:
    """
    Создание виджета
    :param message:
    :param repo:
    :param state:
    :param weather_client:
    :return:
    """
    location = message.location
    weather_data = await weather_client.one_call(location.latitude, location.longitude)

    # Создаём виджет
    await weather.create_widget(
        repo=repo,
        user_id=message.from_user.id,
        name='',
        timezone_offset=weather_data.timezone_offset,
        latitude=location.latitude,
        longitude=location.longitude,
        city_name=None,
        settings={},
        is_default=True,
    )

    widget = WeatherWidget(weather_data, {})

    await message.answer(
        text=widget.as_text(),
        reply_markup=keyboards.get_main_menu(True)
    )
    await state.clear()


async def show_default_widget(
        message: types.Message,
        weather_client: OpenWeatherMapClient,
        repo: Repository,
) -> None:
    """
    Получение виджета по умолчанию
    :param message: Сообщений
    :param weather_client: Клиент для получения погоды
    :param repo: Репозиторий
    :return:
    """
    widget_data = await weather.get_default_widget(
        repo=repo,
        user_id=message.from_user.id,
    )

    weather_data = await weather_client.one_call(widget_data.latitude, widget_data.longitude)
    widget = WeatherWidget(weather_data, {})
    await message.answer(
        text=widget.as_text(),
    )


def register_handlers(router: Router) -> None:
    """
    Регистрация обработчиков
    :param router: Роутер
    :return:
    """

    router.message.register(start_add_widget, F.text == buttons.SETTING_WEATHER.text)
    router.message.register(show_default_widget, F.text == buttons.WEATHER.text)
    router.message.register(create_widget, AddWidget.location, F.content_type == 'location')
