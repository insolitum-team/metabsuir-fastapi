from fastapi import APIRouter


router = APIRouter()


@router.get("")
def coming_soon():
	return {"message": "coming soon"}
