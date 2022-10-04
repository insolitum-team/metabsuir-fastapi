# Global configs
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL =\
    f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'

print(DATABASE_URL)