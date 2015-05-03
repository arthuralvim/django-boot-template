# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.importlib import import_module


GLOBAL_PP_JS = {}
GLOBAL_PP_CSS = {}

for app in settings.INSTALLED_APPS:

    try:
        mod = import_module('%s.assets' % app)
    except:
        continue

    try:
        GLOBAL_PP_JS.update(mod.PIPELINE_JS)
    except:
        pass

    try:
        GLOBAL_PP_CSS.update(mod.PIPELINE_CSS)
    except:
        pass
