# Global configs
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL =\
    f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'

JWT_SECRET = os.getenv("JWT_SECRET")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
