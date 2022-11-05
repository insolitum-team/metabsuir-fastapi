import os
import shutil
from fastapi import Depends, UploadFile, File
from sqlalchemy.orm import Session

from .config import SUBJECT_FILE_PATH, SUBJECT_IMAGE_PATH
from app import database
from .constants import FileKind
from .schemas import SubjectInfoCreate, SubjectCreate
from .models import Subject, SubjectInfo


class SubjectService:

    @classmethod
    def _get_image_path(cls, filename: str) -> str:
        return os.path.join(SUBJECT_IMAGE_PATH, filename)

    @classmethod
    def _get_file_path(cls, filename: str) -> str:
        return os.path.join(SUBJECT_FILE_PATH, filename)

    def __init__(self, session: Session = Depends(database.get_session)):
        self.session = session

    def _upload_image(
            self,
            kind: FileKind,
            file: UploadFile = File(...)
    ):
        if kind == "image":
            path = self._get_image_path(filename=file.filename)
        else:
            path = self._get_file_path(filename=file.filename)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    def get_subjects(self, subject_id: int | None = None) -> list[Subject] | Subject:
        if not subject_id:
            return self.session.query(Subject).all()
        return self.session.query(Subject).get(subject_id)

    def get_subject_info(self, subject_id: int | None = None) -> list[SubjectInfo] | SubjectInfo:
        if not subject_id:
            return self.session.query(SubjectInfo).all()
        return self.session.query(SubjectInfo).filter_by(subject_id=subject_id).first()

    def subject_create(
            self,
            subject_data: SubjectCreate
    ) -> Subject:
        subject = Subject(**subject_data.dict())
        self.session.add(subject)
        self.session.commit()
        return subject

    def subject_info_create(
            self,
            user_id: int,
            subject_info_data: SubjectInfoCreate,
    ) -> SubjectInfo:
        subject_info = SubjectInfo(
            user_id=user_id,
            **subject_info_data.dict(),
        )
        self.session.add(subject_info)
        self.session.commit()
        return subject_info
