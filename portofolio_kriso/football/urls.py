from django.contrib import admin
from django.urls import path, include

from portofolio_kriso.football.views import FootballPageView

urlpatterns = [
    path('', FootballPageView.as_view(), name='football'),
]