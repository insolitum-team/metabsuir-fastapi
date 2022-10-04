# Core of each module with all the endpoints
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

# from app.auth import constants as auth_constants
# from app.auth.constants import ErrorCode as PostsErrorCode
from .schemas import UserCreate
from .service import AuthService


router = APIRouter(
	prefix="/auth"
)


@router.post("/sign-up")
def sign_up(user_data: UserCreate, service: AuthService = Depends()):
	return service.register(user_data)


@router.post("/sign-in")
def sign_in(user_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()):
	return service.login(username=user_data.username, password=user_data.password)
