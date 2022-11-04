import datetime

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
    image_url: str
    file_url: str

    class Config:
        orm_mode = True


class SubjectInfoModel(SubjectInfoBase):
    id: int
    subject_id: int
    user_id: int
    date: datetime.datetime


class SubjectInfoCreate(SubjectInfoBase):
    subject_id: int
