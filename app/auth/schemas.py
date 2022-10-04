# Pydantic models
from pydantic import BaseModel


class UserBase(BaseModel):
	username: str
	email: str

	class Config:
		orm_mode = True


class UserCreate(UserBase):
	password: str


class UserModel(UserBase):
	id: int


class Token(BaseModel):
	access_token: str
	token_type: str = "bearer"
