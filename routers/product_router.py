# routers/product_router.py
from fastapi import APIRouter
from services import product_service

router = APIRouter(prefix="/products")

@router.get("/")
def get_products():
    return product_service.get_products()