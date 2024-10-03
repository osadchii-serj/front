from dataclasses import dataclass

from interfaces import IUsersBase

from user import User


@dataclass
class UsersBase(IUsersBase):

    users_base = dict()

    def add_user(self, user: User):
        self.users_base.update(
            {
                user.user_name: {
                    type(
                        user.user_name,
                        (),
                        {
                            "name": user.user_name,
                            "email": user.user_email,
                            "password": user.user_password,
                            "user_id": user.user_id,
                            "cart": user.cart,
                        },
                    )
                }
            }
        )
        return f"Пользователь: {user.user_name} зарегистрирован"

    def user_search(self, user_name: str):
        if self.users_base.get(user_name):
            print(f"Найден пользователь: {user_name}")
            return self.users_base[user_name]
        return f"Нет пользователя {user_name} в базе"

    def delete_user(self, user_name: str):
        if self.users_base.get(user_name):
            del self.users_base[user_name]
            return f"Пользователь: {user_name} удалён из базы"
        return f"Нет пользователя {user_name} в базе"


if __name__ == "__main__":
    user_1 = User("User_1", "user_1@mail.ru", "user_1_password")
    ub = UsersBase()
    print(ub.add_user(user_1))
    print(ub.user_search(user_1.user_name))
    print(ub.delete_user(user_1.user_name))
    print(ub.users_base)
