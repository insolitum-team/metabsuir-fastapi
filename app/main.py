from fastapi import FastAPI

from app.api.routes.api import router


tags_metadata = [
    {
        "name": "forum",
        "description": "MetaBSUIR forum"
    }
]


def get_application() -> FastAPI:
    application = FastAPI(
        title="MetaBSUIR",
        description="BSUIR meta-universe",
        version="0.1.0",
        openapi_tags=tags_metadata,
    )
    application.include_router(router)
    return application


app = get_application()
