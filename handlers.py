from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from loader import dp


@dp.message(CommandStart())
async def cmd_start_handler(msg: types.Message) -> None:
    await msg.answer(f"Привет, {hbold(msg.from_user.full_name)}!")


@dp.message()
async def echo_handler(msg: types.Message) -> None:
    try:
        await msg.send_copy(chat_id=msg.chat.id)
    except TypeError:
        await msg.answer("Не понял")
