from django.shortcuts import redirect
from django.urls import path, reverse_lazy

from . import views

app_name = 'institutional'

urlpatterns = [
    path('',
         lambda request: redirect(reverse_lazy('institutional:login'),
                                  permanent=True,
                                  name='index')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
