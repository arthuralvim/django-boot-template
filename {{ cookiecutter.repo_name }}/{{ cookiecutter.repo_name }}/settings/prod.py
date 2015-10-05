# -*- coding: utf-8 -*-

"""
Django settings for {{ cookiecutter.repo_name }} project.
"""

from decouple import config
from dj_database_url import parse as db_url
from os.path import join
from sys import path
from unipath import Path

BASE_DIR = Path(__file__).absolute().ancestor(2)
path.insert(0, BASE_DIR.child('apps'))  # insert path to apps

PROJECT_NAME = '{{ cookiecutter.repo_name }}'

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.{{ cookiecutter.repo_name }}.com', ]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ADMINS = ()

# APPS

from .apps import *  # noqa

# URLCONF

ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'

# DATABASE

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///{0}/{1}'.format(BASE_DIR.child('db'), '{{ cookiecutter.repo_name }}.sqlite3'),  # noqa
        cast=db_url),
}

FIXTURE_DIRS = (join(BASE_DIR.child('db'), 'fixtures'), )

# INTERNATIONALIZATION

LANGUAGE_CODE = config('LANGUAGE_CODE', default='pt-br')

LOCALE_PATHS = (BASE_DIR.child('locale'), )

TIME_ZONE = config('TIME_ZONE', default='America/Recife')

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'd/m/Y'

DATETIME_FORMAT = 'd-m-Y H:i:S'

DECIMAL_SEPARATOR = ','

THOUSAND_SEPARATOR = '.'


# STATIC

STATIC_ROOT = config('STATIC_ROOT', default=BASE_DIR.child('staticfiles'))

STATIC_URL = config('STATIC_URL', default='/static/')

STATICFILES_DIRS = (config('STATICFILES_ROOT',
                    default=BASE_DIR.child('static')), )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'djangobower.finders.BowerFinder',
    # 'pipeline.finders.PipelineFinder',
)

# CACHE

# from .cache import *  # noqa

# MEDIA

MEDIA_ROOT = config('MEDIA_ROOT', default=BASE_DIR.child('media'))

MEDIA_URL = config('MEDIA_URL', default='/media/')

# TEMPLATE

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

# MIDDLEWARE

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# BACKENDS

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# AUTH

# AUTH_USER_MODEL = 'app.UserModel'

# LOGIN_URL = 'login_view'

# LOGIN_REDIRECT_URL = 'login_redirect_view'

# LOGOUT_URL = 'logout_view'

# EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# from .email import *  # noqa

# SENTRY

from .sentry import *  # noqa

# BOWER

# from .bower import *  # noqa

# PIPELINE

# from .pipelines import *  # noqa

# DJANGO REST FRAMEWORK

from .rest import *  # noqa

# AWS S3

from .s3 import *  # noqa

# MANDRILL

from .mandrill import *  # noqa

# ELASTICSEARCH

from .elasticsearch import *  # noqa
