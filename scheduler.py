import asyncio
from datetime import datetime


class Scheduler:

    def __init__(self, sheets):

        self.sheets = sheets

    async def start(self):

        print("Scheduler started")

        while True:

            try:

                await self.check_schedule()

            except Exception as e:

                print(f"[Scheduler] ERROR: {e}")

            await asyncio.sleep(60)
    async def check_schedule(self):

        from datetime import datetime

        schedules = self.sheets.get_schedule()

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

            print()
            print("======================================")
            print("READY TO START SESSION")
            print(f"ScheduleID : {schedule['ScheduleID']}")
            print(f"Sender     : {schedule['SenderUserID']}")
            print(f"StartTime  : {schedule['StartDateTime']}")
            print("======================================")
            print()

            self.sheets.update_schedule_executed(
                schedule["ScheduleID"]
            )
 
