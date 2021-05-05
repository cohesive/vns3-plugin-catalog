#!/bin/bash

projectpath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
envDirPath="$projectpath/.env"

if [ ! -d "$envDirPath" ] ; then
    echo "Python environment $envDirPath does not exist. Creating."
    virtualenv .env
fi

echo "Installing dependencies in $envDirPath."
source .env/bin/activate
pip install pyyaml

echo "Converting to json."
python convert.py

deactivate