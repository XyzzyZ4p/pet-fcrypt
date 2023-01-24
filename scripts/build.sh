#!/bin/bash


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR"/.. || exit $?
poetry build
pip uninstall -y fcrypt
pip install ./dist/fcrypt-1.0b1-py3-none-any.whl
