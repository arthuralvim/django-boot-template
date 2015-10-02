# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import Celery
from decouple import config
# from kombu import Exchange
# from kombu import Queue
import multiprocessing
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')  # noqa

from django.conf import settings

BROKER_URL = config('BROKER_URL')
app = Celery('{{ project_name }}')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    CELERYD_CONCURRENCY=(multiprocessing.cpu_count() * 2) + 1,
    CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ENABLE_UTC=True,
    CELERY_TIMEZONE='America/Recife',
    # CELERY_QUEUES = (
    #     Queue('default', Exchange('default'), routing_key='default'),
    # ),
    # CELERY_DEFAULT_QUEUE = 'default',
    # CELERY_DEFAULT_EXCHANGE = 'default',
    # CELERY_DEFAULT_ROUTING_KEY = 'default',
    # CELERY_ROUTES = {
    #     'app.tasks.task_name': {'queue': 'queue_name'},
    #     'app.tasks.task_name': 'low-priority',
    # },
    # CELERY_ANNOTATIONS = {
    #     'app.tasks.task_name': {'rate_limit': '10/m'},
    # },
)
