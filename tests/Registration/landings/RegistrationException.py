class RegistrationException(Exception):
    def __init___(self, err_arguments):
        Exception.__init__(self, 'RegistrationException {0}'.format(err_arguments))
        self.__err_arguments = err_arguments

    def get_err_arguments(self):
        print(self.__err_arguments)
        return self.__err_arguments
