import os
import json

from app.data import list_files


if not os.path.exists(list_files.ANIMALS):
    with open(list_files.ANIMALS, "w", encoding="utf-8") as fh:
        json.dump([], fh)

if not os.path.exists(list_files.ANIMALS_CURED):
    with open(list_files.ANIMALS_CURED, "w", encoding="utf-8") as fh:
        json.dump([], fh)


if not os.path.exists(list_files.REVIEWS):
    with open(list_files.REVIEWS, "w", encoding="utf-8") as fh:
        json.dump([], fh)


if not os.path.exists(list_files.EMPLOYEES):
    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as fh:
        json.dump({}, fh)


def get_animals(path: str = list_files.ANIMALS) -> list[str]:
    with open(path, "r", encoding="utf-8") as fh:
        animals = json.load(fh)
    
    return animals


def get_animal(animal_index: int) -> str:
    animals = get_animals()
    return animals[animal_index]


def get_animals_cured(path: str = list_files.ANIMALS_CURED) -> list[str]:
    with open(path, "r", encoding="utf-8") as fh:
        animals_cured = json.load(fh)

    return animals_cured


def get_reviews(path: str = list_files.REVIEWS) -> list[str]:
    with open(path, "r", encoding="utf-8") as fh:
        reviews = json.load(fh)

    return reviews


def get_employees(path: str = list_files.EMPLOYEES) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        employees = json.load(fh)

    return employees


def get_employee(employee_name: str) -> str:
    employees = get_employees()
    return employees[employee_name]