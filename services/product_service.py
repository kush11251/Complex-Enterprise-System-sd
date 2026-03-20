# services/product_service.py
from models import Product
from repositories import product_repository

class ProductService:
    def get_products(self):
        return product_repository.get_products()