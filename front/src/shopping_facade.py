from dataclasses import dataclass

from warehouse import Warehouse
from users_base import UsersBase
from payment import Payment
from product import Product
from delivery import Delivery
from order import Order
from user import User

from logger import ShopLogger


from pprint import pprint


@dataclass
class ShoppingFacade:

    logger = ShopLogger("ShopLogger")

    user = None
    product = None
    order = Order()
    payment = Payment()
    users_base = UsersBase()
    warehouse = Warehouse()

    def create_product(self, product_name: str, product_price: int | float):
        product = Product(product_name, product_price)
        self.product = product.create_product()
        self.logger.log_info(f"Создан продукт: {product.product_name}")

    def send_product_warehouse(self):
        self.warehouse.add_product(self.product)
        self.logger.log_info(f"{self.product.name} - отправлен на склад {self.warehouse.warehouse}")

    def count_product_warehouse(self):
        counter_product = self.warehouse.count_products(self.product)
        self.logger.log_info(f"Количество: {self.product.name} на складе {counter_product}")

    def get_product_warehouse(self, quantity: int):
        product = self.warehouse.get_products(self.product, quantity)
        self.logger.log_info(f"Получен продукт со склада: {product}")

    def remove_product_warehouse(self):
        self.warehouse.remove_product(self.product)
        self.logger.log_info(f"Продукт: {self.product} удалён со склада")

    def create_user(self, name_user: str, email_user: str, password_user: str):
        self.user = User(name_user, email_user, password_user)
        self.user.create_user_id(self.user)
        self.logger.log_info(f"Создан пользователь: {self.user.user_name}")
        self.logger.log_info(f"Email: {self.user.user_email}")
        self.logger.log_info(f"Password: {self.user.user_password}")
        self.logger.log_info(f"user_id: {self.user.user_id}")

    def user_remove_product_cart(self, product: Product):
        self.user.remove_product_cart(product)
        self.logger.log_info(f"Продукт: {self.product} удалён из корзины")

    def user_base_add_user(self):
        self.users_base.add_user(self.user)
        self.logger.log_info(f"Пользователь: {self.user} добавлен в базу {self.users_base}")

    def order_add_user(self):
        self.order.add_user(self.user)
        self.logger.log_info(f"Создан заказ № {self.order.order_id} - пользователь: {self.user.user_name}")

    def order_add_user_id(self):
        self.order.add_user_id(self.user.user_id)

    def order_add_products(self):
        self.order.add_products(self.user.cart)
        self.logger.log_info(f"Продукт {self.product} добавлен в заказ")

    def order_add_amount_products(self):
        amount = 0
        for product in self.user.cart:
            amount = amount + product.price
        self.order.amount = amount

    def delivery_add_address(self, address):
        address = Delivery(address)
        if address.delivery():
            self.order.delivery = address.address
            self.order.delivery_price = address.price
            self.logger.log_info(f"Адрес - {self.order.delivery}")

    def create_payment(self):
        self.payment.payment_system = self.user.payment_system
        self.payment.payment_id = id(f"{self}")
        self.payment.order = self.order
        self.payment.user = self.user
        self.payment.process_payment()
        if self.payment.status:
            self.user.balance = self.user.balance - self.order.calculate_amount()
            self.logger.log_info(f"Сума заказа: {self.order.amount}")
        else:
            print("Недостаточно средств")


if __name__ == "__main__":
    shop = ShoppingFacade()
    shop.create_product("Lap-top Lenovo293", 25000.387)
    shop.send_product_warehouse()
    pprint(shop.count_product_warehouse())
    pprint(shop.get_product_warehouse(3))
    shop.remove_product_warehouse()
    pprint(shop.get_product_warehouse(3))
    pprint(shop.count_product_warehouse())
    shop.create_user("user_1", "user_1@mail.ru", "user_1password")
    pprint(shop.user)
    shop.user.create_user_id()
    pprint(shop.user.user_id)
    shop.user.add_product_cart(shop.product)
    pprint(shop.user.cart)
    shop.user.add_payment_system("Мир")
    pprint(shop.user.payment_system)
    shop.user.add_money(50000)
    pprint(shop.user.balance)
    # shop.user_remove_product_cart(shop.product)
    pprint(shop.user.cart)
    shop.user_base_add_user()
    pprint(shop.users_base)
    shop.order_add_user()
    pprint(shop.order.user)
    shop.order_add_user_id()
    pprint(shop.order.user_id)
    shop.order.create_order_id()
    pprint(shop.order.order_id)
    shop.order_add_products()
    pprint(shop.order.products)
    shop.order.add_payment(shop.user.payment_system)
    pprint(shop.order.payment)
    shop.order_add_amount_products()
    pprint(shop.order.amount)
    shop.delivery_add_address("Воронеж, ул. Первомайская 25 д 2 кв 8")
    print(shop.order.delivery, shop.order.delivery_price)
    shop.order.create_order()
    shop.create_payment()
    shop.payment.payment_receipt()
    print("Баланс: ", shop.user.balance)
