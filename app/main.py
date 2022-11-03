from fastapi import FastAPI
# from starlette.requests import Request
# from starlette.responses import Response

from app.auth.router import router as auth_router
from app.forum.router import router as forum_router
from app.profile.router import router as profile_router
from app.subjects.router import router as subject_router
# from app.database import SessionLocal

tags_metadata = [
    {
        "name": "forum",
        "description": "MetaBSUIR forum",
    },
    {
        "name": "authentication",
        "description": "MetaBSUIR authentication",
    },
    {
        "name": "profile",
        "description": "Members profile",
    },
    {
        "name": "subjects",
        "description": "Subjects profile",
    },
]


def get_application() -> FastAPI:
    application = FastAPI(
        title="MetaBSUIR",
        description="BSUIR meta-universe",
        version="0.1.0",
        openapi_tags=tags_metadata,
    )
    application.include_router(auth_router)
    application.include_router(forum_router)
    application.include_router(profile_router)
    application.include_router(subject_router)
    return application


app = get_application()
