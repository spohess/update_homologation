from django.shortcuts import render
from django.template.defaultfilters import first
from django.views.generic import TemplateView

from homologations.models import Homologations
from homologations.rules import ProjetcRule, HomologationsRule


class ProjectDetail(TemplateView):
    template_name = 'homologations/project/detail.html'

    def get(self, request, *args, **kwargs):
        homologation_rule = HomologationsRule(request)
        homologation = Homologations.objects.get(pk=kwargs['pk'])

        context = {
            'homologation': homologation_rule.homologation_formatter(homologation),
        }
        return render(request, self.template_name, context)


class ProjectClone(TemplateView):
    template_name = 'homologations/project/output.html'

    def get(self, request, *args, **kwargs):
        projetc_rule = ProjetcRule(request)

        context = {
            'folder_content': projetc_rule.clone_project(kwargs=kwargs),
        }
        return render(request, self.template_name, context)


class ProjectReclone(TemplateView):
    template_name = 'homologations/project/output.html'

    def get(self, request, *args, **kwargs):
        projetc_rule = ProjetcRule(request)

        context = {
            'folder_content': projetc_rule.clone_project(kwargs=kwargs),
        }
        return render(request, self.template_name, context)
