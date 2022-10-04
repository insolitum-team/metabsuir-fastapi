# Module specific business logic
from fastapi import Depends
from sqlalchemy.orm import Session

from app.forum.models import Section
from app.forum.schemas import SectionCreate
from app.database import get_session


def get_section_list(db: Session = Depends(get_session)):
    return db.query(Section).all()


def create_section_service(db: Session, item: SectionCreate):
    section = Section(**item.dict())
    db.add(section)
    db.commit()
    db.refresh(section)
    return section
