# -*- coding: utf-8 -*-

from .apps import LOCAL_APPS
from django.utils.importlib import import_module

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
# STATICFILES_STORAGE = '{{ project_name }}.apps.core.s3.S3PipelineStorage'

PIPELINE_DISABLE_WRAPPER = True

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
