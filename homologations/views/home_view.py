from django.shortcuts import render
from django.views.generic import TemplateView

from homologations.rules import HomologationsRule


class HomeView(TemplateView):
    template_name = 'homologations/home.html'

    def get(self, request, *args, **kwargs):
        homologation_rule = HomologationsRule(request)
        context = {
            'homologations_list': homologation_rule.get_homologations_list()
        }

        return render(request, self.template_name, context)
