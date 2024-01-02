import asyncio
import logging

import bot
import loader


async def main():
    logging.basicConfig(level=logging.DEBUG)

    loader.load_dynamics('dynamic')

    await bot.start()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
