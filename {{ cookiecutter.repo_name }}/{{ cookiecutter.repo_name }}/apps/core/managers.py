# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Count
from django.db.models import Q
from django.db.models import Sum


class LogQuerySet(models.QuerySet):
    pass


class LogManager(models.Manager):

    def get_queryset(self):
        return LogQuerySet(self.model, using=self._db)
