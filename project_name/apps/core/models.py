# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils import timezone
import boto


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now,
                                      editable=False)

    updated_at = models.DateTimeField(auto_now=True, default=timezone.now,
                                      editable=False)

    class Meta:
        abstract = True


class WebModel(models.Model):
    ip_address = models.CharField(max_length=20, blank=True, null=True,
                                  editable=False)

    user_agent = models.CharField(max_length=255, blank=True, null=True,
                                  editable=False)

    referer = models.CharField(max_length=255, blank=True, null=True,
                               editable=False)

    class Meta:
        abstract = True


class AmazonS3PrivateFile(object):

    def get_s3_private_file(self):
        raise ImproperlyConfigured(
            "AmazonS3PrivateFile requires an implementation of "
            "'get_s3_private_file()'")

    def save(self, *args, **kwargs):
        super(AmazonS3PrivateFile, self).save(*args, **kwargs)
        if self.get_s3_private_file() and settings.USE_AWS_S3:
            conn = boto.s3.connection.S3Connection(
                settings.AWS_ACCESS_KEY_ID,
                settings.AWS_SECRET_ACCESS_KEY)
            bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
            k = boto.s3.key.Key(bucket)
            k.key = settings.MEDIA_DIRECTORY + self.private_file.name
            k.set_acl('private')


class Example(AmazonS3PrivateFile, models.Model):

    text = models.TextField(verbose_name='text', blank=True, null=True)
    number = models.IntegerField(verbose_name='number', blank=True, null=True)
    public_file = models.FileField(blank=True, null=True, upload_to='public')
    private_file = models.FileField(blank=True, null=True, upload_to='private')

    def get_s3_private_file(self):
        return self.private_file

    class Meta:
        verbose_name = "example"
        verbose_name_plural = "examples"
