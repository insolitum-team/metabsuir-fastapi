from fastapi import APIRouter, Depends, UploadFile, File

from app.forum.schemas import (
    SectionCreate, ThemeCreate, MessageCreate, MessageUpdate, SectionModel
)
from app.forum.service import ForumService
from app.auth.schemas import UserModel
from app.auth.service import get_user

router = APIRouter(
    prefix="/forum",
    tags=["forum"]
)


# --------- Sections routes --------- #
@router.get("/sections")
def section_list(
        section_id: int | None = None,
        service: ForumService = Depends(),
):
    return service.get_section_list(section_id=section_id)


@router.post("/sections")
def create_section(section_data: SectionCreate, service: ForumService = Depends()):
    return service.create_section_service(section_data)


# --------- Theme routes --------- #
@router.get("/themes")
def theme_list(
        theme_id: int | None = None,
        section_id: int | None = None,
        service: ForumService = Depends(),
):
    return service.get_theme_list(theme_id=theme_id, section_id=section_id)


@router.post("/themes")
def create_theme(
        section_id: int,
        theme_data: ThemeCreate,
        user: UserModel = Depends(get_user),
        service: ForumService = Depends(),
):
    return service.create_theme_service(
        item=theme_data,
        user_id=user.id,
        section_id=section_id,
    )


# --------- Messages routes --------- #
@router.get("/messages")
def message_list(
        theme_id: int | None = None,
        service: ForumService = Depends(),
):
    return service.get_message_list(theme_id=theme_id)


@router.post("/messages")
def create_message(
        message_data: MessageCreate,
        theme_id: int,
        user: UserModel = Depends(get_user),
        service: ForumService = Depends(),
):
    return service.create_message_service(
        item=message_data,
        user_id=user.id,
        theme_id=theme_id,
    )


@router.put("/update-message")
def update_message(
        message_id: int,
        message_info: MessageUpdate,
        service: ForumService = Depends(),
):
    return service.update_message_service(message_id=message_id, message_info=message_info)


@router.delete("/delete-message")
def delete_message(
        message_id: int,
        service: ForumService = Depends()
):
    return service.delete_message_service(message_id=message_id)
