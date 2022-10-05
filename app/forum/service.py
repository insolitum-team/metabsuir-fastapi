# Module specific business logic
from fastapi import Depends
from sqlalchemy.orm import Session

from app.forum.models import Section, Theme, Message
from app.forum.schemas import SectionCreate, ThemeCreate, MessageCreate, MessageUpdate
from app.database import get_session


class ForumService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    # --------- Sections --------- #
    def get_section_list(self):
        return self.session.query(Section).all()

    def create_section_service(self, item: SectionCreate):
        section = Section(**item.dict())
        self.session.add(section)
        self.session.commit()
        return section

    # --------- Themes --------- #
    def get_theme_list(self):
        return self.session.query(Theme).all()

    def create_theme_service(self, item: ThemeCreate, user_id: int):
        theme = Theme(**item.dict(), user_id=user_id)
        self.session.add(theme)
        self.session.commit()
        return theme

    # --------- Messages --------- #
    def get_message(self, message_id: int) -> Message:
        return self.session.query(Message).get(message_id)

    def get_message_list(self):
        return self.session.query(Message).all()

    def create_message_service(self, item: MessageCreate, user_id: int) -> Message:
        message = Message(**item.dict(), user_id=user_id)
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
