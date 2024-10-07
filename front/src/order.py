from dataclasses import dataclass

from interfaces import IOrder

from typing import List


@dataclass
class Order(IOrder):

    order_id = None
    user_id = None
    user = None
    products = None
    payment = None
    delivery = None
    delivery_price = 0
    amount = 0

    def create_order(self):
        self.create_order_id()
        print(f"Заказ № {self.order_id}")
        print(f"Пользователь: {self.user_id}")
        print(f"Платёжная система: {self.payment}")
        print(f"Продукты: {self.products}")
        print(f"Сумма к оплате: {self.calculate_amount()}")


    def create_order_id(self):
        self.order_id = id(f"{self}")

    def add_user_id(self, user_id: object):
        self.user_id = user_id

    def add_products(self, products: List[str]):
        self.products = products

    def add_payment(self, payment: str):
        self.payment = payment

    def add_user(self, user):
        self.create_order_id()
        self.user = user

    def calculate_amount(self):
        return round(self.amount + self.delivery_price, 3)


if __name__ == "__main__":
    order = Order()
    order.create_order()
    order.add_user_id("123456")
    order.add_products(["Apple", "Samsung"])
    order.add_payment("PyPal")
    print(order.order_id, order.payment, order.products, order.user_id)
