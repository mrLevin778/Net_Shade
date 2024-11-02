import os
from cryptography.fernet import Fernet

class FileCryptor:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.f = Fernet(self.key)

    def encrypt_file(self, in_filename, out_filename=None):
        if out_filename is None:
            out_filename = in_filename + ".encrypted"
        with open(in_filename, "rb") as f:
            data = f.read()
        encrypted_data = self.f.encrypt(data)
        with open(out_filename, "wb") as f:
            f.write(encrypted_data)

    def decrypt_file(self, in_filename, out_filename=None):
        if out_filename is None:
            out_filename = os.path.splitext(in_filename)[0]
        with open(in_filename, "rb") as f:
            data = f.read()
        decrypted_data = self.f.decrypt(data)
        with open(out_filename, "wb") as f:
            f.write(decrypted_data)

    def get_key(self):
        return self.key
