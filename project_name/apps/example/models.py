# -*- coding: utf-8 -*-

from django.db import models


class Basic(models.Model):

    text = models.TextField(verbose_name='text', blank=True, null=True)
    number = models.IntegerField(verbose_name='text', blank=True, null=True)

    class Meta:
        verbose_name = "basic"
        verbose_name_plural = "basics"
