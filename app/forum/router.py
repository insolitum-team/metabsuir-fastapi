# Core of each module with all the endpoints

from app.auth import constants as auth_constants
from app.auth.constants import ErrorCode as PostsErrorCode
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_session
from app.forum.service import get_section_list, create_section_service
from app.forum.schemas import SectionCreate, SectionList

router = APIRouter()


# todo Create response model
@router.get("/")
def section_list(db: Session = Depends(get_session)):
    return get_section_list(db)


@router.post("/")
def create_section(item: SectionCreate, db: Session = Depends(get_session)):
    return create_section_service(db, item)
