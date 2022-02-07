from aiogram import types, Router
from magic_filter import F
from services.repo import Repository
from services import user as user_service
from ..keyboards.keyboards import get_main_menu


async def start_bot(message: types.Message, repo: Repository) -> None:
    """
    Обработка команды старт
    :param message: Сообщение
    :param repo: Репозиторий
    :return:
    """
    tg_user = message.from_user
    user = await user_service.create_user(
        repo,
        tg_user.id,
        tg_user.first_name,
        tg_user.last_name,
        tg_user.username,
    )
    await message.answer(
        text=f'👋 Привет {user.first_name}\n'
             f'❕ Для начала работы необходимо создать погодный виджет',
        reply_markup=get_main_menu()
    )


def register_handlers(router: Router) -> None:
    router.message.register(start_bot, F.text == '/start')
