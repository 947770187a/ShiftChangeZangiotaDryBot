import asyncio

from sheets import GoogleSheets
from scheduler import Scheduler
from bot import run_bot


async def main():

    print("=" * 40)
    print("Shift Change Bot")
    print("=" * 40)

    sheets = GoogleSheets()
    sheets.test_connection()

    scheduler = Scheduler(sheets)
    asyncio.create_task(scheduler.start())

    await run_bot()


if __name__ == "__main__":
    asyncio.run(main())
