from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "✅ Shift Change Bot запущен.\n\n"
        "Добро пожаловать!"
    )


async def run_bot():

    print()
    print("===============================")
    print("Telegram Bot Started")
    print("===============================")
    print()

    await dp.start_polling(bot)
