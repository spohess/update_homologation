from django.urls import path

from homologations.views.home_view import HomeView
from homologations.views.project_view import ProjectClone, ProjectReclone, ProjectDetail
from homologations.views.security_view import KeysshView

app_name = 'homologations'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('keyssh/', KeysshView.as_view(), name='keyssh'),

    path('project/detail/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('project/clone/<int:pk>', ProjectClone.as_view(), name='project_clone'),
    path('project/reclone/<int:pk>', ProjectReclone.as_view(), name='project_reclone'),
]
