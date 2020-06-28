from django.contrib import admin

from . import models


class DockerContainerList(admin.ModelAdmin):
    list_display = ('id', 'homologation', 'container_name', 'container_type', 'container_port')
    list_display_links = ('id', 'homologation', 'container_name')
    search_fields = ('homologation', 'container_name', 'container_type')
    list_filter = ('homologation', 'container_name', 'container_type')


admin.site.register(models.DockerContainer, DockerContainerList)


class HomologationList(admin.ModelAdmin):
    list_display = ('id', 'project_name')
    list_display_links = ('id', 'project_name')
    search_fields = ('project_name',)
    list_filter = ('project_name',)


admin.site.register(models.Homologation, HomologationList)


class KeysshList(admin.ModelAdmin):
    list_display = ('id', 'file_name')
    list_display_links = ('id', 'file_name')


admin.site.register(models.Keyssh, KeysshList)
