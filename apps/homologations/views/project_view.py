from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from homologations.models import Homologation
from homologations.rules import ProjetcRule


class ProjectDetail(TemplateView):
    template_name = 'homologations/project/detail.html'

    def get(self, request, *args, **kwargs):
        homologation = Homologation.objects.get(pk=kwargs['pk'])

        context = {
            'homologation': homologation.formatter(),
        }
        return render(request, self.template_name, context)


class ProjectClone(TemplateView):
    def get(self, request, *args, **kwargs):
        homologation = Homologation.objects.get(pk=kwargs['pk'])
        projetc_rule = ProjetcRule(request)

        data = {
            'command_output': projetc_rule.clone_project(homologation),
        }
        return JsonResponse(data=data)


class ProjectReclone(TemplateView):
    def get(self, request, *args, **kwargs):
        homologation = Homologation.objects.get(pk=kwargs['pk'])
        projetc_rule = ProjetcRule(request)

        data = {
            'command_output': projetc_rule.reclone_project(homologation),
        }
        return JsonResponse(data=data)
