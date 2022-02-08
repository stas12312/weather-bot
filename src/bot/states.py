from aiogram.dispatcher.fsm.state import StatesGroup, State


class AddWidget(StatesGroup):
    location = State()
    lat: float
    long: float
