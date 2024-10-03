from abc import ABC, abstractmethod

from dataclasses import dataclass

from typing import Dict, List


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

    @abstractmethod
    def update_stock(self, product: object):
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
    def calculate_total(self):
        pass

    @abstractmethod
    def update_status(self):
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
    def schedule_delivery(self):
        pass

    @abstractmethod
    def update_status(self, new_status):
        pass


# ========================================================================================================================
