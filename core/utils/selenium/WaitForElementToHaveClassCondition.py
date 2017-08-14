class WaitForElementToHaveClassCondition(object):
    def __init__(self, css_selector, class_name):
        self.css_selector = css_selector
        self.class_name = class_name

    def __call__(self, driver):
        element = driver.find_element_by_css_selector(self.css_selector)

        if self.class_name in element.get_attribute('class'):
            return True
        else:
            return False
