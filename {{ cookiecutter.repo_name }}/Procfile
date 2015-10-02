web: gunicorn {{ project_name }}.heroku -w 4 --settings={{ project_name }}.settings.prod --log-file -
celery: python manage.py celery worker -c 4 --loglevel=INFO --settings={{ project_name }}.prod
celerybeat: python manage.py celerybeat --settings={{ project_name }}.prod
