import os
from core.TestCase import TestCase
from core.TestCaseConfiguration import TestCaseConfiguration
from core.utils.configuration.ConfigurationLoader import ConfigurationLoader


class TestCaseFactory(object):
    @staticmethod
    def load(test_case_configuration_file_path):
        test_cases = []
        test_configurations = ConfigurationLoader.load_configuration_file_contents(test_case_configuration_file_path)

        for test_name, test_case_configuration in test_configurations.items():
            if (
                TestCaseFactory.__is_test_defined(test_name) and
                TestCaseFactory.__is_test_enabled(test_case_configuration)
            ):
                test_case_configuration = TestCaseConfiguration(
                    test_name=test_name,
                    configuration=ConfigurationLoader.load_test_case_specific_configuration(test_name)
                )

                test_cases.append(TestCase(test_case_configuration))

        return test_cases

    @staticmethod
    def __is_test_defined(test_name):
        full_test_path = os.path.abspath('../../tests/' + test_name)
        if os.path.isdir(full_test_path):
            return True
        return False
    
    @staticmethod
    def __is_test_enabled(test_configuration):
        key = 'status'
        if key in test_configuration:
            status = test_configuration[key]
            if 'enabled' == status:
                return True
            return False
        else:
            return False
