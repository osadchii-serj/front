from dataclasses import dataclass

from interfaces import IUser

from product import Product


@dataclass
class User(IUser):

    def add_product_cart(self, product):
        if product:
            self.cart.append(product)

    def add_money(self, sum_money: int | float):
        self.balance = sum_money

    def add_payment_system(self, payment_system: str):
        self.payment_system = payment_system

    def remove_product_cart(self, product):
        if product and product in self.cart:
            self.cart.remove(product)

    def create_user_id(self, user):
        self.user_id = id(user)


if __name__ == "__main__":
    user_1 = User("User_1", "user_@mail.ru", "user_password")
    user_1.create_user_id()
    product = Product("LapTop Dell", 20000).create_product()
    user_1.add_product_cart(product)
    print(
        user_1.user_name,
        user_1.user_email,
        user_1.user_password,
        user_1.user_id,
        user_1.cart,
    )
    user_1.remove_product_cart(product)
    print(
        user_1.user_name,
        user_1.user_email,
        user_1.user_password,
        user_1.user_id,
        user_1.cart,
    )
