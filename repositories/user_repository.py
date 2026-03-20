# repositories/user_repository.py
from models import User
from databases import Database

class UserRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_users(self):
        return self.db.query(User).all()