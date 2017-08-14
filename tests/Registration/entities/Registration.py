class Registration(object):
    def __init__(self, registration_data):
        self.__landing = registration_data['landing']
        self.__kvk = registration_data['kvk']
        self.__age = registration_data['age']
        self.__birth_day = registration_data['birth_day']
        self.__birth_month = registration_data['birth_month']
        self.__birth_year = registration_data['birth_year']
        self.__ville = registration_data['ville']
        self.__pseudo = registration_data['pseudo']
        self.__email = registration_data['email']
        self.__password = registration_data['password']
        self.__kvk_wm = registration_data['kvk_wm']
        self.__kvk_mw = registration_data['kvk_mw']
        self.__kvk_ww = registration_data['kvk_ww']
        self.__kvk_mm = registration_data['kvk_mm']
        self.__kvk_man_code = registration_data['kvk_man_code']
        self.__kvk_woman_code = registration_data['kvk_woman_code']
        self.__kvk_profile = registration_data['kvk_profile']
        self.__kvk_search = registration_data['kvk_search']

    def deserialize(self):
        return {
            'landing': self.__landing,
            'kvk': self.__kvk,
            'kvk_profile': self.__kvk_profile,
            'kvk_search': self.__kvk_search,
            'age': self.__age,
            'birth_day': self.__birth_day,
            'birth_month': self.__birth_month,
            'birth_year': self.__birth_year,
            'ville': self.__ville,
            'pseudo': self.__pseudo,
            'email': self.__email,
            'password': self.__password
        }

    @property
    def landing(self):
        return self.__landing

    @property
    def kvk(self):
        return self.__kvk

    @property
    def kvk_profile(self):
        return self.__kvk_profile

    @property
    def kvk_search(self):
        return self.__kvk_search

    @property
    def age(self):
        return self.__age

    @property
    def birth_day(self):
        return self.__birth_day

    @property
    def birth_month(self):
        return self.__birth_month

    @property
    def birth_year(self):
        return self.__birth_year

    @property
    def ville(self):
        return self.__ville

    @property
    def pseudo(self):
        return self.__pseudo

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def kvk_wm(self):
        return self.__kvk_wm

    @property
    def kvk_mw(self):
        return self.__kvk_mw

    @property
    def kvk_ww(self):
        return self.__kvk_ww

    @property
    def kvk_mm(self):
        return self.__kvk_mm

    @property
    def kvk_man_code(self):
        return self.__kvk_man_code

    @property
    def kvk_woman_code(self):
        return self.__kvk_woman_code
