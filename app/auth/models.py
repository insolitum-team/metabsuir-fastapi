# Database models

from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base


class User(Base):
	__tablename__ = "metabsuir_users"

	id = Column(Integer, primary_key=True, index=True, unique=True)
	username = Column(String(20))
	email = Column(String(50))
	password = Column(String(255))


class UserAdditionalInfo(Base):
	__tablename__ = "metabsuir_users_additional_info"

	id = Column(Integer, primary_key=True, index=True, unique=True)
	user_id = Column(Integer, ForeignKey("metabsuir_users.id"))
	first_name = Column(String(20), nullable=True)
	surname = Column(String(20), nullable=True)
	status = Column(String(255), nullable=True)
