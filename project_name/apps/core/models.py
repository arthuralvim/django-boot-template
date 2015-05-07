# -*- coding: utf-8 -*-

from core.contants import LOG_STATUS_CHOICES
from core.contants import LogStatus
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
import boto


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    updated_at = models.DateTimeField(auto_now=True, editable=False)

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


class Log(models.Model):
    model_type = models.ForeignKey(
        ContentType, blank=True, null=True, editable=False)

    model_id = models.PositiveIntegerField(
        blank=True, null=True, editable=False)

    model_object = GenericForeignKey(
        'model_type', 'model_id')

    user = models.ForeignKey(User, blank=True, null=True, editable=False)

    message = models.TextField(blank=True, null=True, editable=False)

    status = models.IntegerField(choices=LOG_STATUS_CHOICES, default=0,
                                 null=True,)

    date_time = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = u'log'
        verbose_name_plural = u'logs'

    def __unicode__(self):
        return self.date_time.strftime('%d-%m-%Y %H:%M:%S')


def register_log(sender, instance, **kwargs):
    log = Log()
    log.model_type = ContentType.objects.get_for_model(sender)
    log.model_id = instance.id

    if hasattr(instance, 'created_by'):
        log.user = instance.created_by
        log.status = LogStatus.CREATE
        log.message = u'Model: {0} ({1}) created by user: {2}'.format(
            log.model_type, log.model_id, log.user)

    if hasattr(instance, 'updated_by'):
        log.user = instance.updated_by
        log.status = LogStatus.UPDATE
        log.message = u'Model: {0} ({1}) updated by user: {2}'.format(
            log.model_type, log.model_id, log.user)

    if hasattr(instance, 'deleted_by'):
        log.user = instance.deleted_by
        log.status = LogStatus.DELETE
        log.message = u'Model: {0} ({1}) deleted by user: {2}'.format(
            log.model_type, log.model_id, log.user)

    log.save()


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

    def __unicode__(self):
        return u'<Example {0} - {1}>'.format(self.text, self.number)

post_save.connect(register_log, sender=Example)
pre_delete.connect(register_log, sender=Example)
