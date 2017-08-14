from yaml.loader import Loader
import yaml
import os


class ConfigurationLoader(object):
    @staticmethod
    def load_configuration_file_contents(configuration_file_path):
        with open(configuration_file_path, 'r') as f:
            configurations = yaml.load(f, Loader=Loader)

            return configurations

    @staticmethod
    def load_test_case_specific_configuration(test_case):
        test_specific_configuration_file_path = os.path.abspath(
            '../../tests/' + test_case + '/resources/configuration/configuration.yml')

        with open(test_specific_configuration_file_path, 'r') as f:
            test_specific_configuration = yaml.load(f, Loader=Loader)

            return test_specific_configuration
