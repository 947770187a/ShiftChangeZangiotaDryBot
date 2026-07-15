import os
import json
import tempfile

import gspread
from google.oauth2.service_account import Credentials

from config import (
    GOOGLE_CREDENTIALS_FILE,
    GOOGLE_SHEET_NAME,
    SHEET_USERS,
    SHEET_QUESTIONS,
    SHEET_SCHEDULE,
    SHEET_SESSIONS,
    SHEET_ANSWERS,
    SHEET_SETTINGS,
    SHEET_TEMPLATES,
    SHEET_LOG
)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


class GoogleSheets:

    def __init__(self):

        if os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"):

            data = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
            creds = Credentials.from_service_account_info(
             data,
             scopes=SCOPES
            )

        else:

            creds = Credentials.from_service_account_file(
                GOOGLE_CREDENTIALS_FILE,
                scopes=SCOPES
            )

        self.client = gspread.authorize(creds)
        self.book = self.client.open(GOOGLE_SHEET_NAME)

        self.users = self.book.worksheet(SHEET_USERS)
        self.questions = self.book.worksheet(SHEET_QUESTIONS)
        self.schedule = self.book.worksheet(SHEET_SCHEDULE)
        self.sessions = self.book.worksheet(SHEET_SESSIONS)
        self.answers = self.book.worksheet(SHEET_ANSWERS)
        self.settings = self.book.worksheet(SHEET_SETTINGS)
        self.templates = self.book.worksheet(SHEET_TEMPLATES)
        self.log = self.book.worksheet(SHEET_LOG)

    def test_connection(self):

        print("=" * 50)
        print("GOOGLE SHEETS CONNECTED")
        print("=" * 50)

        print(f"Users: {self.users.row_count}")
        print(f"Questions: {self.questions.row_count}")
        print(f"Schedule: {self.schedule.row_count}")

        print("=" * 50)

    def get_users(self):
        return self.users.get_all_records()

    def get_questions(self):
        return self.questions.get_all_records()

    def get_schedule(self):
        return self.schedule.get_all_records()
