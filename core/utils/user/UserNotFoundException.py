class UserNotFoundException(Exception):
    def __init__(self, args):
        Exception.__init__(self, 'ElementNotFoundException {0}'.format(args))