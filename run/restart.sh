#!/bin/bash
source ~/.bashrc
source ~/.virtualenvs/mall/bin/activate
cd /code/mall
pip install -r requirements.txt
python manage.py migrate
ps aux | grep "gunicorn" | grep "12000"| grep -v grep| awk '{print $2}'| xargs kill -9
