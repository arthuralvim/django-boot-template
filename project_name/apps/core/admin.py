# -*- coding: utf-8 -*-

from django.contrib import admin
from core.models import Example
from core.models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    date_hierarchy = 'data_hora'
    list_display = ('mensagem', 'usuario', 'status', )
    list_filter = ['status', 'modelo_tipo', ]
    search_fields = ['modelo_id', 'mensagem', 'usuario', ]
    ordering = ('-data_hora', )
    list_per_page = 100
    list_select_related = True

admin.site.register(Example)
