from datetime import datetime

from pydantic import BaseModel


class SubjectBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


class SubjectModel(SubjectBase):
    pass


class SubjectCreate(SubjectBase):
    pass


class SubjectInfoBase(BaseModel):
    title: str
    subtitle: str
    body: str

    class Config:
        orm_mode = True


class SubjectInfoModel(SubjectInfoBase):
    id: int
    user_id: int
    image_url: str
    file_url: str
    date: datetime


class SubjectInfoCreate(SubjectInfoBase):
    subject_id: int
