# -*- coding: utf-8 -*-

from django import template
register = template.Library()


@register.inclusion_tag('templatetags/paginator.html', takes_context=True)
def paginator(context, adjacent_pages=2):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    Required context variables: paged: The Paginator.page() instance.

    """
    paged = context['page_obj']
    paginator = context['paginator']
    startPage = max(paged.number - adjacent_pages, 1)
    if startPage <= 3:
        startPage = 1
    endPage = paged.number + adjacent_pages + 1

    if endPage >= paginator.num_pages - 1:
        endPage = paginator.num_pages + 1

    page_numbers = [n for n in range(startPage, endPage) if n > 0 and
                    n <= paginator.num_pages]

    querystr = context['request'].GET.copy()
    if 'page' in querystr:
        del querystr['page']
    querystr = querystr.urlencode()

    return {
        'paged': paged,
        'querystr': querystr,
        'paginator': paginator,
        'page': paged.number,
        'pages': paginator.num_pages,
        'page_numbers': page_numbers,
        'has_next': paged.has_next(),
        'has_previous': paged.has_previous(),
        'show_first': 1 not in page_numbers,
        'show_last': paginator.num_pages not in page_numbers,
    }
