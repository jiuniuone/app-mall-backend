#!/bin/bash
base_folder=$(cd "$(dirname "$0")"; pwd)
source ~/.bashrc
source ~/.virtualenvs/mall/bin/activate
cd /code/mall
d=`date +%Y-%m-%d`
python manage.py dumpdata | gzip > /mnt/www/backup/mall/$d.json.gz
cd $base_folder