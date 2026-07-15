from state_manager import StateManager


class ConversationManager:

    def __init__(self, sheets, bot):

        self.sheets = sheets
        self.bot = bot
        self.state_manager = StateManager(sheets, bot)

    async def process_telegram_message(
        print(">>> process_telegram_message")
        self,
        telegram_id,
        text
    ):

        user = self.find_user_by_telegram(telegram_id)

        if user is None:
            return

        session = self.sheets.get_active_session_by_sender(
            user["UserID"]
        )

        if session is None:

            session = self.sheets.get_session_by_receiver(
                user["UserID"]
            )

        if session is None:
            return

        await self.state_manager.process_message(
            session=session,
            user=user,
            message=text
        )

    async def process_callback(
        self,
        telegram_id,
        data
    ):

        user = self.find_user_by_telegram(telegram_id)

        if user is None:
            return

        session = self.sheets.get_active_session_by_sender(
            user["UserID"]
        )

        if session is None:

            session = self.sheets.get_session_by_receiver(
                user["UserID"]
            )

        if session is None:
            return

        await self.state_manager.process_callback(
            session=session,
            user=user,
            data=data
        )

    def find_user_by_telegram(self, telegram_id):

        users = self.sheets.get_users()

        for user in users:

            if str(user["TelegramID"]) == str(telegram_id):
                return user

        return None
