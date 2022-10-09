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
    image_url: str | None = None
    date: datetime

    class Config:
        orm_mode = True


class ThemeModel(ThemeBase):
    id: int


class ThemeCreate(ThemeBase):
    pass


class MessageBase(BaseModel):
    reply_to: int | None = None

    class Config:
        orm_mode = True


class MessageModel(MessageBase):
    id: int
    image_url: str | None = None
    date: datetime


class MessageCreate(MessageBase):
    content: str
    image_url: str | None = None


class MessageUpdate(BaseModel):
    content: str

    class Config:
        orm_mode = True
