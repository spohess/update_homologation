from django.urls import path

from homologations.views.home_view import HomeView
from homologations.views.project_view import ProjectClone, ProjectReclone
from homologations.views.security_view import KeysshView

app_name = 'homologations'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('keyssh/', KeysshView.as_view(), name='keyssh'),

    path('project/clone/<int:pk>', ProjectClone.as_view(), name='project_clone'),
    path('project/reclone/<int:pk>', ProjectReclone.as_view(), name='project_reclone'),
]
