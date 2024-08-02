from os import getenv
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.log.log import get_log
from app.routers.start import start_router
from app.routers.animals import animal_router
from app.routers.reviews import review_router
from app.routers.employees import employee_router

# Завантажимо дані середовища з файлу .env(За замовчуванням)
load_dotenv()


# Усі обробники варто закріплювати за Router або Dispatcher
root_router = Router()
root_router .include_routers(start_router, animal_router, review_router, employee_router) 


# Головна функція пакету
async def main() -> None:
    # Дістанемо токен бота з середовища
    TOKEN = getenv("VET_API")
    # Створимо об'єкт Bot
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(root_router)
    # Почнемо обробляти події для бота
    await dp.start_polling(bot)


# Точка входу
if __name__ == "__main__":
    asyncio.run(main())