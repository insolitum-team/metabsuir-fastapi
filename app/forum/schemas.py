from pydantic import BaseModel
from datetime import datetime


class SectionBase(BaseModel):
    title: str
    date: datetime

    class Config:
        orm_mode = True


class SectionModel(SectionBase):
    id: int


class SectionCreate(SectionBase):
    pass


class ThemeBase(BaseModel):
    title: str
    date: datetime
    user_id: int

    class Config:
        orm_mode = True


class ThemeModel(ThemeBase):
    id: int


class ThemeCreate(ThemeBase):
    pass


class MessageBase(BaseModel):
    theme: str
    date: datetime

    class Config:
        orm_mode = True


class MessageModel(MessageBase):
    id: int


class MessageCreate(MessageBase):
    content: str
