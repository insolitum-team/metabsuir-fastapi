# Core of each module with all the endpoints

# from app.auth import constants as auth_constants
# from app.auth.constants import ErrorCode as PostsErrorCode
from fastapi import APIRouter, Depends

from app.forum.schemas import SectionCreate, SectionModel, ThemeCreate, ThemeModel, MessageCreate, MessageModel
from app.forum.service import ForumService
from app.auth.schemas import UserModel
from app.auth.service import get_user

router = APIRouter(
    prefix="/forum",
    tags=["forum"]
)


# --------- Sections routes --------- #
@router.get("/sections", response_model=list[SectionModel])
def section_list(service: ForumService = Depends()):
    return service.get_section_list()


@router.post("/sections")
def create_section(section_data: SectionCreate, service: ForumService = Depends()):
    return service.create_section_service(section_data)


@router.get("/themes", response_model=list[ThemeModel])
def theme_list(service: ForumService = Depends()):
    return service.get_theme_list()


@router.post("/themes")
def create_theme(theme_data: ThemeCreate, user: UserModel = Depends(get_user), service: ForumService = Depends()):
    return service.create_theme_service(theme_data, user.id)


@router.get("/messages", response_model=list[MessageModel])
def message_list(service: ForumService = Depends()):
    return service.get_message_list()


@router.post("/messages")
def create_message(message_data: MessageCreate, user: UserModel = Depends(get_user), service: ForumService = Depends()):
    return service.create_message_service(message_data, user.id)
