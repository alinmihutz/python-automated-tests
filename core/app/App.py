import os
import unittest
from core.TestCase import TestCase
from core.TestCaseFactory import TestCaseFactory
from core.executable.ExecutableTest import ExecutableTest
import HtmlTestRunner


class App(object):
    """
    App
    """

    def __init__(self):
        """
        App constructor.
        """
        test_case_factory = TestCaseFactory()

        self.test_cases_configuration_file_path = os.path.abspath('../resources/configuration/test_cases.yml')
        self.test_cases = test_case_factory.load(self.test_cases_configuration_file_path)

    def run(self):
        """
        Runs Test suite, generates HTML and XML reports
        :return: void
        """
        test_runner = HtmlTestRunner.HTMLTestRunner(self.__get_output())

        test_runner.run(self.__get_executable_test_suite())

    def _get_app_test_case_by_name(self, name):
        """
        Returns a TestCase if found or None otherwise
        :param name: string
        :return: TestCase
        """
        for test_case in self.test_cases:
            test_conf = test_case.test_configuration()
            if name == test_conf.name:
                return test_case

        return None

    def __get_executable_test_suite(self):
        """
        Returns the TestSuite and all TestCases for all tests enabled in /core/resources/configuration/test_cases.yml
        :return: TestSuite
        """
        executable_tests = []

        for test_case in self.test_cases:
            if isinstance(test_case, TestCase):
                executable_test_case_obj = test_case.executable_class()
                if isinstance(executable_test_case_obj, ExecutableTest):
                    executable_class_namespace = test_case.executable_class_namespace()
                    tests_in_executable = unittest.TestLoader().loadTestsFromTestCase(executable_class_namespace)
                    executable_tests.append(tests_in_executable)

        return unittest.TestSuite(executable_tests)

    def __get_output(self):
        """
        Returns reports output
        Used by test runner to generate report files
        :return: dict 
        [
            {'tests.Authentication.AuthenticationExecutableTest.AuthenticationExecutableTest': '/prod/Authentication'},
            {'tests.Dateroulette.DaterouletteExecutableTest.DaterouletteExecutableTest': '/recette/Dateroulette'}
        ]
        """
        output = []

        for app_test_case in self.test_cases:
            env = app_test_case.test_configuration().environment
            test_name = app_test_case.test_configuration().name
            suite_name = app_test_case.test_configuration().executable

            output.append({suite_name: '/' + env + '/' + test_name})

        return output
