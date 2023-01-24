from os import remove

from fcrypt.settings import ENCODING
from fcrypt.descriptors import FileNotExist


class Buffer:
    path: FileNotExist()
    
    def __init__(self, path: str):
        self.path = path
    
    def __enter__(self):
        try:
            file = open(self.path, 'w')
        except OSError as e:
            raise OSError("File already open") from e
        else:
            file.close()
            
        remove(self.path)
        self.fp = open(self.path, 'a', encoding=ENCODING)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()
    
    def __add__(self, other):
        self.fp.write(other)


__all__ = ('Buffer',)
