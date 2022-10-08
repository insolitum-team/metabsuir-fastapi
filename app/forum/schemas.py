from pydantic import BaseModel
from datetime import datetime


class SectionBase(BaseModel):
    title: str
    date: datetime

    class Config:
        orm_mode = True


class SectionModel(SectionBase):
    id: int
    image_path: str | None = None


class SectionCreate(SectionBase):
    pass


class ThemeBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


class ThemeModel(ThemeBase):
    id: int
    image_path: str | None = None
    date: datetime


class ThemeCreate(ThemeBase):
    pass


class MessageBase(BaseModel):
    date: datetime

    class Config:
        orm_mode = True


class MessageModel(MessageBase):
    id: int
    image_path: str | None = None


class MessageCreate(MessageBase):
    content: str


class MessageUpdate(BaseModel):
    content: str

    class Config:
        orm_mode = True
