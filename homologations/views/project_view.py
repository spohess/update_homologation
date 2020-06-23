from django.shortcuts import render
from django.views.generic import TemplateView

from homologations.models import Homologations
from homologations.rules import ProjetcRule


class ProjectDetail(TemplateView):
    template_name = 'homologations/project/detail.html'

    def get(self, request, *args, **kwargs):
        homologation = Homologations.objects.get(pk=kwargs['pk'])

        context = {
            'homologation': homologation.formatter(),
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
