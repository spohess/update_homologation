from django.contrib import admin

from . import models


class HomologationsList(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'container_name', 'container_port')
    list_display_links = ('id', 'project_name')
    search_fields = ('project_name', 'container_name')
    list_filter = ('project_name', 'container_name')


admin.site.register(models.Homologations, HomologationsList)
