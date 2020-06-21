import os

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView

from . import models


class HomeView(TemplateView):
    template_name = 'homologations/home.html'


class KeysshView(TemplateView):
    template_name = 'homologations/keyssh.html'

    def get(self, request, *args, **kwargs):
        keyssh = models.Keyssh.objects.filter(active=True).first()
        path_file = keyssh.absolute_path + keyssh.file_name
        context = {
            'file': None
        }
        if os.path.isfile(path=path_file):
            file_ssh = open(file=path_file, mode='r')
            file_context = file_ssh.readlines()
            context['file'] = file_context[0]
            file_ssh.close()
        else:
            messages.error(request, 'Chave SSH não foi encontrada em <strong>{0}</strong>, certifique-se que'
                                    ' a configuração está correta na área administrativa'.format(path_file))

        return render(request, self.template_name, context)
