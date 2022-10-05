# Database models

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
# from sqlalchemy.orm import relationship
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
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("metabsuir_users.id"))


class Message(Base):
    __tablename__ = "metabsuir_messages"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    content = Column(Text)
    theme = Column(String, ForeignKey("metabsuir_themes.id"))
    user_id = Column(Integer, ForeignKey("metabsuir_users.id"))
    reply_to = Column(Integer)
    # reply_to = relationship('Message', remote_side=['id'], backref='replies')
    date = Column(DateTime)
