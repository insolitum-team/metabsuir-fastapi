# Pydantic models
from pydantic import BaseModel
from datetime import datetime


class SectionBase(BaseModel):
    title: str
    date: datetime

    class Config:
        orm_mode = True


class SectionList(BaseModel):
    id: int


class SectionCreate(SectionBase):
    pass
