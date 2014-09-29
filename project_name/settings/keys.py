# -*- coding: utf-8 -*-

from decouple import config

# put your api keys, important keys, etc here.


USE_LIB_EXAMPLE = config('USE_LIB_EXAMPLE', default=False, cast=bool)

if USE_LIB_EXAMPLE:
    LIB_KEY = config('LIB_KEY')
