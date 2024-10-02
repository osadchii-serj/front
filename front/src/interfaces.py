from abc import ABC, abstractmethod
from typing import Dict


class IUsersBase(ABC):

    users_base = {}

    @abstractmethod
    def add_user(self, user: Dict[str]):
        pass

    @abstractmethod
    def user_search(self, user_name: str):
        pass

    @abstractmethod
    def delete_user(self, user_name: str):
        pass


# =======================================================================================================================
