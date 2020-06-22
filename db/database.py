from connection import connection
from reference import *
from firebase_admin.firestore import DocumentReference, CollectionReference

class Database():

    def __init__(self, root:str):
        self.client = connection('./db-credentials.json')
        self.root = root
        self.root_ref()

    def root_ref(self):
        """
            Sets the reference as root path.
        """
        self.reference = self.client
        self.set_ref(self.root)

    def set_ref(self, ref:str):
        """
            Append reference with the given path.
        """
        self.reference = set_path(self.reference, ref)

    def set(self, obj:dict, ref:str=None):
        if ref:
            reference = self.reference
            self.reference = set_path(self.reference, ref)
        if isinstance(self.reference, DocumentReference):
            if self.batch:
                self.batch.set(self.reference, obj)
            else:
                self.reference.set(obj)
        else:
            print('Reference must be a Document')
        if ref:
            self.reference = reference

    def get(self, ref:str=None):
        if ref:
            reference = self.reference
            self.reference = set_path(self.reference, ref)
        result = self.reference.get()
        return result.to_dict()
        if ref:
            self.reference = reference

    def update(self, obj:object, ref:str=None):
        if ref:
            reference = self.reference
            self.reference = set_path(self.reference, ref)
        if self.batch:
            self.batch.update(self.reference, obj)
        else:
            self.reference.update(obj)
        if ref:
            self.reference = reference

    def delete(self, ref:str=None):
        if ref:
            reference = self.reference
            self.reference = set_path(self.reference, ref)
        if self.batch:
            self.batch.delete(self.reference)
        else:
            self.reference.delete()
        if ref:
            self.reference = reference

    def open_batch(self):
        self.batch = self.client.batch()
    
    def close_batch(self):
        self.batch.commit()
        self.batch = None