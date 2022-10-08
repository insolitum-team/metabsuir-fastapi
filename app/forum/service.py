# Module specific business logic
import os.path
import shutil

from fastapi import Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.forum import config
from app.forum.models import Section, Theme, Message
from app.forum.schemas import SectionCreate, ThemeCreate, MessageCreate, MessageUpdate
from app.database import get_session
from app.forum.constants import ImageType


class ForumService:

    @classmethod
    def _get_path(cls, filename: str, image_type: ImageType):
        if image_type == ImageType.THEME:
            return os.path.join(config.THEME_IMAGE_PATH, filename)
        return os.path.join(config.MESSAGE_IMAGE_PATH, filename)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _upload_image(self, image_type: ImageType, image: UploadFile = File(...),):
        path = self._get_path(filename=image.filename, image_type=image_type)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

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
            image: UploadFile = File(...),
    ):
        if image:
            image_type = ImageType.THEME
            self._upload_image(image=image, image_type=image_type)
            theme = Theme(
                **item.dict(),
                image_path=self._get_path(image.filename, image_type=image_type),
                user_id=user_id,
                section_id=section_id
            )
        else:
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
            item: MessageCreate,
            user_id: int,
            theme_id: int | None = None,
            image: UploadFile = File(),
    ) -> Message:
        image_type = ImageType.MESSAGE
        if theme_id:
            if image:
                message = Message(
                    **item.dict(),
                    user_id=user_id,
                    theme_id=theme_id,
                    image_path=self._get_path(filename=image.filename, image_type=image_type)
                )
            else:
                message = Message(**item.dict(), user_id=user_id, theme_id=theme_id)
        else:
            if image:
                message = Message(
                    **item.dict(),
                    user_id=user_id,
                    theme_id=theme_id,
                    image_path=self._get_path(filename=image.filename, image_type=image_type)
                )
            else:
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
