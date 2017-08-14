import os

from core.environment import Environment
from core.environment.EnvironmentFactory import EnvironmentFactory
from core.resources.ExternalResourceLoader import ExternalResourceLoader
from core.utils.configuration.ConfigurationLoader import ConfigurationLoader


class WorkItem(object):
    def __init__(self, test_name):
        self.__test_name = test_name
        self.__test_configuration = ConfigurationLoader.load_test_case_specific_configuration(self.__test_name)
        self.__custom_build_config = ExternalResourceLoader.get_custom_config()
        self.__environments = self.get_environments()
        self.__external_resources = {}
        self.__preScripts = {}
        self.__postScripts = {}

    @property
    def test_name(self):
        return self.__test_name

    @property
    def test_users(self):
        return self.__external_resources

    @property
    def test_configuration(self):
        return self.__test_configuration

    @property
    def external_resources(self):
        return self.__external_resources

    @property
    def environments(self):
        return self.__environments

    def environment(self, env) -> 'Environment':
        if self.__custom_build_config:
            if 'env' in self.__custom_build_config:
                return self.__environments[self.__custom_build_config['env']]

        return self.__environments[env]

    def load_external_resources(self):
        self.__external_resources['sites'] = ExternalResourceLoader.load('sites', self.test_name)
        self.__external_resources['users'] = ExternalResourceLoader.load('users', self.test_name)

        if 'external_resources' in self.__test_configuration:
            for file_name in self.__test_configuration['external_resources']:
                self.__external_resources[file_name] = ExternalResourceLoader.load(file_name, self.test_name)

    @staticmethod
    def get_environments():
        environments_configuration_file_path = os.path.abspath('../resources/configuration/environments.yml')
        return EnvironmentFactory.load(environments_configuration_file_path)
