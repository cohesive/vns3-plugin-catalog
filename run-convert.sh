#!/bin/bash

projectpath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
envDirPath="$projectpath/.env"
OutFile=catalog
OutFormat=json

if [ ! -d "$envDirPath" ] ; then
    echo "Python environment $envDirPath does not exist. Creating."
    virtualenv .env
fi

rm -rf "$Outfile.$OutFormat"

echo "Installing dependencies in $envDirPath."
source .env/bin/activate
pip install pyyaml

echo "Converting to $OutFormat."
python convert.py --outfile $OutFile --format $OutFormat

if [ $? -gt 0 ]; then
    echo "ERROR"
    exit 1
fi
