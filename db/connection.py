import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def firebase(credentials_path:str):
    try: 
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
        client = firestore.client()
        
        return firestore.client()
    except:
        print('Credentials File not found.')