# -*- coding: utf-8 -*-

from boto.s3.connection import S3Connection
from django.conf import settings
from django.http import Http404
from django.http import HttpResponseGone
from django.http import HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from logging import getLogger
from storages.backends.s3boto import S3BotoStorage

logger = getLogger('django.request')
STATIC_S3_STORAGE = lambda: S3BotoStorage(location=settings.STATIC_DIRECTORY)
MEDIA_S3_STORAGE = lambda: S3BotoStorage(location=settings.MEDIA_DIRECTORY)


class PrivateFileView(RedirectView):
    """
    PrivateFileView

    A generic class to be extended so the Amazon S3 files would act like
    they're private files.
    example of url:
    url(r'^private/(?P<pk>[\d]+)/$', views.SecretFileView.as_view(), name='private_file'),

    """
    permanent = False
    model = None
    file_attr = None
    permissions_required = None

    def get_model(self):
        pass

    def get_redirect_url(self, **kwargs):
        s3 = S3Connection(
            settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY,
            is_secure=True)

        # Create a URL valid for 60 seconds.
        return s3.generate_url(
            60, 'GET', bucket=settings.AWS_STORAGE_BUCKET_NAME,
            key=kwargs['filepath'], force_http=True)

    def get(self, request, *args, **kwargs):
        m = get_object_or_404(self.get_model(), pk=kwargs['pk'])
        u = request.user

        if u.get_permissions():
            if m.private_file:
                filepath = settings.MEDIA_DIRECTORY + m.private_file
                url = self.get_redirect_url(filepath=filepath)

                if url:
                    if self.permanent:
                        return HttpResponsePermanentRedirect(url)
                    else:
                        return HttpResponseRedirect(url)
                else:
                    logger.warning('Gone: %s', self.request.path,
                                   extra={
                                       'status_code': 410,
                                       'request': self.request
                                   })
                    return HttpResponseGone()
            else:
                raise Http404
        else:
            raise Http404
