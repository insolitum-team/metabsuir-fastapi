from fastapi import APIRouter, Depends, UploadFile, File

from app.auth.schemas import UserModel
from app.auth.service import get_user
from app.profile.schemas import AdditionalInfoUpdate, AdditionalInfoCreate, AdditionalInfoModel
from app.profile.service import ProfileService

router = APIRouter(
	prefix="/profile",
	tags=["profile"],
)


@router.post("/set-info", response_model=AdditionalInfoModel)
def set_info(
		info_data: AdditionalInfoCreate = Depends(),
		image: UploadFile = File(...),
		user: UserModel = Depends(get_user),
		service: ProfileService = Depends()
):
	return service.set_additional_info(user_id=user.id, data=info_data, image=image)


@router.get("/get-info")
def get_info(
		user: UserModel = Depends(get_user),
		service: ProfileService = Depends(),
):
	return service.get_additional_info(user_id=user.id)


@router.put("/update-info")
def update_info(
		info_data: AdditionalInfoUpdate = Depends(),
		image: UploadFile = File(),
		user: UserModel = Depends(get_user),
		service: ProfileService = Depends()
):
	return service.update_additional_info(user_id=user.id, data=info_data, image=image)


@router.delete("/delete-info")
def delete_info(
		user: UserModel = Depends(get_user),
		service: ProfileService = Depends()
):
	return service.delete_additional_info(user_id=user.id)


@router.post("/get-chat-id")
def get_chat_id(user_id: str, chat_id: str, service: ProfileService = Depends()):
	return service.get_chat_id_from_bot(user_id=user_id, chat_id=chat_id)
