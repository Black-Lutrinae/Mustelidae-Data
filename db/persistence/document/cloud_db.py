from db.connection import firebase
from db.persistence.document.reference import *
from firebase_admin.firestore import DocumentReference, CollectionReference

class CloudDatabase:

    def __init__(self, root:str, credentials:str):
        self.__client = firebase(credentials)
        self.root = root
        self.root_ref()

    def root_ref(self):
        """
            Sets the reference as root path.
        """
        self.__reference = self.__client
        self.set_ref(self.root)

    def set_ref(self, ref:str):
        """
            Append reference with the given path.
        """
        self.__reference = set_path(self.__reference, ref)

    def set(self, obj:dict, ref:str=None):
        if ref:
            reference = self.__reference
            self.__reference = set_path(self.__reference, ref)
        if isinstance(self.__reference, DocumentReference):
            if self.__batch:
                self.__batch.set(self.__reference, obj)
            else:
                self.__reference.set(obj)
        else:
            print('Reference must be a Document')
        if ref:
            self.__reference = reference

    def get(self, ref:str=None):
        if ref:
            reference = self.__reference
            self.__reference = set_path(self.__reference, ref)
        result = self.__reference.get()
        return result.to_dict()
        if ref:
            self.__reference = reference

    def update(self, obj:object, ref:str=None):
        if ref:
            reference = self.__reference
            self.__reference = set_path(self.__reference, ref)
        if self.__batch:
            self.__batch.update(self.__reference, obj)
        else:
            self.__reference.update(obj)
        if ref:
            self.__reference = reference

    def delete(self, ref:str=None):
        if ref:
            reference = self.__reference
            self.__reference = set_path(self.__reference, ref)
        if self.__batch:
            self.__batch.delete(self.__reference)
        else:
            self.__reference.delete()
        if ref:
            self.__reference = reference

    def open_batch(self):
        self.__batch = self.__client.batch()
    
    def close_batch(self):
        self.__batch.commit()
        self.__batch = None
