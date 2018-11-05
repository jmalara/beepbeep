#!/bin/bash

cd /home/tc/beepbeep

echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1

if [ $? -eq 0 ]; then
    git fetch --all
    git reset --hard origin/master
    git pull origin master
fi

sudo python beep.py &
