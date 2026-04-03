#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# এই অংশটি আপনার পাসওয়ার্ড সেট করবে
export DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD
python manage.py createsuperuser --noinput || true