# -*- coding: utf-8 -*-

from decouple import config

SEND_EMAIL = config('SEND_EMAIL', default=False, cast=bool)

if SEND_EMAIL:
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_USER = config('EMAIL_USER')
    EMAIL_PASSWORD = config('EMAIL_PASSWORD')
    EMAIL_PORT = config('EMAIL_PORT', cast=int)
    EMAIL_TLS = config('EMAIL_TLS')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = EMAIL_HOST
    EMAIL_HOST_USER = EMAIL_USER
    EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
    EMAIL_PORT = EMAIL_PORT
    EMAIL_USE_TLS = EMAIL_TLS
    SERVER_EMAIL = EMAIL_HOST_USER
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

