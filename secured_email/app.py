
import json
import os
from os.path import join

import gnupg

_parent_path = os.path.dirname(__file__)


class MyGPG(object):
    def __init__(self):
        self.mygpg = gnupg.GPG()
        self.recipient = 'Sami'  # Your default recipient's name

    def encrypt_data(self, data):
        encrypted = self.mygpg.encrypt(data, recipients=self.recipient, always_trust=True)
        return encrypted

    def decrypt_data(self, data):
        filename = 'passphrase.json'
        with open(join(_parent_path, filename)) as jfile:
            __passphrase = json.loads(jfile.read())
        decrypted = self.mygpg.decrypt(data, passphrase=__passphrase)
        return decrypted


if __name__ == "__main__":
    print('Test')
    pass
