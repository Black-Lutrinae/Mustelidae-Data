from pymongo import MongoClient
import docker, random, time, math

class Temporary():
    def __init__(self):
        now = math.ceil(time.time())
        self.id = f'temporary_mongo_{int(math.fmod(now, random.randint(0,27017)))}'
        self.docker = docker.from_env()
        self.client = MongoClient('localhost', 27017)
        self.database = self.client['temporary']

    def start_database(self):
        self.docker.containers.run('mongo', detach=True, name=self.id)

    def close_database(self):
        self.docker.containers.get(self.id).kill()
    
    def remove_database(self):
        self.docker.containers.get(self.id).remove()