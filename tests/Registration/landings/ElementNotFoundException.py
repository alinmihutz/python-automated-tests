class ElementNotFoundException(Exception):
    def __init___(self, err_arguments):
        Exception.__init__(self, 'ElementNotFoundException {0}'.format(err_arguments))
        self.__err_arguments = err_arguments

    @property
    def err_arguments(self):
        return self.__err_arguments
