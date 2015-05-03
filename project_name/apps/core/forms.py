# -*- coding: utf-8 -*-

from django import forms

BLANK_CHOICE = (('', 'select one'),)


class EmptyForm(forms.Form):

    def is_valid(self):
        return True


class SearchForm(forms.Form):
    search = forms.CharField()
