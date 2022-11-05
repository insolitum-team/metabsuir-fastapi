from fastapi import APIRouter, Depends

from .service import SubjectService

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
def get_subject_additional_route():
    pass


@router.post("/add-subject")
def add_subject_route():
    pass


@router.post("/add-subject-additional")
def add_subject_additional():
    pass
