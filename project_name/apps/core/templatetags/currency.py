# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import floatformat
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

register = template.Library()


# @register.filter
# def currency(value):
#     return 'R$ {0}'.format(floatformat(value, 2))


@register.filter
def currency(value):
    locale._override_localeconv.update({'p_cs_precedes': 1,
                                        'n_cs_precedes': 1})
    return locale.currency(value, symbol=True, grouping=True)
