# class Singleton:  # класс сделан по принципу Singleton -> будет существовать только один экземпляр класса
#                   # в этом подходе свойства экземпляра класса будут перезаписываться
#
#     __instance = None
#
#     # при подходе использования метакласса экземпляр класса окажется неизменяем
#     # def __call__(cls, *args, **kwargs):
#     #     if cls not in cls.__instance:
#     #         cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#     #     return cls.__instance[cls]
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls._instance = super().__new__(cls)
#         return cls.__instance
#
#
# class User(Singleton):  # класс "Пользователь"; в нем будут храниться ключи, с которыми осуществляются запросы к API
#
#     def __init__(self, credentials: str = None,
#                  user_id: int = None, username: str = None, apartment_id: int = None, contracts_id: list = None, payments_id: dict = None):
#         self.__credentials = credentials
#         self.__user_id = user_id
#         self.__username = username
#         self.__apartment_id = apartment_id
#         self.__contracts_id = contracts_id
#         self.__payments_id = payments_id
#
#     @property
#     def credentials(self) -> str:
#         return self.__credentials
#
#     @credentials.setter
#     def credentials(self, credentials: str) -> None:
#         self.__credentials = credentials
#
#     @property
#     def user_id(self) -> int:
#         return self.__user_id
#
#     @user_id.setter
#     def user_id(self, user_id: int) -> None:
#         self.__user_id = user_id
#
#     @property
#     def username(self) -> str:
#         return self.__username
#
#     @username.setter
#     def username(self, username: str) -> None:
#         self.__username = username
#
#     @property
#     def apartment_id(self) -> int:
#         return self.__apartment_id
#
#     @apartment_id.setter
#     def apartment_id(self, apartment_id: int) -> None:
#         self.__apartment_id = apartment_id
#
#     @property
#     def contracts_id(self) -> list:
#         return self.__contracts_id
#
#     @contracts_id.setter
#     def contracts_id(self, contracts_id: list) -> None:
#         self.__contracts_id = contracts_id
#
#     @property
#     def get_payments_id(self) -> dict:
#         return self.__payments_id
#
#
# # user1 = User()
# # print(user1)
# # print(user1.user_id)
# # print(user1.credentials)
# # # print(user1.get_apartment_id)
# # # print(user1.get_contracts_id)
# # # print(user1.get_payments_id)

# реализуем "МОНОСОСТОЯНИЕ" для того, чтобы иметь возможность обращаться к свойствам класса из разных его объектов
class User:
    __shared_properties = {
        'credentials': None,
        'user_id': None,
        'username': None,
        'apartments': None,
        'contracts': None,
        'payments': None
    }

    def __init__(self):
        self.__dict__ = User.__shared_properties
