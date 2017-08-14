from abc import abstractmethod
from core.utils.authentication.exceptions.AuthenticationException import AuthenticationException
from core.utils.selenium.WebDriverChecker import WebDriverChecker


class FormLoginComponent(object):
    """
    FormLoginComponent
    ...
    """
    COOKIE_REMENC = 'remenc'
    REMEMBER_ME = True

    def __init__(self,
                 web_driver,
                 email_input_css_selector,
                 password_input_css_selector,
                 submit_loginform_css_selector,
                 remember_me_checkbox_css_selector=None,
                 web_driver_checker=None
                 ):
        """
        FormLoginComponent construct.
        :param web_driver: selenium.webdriver
        :param email_input_css_selector: string e.g "input[id='email']"
        :param password_input_css_selector: string
        :param submit_loginform_css_selector: string
        :param remember_me_checkbox_css_selector: string
        """
        self.web_driver = web_driver

        if web_driver_checker:
            self.web_driver_checker = web_driver_checker
        else:
            self.web_driver_checker = WebDriverChecker(web_driver)

        web_elements_css_selectors = [
            email_input_css_selector,
            password_input_css_selector,
            submit_loginform_css_selector
        ]

        if remember_me_checkbox_css_selector:
            web_elements_css_selectors.append(remember_me_checkbox_css_selector)

        self.__has_web_elements_or_raise_exception(web_elements_css_selectors)

        self.email_input_web_element = self.web_driver.find_element_by_css_selector(email_input_css_selector)
        self.password_input_web_element = self.web_driver.find_element_by_css_selector(password_input_css_selector)
        self.submit_form_web_element = self.web_driver.find_element_by_css_selector(submit_loginform_css_selector)

        if remember_me_checkbox_css_selector:
            self.remember_me_web_element\
                = self.web_driver.find_element_by_css_selector(remember_me_checkbox_css_selector)

    def __has_web_elements_or_raise_exception(self, web_elements_css_selectors):
        """
        __has_web_elements_or_raise_exception
        :param web_elements_css_selectors: []
        :return: void
        """
        for web_element_css_selector in web_elements_css_selectors:
            if not self.web_driver_checker.is_element_displayed_by_css(web_element_css_selector, timeout=2):
                raise AuthenticationException({
                    'error': {
                        'context': self.__class__,
                        'problem': web_element_css_selector + ' is not visible on the screen !',
                        'solution': 'Update the property value of ' + web_element_css_selector +
                                    ' to match the selector from the landing html template'
                    }
                })

    @abstractmethod
    def submit_login_form(self):
        """Submits login form"""

    @abstractmethod
    def input_email_address(self, email):
        """Set user email address"""

    @abstractmethod
    def input_password(self, password):
        """Set user password"""

    @abstractmethod
    def check_remember_me_checkbox(self, check_remember_me: bool):
        """Show loginform action"""

    def is_user_logged_or_raise_exception(self):
        if not self.web_driver_checker.driver_has_cookie(self.COOKIE_REMENC, timeout=5):
            raise AuthenticationException({
                'error': {
                    'context': self.__class__,
                    'problem': 'Login failed ! COOKIE ' + self.COOKIE_REMENC + ' was not set !',
                    'solution': ''
                }
            })
