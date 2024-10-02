from dataclasses import dataclass

from interfaces import IUser


class User(IUser):

    def create_user_id(self):
        self.user_id = id(self)
