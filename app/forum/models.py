# Database models

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text

from app.database import Base


class Section(Base):
    __tablename__ = "metabsuir_sections"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(250))
    date = Column(DateTime)


class Theme(Base):
    __tablename__ = "metabsuir_themes"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(250))
    body = Column(Text)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("metabsuir_users.id"))
    section_id = Column(Integer, ForeignKey("metabsuir_sections.id"))


class Message(Base):
    __tablename__ = "metabsuir_messages"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    content = Column(Text)
    theme_id = Column(Integer, ForeignKey("metabsuir_themes.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("metabsuir_users.id"))
    reply_to = Column(Integer)
    date = Column(DateTime)
