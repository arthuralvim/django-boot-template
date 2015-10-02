# -*- coding: utf-8 -*-

from .apps import LOCAL_APPS
from django.utils.importlib import import_module

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_ENABLED = True
PIPELINE_DISABLE_WRAPPER = True

# npm install -g uglify-js

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_UGLIFYJS_ARGUMENTS = '--compress --mangle'

PIPELINE_JS = {}
PIPELINE_CSS = {}

for app in LOCAL_APPS:

    try:
        mod = import_module('%s.assets' % app)
    except:
        continue

    try:
        PIPELINE_JS.update(mod.PIPELINE_JS)
    except:
        pass

    try:
        PIPELINE_CSS.update(mod.PIPELINE_CSS)
    except:
        pass
