from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

handler400 = '{{ cookiecutter.repo_name }}.errors.bad_request'
handler403 = 'django.views.defaults.permission_denied'
handler404 = 'django.views.defaults.page_not_found'
handler500 = '{{ cookiecutter.repo_name }}.errors.server_error'

urlpatterns = patterns(
    '',
    url(r'^', include('core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.views.generic import TemplateView
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += patterns(
        '',
        (r'^403/$', TemplateView.as_view(template_name="403.html")),
        (r'^404/$', TemplateView.as_view(template_name="404.html")),
        (r'^500/$', TemplateView.as_view(template_name="500.html")),
    )

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
