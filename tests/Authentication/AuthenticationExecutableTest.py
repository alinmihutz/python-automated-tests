from core.executable.ExecutableTest import ExecutableTest
from core.utils.authentication.exceptions.AuthenticationException import AuthenticationException
from core.utils.authentication.landings.AventadorLanding import AventadorLanding
from core.utils.authentication.landings.LandingFactory import LandingFactory
from core.utils.resources.UrlFactory import UrlFactory
from core.utils.user.UserFactory import UserFactory
from core.utils.user.UserNotFoundException import UserNotFoundException


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

        user_factory = UserFactory()

        fail_args = []

        for site_domain in self.work_item.external_resources['sites']:
            test_sites = self.work_item.external_resources['sites'][site_domain]
            for test_site in test_sites:
                site_brand = test_site['brand']
                site_url = UrlFactory.construct_url(
                    self.environment.preHost,
                    test_site['site'] + '.' + site_domain,
                    self.environment.postHost
                )

                self.web_driver.get(site_url)
                self.web_driver.maximize_window()
                self.web_driver.delete_all_cookies()

                authentication_landing = self.get_authentication_landing(site_domain, site_brand)

                if isinstance(authentication_landing, AventadorLanding):
                    try:
                        user = user_factory.create_man_looking_for_woman_user(
                            self.work_item.external_resources['users']
                        )
                        authentication_landing.pre_login()
                        authentication_landing.login(user)
                    except AuthenticationException as ex:
                        fail_args.append({site_url: ex.args})
                        continue
                    except UserNotFoundException as ex:
                        self.fail(ex.args)
                else:
                    self.fail('Unknown landing: authentication/landings/' + site_domain + '/' + site_brand)

        if len(fail_args) > 0:
            self.fail(fail_args)

    def get_authentication_landing(self, domain, brand):
        return LandingFactory.create_landing(self.web_driver, domain, brand)
