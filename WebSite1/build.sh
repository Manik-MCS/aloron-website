#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# সরাসরি অটোমেটিক সুপারইউজার তৈরি/রিসেট করার কমান্ড
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
import os

username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'YourPassword123')

# আগের ইউজার থাকলে ডিলিট করে নতুন করে তৈরি করবে
if User.objects.filter(username=username).exists():
    User.objects.filter(username=username).delete()

User.objects.create_superuser(username, email, password)
print(f'Successfully created/reset superuser: {username}')
EOF
