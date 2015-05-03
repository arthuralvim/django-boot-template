# -*- coding: utf-8 -*-

from decouple import config

USE_SENTRY = config('USE_SENTRY', default=False, cast=bool)

# SENTRY

if USE_SENTRY:
    RAVEN_CONFIG = {
        'dsn': config('RAVEN_CONFIG_DSN')
    }
