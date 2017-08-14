from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory(object):
    """
    Web Driver Factory
    """
    DRIVER_CHROME = '../drivers/chromedriver'
    DRIVER_IE = '../drivers/ieDriver'

    @staticmethod
    def get_driver_instance(driver_name):
        """
        Returns a WebDriver
        :param driver_name: string e.g PhantomJs
        :return: selenium.webdriver
        """
        driver = None

        driver_name = driver_name.upper()

        if 'CHROME' == driver_name:
            options = Options()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--disable-extensions')
            driver = webdriver.Chrome(DriverFactory.DRIVER_CHROME, chrome_options=options)
        elif 'IE' == driver_name:
            capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
            capabilities['acceptSslCerts'] = True
            driver = webdriver.Ie(DriverFactory.DRIVER_IE, capabilities=capabilities)
        elif 'PHANTOMJS' == driver_name:
            driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
        else:
            driver = webdriver.Chrome()

        return driver
