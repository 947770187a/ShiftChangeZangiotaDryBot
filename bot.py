from aiogram import Bot, Dispatcher
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


async def send_text(chat_id: int, text: str):

    await bot.send_message(
        chat_id=chat_id,
        text=text
    )


async def run_bot():

    print()
    print("===============================")
    print("Telegram Bot Started")
    print("===============================")
    print()

    await dp.start_polling(bot)
