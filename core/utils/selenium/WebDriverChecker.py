from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from core.utils.selenium.WaitForElementToHaveClassCondition import WaitForElementToHaveClassCondition
from core.utils.selenium.WaitUntilBrowserHasCookieCondition import WaitUntilBrowserHasCookieCondition


class WebDriverChecker(object):
    """
    WebDriverChecker
    """
    def __init__(self, web_driver: webdriver):
        self.web_driver = web_driver

    def is_element_present(self, web_element, timeout):
        """
        Returns true if the web_element WebElement is present in the DOM or false otherwise
        :param web_element: WebElement
        :param timeout: 
        :return: boolean
        """
        try:
            WebDriverWait(self.web_driver, timeout).until(web_element)
            return True
        except TimeoutException:
            return False

    def is_element_present_by_id(self, element_id, timeout=10):
        """
        Returns true if the element with the id 'element_id' exists in DOM or false otherwise
        :param element_id: string
        :param timeout: int
        :return: boolean
        """
        return self.is_element_present(
            EC.presence_of_element_located((By.ID, str(element_id))),
            timeout
        )

    def is_element_present_by_class(self, element_class, timeout=10):
        """
        Returns true if the element with the class 'element_class' exists in DOM or false otherwise
        :param element_class: string
        :param timeout: int
        :return: boolean
        """
        return self.is_element_present(
            EC.presence_of_element_located((By.CLASS_NAME, str(element_class))),
            timeout
        )

    def is_element_visible_by_css(self, css_selector, timeout=1):
        """
        Returns true if the element identified by 'css_selector' is present in the visible DOM or false otherwise
        :param css_selector: string
        :param timeout: int
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.web_driver, timeout)
            wait.until(lambda driver: self.web_driver.find_element_by_css_selector(css_selector))
            return True
        except TimeoutException:
            return False

    def is_element_displayed_by_css(self, css_selector, timeout=10):
        """
        Returns true if the element identified by 'css_selector' is displayed in the visible DOM or false otherwise
        :param css_selector: string
        :param timeout: int
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.web_driver, timeout)
            wait.until(lambda driver: self.web_driver.find_element_by_css_selector(css_selector).is_displayed())
            return True
        except TimeoutException:
            return False

    def is_element_present_by_xpath(self, x_path, timeout=10):
        """
        Returns true if the element identified by 'x_path' is present or false otherwise
        :param x_path: string
        :param timeout: int
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.web_driver, timeout)
            wait.until(lambda driver: self.web_driver.find_element(By.XPATH, x_path))
            return True
        except TimeoutException:
            return False

    def element_has_class(self, css_selector, class_name, timeout=3):
        """
        Returns true if the element identified by 'css_selector' has the class 'class_name' or false otherwise
        :param css_selector: string
        :param class_name: string
        :param timeout: int
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.web_driver, timeout)
            wait.until(WaitForElementToHaveClassCondition(css_selector, class_name))
            return True
        except TimeoutException:
            return False

    def driver_has_cookie(self, cookie_name, timeout=3):
        """
        Returns true if the WebDriver has the cookie 'cookie_name' or false otherwise
        :param cookie_name: string
        :param timeout: int
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.web_driver, timeout)
            wait.until(WaitUntilBrowserHasCookieCondition(cookie_name))
            return True
        except TimeoutException:
            return False
