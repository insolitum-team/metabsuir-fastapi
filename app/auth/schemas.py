from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
	username: str
	email: str

	class Config:
		orm_mode = True


class UserCreate(UserBase):
	password: str


class UserModel(UserBase):
	id: int


class EmailToReset(BaseModel):
	email: list[EmailStr]


class ResetPassword(BaseModel):
	password: str


class Token(BaseModel):
	access_token: str
	token_type: str = "bearer"
