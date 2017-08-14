from abc import abstractmethod

from core.utils.authentication.components.WebDriverLoginComponent import WebDriverLoginComponent
from core.utils.authentication.exceptions.AuthenticationException import AuthenticationException
from core.utils.selenium.WebDriverChecker import WebDriverChecker
from core.utils.user.User import User


class AventadorLanding(object):
    _show_loginform_css_selector = None
    _show_loginform_link_text = None
    _email_input_css_selector = "input[type='email']"
    _password_input_css_selector = "input[id='pwd']"
    _submit_loginform_css_selector = "button[regform-dryrun='login']"
    _remember_me_checkbox_css_selector = "input[id='remember_me']"

    """
    AventadorLanding
    ...
    """
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.web_driver_checker = WebDriverChecker(web_driver)

    def login(self, user: User):
        """Login action"""

        form_login_component = WebDriverLoginComponent(
            self.web_driver,
            self._email_input_css_selector,
            self._password_input_css_selector,
            self._submit_loginform_css_selector,
            self._remember_me_checkbox_css_selector
        )

        form_login_component.input_email_address(user.get_email_address())
        form_login_component.input_password(user.get_password())
        form_login_component.check_remember_me_checkbox()
        form_login_component.submit_login_form()
        form_login_component.is_user_logged_or_raise_exception()

    @abstractmethod
    def registration(self):
        """Registration action"""

    @abstractmethod
    def pre_login(self):
        """Pre Login action"""
        pass

    def _show_loginform_or_raise_error(self):
        if self._show_loginform_css_selector:
            if not self.web_driver_checker.is_element_displayed_by_css(self._show_loginform_css_selector, timeout=1):
                raise AuthenticationException({
                    'error': {
                        'context': self.__class__,
                        'problem': self._show_loginform_css_selector + ' is not visible on the screen !',
                        'solution': ''
                    }
                })

            self.web_driver.find_element_by_link_text(self._show_loginform_link_text).click()

        pass
