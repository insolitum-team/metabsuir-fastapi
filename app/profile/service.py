from fastapi import Depends, UploadFile, File
from sqlalchemy.orm import Session
import shutil
import os

from app import database
from app.profile.models import UserAdditionalInfo
from app.profile.schemas import AdditionalInfoCreate, AdditionalInfoUpdate


class ProfileService:
	def __init__(self, session: Session = Depends(database.get_session)):
		self.session = session

	def set_additional_info(
			self,
			user_id: int,
			data: AdditionalInfoCreate,
			image: UploadFile = File(...),
	) -> UserAdditionalInfo:
		path = os.path.join("images/", image.filename)
		with open(path, "wb") as buffer:
			shutil.copyfileobj(image.file, buffer)
		additional_info = UserAdditionalInfo(
			user_id=user_id,
			**data.dict(),
			image_path=path,
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
		path = os.path.join("images/", image.filename)
		with open(path, "wb") as buffer:
			shutil.copyfileobj(image.file, buffer)
		additional_info = self.get_additional_info(user_id=user_id)
		for field, value in data:
			setattr(additional_info, field, value)
		additional_info.image_path = path
		self.session.commit()
		return additional_info

	def delete_additional_info(self, user_id: int):
		additional_info = self.get_additional_info(user_id=user_id)
		self.session.delete(additional_info)
		self.session.commit()
