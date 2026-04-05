import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-0fr+(l$9qb6g&y@u!@s-4ynv#gmyxd=t5_pm=4&e))88h3f=7v",
)

# SECURITY WARNING: don't run with debug turned on in production!
# ডেভলপমেন্টের সময় এটি True রাখুন যাতে ইমেজ দেখা যায়
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost,192.168.0.112",
    ).split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core", # আপনার অ্যাপ
    "storages",  # AWS S3 এর জন্য
    "cloudinary_storage",
    "cloudinary",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # Static files এর জন্য
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "aloron_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media", # এটি যোগ করা হয়েছে
            ],
        },
    },
]

WSGI_APPLICATION = "aloron_site.wsgi.application"

# Database Configuration
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3'
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "bn-bd"
TIME_ZONE = "Asia/Dhaka"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files (User uploaded images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Cloudinary Configuration for Media Files in Production
CLOUDINARY_CONFIGURED = all(
    os.getenv(key)
    for key in (
        'CLOUDINARY_CLOUD_NAME',
        'CLOUDINARY_API_KEY',
        'CLOUDINARY_API_SECRET',
    )
)

if CLOUDINARY_CONFIGURED:
    try:
        import cloudinary_storage
        CLOUDINARY_STORAGE = {
            'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
            'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
            'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
        }
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        CLOUDINARY_URL = os.getenv('CLOUDINARY_URL') or (
            f"cloudinary://{os.getenv('CLOUDINARY_API_KEY')}:{os.getenv('CLOUDINARY_API_SECRET')}@{os.getenv('CLOUDINARY_CLOUD_NAME')}"
        )
    except ImportError:
        # Cloudinary not installed, fall back to local storage
        pass

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")