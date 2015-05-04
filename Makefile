# Makefile {{ project_name }}

DJADMIN_PY=$(VIRTUAL_ENV)/bin/django-admin.py
FABRIC=$(VIRTUAL_ENV)/bin/fab
GUNICORN=$(VIRTUAL_ENV)/bin/gunicorn
MANAGE_PY=$(VIRTUAL_ENV)/bin/python manage.py
PIP=$(VIRTUAL_ENV)/bin/pip
PY=$(VIRTUAL_ENV)/bin/python
SETTINGS_DEV={{ project_name }}.settings.dev
SETTINGS_PROD={{ project_name }}.settings.prod

# These targets are not files
.PHONY: all bower broadcast check.app check.branch check.email check.file check.settings check.user check.venv clean compile compilemessages coverage db db.delete.sqlite3 db.fixtures.dump db.fixtures.load db.reboot deploy dev env gunicorn help heroku.create heroku.db.create heroku.db.destroy heroku.db.reset heroku.destroy heroku.env.down heroku.env.up heroku.init heroku.migrate heroku.push heroku.remote heroku.static heroku.super makemessages mig mmig new_app pep8 prod provision requirements requirements.dev requirements.update runserver shell static super tests translate.br vm

all: help

help:
	@echo 'Makefile *** {{ project_name }} *** Makefile'

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

env:
	@cp .env-example .env

requirements:
	@$(PIP) install -r requirements.txt

requirements.dev:
	@$(PIP) install -r requirements/test.txt

requirements.update:
	@$(PIP) install -U -r requirements.txt

super: check.user check.email check.settings
	@$(MANAGE_PY) createsuperuser --username=$(USER) --email=$(EMAIL) --settings=$(SETTINGS)

bower: check.settings
	@$(MANAGE_PY) bower install --settings=$(SETTINGS)

shell: check.settings
	@$(MANAGE_PY) shell --settings=$(SETTINGS)

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

clean.migrations:
	@find . -path "*/migrations/*.pyc*"  ! -name "__init__.py" -exec rm -f {} \;

pep8:
	@pep8 --filename="*.py" --ignore=W --exclude="migrations" --first --show-source --statistics --count {{ project_name }}

compile:
	@$(PY) -m compileall {{ project_name }}

init: check.settings env mmig mig runserver

new_app:
	@echo "WIP"
# ---

# SERVER

runserver: check.settings
	@$(MANAGE_PY) runserver --settings=$(SETTINGS)

broadcast: check.settings
	@$(MANAGE_PY) runserver 0.0.0.0:8000 --settings=$(SETTINGS)

gunicorn: check.settings
	@$(GUNICORN) {{ project_name }}.wsgi -w 4 -b 127.0.0.1:8000 --settings=$(SETTINGS)

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

db: check.settings makemig mig

db.delete.sqlite3:
	@rm {{ project_name }}/db/{{ project_name }}.sqlite3

db.reboot: db.delete.sqlite3 db

mig: check.settings
	@$(MANAGE_PY) migrate --settings=$(SETTINGS)

mmig: check.settings
	@$(MANAGE_PY) makemigrations --settings=$(SETTINGS)

db.fixtures.dump: check.app check.settings
	@$(MANAGE_PY) dumpdata $(APP) --indent=4 --format=json > initial_data.json --settings=$(SETTINGS)

db.fixtures.load: check.file check.settings
	@$(MANAGE_PY) loaddata $(FILE) --settings=$(SETTINGS)

# ---

# STATIC

static: check.settings
	@$(MANAGE_PY) collectstatic --clear --noinput --settings=$(SETTINGS)

# ---

# TESTS

tests:
	@$(MANAGE_PY) test --settings=$(SETTINGS_DEV)

coverage:
	@$(MANAGE_PY) test_coverage --settings=$(SETTINGS_DEV)

# ---

# DEPLOY

provision:
	@echo "WIP"

deploy:
	@echo "WIP"

vm:
	@vagrant destroy && vagrant up

# ---

#  HEROKU

heroku.init: heroku.create heroku.env.up heroku.db.create heroku.static heroku.migrate heroku.super

heroku.create:
	@heroku create --stack cedar {{ project_name }}

heroku.destroy:
	@heroku destroy {{ project_name }}

heroku.remote:
	@heroku git:remote -a {{ project_name }}

heroku.db.create:
	@heroku addons:add heroku-postgresql

heroku.db.destroy:
	@heroku addons:remove heroku-postgresql

heroku.db.reset:
	@heroku pg:reset DATABASE_URL

heroku.static:
	@heroku run python manage.py collectstatic --clear --noinput --settings=$(SETTINGS_PROD)

heroku.super:
	@heroku run python manage.py createsuperuser --settings=$(SETTINGS_PROD)

heroku.migrate:
	@heroku run python manage.py migrate --settings=$(SETTINGS_PROD)

heroku.push:
	@git push heroku master

heroku.env.up:
	@heroku config:push

heroku.env.down:
	@heroku config:pull

# --- EOF --- #
