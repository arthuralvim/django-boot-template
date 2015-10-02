# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


class MaintenanceView(TemplateView):
    template_name = "core/maintenance.html"

index = IndexView.as_view()
maintenance = MaintenanceView.as_view()
