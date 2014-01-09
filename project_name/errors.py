from django import http
from django.template import loader
from django.template import RequestContext
from django.template import TemplateDoesNotExist
from django.views.decorators.csrf import requires_csrf_token


@requires_csrf_token
def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: :template:`500.html`
    """
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        return http.HttpResponseServerError('<h1>Server Error (500)</h1>',
                                            content_type='text/html')
    return http.HttpResponseServerError(
        template.render(RequestContext(request)))


@requires_csrf_token
def bad_request(request, template_name='400.html'):
    """
    400 error handler.

    Templates: :template:`400.html`
    """
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        return http.HttpResponseBadRequest('<h1>Bad Request (400)</h1>',
                                           content_type='text/html')
    return http.HttpResponseBadRequest(
        template.render(RequestContext(request)))
