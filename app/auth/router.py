# Core of each module with all the endpoints
from fastapi import APIRouter

# from app.auth import constants as auth_constants
# from app.auth.constants import ErrorCode as PostsErrorCode


router = APIRouter(
	prefix="/auth"
)


@router.post("/sign-up")
def sign_up():
	pass


@router.post("/sign-in")
def sign_in():
	pass
