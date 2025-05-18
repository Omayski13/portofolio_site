from django.contrib import admin
from django.urls import path, include

from portofolio_kriso.main.views import MainPageview

urlpatterns = [
    path('', MainPageview.as_view(), name='main'),
]