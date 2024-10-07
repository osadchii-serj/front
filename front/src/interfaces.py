from abc import ABC, abstractmethod

from dataclasses import dataclass

from typing import Dict


@dataclass
class IUsersBase(ABC):

    @abstractmethod
    def add_user(self, user: Dict):
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

    user_name: str
    user_email: str
    user_password: str
    user_id = None
    payment_system = None
    balance = 0
    cart = []

    @abstractmethod
    def create_user_id(self):
        pass

    @abstractmethod
    def add_product_cart(self, product):
        pass

    @abstractmethod
    def remove_product_cart(self, product):
        pass


# ========================================================================================================================


@dataclass
class IProduct(ABC):

    product_name: str
    product_price: float

    product_id = None

    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def create_product_id(self):
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

    @abstractmethod
    def create_order(self):
        pass


# ========================================================================================================================


@dataclass
class IPayment(ABC):

    @abstractmethod
    def process_payment(self):
        pass


# ========================================================================================================================


@dataclass
class IDelivery(ABC):

    @abstractmethod
    def delivery(self):
        pass


# ========================================================================================================================
