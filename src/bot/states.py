from aiogram.dispatcher.fsm.state import StatesGroup, State


class AddWidget(StatesGroup):
    location = State()
    name = State()
    lat: float
    long: float
