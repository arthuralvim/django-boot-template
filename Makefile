# Makefile {{ project_name }}

DJADMIN_PY=$(VIRTUAL_ENV)/bin/django-admin.py
FABRIC=$(VIRTUAL_ENV)/bin/fab
GUNICORN=$(VIRTUAL_ENV)/bin/gunicorn_django
MANAGE_PY=$(VIRTUAL_ENV)/bin/python manage.py
PIP=$(VIRTUAL_ENV)/bin/pip
PROVY=$(VIRTUAL_ENV)/bin/provy
PY=$(VIRTUAL_ENV)/bin/python
UWSGI=$(VIRTUAL_ENV)/bin/uwsgi

SETTINGS_DEV={{ project_name }}.settings.dev
SETTINGS_PROD={{ project_name }}.settings.prod
SETTINGS_STAGE={{ project_name }}.settings.stage
SETTINGS_TEST={{ project_name }}.settings.test

# These targets are not files
.PHONY: all dev prod stage test boot requirements requirements.update createsuperuser shell clean clean.django pep8 compile help runserver server gunicorn uwsgi translate.br makemessages compilemessages db db.delete.sqlite3 db.fresh db.clear migrate migration.initial migration fixtures.dump fixtures.load provision deploy static tests heroku.remote heroku.create heroku.delete heroku.static heroku.migrate heroku.push heroku.deploy open vm check.venv check.app check.file check.settings check.user check.email check.branch

all: help

check.venv:
	@if test "$(VIRTUAL_ENV)" = "" ; then echo "VIRTUAL_ENV is undefined"; exit 1; fi

check.app:
	@if test "$(APP)" = "" ; then echo "APP is undefined"; exit 1; fi

check.file:
	@if test "$(FILE)" = "" ; then echo "FILE is undefined"; exit 1; fi

check.settings:
	@if test "$(SETTINGS)" = "" ; then echo "SETTINGS is undefined"; exit 1; fi

check.branch:
	@if test "$(BRANCH)" = "" ; then echo "BRANCH is undefined"; exit 1; fi

check.user:
	@if test "$(USER)" = "" ; then echo "USER is undefined"; exit 1; fi

check.email:
	@if test "$(EMAIL)" = "" ; then echo "EMAIL is undefined"; exit 1; fi

# SETTINGS FILES

dev: check.venv
	$(eval SETTINGS:=$(SETTINGS_DEV))

prod: check.venv
	$(eval SETTINGS:=$(SETTINGS_PROD))

stage: check.venv
	$(eval SETTINGS:=$(SETTINGS_STAGE))

test: check.venv
	$(eval SETTINGS:=$(SETTINGS_TEST))

# ---

# UTIL

requirements:
	@$(PIP) install -r requirements.txt

requirements.update:
	@$(PIP) install -U -r requirements.txt

createsuperuser: check.user check.email check.settings
	@$(MANAGE_PY) createsuperuser --username=$(USER) --email=$(EMAIL) --settings=$(SETTINGS)

shell: check.settings
	@$(MANAGE_PY) shell --settings=$(SETTINGS)

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

pep8:
	@pep8.py --filename=*.py --ignore=W --exclude="manage.py,settings.py,migrations" --statistics --repeat {{ project_name }}

compile:
	@$(PY) -m compileall {{ project_name }}

help:
	@echo 'Just a makefile to help django-projects.'

boot: db migrate static
# ---

# SERVER

runserver: check.settings
	@$(MANAGE_PY) runserver --settings=$(SETTINGS)

server: check.settings
	@$(MANAGE_PY) runserver 0.0.0.0:8000 --settings=$(SETTINGS)

gunicorn: check.settings
	@$(GUNICORN) -C deploy/gunicorn.conf.py -b 127.0.0.1:8000 --settings=$(SETTINGS)

uwsgi:
	@uwsgi -p 4 -s 127.0.0.1:8000 --ini deploy/uwsgi.ini

# ---

# LANGUAGE / INTERNATIONALIZATION

translate.br:
	@cd {{ project_name }}; $(DJADMIN_PY) makemessages -l pt-br

makemessages:
	@cd {{ project_name }}; $(DJADMIN_PY) makemessages -a

compilemessages: check.settings
	@$(MANAGE_PY) compilemessages --settings=$(SETTINGS)

# ---

# DATABASE

db: check.settings
	@$(MANAGE_PY) syncdb --noinput --settings=$(SETTINGS)

db.delete.sqlite3:
	@rm {{ project_name }}/db/{{ project_name }}.sqlite3

db.fresh: db.delete.sqlite3 db

db.clear: check.app check.settings
	@$(MANAGE_PY) sqlclear $(APP) --settings=$(SETTINGS) | $(MANAGE_PY) dbshell --settings=$(SETTINGS)

migrate: check.settings
	@$(MANAGE_PY) migrate --settings=$(SETTINGS)

migration.initial: check.app check.settings
	@$(MANAGE_PY) schemamigration $(APP) --initial  --settings=$(SETTINGS)

migration: check.app check.settings
	@$(MANAGE_PY) schemamigration $(APP) --auto --settings=$(SETTINGS)

fixtures.dump: check.app check.settings
	@$(MANAGE_PY) dumpdata $(APP) --indent=4 --format=json > initial_data.json --settings=$(SETTINGS)

fixtures.load: check.file check.settings
	@$(MANAGE_PY) loaddata $(FILE) --settings=$(SETTINGS)

# ---

# DEPLOY

provision:
	@$(PROVY) -s prod

deploy:
	@$(FABRIC) deploy

# ---

# STATIC

static: check.settings
	@$(MANAGE_PY) collectstatic --clear --noinput --settings=$(SETTINGS)

# to push files to s3
# publish:

# ---

# TESTS

tests:
	@$(MANAGE_PY) test --settings=$(SETTINGS_TEST)

# ---

#  HEROKU

heroku.create:
	@heroku create --stack cedar {{ project_name }}

heroku.delete:
	@heroku destroy {{ project_name }}

heroku.remote:
	@heroku git:remote -a {{ project_name }}
	# git remote add heroku git@heroku.com:{{ project_name }}.git

heroku.static:
	@heroku run python manage.py collectstatic --clear --noinput

heroku.migrate:
	@heroku run python manage.py syncdb --noinput
	@heroku run python manage.py migrate

heroku.push: check.branch
	@git push heroku $(BRANCH):master

heroku.deploy: heroku.push heroku.migrate heroku.static

open:
	@heroku open

# ---

# VIRTUAL MACHINES

vm:
	@vagrant destroy && vagrant up

# ---
