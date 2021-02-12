import docker, random, time, math, os
from pymongo import MongoClient
from db.persistence.config import Config

class LocalDocumentDatabase:
    def __init__(self, id:str=None):
        self.__config = Config('mongodb', 'localhost', '27017')
        now = math.ceil(time.time())
        if not id:
            id = int(math.fmod(now, random.randint(0,int(self.config.port))))
        self.__id = f'local_mongo_{id}'
        self.__docker = docker.from_env()
        self.__client = MongoClient(self.config.db_uri)
        self.__database = self.__client['local']

    @property
    def database(self):
        return self.__database

    @property
    def config(self):
        return self.__config

    def start_database(self):
        try:
            self.__docker.containers.run('mongo', detach=True, name=self.__id, ports={'27017/tcp': self.config.port})
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
