from warehouse import Warehouse

from dataclasses import dataclass

from interfaces import IProduct


@dataclass
class Product(IProduct):

    def create_product(self):
        self.create_product_id()
        return type(
            self.product_name,
            (),
            {
                f"name": self.product_name,
                f"price": self.product_price,
                f"id": self.product_id,
            },
        )

    def create_product_id(self):
        self.product_id = id(self)


if __name__ == "__main__":
    product = Product("Huawei", 12.325).create_product()
    print(product)
    print(product.name)
    print(product.price)
    print(product.id)
