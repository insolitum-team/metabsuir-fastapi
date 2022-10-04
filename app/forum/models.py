# Database models

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Section(Base):
    __tablename__ = "metabsuir_sections"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(250))
    date = Column(DateTime)


class Theme(Base):  # Not migrated
    __tablename__ = "metabsuir_themes"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(250))
    date = Column(DateTime)
    # user = Column(Integer, ForeignKey("user.id"))
    # user_id = relationship("User")
