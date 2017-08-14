class Environment(object):
    def __init__(self, environmentName, environmentConfiguration):
        self.__name = environmentName
        if (environmentConfiguration['preHost'] is not None):
            self.__preHost = environmentConfiguration['preHost']
        else:
            self.__preHost = ''
        
        if (environmentConfiguration['postHost'] is not None):
            self.__postHost = environmentConfiguration['postHost']
        else:
            self.__postHost = ''

        self.__apiServiceUrl = environmentConfiguration['apiService']['url']
        self.__apiServiceUserName = environmentConfiguration['apiService']['userName']
        self.__apiServicePassword = environmentConfiguration['apiService']['password']
        self.__microServiceUrl = environmentConfiguration['microService']['url']
        self.__microServiceUserName = environmentConfiguration['microService']['userName']
        self.__microServicePassword = environmentConfiguration['microService']['password']
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def preHost(self):
        return self.__preHost
    
    @preHost.setter
    def preHost(self, preHost):
        self.__preHost = preHost
        
    @property
    def postHost(self):
        return self.__postHost
    
    @postHost.setter
    def postHost(self, postHost):
        self.__postHost = postHost
        
    @property
    def apiServiceUrl(self):
        return self.__apiServiceUrl
    
    @apiServiceUrl.setter
    def apiServiceUrl(self, apiServiceUrl):
        self.__apiServiceUrl = apiServiceUrl
        
    @property
    def apiServiceUserName(self):
        return self.__apiServiceUserName
    
    @apiServiceUserName.setter
    def apiServiceUserName(self, apiServiceUserName):
        self.__apiServiceUserName = apiServiceUserName
        
    @property
    def apiServicePassword(self):
        return self.__apiServicePassword
    
    @apiServicePassword.setter
    def apiServicePassword(self, apiServicePassword):
        self.__apiServicePassword = apiServicePassword
        
    @property
    def microServiceUrl(self):
        return self.__microServiceUrl
    
    @microServiceUrl.setter
    def microServiceUrl(self, microServiceUrl):
        self.__microServiceUrl = microServiceUrl
        
    @property
    def microServiceUserName(self):
        return self.__microServiceUserName
    
    @microServiceUserName.setter
    def microServiceUserName(self, microServiceUserName):
        self.__microServiceUserName = microServiceUserName
        
    @property
    def microServicePassword(self):
        return self.__microServicePassword
    
    @microServicePassword.setter
    def microServicePassword(self, microServicePassword):
        self.__microServicePassword = microServicePassword
