from core.resources.InvalidExternalResourceException import InvalidExternalResourceException
from yaml.loader import Loader
import os
import yaml


class ExternalResourceLoader(object):
    @staticmethod
    def load(resource_name, test_name):
        resource = ExternalResourceLoader.__load_from_custom_build_config(resource_name)

        if resource:
            return resource

        return ExternalResourceLoader.__load_generic_yaml(test_name, resource_name)

    @staticmethod
    def get_custom_config():
        path_to_custom_config_resource = os.path.abspath('../app/build/custom_build_config.yml')
        if os.path.isfile(path_to_custom_config_resource):
            with open(path_to_custom_config_resource, 'r') as f:
                return yaml.load(f, Loader=Loader)

        return None

    @staticmethod
    def __load_from_custom_build_config(resource_name):
        custom_build_config_values = ExternalResourceLoader.get_custom_config()
        if custom_build_config_values:
            if resource_name in custom_build_config_values:
                dict_values = {}
                for value in custom_build_config_values[resource_name]:
                    dict_values.update(value)

                return dict_values

        return None

    @staticmethod
    def __load_generic_yaml(test_name, file_name):
        path = None

        path_to_resource = os.path.abspath('../resources/' + file_name + '.yml')
        path_to_test_resource = os.path.abspath('../../tests/' + test_name + '/resources/' + file_name + '.yml')

        if os.path.isfile(path_to_test_resource):
            path = path_to_test_resource
        else:
            if os.path.isfile(path_to_resource):
                path = path_to_resource
            else:
                raise InvalidExternalResourceException(
                    'File ' + file_name + '.yml does not exists (neither in CORE nor in test ' + test_name + '!'
                )

        with open(path, 'r') as f:
            config_values = yaml.load(f, Loader=Loader)
            return config_values
