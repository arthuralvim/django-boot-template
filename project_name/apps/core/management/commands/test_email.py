# -*- coding: utf-8 -*-

from django.core.management import BaseCommand
from django.core.mail import EmailMessage


class Command(BaseCommand):

    def handle(self, **kwargs):
        email = EmailMessage('Subject', 'Message', to=['example@example.com'])
        email.send()
        print 'Email: Ok.'
