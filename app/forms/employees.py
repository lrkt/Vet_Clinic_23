from aiogram.fsm.state import State, StatesGroup


class EmployeeNewForm(StatesGroup):
    name = State()
    pos = State()
    salary = State()

class EmployeeEditForm(StatesGroup):
    pos = State()
    salary = State()