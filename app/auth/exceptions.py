# Module specific exceptions.py, e.g. PostNotFound, InvalidUserData
from fastapi import HTTPException, status


unauthorized = HTTPException(
	status_code=status.HTTP_401_UNAUTHORIZED,
	detail="Could not validate input data",
	headers={"WWW-Authenticate": "Bearer"}
)

user_not_found = HTTPException(
	status_code=status.HTTP_401_UNAUTHORIZED,
	detail="There is no user with this email",
	headers={"WWW-Authenticate": "Bearer"},
)
