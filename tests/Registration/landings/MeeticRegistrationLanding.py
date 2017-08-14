import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
from tests.Registration.landings.ElementNotFoundException import ElementNotFoundException
from tests.Registration.landings.MeeticThreeStepsRegistrationLanding import MeeticThreeStepsRegistrationLanding
from selenium.webdriver.common.by import By


class MeeticRegistrationLanding(MeeticThreeStepsRegistrationLanding):
    SELECT_LOCATION_MAX_ATTEMPTS = 2

    def complete_step_one(self):
        if self.is_element_visible_by_css("select[name='kvk_profile']"):
            self.select_kvk_profile_and_search()
        else:
            self.select_kvk()

        self.select_birth_date()

    def complete_step_two(self):
        try:
            self.select_location(self.select_location_attempt)
        except ElementNotFoundException as ex:
            self.select_location_attempt += 1
            self.load_step_two()
            self.select_location(self.select_location_attempt)

    def complete_step_three(self):
        self.set_user_information()

        if self.is_element_displayed_by_css("input[name='terms_check']", 1):
            self.web_driver.find_element_by_css_selector("input[name='terms_check']").click()

        if self.is_element_displayed_by_css("input[name='privacy_check']", 1):
            self.web_driver.find_element_by_css_selector("input[name='privacy_check']").click()

        if self.is_element_displayed_by_css("input[name='partners_offers']", 1):
            self.web_driver.find_element_by_css_selector("input[name='partners_offers']").click()

        if self.is_element_visible_by_css("select[name='survey']"):
            select = Select(self.web_driver.find_element_by_css_selector("select[name='survey']"))
            select.select_by_value('number:6')

    def submit_registration_form(self):
        x_path = '//*[text()="Confirmer"]'

        if self.is_element_present_by_xpath(x_path):
            next_step_btn = self.web_driver.find_element(By.XPATH, x_path)
            next_step_btn.click()

    def load_step_two(self):
        self.__load_next_step()

    def load_step_three(self):
        x_path = '//*[text()="Continuer"]'

        if self.is_element_present_by_xpath(x_path):
            next_step_btn = self.web_driver.find_element(By.XPATH, x_path)
            self.wait_and_close_lara_bot_if_displayed()
            next_step_btn.click()

    def set_user_information(self):
        self.__set_user_nickname()
        self.__set_user_email()
        self.__set_user_password()

    def select_birth_date(self):
        select_birth_date_day = Select(self.web_driver.find_element_by_name('birth_date_day'))
        select_birth_date_month = Select(self.web_driver.find_element_by_name('birth_date_month'))
        select_birth_date_year = Select(self.web_driver.find_element_by_name('birth_date_year'))

        select_birth_date_day.select_by_value(self.registration.birth_day)
        select_birth_date_month.select_by_value(self.registration.birth_month)
        self.wait_and_close_lara_bot_if_displayed()
        select_birth_date_year.select_by_value(self.registration.birth_year)

        self.is_input_field_value_valid_or_raise_err(
            "label[for='bday']",
            str(self.registration.birth_month + '-' + self.registration.birth_day + '-' + self.registration.birth_year)
        )

    def select_location(self, attempt):
        self.attempt_action_or_raise_err('select_location', attempt, self.SELECT_LOCATION_MAX_ATTEMPTS)

        css_selector = "input[name='geoPlace']"

        self.is_element_on_screen_or_raise_err(css_selector)

        for char in list(self.registration.ville):
            self.web_driver.find_element_by_css_selector(css_selector).send_keys(char)
            time.sleep(1)

        css_selector_places_list = "ul[class='google-places-api-autocomplete-list']"

        self.is_element_on_screen_or_raise_err(css_selector_places_list)

        google_places_list = self.web_driver.find_element_by_css_selector(css_selector_places_list)
        google_places = google_places_list.find_elements_by_tag_name('li')

        if len(google_places) > 0:
            google_places[0].click()

        self.is_input_field_value_valid_or_raise_err("label[for='geoPlace']", self.registration.ville)

    def select_kvk(self):
        select = Select(self.web_driver.find_element_by_name('kvk'))

        select.select_by_value(self.get_kvk_code_value())
        self.is_input_field_value_valid_or_raise_err("label[for='kvk']", self.get_kvk_code_value())

    def select_kvk_profile_and_search(self):
        kvk_profile_code = self.get_kvk_code_value_by_kvk(self.registration.kvk_profile)
        kvk_search_code = self.get_kvk_code_value_by_kvk(self.registration.kvk_search)

        kvk_profile_select = Select(self.web_driver.find_element_by_name('kvk_profile'))
        kvk_profile_select.select_by_value(str(kvk_profile_code))

        self.wait_and_close_lara_bot_if_displayed(timeout=1)

        kvk_search_select = Select(self.web_driver.find_element_by_name('kvk_search'))
        kvk_search_select.select_by_value(str(kvk_search_code))

        self.is_input_field_value_valid_or_raise_err("label[for='kvk_search']", kvk_search_code)
        self.is_input_field_value_valid_or_raise_err("label[for='kvk_profile']", kvk_profile_code)

    def __set_user_nickname(self):
        css_selector = "input[name='nickname']"

        self.is_element_on_screen_or_raise_err(css_selector)
        self.web_driver.find_element_by_css_selector(css_selector).send_keys(self.registration.pseudo)
        self.lose_input_focus_to_check_value()
        self.is_input_field_value_valid_or_raise_err("label[for='nickname']", self.registration.pseudo)

    def __set_user_email(self):
        css_selector = "input[name='email']"

        self.is_element_on_screen_or_raise_err(css_selector)
        self.web_driver.find_element_by_css_selector(css_selector).send_keys(self.registration.email)
        self.lose_input_focus_to_check_value()
        self.is_input_field_value_valid_or_raise_err(
            "label[for='email']",
            self.registration.email,
            timeout=3,
            message="Email address is invalid or already used !"
        )

    def __set_user_password(self):
        css_selector = "input[name='password']"

        self.is_element_on_screen_or_raise_err(css_selector)

        for char in list(self.registration.password):
            self.web_driver.find_element_by_css_selector(css_selector).send_keys(char)

        self.lose_input_focus_to_check_value()
        self.is_input_field_value_valid_or_raise_err(
            "label[ng-show='passwordStrength.strength == 3']",
            self.registration.password
        )

    def __load_next_step(self):
        next_step_btn = self.web_driver.find_element_by_css_selector("button[ng-disabled='activityIndicator']")
        try:
            next_step_btn.click()
        except WebDriverException as ex:
            self.wait_and_close_lara_bot_if_displayed(0)
            next_step_btn.click()
