import json

from app.data import list_files, open_files


def add_employee(name: str, pos: str, salary: str) -> str:
    employees = open_files.get_employees()

    employees[name] = {
        "Посада": pos,
        "Зарплата": salary
    }

    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as fh:
        json.dump(employees, fh)

    msg = f"Працівник {name} успішно доданий."
    return msg


def remove_employee(name: str) -> str:
    employees = open_files.get_employees()
    employees.pop(name)

    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as fh:
        json.dump(employees, fh)

    msg = f"Працівника {name} успішно видалено."
    return msg


def edit_pos(name: str, pos) -> str:
    employees = open_files.get_employees()
    employees[name]["Посада"] = pos

    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as fh:
        json.dump(employees, fh)

    msg = f"Посада працівника {name} успішно змінена на {pos}."
    return msg


def edit_salary(name: str, salary) -> str:
    employees = open_files.get_employees()
    employees[name]["Зарплата"] = salary

    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as fh:
        json.dump(employees, fh)

    msg = f"Зарплата працівника {name} успішно змінена."
    return msg