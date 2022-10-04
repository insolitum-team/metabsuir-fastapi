# Module specific business logic
from passlib.hash import bcrypt
from jose import jwt
from pydantic.schema import datetime, timedelta

from app import config
from .schemas import UserModel, Token
from .models import User


class AuthService:

	@classmethod
	def verify_password(cls, password: str, hashed_password: str) -> bool:
		return bcrypt.verify(password, hashed_password)

	@classmethod
	def hash_password(cls, password: str) -> str:
		return bcrypt.hash(password)

	@classmethod
	def validate_token(cls, token: str) -> UserModel:
		payload = jwt.decode(token, config.JWT_SECRET, algorithms=["HS256"])
		user_data = payload.get("user")
		user = UserModel.parse_obj(user_data)
		return user

	@classmethod
	def create_token(cls, user: User) -> Token:
		user_data = UserModel.from_orm(user)
		now = datetime.utcnow()
		payload = {
			"iat": now,
			"nbf": now,
			"exp": now + timedelta(seconds=3600),
			"sub": str(user_data.id),
			"user": user_data.dict(),
		}
		token = jwt.encode(payload, config.JWT_SECRET, algorithm=["HS256"])
		return Token(access_token=token)
