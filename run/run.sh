#!/bin/bash

base_folder=$(cd "$(dirname "$0")"; pwd)
source ~/.bashrc
source ~/.virtualenvs/mall/bin/activate
cd /code/mall
pip install -r requirements.txt
python manage.py migrate

ps aux | grep "runserver" | grep "12000"| grep -v grep| awk '{print $2}'| xargs kill -9
#nohup python manage.py runserver 0.0.0.0:18000 --insecure  >/dev/null 2>&1 &
nohup python manage.py runserver 0.0.0.0:12000 >/dev/null 2>&1 &
#ps aux | grep "gunicorn" | grep "12000"| grep -v grep| awk '{print $2}'| xargs kill -9
#nohup gunicorn main.wsgi -b "0.0.0.0:12000" -w 3 >/dev/null 2>&1 &
cd $base_folder