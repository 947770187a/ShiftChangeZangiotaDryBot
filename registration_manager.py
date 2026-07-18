import uuid
from aiogram.types import Message

class RegistrationManager:

    def __init__(self, sheets, bot):

        self.sheets = sheets
        self.bot = bot

    async def start_registration(
        self,
        telegram_id
    ):

        await self.bot.send_message(
            chat_id=telegram_id,
            text=(
                "👋 Добро пожаловать!\n\n"
                "Вы еще не зарегистрированы.\n\n"
                "Введите ваши Фамилию Имя Отчество."
            )
        )

        async def process_registration(
        self,
        telegram_id,
        full_name
    ):

        user_id = str(uuid.uuid4())

        self.sheets.add_user(
            user_id=user_id,
            full_name=full_name,
            telegram_id=telegram_id
        )

        await self.bot.send_message(
            chat_id=telegram_id,
            text=(
                "✅ Регистрация успешно завершена.\n\n"
                "Теперь вы можете пользоваться ботом."
            )
        )
