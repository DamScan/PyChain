from Crypto.PublicKey import RSA
import os


class ManualGen:
    key = RSA.generate(2048)

    def __init__(self, inputs):
        self.passPhrase = inputs.get('passPhrase')
        self.path = inputs.get('path')
        self.name = inputs.get('name')

    def create(self):
        self._directory()
        self._create_private_key()
        self._create_public_key()

    def _directory(self):
        if not os.path.exists(f"./{self.path}"):
            os.mkdir(os.path.join("./", self.path))

    def _get_encrypt_key(self):
        return self.key.export_key(passphrase=self.passPhrase, pkcs=8, protection="scryptAndAES128-CBC")

    def _get_encoded_key(self):
        return open(f"./{self.path}/{self.name}.pem", "rb").read()

    def _create_private_key(self):
        file_out = open(f"./{self.path}/{self.name}.pem", "wb")
        file_out.write(self._get_encrypt_key())
        file_out.close()

    def _create_public_key(self):
        encoded_key = open(f"./{self.path}/{self.name}.pem", "rb").read()
        key = RSA.import_key(encoded_key, passphrase=self.passPhrase)
        file_out = open(f"./{self.path}/{self.name}_pub.pem", "wb")
        file_out.write(key.publickey().export_key())
        file_out.close()
