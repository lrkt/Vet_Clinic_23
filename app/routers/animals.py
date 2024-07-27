from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import open_files
from app.keyboards.animals import build_animals_keyboard, build_animal_actions_keyboard

animal_router = Router()



async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@animal_router.message(F.text == "Список тварин")
async def show_animals(message: Message, state: FSMContext):
    animals = open_files.get_animals()
    keyboard = build_animals_keyboard(animals)
    await edit_or_answer(
        message=message, 
        text="Список тварин", 
        keyboard=keyboard
    )


@animal_router.callback_query(F.data.startswith("product_"))
async def animal_actions(call_back: CallbackQuery, state: FSMContext):
    animal_index = int(call_back.data.split("_")[-1])
    animal = open_files.get_animal(animal_index)
    keyboard = build_animal_actions_keyboard(animal_index)
    await edit_or_answer(
        message=call_back.message, 
        text=animal, 
        keyboard=keyboard
    )