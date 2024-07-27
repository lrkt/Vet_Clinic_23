import os
import json

from app.data import list_files


if not os.path.exists(list_files.ANIMALS):
    with open(list_files.ANIMALS, "w", encoding="utf-8") as fh:
        json.dump([], fh)


def get_animals(path: str = list_files.ANIMALS) -> list[str]:
    with open(path, "r", encoding="utf-8") as fh:
        animals = json.load(fh)
    
    return animals


def get_animal(animal_index: int) -> str:
    animals = get_animals()
    return animals[animal_index]