from aiogram import Dispatcher, Bot, Router
from aiogram.enums import ParseMode

from config import config

router = Router()

main_bot = Bot(config['bot']['token'], parse_mode=ParseMode.HTML)

dispatcher = Dispatcher()
dispatcher.include_router(router)


async def start():
    await dispatcher.start_polling(main_bot)
