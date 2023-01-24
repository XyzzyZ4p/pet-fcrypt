#!/bin/bash


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ENV_PATH="$SCRIPT_DIR/../.env"
PASSWORD="$(openssl rand -hex 64)"

echo "SECRET_KEY=$PASSWORD" > $ENV_PATH
exit $?
