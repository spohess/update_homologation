# Generated by Django 3.0.7 on 2020-06-21 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homologations', '0003_auto_20200620_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyssh',
            name='active',
            field=models.BooleanField(default=True, help_text='Arquivo está ativo', unique=True, verbose_name='Ativo'),
        ),
    ]
