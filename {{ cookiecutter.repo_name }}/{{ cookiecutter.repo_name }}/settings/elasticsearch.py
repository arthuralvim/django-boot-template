# -*- coding: utf-8 -*-

from decouple import config

ELASTICSEARCH_URL = config('ELASTICSEARCH_URL',
                           default='http://127.0.0.1:9200')
ELASTICSEARCH_INDEX = config('ELASTICSEARCH_INDEX',
                             default='{{ project_name }}')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',  # noqa
        'URL': ELASTICSEARCH_URL,
        'INDEX_NAME': ELASTICSEARCH_INDEX
    }
}

HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'
