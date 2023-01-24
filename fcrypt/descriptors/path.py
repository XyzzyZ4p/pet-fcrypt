from pathlib import Path


class FileExist:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        value = getattr(instance, self.name)
        path = Path(value) 
        if not path.exists() and not path.is_file():
            raise FileNotFoundError()
        return str(path)


class FileNotExist:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        value = getattr(instance, self.name)
        path = Path(value)
        if path.exists() and path.is_dir():
            raise FileExistsError()
        return str(path)


__all__ = ('FileExist', 'FileNotExist')
