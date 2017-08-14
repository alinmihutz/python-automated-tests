class TestCaseConfiguration(object):
    def __init__(self, test_name, configuration):
        self.__name = test_name
        self.__executable = configuration['executable']
        self.__driver = configuration['driver']
        self.__environment = configuration['environment']

    @property
    def name(self):
        return self.__name

    @property
    def executable(self):
        return self.__executable

    @property
    def driver(self):
        return self.__driver

    @property
    def environment(self):
        return self.__environment

    def set_environment(self, env):
        self.__environment = env

    def set_driver(self, driver):
        self.__driver = driver

    def set_executable(self, exeClass):
        self.__executable = exeClass

    def set_name(self, name):
        self.__name = name
