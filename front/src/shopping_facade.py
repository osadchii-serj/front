from dataclasses import dataclass

from warehouse import Warehouse
from users_base import UsersBase
from payment import Payment
from product import Product
from delivery import Delivery
from order import Order
from user import User


@dataclass
class ShoppingFacade:
    pass