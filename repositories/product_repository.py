# repositories/product_repository.py
from models import Product
from databases import Database

class ProductRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_products(self):
        return self.db.query(Product).all()