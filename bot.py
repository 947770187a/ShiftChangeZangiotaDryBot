from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

conversation_manager = None


def set_conversation_manager(manager):

    global conversation_manager

    conversation_manager = manager


@dp.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "✅ Shift Change Bot запущен.\n\n"
        "Добро пожаловать!"
    )


@dp.message(F.text)
async def any_message(message: Message):

    if conversation_manager is None:
        return

    await conversation_manager.process_telegram_message(
        telegram_id=message.from_user.id,
        text=message.text
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
