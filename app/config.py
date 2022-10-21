import os
from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig
from pathlib import Path

load_dotenv()

DATABASE_URL =\
    f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'

JWT_SECRET = os.getenv("JWT_SECRET")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
DOMAIN = os.getenv("DOMAIN")

EMAIL_CONFIG = ConnectionConfig(
    MAIL_USERNAME=os.getenv("SENDER"),
    MAIL_PASSWORD=os.getenv("EMAIL_PASSWORD"),
    MAIL_FROM=os.getenv("SENDER"),
    MAIL_PORT=587,
    MAIL_SERVER="mail.insolitum.team",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
)
