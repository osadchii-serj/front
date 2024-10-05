from dataclasses import dataclass

from interfaces import IDelivery


@dataclass
class Delivery(IDelivery):

    address: str
    status = False
    price = .100

    def delivery(self):
        if self.address:
            self.status = True
            return self.address, self.price, self.status
        return self.status


if __name__ == "__main__":
    delivery = Delivery("Moscow, Krasnoarmeyskaya 23", 100)
    print(delivery.delivery())
