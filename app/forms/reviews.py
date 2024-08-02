from aiogram.fsm.state import State, StatesGroup


class ReviewForm(StatesGroup):
    text = State()