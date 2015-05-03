# -*- coding: utf-8 -*-

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
# STATICFILES_STORAGE = '{{ project_name }}.apps.core.s3.S3PipelineStorage'

# PIPELINE_ENABLED = True
PIPELINE_DISABLE_WRAPPER = True
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_UGLIFYJS_ARGUMENTS = '--compress --mangle'

PIPELINE_JS = '{{ project_name }}.apps.core.pipeline.GLOBAL_PP_JS'
PIPELINE_CSS = '{{ project_name }}.apps.core.pipeline.GLOBAL_PP_CSS'
