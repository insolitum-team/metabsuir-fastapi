from fastapi import Depends
from sqlalchemy.orm import Session

from app import database
from app.profile.models import UserAdditionalInfo
from app.profile.schemas import AdditionalInfoCreate, AdditionalInfoUpdate


class ProfileService:
	def __init__(self, session: Session = Depends(database.get_session)):
		self.session = session

	def set_additional_info(self, user_id: int, info_data: AdditionalInfoCreate) -> UserAdditionalInfo:
		additional_info = UserAdditionalInfo(**info_data.dict(), user_id=user_id)
		self.session.add(additional_info)
		self.session.commit()
		return additional_info

	def get_additional_info(self, user_id: int) -> UserAdditionalInfo:
		additional_info = self.session.query(UserAdditionalInfo).filter_by(user_id=user_id).first()
		return additional_info

	def update_additional_info(self, user_id: int, info_data: AdditionalInfoUpdate) -> UserAdditionalInfo:
		additional_info = self.get_additional_info(user_id=user_id)
		for field, value in info_data:
			setattr(additional_info, field, value)
		self.session.commit()
		return additional_info

	def delete_additional_info(self, user_id: int):
		additional_info = self.get_additional_info(user_id=user_id)
		self.session.delete(additional_info)
		self.session.commit()
