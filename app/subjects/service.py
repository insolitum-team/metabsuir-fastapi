from fastapi import Depends
from sqlalchemy.orm import Session

from app import database


class SubjectService:
    def __init__(self, session: Session = Depends(database.get_session)):
        self.session = session
