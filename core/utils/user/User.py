class User(object):
    """
    User entity
    """
    def __init__(self, email_address, password, brand):
        """
        User class construct
        :param email_address: string
        :param password: string
        :param brand: string
        """
        self.__password = password
        self.__email_address = email_address
        self.__brand = brand

    def get_email_address(self):
        return self.__email_address

    def get_password(self):
        return self.__password

    def get_brand(self):
        return self.__brand

    def deserialize(self):
        return {
            'email': self.__email_address,
            'password': self.__password,
            'brand': self.__brand
        }
