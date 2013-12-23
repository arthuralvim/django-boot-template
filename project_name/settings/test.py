from prod import *

INSTALLED_APPS += (
    'django_nose',
)

SOUTH_TEST_MIGRATE=False

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--match=^(must|ensure|should|test|it_should)',
    '--where={{ project_name }}',
    '--id-file=.noseids',
    '--all-modules',
    '--with-id',
    '--verbosity=2',
    '--nologcapture',
    '--rednose',
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-html-dir=../cover',
    '--cover-package={{ project_name }}',
    '--cover-inclusive',
]
