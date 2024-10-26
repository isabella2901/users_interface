# repository/user_repository.py

import json
import os

class UserRepository:
    def __init__(self, filename='repository/user.json'):
        self.filename = filename

    def _read_users(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)

    def _write_users(self, users):
        with open(self.filename, 'w') as f:
            json.dump(users, f, indent=4)

    def get_all_users(self):
        return self._read_users()

    def get_user_by_id(self, user_id):
        users = self._read_users()
        return next((user for user in users if user['username'] == user_id), None)

    def create_user(self, user):
        users = self._read_users()
        users.append(user)
        self._write_users(users)
        return user

    def delete_user(self, user_id):
        users = self._read_users()
        users = [user for user in users if user['username'] != user_id]
        self._write_users(users)
    
    def update_user(self, user_id, user):
        users = self._read_users()
        for i, u in enumerate(users):
            if u['username'] == user_id:
                users[i] = user
                break
        self._write_users(users)
        
        return user