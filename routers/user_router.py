# routers/user_router.py
from fastapi import APIRouter
from services import user_service

router = APIRouter(prefix="/users")

@router.get("/")
def get_users():
    return user_service.get_users()