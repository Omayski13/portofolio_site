from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class MainPageview(TemplateView):
    template_name = 'main/../../templates/main.html'

