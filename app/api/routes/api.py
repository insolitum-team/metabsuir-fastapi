from fastapi import APIRouter

from app.api.routes import forum


router = APIRouter()


router.include_router(forum.router, prefix="/forum", tags=["forum"])
