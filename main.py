from sheets import GoogleSheets


def main():
    print()
    print("========================================")
    print("   Shift Change Bot v0.1")
    print("========================================")
    print()

    try:
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
        print("✓ Проверка завершена успешно")

    except Exception as e:

        print()
        print("========================================")
        print("ОШИБКА")
        print("========================================")
        print(e)
        print("========================================")


if __name__ == "__main__":
    main()
