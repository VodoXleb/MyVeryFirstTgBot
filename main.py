import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.enums import ParseMode

from handlers import cmd_start_handler, echo_handler
from loader import dp
from loader import TOKEN


async def main() -> None:
    dp.message.register(cmd_start_handler)
    dp.message.register(echo_handler)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

