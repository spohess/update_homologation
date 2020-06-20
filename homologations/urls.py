from django.urls import path

from homologations.views import home_view

app_name = 'homologations'

urlpatterns = [
    path('', home_view.HomeView.as_view(), name='home'),
]
