def verifyName(name):
    parts = name.split('.')
    return len(parts)==2

def verifyPointer(path,pointer):
    return True