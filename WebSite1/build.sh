#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# সরাসরি পাইথন কোড দিয়ে ইউজার তৈরি
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "$DJANGO_SUPERUSER_USERNAME"
email = "$DJANGO_SUPERUSER_EMAIL"
password = "$DJANGO_SUPERUSER_PASSWORD"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("SUPERUSER_CREATED")
else:
    u = User.objects.get(username=username)
    u.set_password(password)
    u.save()
    print("SUPERUSER_PASSWORD_UPDATED")
EOF
