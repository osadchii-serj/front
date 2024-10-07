from shopping_facade import ShoppingFacade

from icecream import ic


def client_code(
    shop: ShoppingFacade,
    product_name: str,
    product_price: str,
    name_user: str,
    email_user: str,
    password_user: str,
    balance: int | float
):
    shop.create_product(product_name, product_price)
    shop.send_product_warehouse()
    shop.count_product_warehouse()
    shop.get_product_warehouse(100)
    shop.create_user(name_user, email_user, password_user)
    shop.user.add_money(balance)



if __name__ == "__main__":
    shop = ShoppingFacade()
    petro = client_code(shop, "NokiaX200", 34.999, "Петров", "petrov@mail.ru", "petro231!@QW", 50324)
    sidon = client_code(shop, "NokiaX200", 34.999, "Сидоров", "sidorov@mail.ru", "sidon!@QW", 43500)
    tatiana = client_code(shop, "AstrLinux", 57.399, "Татьяна", "tatyana@mail.ru", "tatiana200@QW", 102345)
    ivanov = client_code(shop, "HuaweiNetPro500", 44.999, "Иванов", "ivanov@mail.ru", "ivanov1!@QW", 87329)
