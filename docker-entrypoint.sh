#!/bin/sh
set -e

echo "Waiting for database..."
/wait-for-it.sh db:3306 --timeout=60 --strict -- echo "Database is ready!"

# Rodar migrations e criar superuser se quiser
python manage.py makemigrations
python manage.py migrate
python create_superuser.py
python manage.py runserver 0.0.0.0:8000

# Depois iniciar o gunicorn
exec gunicorn lojaonline.wsgi:application --bind 0.0.0.0:8000
