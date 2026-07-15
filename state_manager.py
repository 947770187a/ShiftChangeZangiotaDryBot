class StateManager:

    def __init__(self, sheets):

        self.sheets = sheets

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

        print("Sender answer")

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
