from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import open_files, action_employees
from app.keyboards.employees import build_employees_keyboard, build_employee_actions_keyboard
from app.forms.employees import EmployeeNewForm, EmployeeEditForm


employee_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@employee_router.message(F.text == "Список працівників")
async def show_employees(message: Message, state: FSMContext):
    employees = open_files.get_employees()
    employees_name = employees.keys()
    keyboard = build_employees_keyboard(employees_name)
    await edit_or_answer(
        message=message,
        text="Список працівників:",
        keyboard=keyboard
    )


@employee_router.callback_query(F.data.startswith("employee_"))
async def employee_actions(call_back: CallbackQuery, state: FSMContext):
    employee_name = call_back.data.split("_")[-1]
    employee = open_files.get_employee(employee_name)
    keyboard = build_employee_actions_keyboard(employee_name)
    msg = f"{employee_name}:\n\nПосада: {employee["Посада"]};\nЗарплата: {employee["Зарплата"]}."
    await edit_or_answer(
        message=call_back.message, 
        text=msg, 
        keyboard=keyboard
    )


@employee_router.callback_query(F.data.startswith("remove_employee_"))
async def remove_employee(call_back: CallbackQuery, state: FSMContext):
    employee_name = call_back.data.split("_")[-1]
    msg = action_employees.remove_employee(employee_name)
    await edit_or_answer(message=call_back.message,text=msg)


@employee_router.callback_query(F.data.startswith("edit_salary_"))
async def edit_salary(call_back: CallbackQuery, state: FSMContext):
    employee_name = call_back.data.split("_")[-1]
    await state.clear()
    await state.update_data(employee_name=employee_name)
    await state.set_state(EmployeeEditForm.salary)
    await edit_or_answer(
        message=call_back.message,
        text="Введіть нову зарплату..."
        )


@employee_router.message(EmployeeEditForm.salary)
async def edit_salary_salary(message: Message, state: FSMContext):
    salary = message.text
    data = await state.get_data()
    employee_name = data.get("employee_name")
    msg = action_employees.edit_salary(employee_name, salary)
    await edit_or_answer(message=message, text=msg)


@employee_router.callback_query(F.data.startswith("edit_pos_"))
async def edit_pos(call_back: CallbackQuery, state: FSMContext):
    employee_name = call_back.data.split("_")[-1]
    await state.clear()
    await state.update_data(employee_name=employee_name)
    await state.set_state(EmployeeEditForm.pos)
    await edit_or_answer(
        message=call_back.message,
        text="Введіть нову посаду..."
        )


@employee_router.message(EmployeeEditForm.pos)
async def edit_pos_pos(message: Message, state: FSMContext):
    pos = message.text
    data = await state.get_data()
    employee_name = data.get("employee_name")
    msg = action_employees.edit_pos(employee_name, pos)
    await edit_or_answer(message=message, text=msg)


@employee_router.message(F.text == "Додати нового працівника")
async def add_employee(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(EmployeeNewForm.name)
    await edit_or_answer(
        message=message,
        text="Введіть ім'я нового працівника..."
    )


@employee_router.message(EmployeeNewForm.name)
async def add_employee_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(EmployeeNewForm.pos)
    await edit_or_answer(
        message=message,
        text="Введіть посаду нового працівника..."
    )


@employee_router.message(EmployeeNewForm.pos)
async def add_employee_pos(message: Message, state: FSMContext):
    await state.update_data(pos=message.text)
    await state.set_state(EmployeeNewForm.salary)
    await edit_or_answer(
        message=message,
        text="Введіть зарплату нового працівника..."
    )


@employee_router.message(EmployeeNewForm.salary)
async def add_employee_salary(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    pos = data.get("pos")
    salary = message.text
    await state.update_data(salary=salary)
    await state.clear()
    msg = action_employees.add_employee(name, pos, salary)
    await edit_or_answer(
        message=message,
        text = msg
    )

