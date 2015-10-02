# -*- coding: utf-8 -*-

from decouple import config

BOWER_COMPONENTS_ROOT = config('BOWER_COMPONENTS_ROOT')

BOWER_INSTALLED_APPS = (
    'backbone#1.1.2',
    'backbone.marionette#2.4.1',
    'bootstrap#3.1.0',
    'bootstrap-datepicker#1.3.1',
    'c3#0.4.10',
    'd3#3.5.0',
    'font-awesome#4.3.0',
    'handlebars#3.0.0',
    'jquery#2.1.1',
    'selectize#0.12.1',
)
