#!/bin/bash

mkdir -pv /var/log/gunicorn/
mkdir -pv /var/run/gunicorn/
pipenv run python manage.py migrate
pipenv run gunicorn -c /app/config/gunicorn/prod.py
