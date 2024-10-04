from dataclasses import dataclass

from interfaces import IWarehouse

from product import Product


@dataclass
class Warehouse(IWarehouse):

    def add_product(self, product):
        if product.name not in self.warehouse:
            self.warehouse.update(
                {
                    product.name: [
                        product,
                    ]
                }
            )
        elif product.name in self.warehouse:
            self.warehouse[product.name].append(product)

    def remove_product(self, product):
        if product.name in self.warehouse:
            self.warehouse[product.name].remove(product)

    def count_products(self, product):
        if product.name in self.warehouse:
            return len(self.warehouse[product.name])

    def get_products(self, product, quantity):
        return self.warehouse[product.name][0:quantity]


if __name__ == "__main__":
    warehouse = Warehouse()
    phone = Product("Apple", 1232).create_product()
    TV = Product("Samsung", 3000).create_product()
    computer = Product("Lenovo", 15.500).create_product()
    warehouse.add_product(phone)
    warehouse.add_product(TV)
    warehouse.add_product(computer)
    warehouse.add_product(phone)
    warehouse.add_product(TV)
    warehouse.add_product(computer)
    print(warehouse.warehouse)
    print(warehouse.count_products(phone))
    warehouse.remove_product(TV)
    print(warehouse.warehouse)
    print(warehouse.get_products(phone, 2))
