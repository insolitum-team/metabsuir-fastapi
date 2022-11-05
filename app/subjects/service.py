from fastapi import Depends
from sqlalchemy.orm import Session

from app import database
from .schemas import SubjectInfoCreate, SubjectCreate
from .models import Subject, SubjectInfo


class SubjectService:
    def __init__(self, session: Session = Depends(database.get_session)):
        self.session = session

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
