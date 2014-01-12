from prod import *

DEBUG = True
DEBUG_TEMPLATE = True
DEBUG_TOOLBAR = config('DEBUG_TOOLBAR', default=False, cast=bool)
COVERAGE = config('COVERAGE', default=False, cast=bool)
ALLOWED_HOSTS = ['*', ]

if DEBUG_TOOLBAR:

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    DEBUG_APPS = ('debug_toolbar', )
    INSTALLED_APPS += DEBUG_APPS

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

if COVERAGE:
    COVERAGE_APPS = ('django_coverage', )
    INSTALLED_APPS += COVERAGE_APPS
    COVERAGE_REPORT_HTML_OUTPUT_DIR = 'cover'
    COVERAGE_USE_STDOUT = True
    COVERAGE_USE_CACHE = True

    COVERAGE_MODULE_EXCLUDES = [
        'tests$', 'settings$', 'urls$', 'fixtures$',
        '__init__', 'django', 'migrations'] + list(DJANGO_APPS) + \
        list(THIRD_PARTY_APPS) + list(DEBUG_APPS) + list(COVERAGE_APPS)
