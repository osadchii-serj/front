from abc import ABC, abstractmethod

from dataclasses import dataclass

from typing import Dict, List


class IUsersBase(ABC):

    users_base: Dict[str] = {}

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


@dataclass
class IUser(ABC):

    user_name: str = None
    user_email: str = None
    user_password: str = None
    user_id = None
    user_cart = []

    @abstractmethod
    def create_user_id(self):
        pass

    @abstractmethod
    def add_product_cart(self, product):
        pass

    @abstractmethod
    def remove_product_cart(self, product):
        pass

    @abstractmethod
    def checkout(self):
        pass


# ========================================================================================================================


@dataclass
class IProduct(ABC):

    product_name: str = None
    product_description: str = None
    product_price: float = 0

    product_stock_quantity = None
    product_id = None

    @abstractmethod
    def update_stock(self, product: Dict[str]):
        pass


# ========================================================================================================================


@dataclass
class IWarehouse(ABC):

    warehouse = {}

    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def remove_product(self, product):
        pass


# ========================================================================================================================


@dataclass
class IOrder(ABC):

    products: List[object]

    order_id = None
    user_id = None
    total_amount = 0
    status = None

    @abstractmethod
    def calculate_total(self):
        pass

    @abstractmethod
    def update_status(self):
        pass


# ========================================================================================================================
