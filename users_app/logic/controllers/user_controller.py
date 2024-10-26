# controllers/user_controller.py

from services.user_service import UserService


class UserController:
    def __init__(self):
        self.user_service = UserService()

    def get_all_users(self):
        """Retorna todos los usuarios."""
        return self.user_service.get_all_users()

    def get_user_by_id(self, user_id):
        """Retorna un usuario por su ID."""
        user = self.user_service.get_user_by_id(user_id)
        if user:
            return user
        return {"message": "User not found"}

    def create_user(self, user_data):
        """Crea un nuevo usuario."""
        user = {
            "username": user_data.get(
                "username"
            ),  
            "password": user_data.get("password"),
            "name": user_data.get("name"),
            "lastName": user_data.get("lastName"),

        }
        return self.user_service.create_user(user)

    def delete_user(self, user_id):
        """Elimina un usuario por su ID."""
        self.user_service.delete_user(user_id)
        return {"message": "User deleted"}
    
    def update_user(self, user_id, user_data):
        """Actualiza un usuario por su ID."""

        user_get = user_data.get("username")
        print(user_get)
        
        if user_get is None:
            return {"message": "User not found"}
        
        user = {
            "username": user_data.get(
                "username"
            ),  
            "password": user_data.get("password"),
            "name": user_data.get("name"),
            "lastName": user_data.get("lastName"),
        }
        return self.user_service.update_user(user_id, user)
