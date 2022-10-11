# Module specific business logic
from fastapi import Depends
from sqlalchemy.orm import Session
import requests

from app.forum.models import Section, Theme, Message
from app.forum.schemas import SectionCreate, ThemeCreate, MessageCreate, MessageUpdate
from app.database import get_session
from app.profile.models import UserAdditionalInfo
from app import config


class ForumService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    # --------- Sections --------- #
    def get_section_list(
            self,
            section_id: int | None = None,
    ):
        if section_id:
            return self.session.query(Section).get(section_id)
        return self.session.query(Section).all()

    def create_section_service(self, item: SectionCreate):
        section = Section(**item.dict())
        self.session.add(section)
        self.session.commit()
        return section

    # --------- Themes --------- #
    def get_theme_list(
            self,
            theme_id: int | None = None,
            section_id: int | None = None,
    ):
        if theme_id:
            return self.session.query(Theme).get(theme_id)
        elif section_id:
            return self.session.query(Theme).filter_by(section_id=section_id).all()
        return self.session.query(Theme).all()

    def create_theme_service(
            self,
            item: ThemeCreate,
            user_id: int,
            section_id: int,
    ):
        theme = Theme(
            **item.dict(),
            user_id=user_id,
            section_id=section_id
        )
        self.session.add(theme)
        self.session.commit()
        return theme

    # --------- Messages --------- #
    def get_message(self, message_id: int) -> Message:
        return self.session.query(Message).get(message_id)

    def get_message_list(
            self,
            theme_id: int | None = None
    ):
        if theme_id:
            return self.session.query(Message).filter_by(theme_id=theme_id).all()
        return self.session.query(Message).all()

    def create_message_service(
            self,
            user_id: int,
            item: MessageCreate,
            theme_id: int,
    ) -> Message:
        if item.reply_to:
            user_additional = self.session.query(UserAdditionalInfo).filter_by(user_id=item.reply_to)
            if user_additional.telegram_id:
                chat_id = user_additional.telegram_id
                response = requests.post(
                    url=f"api.telegram.org/"
                        f"bot{config.TELEGRAM_API_KEY}/"
                        f"sendMessage?chat_id={chat_id}&text={item.content}"
                )
                print(response)
        message = Message(**item.dict(), user_id=user_id, theme_id=theme_id)
        self.session.add(message)
        self.session.commit()
        return message

    def delete_message_service(self, message_id: int):
        message = self.get_message(message_id)
        self.session.delete(message)
        self.session.commit()

    def update_message_service(self, message_id: int, message_info: MessageUpdate) -> Message:
        message = self.get_message(message_id=message_id)
        for field, value in message_info:
            setattr(message, field, value)
        self.session.commit()
        return message
