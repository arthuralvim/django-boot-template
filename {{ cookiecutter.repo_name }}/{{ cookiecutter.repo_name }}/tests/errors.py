from django.test import TestCase
from django.test.client import RequestFactory
from django.views.defaults import permission_denied as handler403
from django.views.defaults import page_not_found as handler404
from {{ cookiecutter.repo_name }} import urls
from {{ cookiecutter.repo_name }}.errors import bad_request as handler400
from {{ cookiecutter.repo_name }}.errors import server_error as handler500


class TestErrorPages(TestCase):

    def test_error_handlers(self):
        self.assertTrue(urls.handler400 == '{{ cookiecutter.repo_name }}.'
                        'errors.bad_request')
        self.assertTrue(urls.handler403 == 'django.views.'
                        'defaults.permission_denied')
        self.assertTrue(urls.handler404 == 'django.views.'
                        'defaults.page_not_found')
        self.assertTrue(urls.handler500 == '{{ cookiecutter.repo_name }}.'
                        'errors.server_error')
        factory = RequestFactory()
        request = factory.get('/')
        response = handler400(request)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Error 400 - Bad Request', unicode(response))
        response = handler403(request)
        self.assertEqual(response.status_code, 403)
        self.assertIn('Error 403 - Forbidden', unicode(response))
        response = handler404(request)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Error 404 - Page Not Found', unicode(response))
        response = handler500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn('Error 500 - Internal Server Error', unicode(response))
