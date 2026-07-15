import asyncio

from session_manager import SessionManager
from datetime import datetime


class Scheduler:

    def __init__(self, sheets):

        self.sheets = sheets
        self.session_manager = SessionManager(sheets)

    async def start(self):

        print("Scheduler started V2")

        while True:

            try:

                await self.check_schedule()

            except Exception as e:

                print(f"[Scheduler] ERROR: {e}")

            await asyncio.sleep(5)
            
    async def check_schedule(self):

        print("check_schedule() called")

        schedules = self.sheets.get_schedule()

        print(schedules)

        for schedule in schedules:

            if schedule["Active"] != "TRUE":
                continue

            if schedule["Executed"] == "TRUE":
                continue

            start_time = datetime.strptime(
                schedule["StartDateTime"],
                "%d.%m.%Y %H:%M"
            )

            if start_time > datetime.now():
                continue

            session = self.session_manager.create_session(schedule)

            self.sheets.update_schedule_executed(
                schedule["ScheduleID"]
            )
