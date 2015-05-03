# -*- coding: utf-8 -*-

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'core',
)

THIRD_PARTY_APPS = (
    'bootstrap3',
    'django_filters',
    'djangobower',
    'gunicorn',
    'pipeline',
    'raven.contrib.django.raven_compat',
    'rest_framework',
    'storages',
    'taggit',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
