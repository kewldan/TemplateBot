import asyncio
import logging
import os.path

import loader
from bot import TemplateBot


async def main():
    logging.basicConfig(level=logging.DEBUG)

    if not os.path.exists('data'):
        os.mkdir('data')

    bot = TemplateBot()
    loader.load_dynamics('dynamic')

    await bot.start()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
