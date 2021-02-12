class Config:
    def __init__(self, db_type:str, host:str, port:str, user:str=None, password:str=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_type = db_type

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host:str):
        self.__host = host

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port:str):
        self.__port = port

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user:str):
        self.__user = user

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password:str):
        self.__password = password

    @property
    def db_type(self):
        return self.__db_type

    @db_type.setter
    def db_type(self, db_type:str):
        self.__db_type = db_type

    @property
    def db_uri(self):
        connection = f'{self.db_type}://{self.host}:{self.port}/'
        if self.user and self.password:
            return connection + f'{self.user}:{self.password}'
        return connection