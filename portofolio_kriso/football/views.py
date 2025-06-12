from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class FootballPageView(TemplateView):
    template_name = 'football.html'
