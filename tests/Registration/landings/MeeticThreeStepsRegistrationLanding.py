import time
from abc import abstractmethod
from selenium.webdriver import ActionChains
from tests.Registration.landings.ElementNotFoundException import ElementNotFoundException
from tests.Registration.landings.RegistrationException import RegistrationException
from tests.Registration.landings.RegistrationLanding import RegistrationLanding


class MeeticThreeStepsRegistrationLanding(RegistrationLanding):
    INVALID_INPUT_ERR_CODE = 'REGISTRATION_INVALID_INPUT'
    ELEMENT_NOT_FOUND_ERR_CODE = 'REGISTRATION_DOM_ELEMENT_NOT_DISPLAYED'
    MAX_ATTEMPTS_REACHED_ERR_CODE = 'REGISTRATION_TOO_MANY_ATTEMPTS'
    NOT_LOGGED_ERR_CODE = 'REGISTRATION_NOT_LOGGED'

    VALIDATION_ICON_CLASS_NAME = 'validation-icon'

    @abstractmethod
    def complete_step_one(self):
        pass

    @abstractmethod
    def complete_step_two(self):
        pass

    @abstractmethod
    def complete_step_three(self):
        pass

    @abstractmethod
    def load_step_two(self):
        pass

    @abstractmethod
    def load_step_three(self):
        pass

    def select_kvk(self):
        pass

    def submit_registration_form(self):
        pass

    def set_user_information(self):
        pass

    def select_birth_date(self):
        pass

    def select_location(self, attempt):
        pass

    def lose_input_focus_to_check_value(self):
        ActionChains(self.web_driver).move_by_offset(0, 0).click().perform()

    def wait_and_close_lara_bot_if_displayed(self, timeout=0.5):
        time.sleep(timeout)
        ActionChains(self.web_driver).move_by_offset(0, 0).click().perform()

    def is_user_logged_or_raise_err(self, timeout=15):
        if not self.driver_has_cookie('remenc', timeout):
            raise RegistrationException({
                'error': {
                    'code': self.NOT_LOGGED_ERR_CODE,
                    'detail': 'Registration failed ! remenc cookie is not set ' + str(self.registration.deserialize())
                }
            })

    def is_input_field_value_valid_or_raise_err(self, css_selector, value, timeout=3, message=None):
        if not self.element_has_class(css_selector, self.VALIDATION_ICON_CLASS_NAME, timeout):
            if message:
                err_message = message
            else:
                err_message = 'Invalid input value \'' + value + '\' for \'' + css_selector + '\' !'

            raise RegistrationException({
                'error': {
                    'code': self.INVALID_INPUT_ERR_CODE,
                    'detail': err_message
                }
            })

        return True

    def is_element_on_screen_or_raise_err(self, css_selector, timeout=10):
        if not self.is_element_displayed_by_css(css_selector, timeout):
            raise ElementNotFoundException({
                'error': {
                    'code': self.ELEMENT_NOT_FOUND_ERR_CODE,
                    'detail': 'Element \\' + css_selector + '\' was not displayed on screen !'
                }
            })

        return True

    def attempt_action_or_raise_err(self, action, current_attempt, max_attempts):
        if current_attempt > max_attempts:
            raise RegistrationException({
                'error': {
                    'code': self.MAX_ATTEMPTS_REACHED_ERR_CODE,
                    'detail': 'Too many attempts to \\' + action + '\' . Max attempts is \'' + max_attempts + '\''
                }
            })
