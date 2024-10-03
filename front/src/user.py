from dataclasses import dataclass

from interfaces import IUser


@dataclass
class User(IUser):
    
    def add_product_cart(self, product):
        return super().add_product_cart(product)
    
    def checkout(self):
        return super().checkout()
    
    def remove_product_cart(self, product):
        return super().remove_product_cart(product)
    
    def create_user_id(self):
        return super().create_user_id()
