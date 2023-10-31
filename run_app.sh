#!/bin/bash

poetry run python manage.py makemigrations
poetry run python manage.py migrate
python manage.py runserver
