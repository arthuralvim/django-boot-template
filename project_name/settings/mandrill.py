# -*- coding: utf-8 -*-

from decouple import config

SEND_EMAIL = config('SEND_EMAIL', default=False, cast=bool)
USE_MANDRILL = config('USE_MANDRILL', default=False, cast=bool)

# MANDRILL

if USE_MANDRILL:
    if SEND_EMAIL:
        EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
    MANDRILL_API_KEY = config('MANDRILL_API_KEY')
