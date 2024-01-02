from aiogram import types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot import router


def get_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


@router.message(CommandStart())
async def on_start_command(message: types.Message):
    await message.answer('Команда /start обработана',
                         reply_markup=get_keyboard())
