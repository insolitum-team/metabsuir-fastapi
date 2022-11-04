from fastapi import APIRouter


router = APIRouter(
    prefix="/subjects",
    tags=["subjects"],
)


@router.get("/get-subject")
def get_subject_route():
    pass


@router.get("/get-subject-additional")
def get_subject_additional_route():
    pass


@router.post("/add-subject")
def add_subject_route():
    pass


@router.post("/add-subject-additional")
def add_subject_additional():
    pass
