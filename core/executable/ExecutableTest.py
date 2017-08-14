import os
import re
import unittest
from datetime import datetime

from core.utils.DriverFactory import DriverFactory
from core.utils.user.UserFactory import UserFactory
from core.worker.WorkItemFactory import WorkItemFactory


class ExecutableTest(unittest.TestCase):
    """
    Executable Test concrete class
    type unittest.TestCase
    """
    def setUp(self):
        """
        Load test configuration files, external resources & test environment, etc
        :return: void
        """
        work_item_factory = WorkItemFactory()
        user_factory = UserFactory()

        self.work_item = work_item_factory.create_work_item(self.get_test_name())
        self.web_driver = DriverFactory.get_driver_instance(self.work_item.test_configuration['driver'])
        self.environment = self.work_item.environment(self.work_item.test_configuration['environment'])
        self.user = user_factory.create_man_looking_for_woman_user(self.work_item.external_resources['users'])
        self.screenshots_reports_files_absolute_path = os.getcwd() + '/reports/screenshots/'
        self.timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    def tearDown(self):
        """
        Executes after all tests are done
        Close the browser
        :return: void
        """
        self.web_driver.quit()

    def get_test_name(self):
        """
        Splits the class name by upper letters and returns the prefix of the executable test class
        e.g TestnameExecutableTest => Testname
        :return: string
        """
        return re.findall('[A-Z][^A-Z]*', self.__class__.__name__)[0]
