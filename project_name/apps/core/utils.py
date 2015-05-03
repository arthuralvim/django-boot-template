# -*- coding: utf-8 -*-

from contextlib import contextmanager
from django.http import HttpResponse
import locale
import threading
import unicodedata


LOCALE_LOCK = threading.Lock()

TRANSPARENT_1_PIXEL_GIF = "\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b"  # noqa


def tracking_pixel():
    return HttpResponse(TRANSPARENT_1_PIXEL_GIF, content_type='image/gif')


def normalize_ascii(value):
    return unicodedata.normalize('NFKD', unicode(value))\
        .encode('ascii', 'ignore')


@contextmanager
def setlocale(name):
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)

        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)
