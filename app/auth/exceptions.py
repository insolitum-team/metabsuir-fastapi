# Module specific exceptions.py, e.g. PostNotFound, InvalidUserData
from fastapi import HTTPException, status


unauthorized = HTTPException(
	status_code=status.HTTP_401_UNAUTHORIZED,
	detail="Could not validate input data",
	headers={"WWW-Authenticate": "Bearer"}
)
