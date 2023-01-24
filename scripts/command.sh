#!/bin/bash


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SECRET_KEY=$(cat "$SCRIPT_DIR"/../.env | sed 's/.*=//g' | xargs)
IN_FILE=""
OUT_FILE=""
COMMAND=""

python3 -m fcrypt $COMMAND --secret-key $SECRET_KEY --out $OUT_FILE $IN_FILE 
