class AuthenticationException(Exception):
    def __init__(self, args):
        Exception.__init__(self, 'AuthenticationException {0}'.format(args))
