from pydantic import BaseModel


class AdditionalInfoBase(BaseModel):
	first_name: str | None = None
	surname: str | None = None
	status: str | None = None

	class Config:
		orm_mode = True


class AdditionalInfoModel(AdditionalInfoBase):
	id: int
	image_path: str


class AdditionalInfoCreate(AdditionalInfoBase):
	pass


class AdditionalInfoUpdate(AdditionalInfoBase):
	pass
