from aiogram import types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot import TemplateBot
from config import config


def get_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


@TemplateBot.router.message(CommandStart())
async def on_start_command(message: types.Message):
    await message.answer('Спасибо, что пользуетесь нашим ботом!\n'
                         f'Ваш ID в системе - <code>{message.from_user.id}</code>\n\n'
                         f'Обратная связь {config["bot"]["support"]}',
                         reply_markup=get_keyboard())
