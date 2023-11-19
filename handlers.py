from aiogram.filters import CommandStart, Command
from aiogram import types, Bot, F
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from loader import dp
from random import *
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.message(CommandStart())
async def cmd_start_handler(msg: types.Message) -> None:
    await msg.answer(f"Привет, {msg.from_user.first_name}.")
    kb = [
        [types.KeyboardButton(text="Дядя"),
         types.KeyboardButton(text="Тётя")],
        [types.KeyboardButton(text="Убери клавиатуру")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="А?")
    await msg.answer("Выберите пользователя", reply_markup=keyboard)


@dp.message(Command("password"))
async def reply_build(msg: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(3)
    await msg.answer("Введите пароль:", reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message(Command("inline_url"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
        )
    builder.row(types.InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
        )
    user_id = 5309569878
    chat_info = await bot.get_chat(user_id)
    if chat_info.has_private_forwards:
        builder.row(types.InlineKeyboardButton(
                text="Ivan Andreevich",
                url=f"tg://user?id={user_id}")
            )
    await message.answer(
        'Выберите ссылку', reply_markup=builder.as_markup(),
    )


@dp.message(Command("inline_password"))
async def reply_build(msg: types.Message):
    builder = InlineKeyboardBuilder()
    for i in range(1, 10):
        builder.button(text=str(i), callback_data=f"set:{i}")
    builder.adjust(3)
    await msg.answer("Введите пароль:", reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message(Command("random_generator"))
async def reply_build(msg: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Нажми меня", callback_data="random_number")
    builder.adjust(3)
    await msg.answer("Кнопка отправки случайного числа:", reply_markup=builder.as_markup(resize_keyboard=True))


@dp.callback_query(F.data == "random_number")
async def random_number(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))


@dp.message()
async def echo_handler(msg: types.Message) -> None:
    try:
        if msg.text == "Убери клавиатуру":
            await msg.reply("Понял, убираю", reply_markup=types.ReplyKeyboardRemove())
        else:
                await msg.reply(f"{msg.text}, отлично")
    except TypeError:
        await msg.answer("Не понял")


