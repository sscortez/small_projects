
from .app import MyGPG

MYGPG = MyGPG()


def encrypt_data(data):
    return MYGPG.encrypt_data(data)


def decrypt_data(data):
    return MYGPG.decrypt_data(data)
