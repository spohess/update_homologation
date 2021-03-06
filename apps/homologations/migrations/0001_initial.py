# Generated by Django 3.0.7 on 2020-06-28 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyssh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('absolute_path', models.CharField(help_text='/home/(usuário)/.ssh/', max_length=128, verbose_name='Caminho para chave')),
                ('file_name', models.CharField(help_text='(arquivo).pub', max_length=32, verbose_name='Nome do arquivo')),
                ('active', models.BooleanField(default=True, help_text='Arquivo está ativo', unique=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Chave SSH',
                'verbose_name_plural': 'Chaves SSH',
            },
        ),
        migrations.CreateModel(
            name='Homologation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('project_name', models.CharField(max_length=128, verbose_name='Nome do projeto')),
                ('project_folder', models.CharField(help_text='Nome do diretório que será usado para criar o projeto', max_length=32, verbose_name='Diretório do projeto')),
                ('git_repository_url', models.CharField(help_text='git remote url ssh: git@(domínio):(usuário)/(projeto).git', max_length=255, verbose_name='URL Git')),
                ('docker_folder', models.CharField(help_text='Nome do diretório onde fica o arquivo docker-composer, se for na raiz deixe em branco', max_length=32, verbose_name='Diretório do docker')),
                ('project_description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Responsável')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DockerContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('container_name', models.CharField(help_text='Nome que é usado para acessar o container', max_length=128, verbose_name='Nome do container')),
                ('container_type', models.CharField(choices=[('database', 'Banco de Dados'), ('webserver', 'Servidor Web'), ('others', 'Outros')], max_length=32, verbose_name='Tipo de serviço do container')),
                ('container_port', models.IntegerField(blank=True, null=True, verbose_name='Porta externa de acesso')),
                ('homologation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homologations.Homologation')),
            ],
            options={
                'verbose_name': 'Homologação',
                'verbose_name_plural': 'Homologações',
            },
        ),
    ]
