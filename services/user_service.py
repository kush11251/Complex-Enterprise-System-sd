# services/user_service.py
from models import User
from repositories import user_repository

class UserService:
    def get_users(self):
        return user_repository.get_users()