# Module specific business logic
from passlib.hash import bcrypt
from jose import jwt, JWTError
from pydantic import ValidationError
from pydantic.schema import datetime, timedelta
from fastapi import Depends
from sqlalchemy.orm import Session

from .exceptions import unauthorized
from app import config, database
from .schemas import UserModel, Token, UserCreate
from .models import User
from .dependencies import oauth2_scheme


def get_user(token: str = Depends(oauth2_scheme)) -> UserModel:
	return AuthService.validate_token(token=token)


class AuthService:

	@classmethod
	def verify_password(cls, password: str, hashed_password: str) -> bool:
		return bcrypt.verify(password, hashed_password)

	@classmethod
	def hash_password(cls, password: str) -> str:
		return bcrypt.hash(password)

	@classmethod
	def validate_token(cls, token: str) -> UserModel:
		try:
			payload = jwt.decode(token, config.JWT_SECRET, algorithms=["HS256"])
		except JWTError:
			raise unauthorized
		user_data = payload.get("user")
		try:
			user = UserModel.parse_obj(user_data)
		except ValidationError:
			raise unauthorized
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
		token = jwt.encode(payload, config.JWT_SECRET, algorithm="HS256")
		return Token(access_token=token)

	def __init__(self, session: Session = Depends(database.get_session)):
		self.session = session

	def register(self, user_data: UserCreate) -> Token:
		user = User(
			username=user_data.username,
			email=user_data.email,
			password=self.hash_password(user_data.password)
		)
		self.session.add(user)
		self.session.commit()
		return self.create_token(user)

	def login(self, username: str, password: str) -> Token:
		user = self.session.query(User).filter_by(username=username).first()
		if not user:
			raise unauthorized
		if not self.verify_password(password=password, hashed_password=user.password):
			raise unauthorized
		return self.create_token(user)
