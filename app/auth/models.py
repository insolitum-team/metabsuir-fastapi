# Database models
from sqlalchemy import Column, String, Integer

from app.database import Base


class User(Base):
	__tablename__ = "metabsuir_users"

	id = Column(Integer, primary_key=True, index=True, unique=True)
	username = Column(String(20))
	email = Column(String(50))
	password = Column(String(255))
