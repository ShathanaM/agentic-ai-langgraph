vectorstore = None

def set_vectorstore(vs):
    global vectorstore
    vectorstore = vs

def get_vectorstore():
    return vectorstore