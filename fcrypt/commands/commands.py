import click

from fcrypt.settings import PASSWORD, DECODE_EXT, ENCODE_EXT
from fcrypt.utils import file_path_helper
from fcrypt.models import File

__all__ = ('cli',)


@click.group()
def cli(): ...


@cli.command("encrypt")
@click.option("--secret-key", default=PASSWORD, help="Encrypting password")
@click.option("--out", default='', help="Output file")
@click.argument("file")
def encrypt(file, secret_key, out):
    """Encrypt file

    FILE - path to file
    
    \bExample:
        crypt1.py encrypt [path]
        crypt1.py encrypt --secret-key [PASSWORD] [path]
        crypt1.py encrypt --out [path] [path]
    """
    if not out:
        out = file_path_helper(out, ENCODE_EXT)
    file = File(file, secret=secret_key)
    file.encrypt(out)
    

@cli.command("decrypt")
@click.option("--secret-key", default=PASSWORD, help="Encrypting password")
@click.option("--out", default='', help="Output file")
@click.argument("file")
def decrypt(file, secret_key, out):
    """Decrypt file

    FILE - path to file

    \bExample:
        crypt1.py decrypt [path]
        crypt1.py decrypt --secret-key [PASSWORD] [path]
        crypt1.py decrypt --out [path] [path]
    """
    if not out:
        out = file_path_helper(out, DECODE_EXT)
    file = File(file, secret=secret_key)
    file.decrypt(out)
