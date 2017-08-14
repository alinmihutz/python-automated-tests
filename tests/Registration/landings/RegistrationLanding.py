from abc import abstractmethod
from selenium import webdriver
from core.utils.selenium.WebDriverChecker import WebDriverChecker
from tests.Registration.entities.Registration import Registration


class RegistrationLanding(object):
    def __init__(self, web_driver: webdriver, registration: Registration):
        self.web_driver = web_driver
        self.registration = registration
        self.select_location_attempt = 1
        self.web_driver_checker = WebDriverChecker(web_driver)

    @abstractmethod
    def select_kvk(self):
        """Sets the user kvk."""

    @abstractmethod
    def submit_registration_form(self):
        """Submit registration form"""

    @abstractmethod
    def select_birth_date(self):
        """Sets the user birth date."""

    @abstractmethod
    def select_location(self, attempt):
        """Sets the user location."""

    @abstractmethod
    def set_user_information(self):
        """Sets the user nickname, email, password, etc.."""

    def is_element_present_by_id(self, element_id, timeout=10):
        return self.web_driver_checker.is_element_present_by_id(element_id, timeout)

    def is_element_present_by_class(self, element_class, timeout=10):
        return self.web_driver_checker.is_element_present_by_class(element_class, timeout)

    def is_element_visible_by_css(self, css_selector, timeout=1):
        return self.web_driver_checker.is_element_visible_by_css(css_selector, timeout)

    def is_element_displayed_by_css(self, css_selector, timeout=10):
        return self.web_driver_checker.is_element_displayed_by_css(css_selector, timeout)

    def is_element_present_by_xpath(self, x_path, timeout=10):
        return self.web_driver_checker.is_element_present_by_xpath(x_path, timeout)

    def element_has_class(self, css_selector, class_name, timeout=3):
        return self.web_driver_checker.element_has_class(css_selector, class_name, timeout)

    def driver_has_cookie(self, cookie_name, timeout=3):
        return self.web_driver_checker.driver_has_cookie(cookie_name, timeout)

    def get_kvk_code_value(self):
        return {
            'mw': self.registration.kvk_mw,
            'wm': self.registration.kvk_wm,
            'ww': self.registration.kvk_ww,
            'mm': self.registration.kvk_mm,
        }.get(self.registration.kvk, '12')

    def get_kvk_code_value_by_kvk(self, kvk):
        return {
            'man': self.registration.kvk_man_code,
            'woman': self.registration.kvk_woman_code
        }.get(kvk, None)
