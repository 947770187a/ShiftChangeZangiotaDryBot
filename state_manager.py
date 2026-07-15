import uuid
from datetime import datetime


class StateManager:

    def __init__(self, sheets, bot):

        self.sheets = sheets
        self.bot = bot

    async def process_message(
        self,
        session,
        user,
        message
    ):

        status = session["Status"]

        if status == "WAITING_SENDER_ANSWER":

            await self.process_sender_answer(
                session,
                user,
                message
            )

            return

        if status == "WAITING_RECEIVER_CONFIRM":

            await self.process_receiver_confirm(
                session,
                user,
                message
            )

            return

        if status == "WAITING_RECEIVER_ANSWER":

            await self.process_receiver_answer(
                session,
                user,
                message
            )

            return

        print(f"Unknown status: {status}")

    async def process_sender_answer(
        self,
        session,
        user,
        message
    ):

        questions = self.sheets.get_sender_questions()

        current_order = int(session["CurrentQuestionOrder"])

        current_question = None

        for question in questions:

            if int(question["QuestionOrder"]) == current_order:
                current_question = question
                break

        if current_question is None:

            print("Current question not found")
            return

        answer = {
            "AnswerID": str(uuid.uuid4()),
            "SessionID": session["SessionID"],
            "UserID": user["UserID"],
            "Role": "Sender",
            "QuestionID": current_question["QuestionID"],
            "Answer": message,
            "AnswerDateTime": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        }

        self.sheets.save_answer(answer)

        next_order = current_order + 1

        next_question = None

        for question in questions:

            if int(question["QuestionOrder"]) == next_order:
                next_question = question
                break

        if next_question is not None:

            self.sheets.update_session_question_order(
                session["SessionID"],
                next_order
            )

            await self.bot.send_message(
                chat_id=int(user["TelegramID"]),
                text=next_question["Question"]
            )

            return

        self.sheets.update_session_status(
            session["SessionID"],
            "WAITING_RECEIVER_CONFIRM"
        )

        print("Sender questionnaire completed.")

    async def process_receiver_confirm(
        self,
        session,
        user,
        message
    ):

        print("Receiver confirm")

    async def process_receiver_answer(
        self,
        session,
        user,
        message
    ):

        print("Receiver answer")
