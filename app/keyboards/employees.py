from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_employees_keyboard(employees_name: list):
    builder = InlineKeyboardBuilder()

    for employee in employees_name:
        builder.button(text=employee, callback_data=f"employee_{employee}")

    builder.adjust(3)
    return builder.as_markup()


def build_employee_actions_keyboard(employee: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Видалити працівника", callback_data=f"remove_employee_{employee}")
    builder.button(text="Змінити посаду", callback_data=f"edit_pos_{employee}")
    builder.button(text="Змінити зарплату", callback_data=f"edit_salary_{employee}")
    builder.adjust(1)
    return builder.as_markup()