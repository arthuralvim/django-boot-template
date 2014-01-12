from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

from django.contrib import admin
admin.autodiscover()

handler400 = '{{ project_name }}.errors.bad_request'
handler403 = 'django.views.defaults.permission_denied'
handler404 = 'django.views.defaults.page_not_found'
handler500 = '{{ project_name }}.errors.server_error'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^pattern/', include('app.urls', namespace='some_name')),

    url(r'^admin/', include(admin.site.urls)),
)
