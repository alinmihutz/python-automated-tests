from core.TestCaseConfiguration import TestCaseConfiguration
from core.utils.ClassLoader import ClassLoader


class TestCase(object):
    """
    App TestCase class
    ...
    """
    def __init__(self, test_case_configuration: TestCaseConfiguration):
        """
        TestCase class construct.
        :param test_case_configuration: TestCaseConfiguration
        """
        self.__test_configuration = test_case_configuration
        self.__executable_class_namespace = ClassLoader.get_class(test_case_configuration.executable)

    def test_configuration(self):
        """
        Get TestCaseConfiguration[]
        :return: TestCaseConfiguration[]
        """
        return self.__test_configuration

    def executable_class_namespace(self):
        """
        Returns test executable namespace
        :return: class example: <class 'tests.Authentication.AuthenticationExecutableTest.AuthenticationExecutableTest'>
        """
        return self.__executable_class_namespace

    def executable_class(self):
        return self.__executable_class_namespace()

