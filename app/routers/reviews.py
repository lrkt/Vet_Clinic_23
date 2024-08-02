from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.data import open_files, action_reviews
from app.forms.reviews import ReviewForm


review_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@review_router.message(F.text == "Показати відгуки")
async def show_reviews(message: Message, state: FSMContext):
    reviews = open_files.get_reviews()
    msg = ""
    for i, review in enumerate(reviews, start=1):
        msg += f"{i}. {review}\n"

    await message.answer(text = msg)


@review_router.message(F.text == "Написати відгук")
async def add_review(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ReviewForm.text)
    await edit_or_answer(
        message = message,
        text = "Введіть свій відгук"
    )


@review_router.message(ReviewForm.text)
async def add_review_name(message: Message, state: FSMContext):
    data = await state.update_data(text=message.text)
    await state.clear()
    msg = action_reviews.add_review(data.get("text"))
    await message.answer(text=msg)
