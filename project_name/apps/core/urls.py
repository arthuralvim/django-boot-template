from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    'core.views',
    url(r'^$', 'index', name='index'),
    url(r'^maintenance$', 'maintenance', name='mnt'),
)
