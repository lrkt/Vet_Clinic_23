import json

from app.data import list_files, open_files


def remove_animal(animal_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(animal_index)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as fh:
        json.dump(animals, fh)

    msg = f"Тваринку {animal} успішно видалено."
    return msg


def add_cured(animal_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(animal_index)

    animals_cured = open_files.get_animals_cured()
    animals_cured.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as fh:
        json.dump(animals, fh)

    with open(list_files.ANIMALS_CURED, "w", encoding="utf-8") as fh:
        json.dump(animals_cured, fh)

    msg = f"Тваринку {animal} перенесено до списку вилікуваних."
    return msg 


def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        msg = f"Тваринка {animal} вже є у списку."
        return msg

    animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as fh:
        json.dump(animals, fh)

    msg = f"Тваринка {animal} успішно додана до списку."
    return msg 