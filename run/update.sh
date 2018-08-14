#!/usr/bin/env bash

cd /code/mall
git pull
git submodule update
cp -Rf acmin/static/* /var/www/static/mall/
cp -Rf mall/static/* /var/www/static/mall/