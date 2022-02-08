from aiogram import types, Router
from aiogram.dispatcher.fsm.context import FSMContext

from open_weather_map import OpenWeatherMapClient
from services.repo import Repository
from ..keyboards import buttons, keyboards
from magic_filter import F

from ..states import AddWidget


async def start_add_widget(message: types.Message, state: FSMContext) -> None:
    """
    Начало процесса добавления виджета
    :param message:
    :param state:
    :return:
    """
    await state.set_state(AddWidget.location)
    await message.answer(
        text='Отправьте геопозицию для определения погоды',
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
    await message.answer(
        text='Создание виджета',
        reply_markup=keyboards.get_main_menu(),
    )
    location = message.location

    weather_data = await weather_client.one_call(location.latitude, location.longitude)

    await state.clear()
    await message.answer(
        text=f'{weather_data.current.temp}'
    )


def register_handlers(router: Router) -> None:
    """
    Регистрация обработчиков
    :param router: Роутер
    :return:
    """

    router.message.register(start_add_widget, F.text == buttons.ADD_WIDGET.text)
    router.message.register(create_widget, AddWidget.location, F.content_type == 'location')
