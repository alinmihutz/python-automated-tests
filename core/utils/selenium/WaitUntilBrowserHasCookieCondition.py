class WaitUntilBrowserHasCookieCondition(object):
    def __init__(self, cookie_name):
        self.cookie_name = cookie_name

    def __call__(self, driver):
        cookie_exists = False

        for cookie in driver.get_cookies():
            if cookie['name'] == self.cookie_name:
                cookie_exists = True
                break

        return cookie_exists
