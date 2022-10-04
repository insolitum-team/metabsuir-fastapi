from fastapi import FastAPI

from app.auth.router import router as auth_router
# from app.forum.router import router as forum_router


tags_metadata = [
    {
        "name": "forum",
        "description": "MetaBSUIR forum"
    },
    {
        "name": "auth",
        "description": "MetaBSUIR authentication"
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
    return application


app = get_application()
