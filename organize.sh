#!/bin/bash

# check if python exists
pyversion=$(python3 -c 'import sys; print(sys.version_info[0])')
if [ $pyversion != 3 ]
then
    echo "Please install python3 \n Try this: "
    echo "\t\tbrew install python3"
    exit
fi

python3 ./src/organize.py $1