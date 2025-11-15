from fastapi import APIRouter
from api.v1 import ai_routes

router = APIRouter()
router.include_router(ai_routes.router)
