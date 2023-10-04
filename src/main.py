import asyncio
import logging

import loader
from bot import TemplateBot


async def main():
    logging.basicConfig(level=logging.DEBUG)

    bot = TemplateBot()
    loader.load_dynamics('dynamic')

    await bot.start()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
