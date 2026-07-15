import uuid
from datetime import datetime


class SessionManager:

    def __init__(self, sheets):

        self.sheets = sheets

    def create_session(self, schedule):

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

        print()
        print("=" * 50)
        print("SESSION CREATED")
        print(session)
        print("=" * 50)
        print()

        return session
