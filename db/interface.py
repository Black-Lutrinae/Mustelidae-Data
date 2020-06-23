from .database import CloudDatabase, LocalDocumentDatabase
import random, math

class Interface():
    def __init__(self, project:str, conn:str='local'):
        self.conn = conn
        self.__local_conn = LocalDocumentDatabase(project)
        self.project = project
        self.set_reference(self.project)

    def connect(self):
        try:
            self.__local_conn.start_database()
        except:
            print('Error on Connecting')
    
    def disconnect(self):
        try:
            self.__local_conn.close_database()
        except:
            print('Error on Disconnecting')
 
    def set_reference(self, ref:str):
        self.__reference = self.__local_conn.database[ref]
    
    def local_to_cloud(self, credentials_path:str):
        self.__cloud_conn = CloudDatabase(f'c:{project}', credentials_path)
        self.__cloud_conn.open_batch()
        # operations
        self.__cloud_conn.close_batch()  
    
    def set(self, data, multiple=False):
        try:
            if not multiple:
                return self.__reference.insert_one(data).inserted_id
            else:
                return self.__reference.insert_many(data).inserted_ids
        except:
            print('Error Setting Objects')

    def get(self, data, multiple=False):
        try:
            if not multiple:
                return self.__reference.find_one(data)
            else:
                return self.__reference.find(data)
        except:
            print('Error Getting Objects')

    def update(self, selector, data, multiple=False):
        try:
            if not multiple:
                self.__reference.update_one(selector,data)
            else:
                self.__reference.update_many(selector, data)
        except:
            print('Error Updating Objects')

    def delete(self, selector, multiple=False):
        try:
            if not multiple:
                self.__reference.delete_one(selector)
            else:
                self.__reference.delete_many(selector)
        except:
            print('Error Deleting Objects')

    def count(self, data):
        try:
            return self.__reference.count_documents(data)
        except:
            print('Error Counting Objects')
