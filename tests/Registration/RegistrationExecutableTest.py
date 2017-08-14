from core.executable.ExecutableTest import ExecutableTest
from core.utils.resources.UrlFactory import UrlFactory
from tests.Registration.entities.Registration import Registration
from tests.Registration.landings.MeeticRegistrationLanding import MeeticRegistrationLanding
from tests.Registration.landings.RegistrationException import RegistrationException
from tests.Registration.landings.RegistrationLanding import RegistrationLanding
from tests.Registration.landings.MeeticThreeStepsRegistrationLanding import MeeticThreeStepsRegistrationLanding


class RegistrationExecutableTest(ExecutableTest):
    TEST_NAME = 'Registration'

    def setUp(self):
        ExecutableTest.setUp(self)
        self.registration = Registration(self.work_item.external_resources['registration'])

    def tearDown(self):
        self.web_driver.quit()

    def test_registration(self):
        for site_locale in self.work_item.external_resources['sites']:
            test_sites = self.work_item.external_resources['sites'][site_locale]
            for test_site in test_sites:
                site_url = UrlFactory.construct_url(
                    self.environment.preHost,
                    test_site['site'] + '.' + site_locale,
                    self.environment.postHost
                )

                self.web_driver.get(site_url)
                self.web_driver.maximize_window()

                landing = self.get_registration_landing()

                if isinstance(landing, MeeticThreeStepsRegistrationLanding):
                    try:
                        landing.complete_step_one()
                        landing.load_step_two()
                        landing.complete_step_two()
                        landing.load_step_three()
                        landing.complete_step_three()
                        landing.submit_registration_form()
                        landing.is_user_logged_or_raise_err()
                    except RegistrationException as ex:
                        self.web_driver.save_screenshot('RegistrationException.png')
                        self.fail('Check /workspace/RegistrationException.png')
                elif isinstance(landing, RegistrationLanding):
                    pass
                else:
                    self.fail('FAIL ! Registration landing not set or defined for ' + "'" + self.registration.landing + "'")

    def get_registration_landing(self):
        return {
            'Meetic': MeeticRegistrationLanding(self.web_driver, self.registration)
        }.get(self.registration.landing, None)
