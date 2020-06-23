"""update_homologation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy

# handler400 = 'institutional.views.bad_request'
# handler403 = 'institutional.views.permission_denied'
# handler404 = 'institutional.views.page_not_found'
# handler500 = 'institutional.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect(reverse_lazy('institutional:login'), permanent=True)),
    path('institutional/', include('institutional.urls')),
    path('homologations/', include('homologations.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
