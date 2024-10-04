from dataclasses import dataclass

from interfaces import IPayment

from order import Order

from typing import List


@dataclass
class Payment(IPayment):

    payment_system = None
    payment_id = None
    order = None
    amount = 0

    def add_payment_system(self, payment_system: str):
        self.payment_system = payment_system

    def create_payment_id(self):
        self.payment_id = id(self)

    def add_order(self, order: Order):
        self.order = order

    def calculate(self, list_prices: List[int | float]):
        return sum(list_prices)

    def process_payment(self):
        return super().process_payment()


if __name__ == "__main__":
    p = Payment()
    p.add_payment_system("PyPal")
    p.create_payment_id()
    p.add_order("1234567")
    print(p.payment_system, p.payment_id, p.order)
    print(p.calculate([123, 345, 132.345]))
