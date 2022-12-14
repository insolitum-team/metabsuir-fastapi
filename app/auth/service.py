from passlib.hash import bcrypt
from jose import jwt, JWTError
from pydantic import ValidationError
from pydantic.schema import datetime, timedelta
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi_mail import MessageSchema, MessageType, FastMail

from .exceptions import unauthorized, user_not_found
from .schemas import UserModel, Token, UserCreate, EmailToReset, ResetPassword
from .models import User
from .dependencies import oauth2_scheme
from app.profile.models import UserAdditionalInfo
from app import config, database


def get_user(token: str = Depends(oauth2_scheme)) -> UserModel:
	return AuthService.validate_token(token=token)


class AuthService:

	NOW = datetime.utcnow()

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
		payload = {
			"iat": cls.NOW,
			"nbf": cls.NOW,
			"exp": cls.NOW + timedelta(seconds=3600),
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
		user_additional_info = UserAdditionalInfo(
			user_id=user.id,
		)
		self.session.add(user_additional_info)
		self.session.commit()
		return self.create_token(user)

	def login(self, username: str, password: str) -> Token:
		user = self.session.query(User).filter_by(username=username).first()
		if not user:
			raise unauthorized
		if not self.verify_password(password=password, hashed_password=user.password):
			raise unauthorized
		return self.create_token(user)

	def create_reset_password_token(self, email: str) -> Token:
		user = self.session.query(User).filter_by(email=email).first()
		payload = {
			"iat": self.NOW,
			"nbf": self.NOW,
			"exp": self.NOW + timedelta(seconds=3600),
			"sub": str(user.id),
			"user_email": email,
		}
		token = jwt.encode(payload, config.JWT_SECRET, algorithm="HS256")
		return Token(access_token=token)

	def email_to_reset(self, email_data: EmailToReset) -> str | int:
		user = self.session.query(User).filter_by(email=email_data.email[0]).first()
		if not user:
			raise user_not_found
		token = self.create_reset_password_token(email=email_data.email[0])
		url = f"{config.DOMAIN}auth/restore-password?token={token}"
		message = MessageSchema(
			subject="Fastapi-Mail module",
			recipients=email_data.dict().get("email"),
			template_body={
				"url": url,
				"username": user.username,
			},
			subtype=MessageType.html,
		)
		fm = FastMail(config.EMAIL_CONFIG)
		fm.send_message(message=message, template_name="reset_password.html",)
		return url

	def restore_password(self, password: ResetPassword, token: str) -> 0:
		payload = jwt.decode(token, config.JWT_SECRET, algorithms=["HS256"])
		email = payload.get("user_email")
		user = self.session.query(User).filter_by(email=email).first()
		user.password = self.hash_password(password=password.password)
		self.session.commit()
		return self.create_token(user)
