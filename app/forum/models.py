# Database models

from sqlalchemy import Column, String, Integer, DateTime
from app.database import Base


class Section(Base):
    __tablename__ = "metabsuir_sections"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(250))
    date = Column(DateTime)
