import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime

from app.database import Base


class Subject(Base):
    __tablename__ = "metabsuir_subject"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(100), nullable=False, unique=True)


class SubjectInfo(Base):
    __tablename__ = "metabsuir_subject_info"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    subject_id = Column(Integer, ForeignKey("metabsuir_subject.id"))
    user_id = Column(Integer, ForeignKey("metabsuir_users.id"))
    title = Column(String(255), nullable=False, unique=True)
    subtitle = Column(Text, nullable=False)
    body = Column(Text)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    image_url = Column(String, nullable=True)
    file_url = Column(String, nullable=True)
