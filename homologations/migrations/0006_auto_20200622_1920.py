# Generated by Django 3.0.7 on 2020-06-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homologations', '0005_auto_20200621_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homologations',
            name='project_folder',
            field=models.CharField(default='', help_text='Nome do diretório que será usado para criar o projeto', max_length=32, verbose_name='Diretório do projeto'),
            preserve_default=False,
        ),
    ]
