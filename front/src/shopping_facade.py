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

    user_name: str = None
    user_email: str = None
    user_password: str = None

    warehouse_service = Warehouse
    users_base_service = UsersBase
    payment_service = Payment
    product_service = Product
    delivery_service = Delivery
    order_service = Order
    user_service = User

