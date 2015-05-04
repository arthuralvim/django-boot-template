web: gunicorn {{ project_name }}.heroku -w 4 --settings={{ project_name }}.settings.prod --log-file -
celeryd: python manage.py celeryd -E -B --loglevel=INFO --settings={{ project_name }}.prod
celerybeat: python manage.py celerybeat --settings={{ project_name }}.prod
