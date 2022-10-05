from fastapi import APIRouter, Depends

from app.auth.schemas import UserModel
from app.auth.service import get_user
from app.profile.schemas import AdditionalInfoUpdate, AdditionalInfoCreate
from app.profile.service import ProfileService

router = APIRouter(
	prefix="/profile",
	tags=["profile"],
)


@router.post("/set-info")
def set_info(
		info_data: AdditionalInfoCreate,
		user: UserModel = Depends(get_user),
		service: ProfileService = Depends()
):
	return service.set_additional_info(user_id=user.id, info_data=info_data)


@router.get("/get-info")
def get_info(
		user: UserModel = Depends(get_user),
		service: ProfileService = Depends(),
):
	return service.get_additional_info(user_id=user.id)


@router.put("/update-info")
def update_info(
		info_data: AdditionalInfoUpdate,
		user: UserModel = Depends(get_user),
		service: ProfileService = Depends()
):
	return service.update_additional_info(user_id=user.id, info_data=info_data)


@router.delete("/delete-info")
def delete_info(
		user: UserModel = Depends(get_user),
		service: ProfileService = Depends()
):
	return service.delete_additional_info(user_id=user.id)
