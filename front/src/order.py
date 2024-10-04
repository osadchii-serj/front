from dataclasses import dataclass

from interfaces import IOrder

from typing import List


@dataclass
class Order(IOrder):

    order_id = None
    user_id = None
    products = None
    payment = None

    def create_order(self):
        self.create_order_id()
        return self

    def create_order_id(self):
        self.order_id = id(self)

    def add_user_id(self, user_id: object):
        self.user_id = user_id

    def add_products(self, products: List[str]):
        self.products = products

    def add_payment(self, payment: str):
        self.payment = payment


if __name__ == "__main__":
    order = Order()
    order.create_order()
    order.add_user_id("123456")
    order.add_products(["Apple", "Samsung"])
    order.add_payment("PyOal")
    print(order.order_id, order.payment, order.products, order.user_id)
