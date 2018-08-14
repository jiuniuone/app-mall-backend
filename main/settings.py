import os
import socket
import sys
import time

from unipath import Path

APP_NAME = 'mall'
FUNCTION_NAME = "shopping mall"
DEBUG = socket.gethostname() not in ['public', 'stage']
# DEBUG = False
SHOW_SQL = 'runserver' in sys.argv
if DEBUG: SHOW_SQL = False

BASE_DIR = Path(__file__).ancestor(2)
SECRET_KEY = 'i%25adry^l0r87l+228213a^%67q015z7j9^uc96jm=n%%0e^l'
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = 'main.urls'
WSGI_APPLICATION = 'main.wsgi.application'
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'
PAGINATE_BY = 10
START_TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

AUTH_USER_MODEL = f'{APP_NAME}.User'
LOGIN_URL = f'/{APP_NAME}/user/login/'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    f'{APP_NAME}.middlewares.HttpsCheckMiddleware',
    f'{APP_NAME}.middlewares.LogMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [BASE_DIR.child('templates')],
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'acmin.processors.extra_context'
            ],
        },
    },
]


def rotating_handler(name):
    return {
        'level': 'DEBUG',
        'filters': ['f1'],
        'formatter': 'simple',
        'class': 'logging.handlers.TimedRotatingFileHandler',
        'when': 'midnight',
        'interval': 1,
        'backupCount': 100,
        'filename': f'/var/log/{APP_NAME}/{name}.log',
    }


def file_handler(name):
    return {
        'level': 'DEBUG',
        'filters': ['f1'],
        'formatter': 'simple',
        'class': 'logging.FileHandler',
        'filename': f'/var/log/{APP_NAME}/{name}.log',
    }


def console_handler():
    return {'level': 'DEBUG', 'filters': ['f1'], 'formatter': 'simple', 'class': 'logging.StreamHandler', }


def get_log_setting(debug):
    log_modules = [APP_NAME]
    return {
        'version': 1,
        'disable_existing_loggers': True,
        'filters': {'f1': {'()': 'django.utils.log.RequireDebug' + str(debug)}},
        'formatters': {'simple': {'format': '%(levelname)s %(asctime)s %(message)s'}, },
        'handlers': dict({key: file_handler(key) for key in log_modules}, **{'console': console_handler()}),
        'loggers': {key: {'level': 'INFO', 'handlers': ['console', key]} for key in log_modules}
    }


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'acmin',
    APP_NAME
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

CACHALOT_UNCACHABLE_TABLES = (
    'django_migrations',

)

from acmin.utils import get_ip, is_windows

MEDIA_ROOT = "e:/var/www/media/" if is_windows() else "/var/www/media/"
MEDIA_URL = f'http://{get_ip()}/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.child(APP_NAME, "static")
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

USE_SQLITE3 = True
if DEBUG:
    name = 'test' if 'test' in sys.argv else 'app'
    if USE_SQLITE3:
        DATABASES = {'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR.child(f'{APP_NAME}.db'),
            'TEST_NAME': BASE_DIR.child(f'{APP_NAME}-test.db'),
        }}
    else:
        DATABASES = {'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': APP_NAME,
            'USER': APP_NAME,
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }}
else:
    DATABASES = {'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': APP_NAME,
        'USER': APP_NAME,
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }}

LOGGING = get_log_setting(DEBUG)
