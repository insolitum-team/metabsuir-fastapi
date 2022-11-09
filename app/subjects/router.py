from fastapi import APIRouter, Depends

from .service import SubjectService
from .schemas import SubjectCreate, SubjectInfoCreate, SubjectUpdate, SubjectInfoUpdate
from app.auth.schemas import UserModel
from app.auth.service import get_user

router = APIRouter(
    prefix="/subjects",
    tags=["subjects"],
)


@router.get("/get-subject")
def get_subject_route(
    subject_id: int | None = None,
    service: SubjectService = Depends(),
):
    return service.get_subjects(subject_id=subject_id)


@router.get("/get-subject-additional")
def get_subject_additional_route(
        subject_id: int,
        service: SubjectService = Depends()
):
    return service.get_subject_info(subject_id=subject_id)


@router.post("/add-subject")
def add_subject_route(
        subject_data: SubjectCreate,
        service: SubjectService = Depends()
):
    return service.subject_create(subject_data=subject_data)


@router.post("/add-subject-additional")
def add_subject_additional(
        user: UserModel = Depends(get_user),
        subject_info_data: SubjectInfoCreate = Depends(),
        service: SubjectService = Depends(),
):
    return service.subject_info_create(
        user_id=user.id,
        subject_info_data=subject_info_data,
    )


@router.put("/update-subject")
def update_subject(
        subject_id: int,
        subject_data: SubjectUpdate,
        service: SubjectService = Depends(),
):
    return service.subject_update(subject_id=subject_id, subject_data=subject_data)


@router.put("/update-subject-info")
def update_subject_info(
        subject_info_id: int,
        subject_ingo_data: SubjectInfoUpdate,
        service: SubjectService = Depends(),
):
    return service.subject_info_update(subject_info_id=subject_info_id, subject_info_data=subject_ingo_data)
