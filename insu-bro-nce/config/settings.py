"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-%r3dk*n@4w)fvrd+b4gt7t7nu98@37ev#d&yfbs*kdr1dmm3n)'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_elasticsearch_dsl',
    'django_bootstrap5',
    'django_filters',
    'django_tables2',
    'anymail',

    'users',
    'insurance',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', (BASE_DIR / 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = reverse_lazy('insurance:product:table')
LOGIN_URL = reverse_lazy('users:login')


# django_tables2
DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap-responsive.html'
DJANGO_TABLES2_PAGE_RANGE = 5


# Email (anymail) config
EMAIL_BACKEND = os.environ.get(
    'EMAIL_BACKEND', 'anymail.backends.sendinblue.EmailBackend')
DEFAULT_FROM_EMAIL = os.environ.get(
    'DEFAULT_FROM_EMAIL', 'webmaster@localhost')
if EMAIL_BACKEND == 'anymail.backends.sendinblue.EmailBackend':
    ANYMAIL = {
        'SENDINBLUE_API_KEY': os.environ.get('SENDINBLUE_API_KEY'),
    }


# RabbitMQ properties
RABBITMQ_DEFAULT_USER = os.environ.get('RABBITMQ_DEFAULT_USER', 'admin')
RABBITMQ_DEFAULT_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS', 'admin')
RABBITMQ_DEFAULT_VHOST = os.environ.get('RABBITMQ_DEFAULT_VHOST', '/')


# Celery properties
CELERY_BROKER_URL = f'pyamqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@rabbit:5672/{RABBITMQ_DEFAULT_VHOST}'


# Elasticsearch properties
ELASTICSEARCH_DSL_HOST = os.environ.get('ELASTICSEARCH_DSL_HOST', 'localhost')
ELASTICSEARCH_DSL_PORT = os.environ.get('ELASTICSEARCH_DSL_PORT', '9200')
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': f'{ELASTICSEARCH_DSL_HOST}:{ELASTICSEARCH_DSL_PORT}'
    },
}
# TODO: создать CelerySignalProcessor для индексации через очередь задач
# ELASTICSEARCH_DSL_SIGNAL_PROCESSOR = 'CelerySignalProcessor'
# TODO: для PostgreSQL в будущем использовать строку ниже
# ELASTICSEARCH_DSL_PARALLEL = True
