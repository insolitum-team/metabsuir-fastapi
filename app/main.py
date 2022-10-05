from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from app.auth.router import router as auth_router
from app.forum.router import router as forum_router
from app.database import SessionLocal

tags_metadata = [
    {
        "name": "forum",
        "description": "MetaBSUIR forum"
    },
    {
        "name": "authentication",
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
    application.include_router(forum_router)
    return application


app = get_application()


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response

