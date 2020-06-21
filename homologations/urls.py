from django.urls import path

from . import views

app_name = 'homologations'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('keyssh/', views.KeysshView.as_view(), name='keyssh'),
]
