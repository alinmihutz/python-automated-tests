from core.resources.ExternalResourceLoader import ExternalResourceLoader
from core.utils.configuration.ConfigurationLoader import ConfigurationLoader
from core.environment.Environment import Environment


class EnvironmentFactory(object):
    @staticmethod
    def load(environments_configuration_file_path):
        environments = {}
        environment_configurations = ConfigurationLoader.load_configuration_file_contents(
            environments_configuration_file_path
        )

        custom_build_config = ExternalResourceLoader.get_custom_config()

        for environment_name, environment_configuration in environment_configurations.items():
            if custom_build_config:
                if 'api_user' in custom_build_config and 'env' in custom_build_config and 'prod' != custom_build_config['env']:
                    environment_configuration['preHost'] = custom_build_config['api_user']

            environments[environment_name] = EnvironmentFactory.__create_environment(
                environment_name,
                environment_configuration
            )
        
        return environments

    @staticmethod
    def __create_environment(environment_name, environment_configuration):
        return Environment(environment_name, environment_configuration)
