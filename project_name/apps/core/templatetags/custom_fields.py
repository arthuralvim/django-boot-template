# -*- coding: utf-8 -*-

from django.template import Library


register = Library()


def custom_field(field):
    return {
        'id': field.id_for_label,
        'name': field.name,
        'label': field.label,
        'field': field
    }

def register_custom_field_tag(tag_name):
    template_name = 'custom_fields/_{0}.html'.format(tag_name)
    register.inclusion_tag(template_name, name=tag_name)(custom_field)


register_custom_field_tag('switch_field')

register_custom_field_tag('currency_field')

register_custom_field_tag('date_field')

register_custom_field_tag('cpf_field')
