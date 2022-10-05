# Pydantic models
from pydantic import BaseModel
from datetime import datetime


# --------- Sections --------- #
class SectionBase(BaseModel):
    title: str
    date: datetime

    class Config:
        orm_mode = True


class SectionList(SectionBase):
    id: int


class SectionCreate(SectionBase):
    pass


# --------- Themes --------- #
class ThemeBase(BaseModel):
    title: str
    date: datetime
    user_id = int

    class Config:
        orm_mode = True


class ThemeList(ThemeBase):
    id: int


class ThemeCreate(ThemeBase):
    pass


# --------- Messages --------- #
class MessageBase(BaseModel):
    theme = str
    date = datetime

    class Config:
        orm_mode = True


class MessageList(MessageBase):
    id: int


class MessageCreate(MessageBase):
    content: str
