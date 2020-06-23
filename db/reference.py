def set_reference(db, path:str):
    """
        Build your path as:
        
        `type:value`
        
        Type can be `c` or `d`;
        
        C stands for collection;
        D stands for document;
    """
    if path not in ['', None]:
        print(path)
        obj, ref = path.split(':')
    else:
        obj = 'd'
        ref = ''
    if 'c' == obj:
        return db.collection(ref)
    elif 'd' == obj:
        return db.document(ref)
    else:
        print('Invalid Reference')

def set_path(db, path:str):
    """
        Your path should be multiple references separated by `/`, like:

        `type:value/type:value/type:value`
    """
    refs = path.split('/')
    for ref in refs:
        db = set_reference(db, ref)
    return db