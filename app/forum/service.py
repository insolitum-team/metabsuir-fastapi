# Module specific business logic

from sqlalchemy.orm import Session
from app.forum.models import Section
from app.forum.schemas import SectionCreate


def get_section_list(db: Session):
    return db.query(Section).all()


def create_section_service(db: Session, item: SectionCreate):
    section = Section(**item.dict())
    db.add(section)
    db.commit()
    db.refresh(section)
    return section
