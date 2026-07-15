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

        print(f"[Scheduler] {datetime.now():%Y-%m-%d %H:%M:%S}")

        # Пока только проверяем, что Scheduler живой.
        # Логику запуска Session добавим следующим шагом.
