"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wmmx*^_i6@p)kP5nxa=89byfm0=gzc_h%13q)*7g7+181rk0po'

# SECURITY WARNING: don't run with debug turned on in production!
PRODUCTION = os.getenv('DATABASE_URL') is not None

# SECURITY WARNING: don't run with debug turned on in production!
# If you want to enable debugging on Heroku for learning purposes,
# set this to True.
# DEBUG = not PRODUCTION
DEBUG = True

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME', '')

ALLOWED_HOSTS = [f'{HEROKU_APP_NAME}.herokuapp.com']

if not PRODUCTION:
    ALLOWED_HOSTS += ['localhost', '127.0.0.1', '[::1]', '*']

WSGI_APPLICATION = 'thecims.wsgi.application'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'utils',
    'database',
    'home',
    'warnakulit',
    'tokoh',
    'barang',
    'pekerjaan',
    'misiutama',
    'level',
    'menggunakan_apparel',
    'crispy_forms',
    'menjalankan_misi',
    'makanan',
    'makan',
    'kategori_apparel',
    'koleksi',
    'koleksi_tokoh',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'thecims.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'thecims.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASE_URL = "postgres://arbssegqzgsvto:22bff49c056336a635b02e0a94d8f0ba0add32023b5ba74f054c8b7987ad2728@ec2-54-172-175-251.compute-1.amazonaws.com:5432/d8lkmntmudsje8"

DATABASES = {
    "default" : dj_database_url.config(),
}

DATABASES['default'] = dj_database_url.config()
DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

if PRODUCTION:
    DATABASES['default'] = dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
