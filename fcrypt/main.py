"""Crypt.

Usage:
  crypt1.py hello
  commands.py goodbye
  commands.py -h | --help

Options:
  -h --help     Show this screen.
"""
from fcrypt.commands import cli


if __name__ == "__main__":
    cli()
