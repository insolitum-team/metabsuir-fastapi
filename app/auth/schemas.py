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


class AdditionalInfoBase(BaseModel):
	user_id: int
	first_name: str | None = None
	surname: str | None = None
	status: str | None = None

	class Config:
		orm_mode = True


class AdditionalInfoModel(AdditionalInfoBase):
	id: int


class AdditionalInfoCreate(AdditionalInfoBase):
	pass
