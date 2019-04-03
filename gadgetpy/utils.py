import os

def verifyName(name):
    parts = name.split('.')
    return len(parts)==2

def verifyPointer(path,pointer):
    for gadget in os.listdir(path):
        if os.path.isfile(os.path.join(path,gadget,'UDC')):
            with open(os.path.join(path,gadget,'UDC')) as f:
                res = f.read().strip()
                print(res)
                print(pointer)
                if res == pointer.strip():
                    return False
    return pointer in os.listdir('/sys/class/udc')
