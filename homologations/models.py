from django.contrib.auth.models import User
from django.db import models

from mixins.models_mixins import TimestampableMixin


class Homologations(TimestampableMixin):
    project_name = models.CharField(verbose_name='Nome do projeto',
                                    max_length=128)
    project_folder = models.CharField(verbose_name='Diretório do projeto',
                                      max_length=32,
                                      help_text='Caso queira que o diretório tenha um nome diferente do projeto git',
                                      null=True,
                                      blank=True)
    docker_folder = models.CharField(verbose_name='Diretório do docker',
                                     max_length=32,
                                     help_text='Nome do diretório onde fica o arquivo docker-composer,'
                                               ' se for na raiz deixe em branco',
                                     null=True,
                                     blank=True)
    git_repository_url = models.CharField(verbose_name='URL Git',
                                          max_length=255,
                                          help_text='git remote url ssh: git@(domínio):(usuário)/(projeto).git')
    container_name = models.CharField(verbose_name='Nome do Container',
                                      max_length=128,
                                      help_text='Nome dado para o cotainer principal do docker')
    container_port = models.CharField(verbose_name='Porta do Container',
                                      max_length=128,
                                      help_text='Número da porta dada para o cotainer principal do docker')
    settings_file = models.TextField(verbose_name='Configurações .env',
                                     help_text='Configurações que serão copiadas para o .env')
    project_description = models.TextField(verbose_name='Descrição',
                                           null=True,
                                           blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT,
                             verbose_name='Responsável')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Homologação'
        verbose_name_plural = 'Homologações'
