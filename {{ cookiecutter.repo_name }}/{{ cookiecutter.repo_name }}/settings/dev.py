# -*- coding: utf-8 -*-

from prod import *  # noqa

DEBUG_TEMPLATE_VARS = config('DEBUG_TEMPLATE_VARS', default=False, cast=bool)
DEBUG_TOOLBAR = config('DEBUG_TOOLBAR', default=False, cast=bool)
TEST_COVERAGE = config('TEST_COVERAGE', default=False, cast=bool)
TEST_NOSE = config('TEST_NOSE', default=False, cast=bool)
USE_AWS_S3 = config('USE_AWS_S3', default=False, cast=bool)

if DEBUG_TOOLBAR:
    DEBUG_APPS = ('debug_toolbar', )
    INSTALLED_APPS += DEBUG_APPS

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    INTERNAL_IPS = ('127.0.0.1', )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'JQUERY_URL': None,
    }

    if USE_AWS_S3:
        # removed by a clash with S3 lib
        DEBUG_TOOLBAR_CONFIG['DISABLE_PANELS'] = set([
            'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        ])

    CONFIG_DEFAULTS = {
        # Toolbar options
        'SHOW_COLLAPSED': True,
        # Panel options
        'SQL_WARNING_THRESHOLD': 300,   # milliseconds
    }

if DEBUG_TEMPLATE_VARS:
    class InvalidVarException(object):
        def __mod__(self, missing):
            try:
                missing_str = unicode(missing)
            except:
                missing_str = 'Failed to create string representation'
            raise Exception('Unknown template variable %r %s' % (missing,
                            missing_str))

        def __contains__(self, search):
            if search == '%s':
                return True
            return False

    TEMPLATE_DEBUG = True
    TEMPLATE_STRING_IF_INVALID = InvalidVarException()

if TEST_COVERAGE:
    COVERAGE_APPS = ('django_coverage', )
    INSTALLED_APPS += COVERAGE_APPS
    COVERAGE_REPORT_HTML_OUTPUT_DIR = 'cover'
    COVERAGE_USE_STDOUT = True
    COVERAGE_USE_CACHE = True

    COVERAGE_MODULE_EXCLUDES = [
        'tests$', 'settings$', 'urls$', 'fixtures$',
        '__init__', 'django', 'migrations'] + list(DJANGO_APPS) + \
        list(THIRD_PARTY_APPS) + list(DEBUG_APPS) + list(COVERAGE_APPS)

if TEST_NOSE:
    INSTALLED_APPS += (
        'django_nose',
    )

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

    NOSE_ARGS = [
        '--match=^(must|ensure|should|test|it_should)',
        '--where={{ project_name }}',
        '--verbosity=2',
        '--nologcapture',
        '--rednose',
        # '--with-id',
        # '--id-file=.noseids',
        # '--failed',
        # '--with-coverage',
        # '--cover-erase',
        # '--cover-html',
        # '--cover-html-dir=../cover',
        # '--cover-package={{ project_name }}',
        # '--cover-inclusive',
    ]
