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


class SubjectUpdate(SubjectBase):
    pass


class SubjectInfoBase(BaseModel):
    title: str
    subtitle: str
    body: str
    image_url: str | None = None
    file_url: str | None = None

    class Config:
        orm_mode = True


class SubjectInfoModel(SubjectInfoBase):
    id: int
    user_id: int
    date: datetime


class SubjectInfoCreate(SubjectInfoBase):
    subject_id: int


class SubjectInfoUpdate(SubjectInfoBase):
    pass
