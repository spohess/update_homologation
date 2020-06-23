from django.shortcuts import render
from django.views.generic import TemplateView

from homologations.models import Homologations


class HomeView(TemplateView):
    template_name = 'homologations/home.html'

    def get(self, request, *args, **kwargs):
        homologations = Homologations.objects.all()
        homologations_list = []
        for homologation in homologations:
            homologations_list.append(homologation.formatter())

        context = {
            'homologations_list': homologations_list,
        }

        return render(request, self.template_name, context)
