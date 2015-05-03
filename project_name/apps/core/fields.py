# -*- coding: utf-8 -*-

from django.forms.fields import DecimalField


class BRLCurrencyField(DecimalField):

    def to_python(self, value):
        if value in self.empty_values:
            return None

        value = value.replace('.', '').replace(',', '.')

        return super(BRLCurrencyField, self).to_python(value)
