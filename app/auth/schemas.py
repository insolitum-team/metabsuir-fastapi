from pydantic import BaseModel, validator, ValidationError


class UserBase(BaseModel):
	username: str
	email: str

	class Config:
		orm_mode = True


class UserCreate(UserBase):
	password: str

	@validator("password")
	def validate_password(cls, password: str) -> str:
		if len(password) < 5 or len(password) > 10:
			raise ValidationError
		return password


class UserModel(UserBase):
	id: int


class Token(BaseModel):
	access_token: str
	token_type: str = "bearer"
