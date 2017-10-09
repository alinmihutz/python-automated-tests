from core.executable.ExecutableTest import ExecutableTest
from core.utils.authentication.exceptions.AuthenticationException import AuthenticationException
from core.utils.authentication.landings.AventadorLanding import AventadorLanding
from core.utils.authentication.landings.LandingFactory import LandingFactory


class AuthenticationExecutableTest(ExecutableTest):
    """
    AuthenticationExecutableTest
    ...
    """
    TEST_NAME = 'Authentication'

    def setUp(self):
        ExecutableTest.setUp(self)

    def tearDown(self):
        ExecutableTest.tearDown(self)

    def test_authentication(self):
        """
        test_authentication
        :return: void
        """

        fail_args = []

        for site_domain in self.work_item.external_resources['sites']:
            test_sites = self.work_item.external_resources['sites'][site_domain]
            for test_site in test_sites:
                site_brand = test_site['brand']
                site_url = ExecutableTest.get_test_url(self, test_site['site'], site_domain)

                self.web_driver.get(site_url)
                self.web_driver.maximize_window()
                self.web_driver.delete_all_cookies()

                authentication_landing = self.get_authentication_landing(site_domain, site_brand)

                if isinstance(authentication_landing, AventadorLanding):
                    try:
                        authentication_landing.pre_login()
                        authentication_landing.login(self.user)
                    except AuthenticationException as ex:
                        fail_args.append({site_url: ex.args})
                        continue
                else:
                    self.fail('Unknown landing: authentication/landings/' + site_domain + '/' + site_brand)

        if len(fail_args) > 0:
            self.fail(fail_args)

    def get_authentication_landing(self, domain, brand):
        return LandingFactory.create_landing(self.web_driver, domain, brand)
