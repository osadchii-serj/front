from dataclasses import dataclass

from interfaces import IPayment


@dataclass
class Payment(IPayment):

    payment_system = None
    payment_id = None
    order = None
    user = None
    status = False

    def process_payment(self):
        if self.user.balance >= self.order.calculate_amount():
            self.status = True

    def payment_receipt(self):
        print(f"Платёжная система: {self.payment_system}")
        print(f"Чек № {self.payment_id}")
        print(f"Статус: {self.status}")


if __name__ == "__main__":
    p = Payment()
