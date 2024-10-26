# services/user_service.py

from repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, user):
        return self.user_repository.create_user(user)

    def delete_user(self, user_id):
        self.user_repository.delete_user(user_id)
    
    def update_user(self, user_id, user):
        self.user_repository.update_user(user_id, user)
