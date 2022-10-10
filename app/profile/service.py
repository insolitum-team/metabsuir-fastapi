from fastapi import Depends, UploadFile, File
from sqlalchemy.orm import Session
import shutil
import os

from app.profile import config
from app import database
from app.profile.models import UserAdditionalInfo
from app.profile.schemas import AdditionalInfoCreate, AdditionalInfoUpdate, AdditionalInfoTelegram


class ProfileService:

	@classmethod
	def _get_path(cls, filename: str):
		return os.path.join(config.PROFILE_IMAGE_PATH, filename)

	def __init__(self, session: Session = Depends(database.get_session)):
		self.session = session

	def _upload_image(self, image: UploadFile = File(...)):
		path = self._get_path(filename=image.filename)
		with open(path, "wb") as buffer:
			shutil.copyfileobj(image.file, buffer)

	def set_additional_info(
			self,
			user_id: int,
			data: AdditionalInfoCreate,
			image: UploadFile = File(...),
	) -> UserAdditionalInfo:
		self._upload_image(image=image)
		additional_info = UserAdditionalInfo(
			user_id=user_id,
			**data.dict(),
			image_path=self._get_path(filename=image.filename),
		)
		self.session.add(additional_info)
		self.session.commit()
		return additional_info

	def get_additional_info(self, user_id: int) -> UserAdditionalInfo:
		additional_info = self.session.query(UserAdditionalInfo).filter_by(user_id=user_id).first()
		return additional_info

	def update_additional_info(
			self,
			user_id: int,
			data: AdditionalInfoUpdate,
			image: UploadFile = File(),
	) -> UserAdditionalInfo:
		self._upload_image(image=image)
		additional_info = self.get_additional_info(user_id=user_id)
		for field, value in data:
			setattr(additional_info, field, value)
		additional_info.image_path = self._get_path(filename=image.filename)
		self.session.commit()
		return additional_info

	def delete_additional_info(self, user_id: int):
		additional_info = self.get_additional_info(user_id=user_id)
		self.session.delete(additional_info)
		self.session.commit()

	def get_chat_id_from_bot(self, data: AdditionalInfoTelegram):
		user_info = self.session.query(UserAdditionalInfo).filter_by(user_id=int(data.user_id)).first()
		user_info.chat_id = data.chat_id
		self.session.commit()
		return user_info
