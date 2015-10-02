# -*- coding: utf-8 -*-

from django.core.management import BaseCommand
from django.conf import settings
from django.db import connection
import sys


class Command(BaseCommand):

    def handle(self, **kwargs):
        db_settings = settings.DATABASES['default']

        conn_string = "DB CONNECTION -> ENGINE={ENGINE} \n host={HOST} \n " \
                      "DB={NAME} \n USER={USER} \n PASSWORD={PASSWORD} \n " \
                      "PORT={PORT}".format(**db_settings)
        print conn_string

        c = connection.cursor()
        try:
            c.execute('SELECT 1')
            print "Connected!"
        except Exception:
            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
        finally:
            c.close()
