from conn import connection 

class Database():


    def __init__(self):
        self.client = connection('./db-credentials.json')
        self.reference = self.client


    def clean_ref(self):
        self.reference = self.client


    def set_ref(self, ref):
        ref = ref.split(':')
        if ref[0] == 'c':
            self.reference = self.reference.collection(ref[1])
        else:
            self.reference = self.reference.document(ref[1])


    def set(self, obj:dict):
        try:
            if self.reference:
                self.reference.set(obj)
            else:
                self.error('reference')
        except:
            self.error('set')


    def read(self, id):
        try:
            if self.reference:
                document = self.reference.document(id).get()
                return document.to_dict()
            else:
                self.error('reference')
        except:
            self.error('read')


    def update(self, obj):
        try:
            if self.reference:
                pass
            else:
                self.error('reference')
        except:
            self.error('update')


    def delete(self, obj):
        try:
            if self.reference:
                pass
            else:
                self.error('reference')
        except:
            self.error('delete')


    def error(self, err):
        if err == 'reference':
            print('Error: Missing Reference Object')
        elif err == 'set':
            print('Error: Setting Object')
        elif err == 'read':
            print('Error: Reading Object')
        elif err == 'update':
            print('Error: Updating Object')
        elif err == 'delete':
            print('Error: Deleting Object')
        else:
            print('Error: Unknown')
