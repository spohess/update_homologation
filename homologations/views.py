from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'homologations/home.html'


class KeysshView(TemplateView):
    template_name = 'homologations/keyssh.html'
