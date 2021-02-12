import docker, random, time, math, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.persistence.config import Config

class LocalRelationalDatabase:
    def __init__(self, id:str=None):
        self.__config = Config('psql', 'localhost', '5434', 'postgres', 'postgres')
        now = math.ceil(time.time())
        if not id:
            id = int(math.fmod(now, random.randint(0,int(self.config.port))))
        self.__id = f'local_postgres_{id}'
        self.__docker = docker.from_env()
        self.__engine = create_engine(self.config.db_uri)
        self.__session = sessionmaker(bind=self.__engine)

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self.__session
    
    @property
    def config(self):
        return self.__config


    def start_database(self):
        try:
            self.__docker.containers.run('postgres', detach=True, name=self.__id, ports={'5432/tcp': self.config.port}, environment={'POSTGRES_PASSWORD':self.config.password})
        except:
            try:
                os.system(f'docker start {self.__id}')
            except:
                print('Error Trying to Start Database')


    def close_database(self):
        try:
            self.__docker.containers.get(self.__id).kill()
        except:
            print('Error trying to Close Database')
 

    def remove_database(self):
        self.__docker.containers.get(self.__id).remove()
