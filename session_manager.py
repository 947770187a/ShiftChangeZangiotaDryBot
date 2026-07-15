import uuid
from datetime import datetime

from bot import send_text


class SessionManager:

    def __init__(self, sheets):

        self.sheets = sheets

    async def create_session(self, schedule):

        session = {
            "SessionID": str(uuid.uuid4()),
            "ScheduleID": schedule["ScheduleID"],
            "StartDateTime": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "SenderUserID": schedule["SenderUserID"],
            "ReceiverUserID": "",
            "Status": "CREATED",
            "AcceptDateTime": "",
            "FinishDateTime": ""
        }

        self.sheets.save_session(session)

        user = self.sheets.get_user_by_id(
            schedule["SenderUserID"]
        )

        if user is None:

            print("Sender not found")

            return

        telegram_id = user["TelegramID"]

        await send_text(
            int(telegram_id),
            "🚚 Начинаем передачу смены.\n\nПодготовьтесь к ответам на вопросы."
        )

        print()
        print("=" * 50)
        print("SESSION CREATED")
        print(session)
        print("=" * 50)
        print()

        return session
