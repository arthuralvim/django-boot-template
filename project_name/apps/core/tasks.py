# -*- coding: utf-8 -*-

from celery.decorators import periodic_task
from celery.task.schedules import crontab
from core.models import Example
import celery
import random
import string


@celery.task
def criar_exemplo(text, number):
    ex, created = Example.objects.get_or_create(text=text, number=number)


@periodic_task(run_every=(crontab(minute="*/20")))
def auto_criar_exemplo():
    for ex in range(10):
        text = ''.join(random.sample(string.letters, 10))
        number = random.randint(1, 100)
        criar_exemplo.delay(text, number)
