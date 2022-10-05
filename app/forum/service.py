# Module specific business logic
from fastapi import Depends
from sqlalchemy.orm import Session

from app.forum.models import Section, Theme, Message
from app.forum.schemas import SectionCreate, ThemeCreate, MessageCreate
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
    def get_message_list(self):
        return self.session.query(Message).all()

    def create_message_service(self, item: MessageCreate, user_id: int):
        message = Message(**item.dict(), user_id=user_id)
        self.session.add(message)
        self.session.commit()
        return message
