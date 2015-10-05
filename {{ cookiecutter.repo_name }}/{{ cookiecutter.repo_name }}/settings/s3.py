# -*- coding: utf-8 -*-

from decouple import config

USE_AWS_S3 = config('USE_AWS_S3', default=False, cast=bool)

if USE_AWS_S3:
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('S3_BUCKET_NAME')
    AWS_HEADERS = {'Cache-Control': 'max-age=86400', }
    AWS_PRELOAD_METADATA = True
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_SECURE_URLS = False
    STATIC_DIRECTORY = config('S3_STATIC_ROOT', default='static/')
    MEDIA_DIRECTORY = config('S3_MEDIA_ROOT', default='media/')
    DEFAULT_FILE_STORAGE = '{{ cookiecutter.repo_name }}.apps.core.s3.MEDIA_S3_STORAGE'
    STATICFILES_STORAGE = '{{ cookiecutter.repo_name }}.apps.core.s3.STATIC_S3_STORAGE'
    S3_URL = "https://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = config('S3_STATIC_URL', default=S3_URL + STATIC_DIRECTORY)
    MEDIA_URL = config('S3_MEDIA_URL', default=S3_URL + MEDIA_DIRECTORY)
