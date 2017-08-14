from core.environment import Environment


class Login(object):
    __email_address = None
    __password = None
    __brand = None
    __type = None
    __environment = None
    __host = None

    def __init__(
        self,
        environment: Environment,
        email,
        password,
        host,
        brand='meetic',
        login_type='API',
    ):
        self.__environment = environment
        self.__email_address = email
        self.__password = password
        self.__brand = brand
        self.__type = login_type
        self.__host = '//www.' + str(host)

    def get_brand(self):
        return self.__brand

    def get_email(self):
        return self.__email_address

    def get_password(self):
        return self.__password

    def get_env(self):
        return self.__environment

    def get_type(self):
        return self.__type

    def get_host(self):
        return self.__host
