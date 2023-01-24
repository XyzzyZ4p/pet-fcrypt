from fcrypt.settings import ENCODING
from fcrypt.cipher import AESCipher
from fcrypt.descriptors import FileExist
from .buffer import Buffer


class File:
    path: FileExist
    
    def __init__(self, path, secret):
        self.path = path
        self.cipher = AESCipher(secret)
    
    def encrypt(self, dist_path: str) -> None:
        with open(self.path, 'r', encoding=ENCODING) as fp:
            with Buffer(dist_path) as buffer:
                for line in fp.readlines():
                    encrypted = self.cipher.encrypt(line).decode(ENCODING)
                    buffer += (encrypted + '\n')
        
    def decrypt(self, dist_path) -> None:
        with open(self.path, 'r', encoding=ENCODING) as fp:
            with Buffer(dist_path) as buffer:
                for line in fp.readlines():
                    decrypted = self.cipher.decrypt(line.strip().encode('utf-8'))
                    buffer += decrypted
