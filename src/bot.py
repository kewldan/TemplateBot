import aaio
from aiogram import Dispatcher, Bot, Router
from aiogram.enums import ParseMode

import config
from middlewares.user_fetch import UserFetchMiddleware


class TemplateBot(Bot):
    router = Router()
    client: aaio.AAIO
    instance: Bot

    def __init__(self):
        super().__init__(config.config['bot']['token'], parse_mode=ParseMode.HTML)
        self.dp = None

        TemplateBot.router.message.middleware(UserFetchMiddleware())
        TemplateBot.router.callback_query.middleware(UserFetchMiddleware())
        TemplateBot.instance = self

    async def start(self):
        self.dp = Dispatcher()
        self.dp.include_router(TemplateBot.router)

        TemplateBot.client = aaio.AAIO(config.config['aaio']['merchant_id'], config.config['aaio']['secret'],
                                       config.config['aaio']['api_key'])
        await self.dp.start_polling(self)
