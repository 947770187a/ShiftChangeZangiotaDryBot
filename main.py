import asyncio

from sheets import GoogleSheets
from bot import run_bot


async def main():

    print()
    print("========================================")
    print("Shift Change Bot")
    print("========================================")
    print()

    sheets = GoogleSheets()

    sheets.test_connection()

    users = sheets.get_users()

    print(f"Загружено пользователей: {len(users)}")

    print()

    for user in users:

        print(
            f"ID={user['UserID']} | "
            f"{user['FullName']} | "
            f"Active={user['Active']}"
        )

    print()
    print("Telegram запускается...")
    print()

    await run_bot()


if __name__ == "__main__":
    asyncio.run(main())
