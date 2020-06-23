from django.shortcuts import render
from django.views.generic import TemplateView

from homologations.rules import ProjetcRule


class ProjectClone(TemplateView):
    template_name = 'homologations/output.html'

    def get(self, request, *args, **kwargs):
        projetc_rule = ProjetcRule(request)

        context = {
            'folder_content': projetc_rule.clone_project(kwargs=kwargs),
        }
        return render(request, self.template_name, context)


class ProjectReclone(TemplateView):
    template_name = 'homologations/output.html'

    def get(self, request, *args, **kwargs):
        projetc_rule = ProjetcRule(request)

        context = {
            'folder_content': projetc_rule.clone_project(kwargs=kwargs),
        }
        return render(request, self.template_name, context)
