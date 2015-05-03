# -*- coding: utf-8 -*-

from decouple import config
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, **kwargs):
        u = User.objects.create_superuser(
            username=config('USER'),
            email=config('EMAIL'),
            password=config('PASSWORD', default=1, cast=int),
            full_name=config('USER'))
        u.save()

        print 'SUPERUSER CREATED!'
