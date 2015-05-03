# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.filter
def attr(field, arg):
    s = arg.split(':')
    attr = s[0]
    value = s[1]
    return field.as_widget(attrs={attr: value})


@register.filter
def attrs(field, args):
    el = args.split(';')
    attrs = {}
    for e in el:
        s = e.split(':')
        attr = s[0]
        value = s[1]
        attrs.update({attr: value})
    return field.as_widget(attrs=attrs)
