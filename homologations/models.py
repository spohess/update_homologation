import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from mixins.models_mixins import TimestampableMixin


class Homologations(TimestampableMixin):
    project_name = models.CharField(verbose_name='Nome do projeto',
                                    max_length=128)
    project_folder = models.CharField(verbose_name='Diretório do projeto',
                                      max_length=32,
                                      help_text='Nome do diretório que será usado para criar o projeto',)
    git_repository_url = models.CharField(verbose_name='URL Git',
                                          max_length=255,
                                          help_text='git remote url ssh: git@(domínio):(usuário)/(projeto).git')
    docker_folder = models.CharField(verbose_name='Diretório do docker',
                                     max_length=32,
                                     help_text='Nome do diretório onde fica o arquivo docker-composer,'
                                               ' se for na raiz deixe em branco',
                                     null=True,
                                     blank=True)
    container_name = models.CharField(verbose_name='Nome do Container',
                                      max_length=128,
                                      help_text='Nome dado para o cotainer principal do docker',
                                      null=True,
                                      blank=True)
    container_port = models.CharField(verbose_name='Porta do Container',
                                      max_length=128,
                                      help_text='Número da porta dada para o cotainer principal do docker',
                                      null=True,
                                      blank=True)
    settings_file = models.TextField(verbose_name='Configurações .env',
                                     help_text='Configurações que serão copiadas para o .env',
                                     null=True,
                                     blank=True)
    project_description = models.TextField(verbose_name='Descrição',
                                           null=True,
                                           blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT,
                             verbose_name='Responsável')

    def __str__(self):
        return self.project_name

    def docker_folder_normalized(self):
        return self.docker_folder if self.docker_folder else '-'

    def container_name_normalized(self):
        return self.container_name if self.container_name else '-'

    def container_port_normalized(self):
        return self.container_port if self.container_port else '-'

    def settings_file_normalized(self):
        return self.settings_file if self.settings_file else '-'

    def project_description_normalized(self):
        return self.project_description if self.project_description else '-'

    def formatter(self):
        project_absolute_folder = os.path.join(settings.REPOSITORIES_FOLDER, self.project_folder),
        return {
            'pk': self.pk,
            'project_name': self.project_name,
            'project_folder': self.project_folder,
            'project_absolute_folder': project_absolute_folder[0],
            'git_repository_url': self.git_repository_url,
            'docker_folder': self.docker_folder_normalized,
            'container_name': self.container_name_normalized,
            'container_port': self.container_port_normalized,
            'settings_file': self.settings_file_normalized,
            'project_description': self.project_description_normalized,
            'responsible': '{0} {1}'.format(self.user.first_name, self.user.last_name),
            'user': self.user,
            'file_exists': os.path.isdir(project_absolute_folder[0]),
        }

    class Meta:
        verbose_name = 'Homologação'
        verbose_name_plural = 'Homologações'


class Keyssh(TimestampableMixin):
    absolute_path = models.CharField(verbose_name='Caminho para chave',
                                     max_length=128,
                                     help_text='/home/(usuário)/.ssh/')
    file_name = models.CharField(verbose_name='Nome do arquivo',
                                 max_length=32,
                                 help_text='(arquivo).pub')
    active = models.BooleanField(verbose_name='Ativo',
                                 unique=True,
                                 default=True,
                                 help_text='Arquivo está ativo')

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = 'Chave SSH'
        verbose_name_plural = 'Chaves SSH'
