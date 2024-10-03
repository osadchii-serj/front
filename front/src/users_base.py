from dataclasses import dataclass
from typing import Dict

from interfaces import IUsersBase


class UsersBase(IUsersBase):
    
    def add_user(self, user: Dict):
        name = user["name"]
        self.users_base.update({name: user})
        print(f"Пользователь: {name} зарегистрирован")
    
    def user_search(self, user_name: str):
        return super().user_search(user_name)
    
    def delete_user(self, user_name: str):
        return super().delete_user(user_name)
