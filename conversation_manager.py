from state_manager import StateManager


class ConversationManager:

    def __init__(self, sheets):

        self.sheets = sheets
        self.state_manager = StateManager(sheets)

    async def process_message(
        self,
        session,
        user,
        message
    ):

        await self.state_manager.process_message(
            session=session,
            user=user,
            message=message
        )
