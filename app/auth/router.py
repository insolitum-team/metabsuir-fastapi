# Core of each module with all the endpoints
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

# from app.auth import constants as auth_constants
# from app.auth.constants import ErrorCode as PostsErrorCode
from .schemas import UserCreate, UserModel, Token, EmailToReset, ResetPassword
from .service import AuthService, get_user


router = APIRouter(
	prefix="/auth",
	tags=["authentication"]
)


@router.post("/sign-up", response_model=Token)
def sign_up(user_data: UserCreate, service: AuthService = Depends()):
	"""Регистрация пользователя"""
	return service.register(user_data)


@router.post("/sign-in", response_model=Token)
def sign_in(form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()):
	"""Авторизация пользователя"""
	return service.login(username=form_data.username, password=form_data.password)


@router.get("/user", response_model=UserModel)
def get_user(user: UserModel = Depends(get_user)):
	return user


@router.post("/reset-password")
def reset_password_route(
		email: EmailToReset,
		service: AuthService = Depends(),
):
	return service.reset_password(email_data=email)


@router.post("/restore-password")
def restore_password_route(
		token: str,
		password: ResetPassword,
		service: AuthService = Depends(),
):
	return service.restore_password(password=password, token=token)
