from django.shortcuts import render
from django.views.generic import TemplateView
from .google_auth import authenticate_google
from googleapiclient.discovery import build


# Create your views here.

class FootballPageView(TemplateView):
    template_name = 'football.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     creds = authenticate_google()
    #     service = build('calendar', 'v3', credentials=creds)

    #     events_result = service.events().list(
    #         calendarId='primary',
    #         timeMin='2025-06-10T00:00:00Z',
    #         maxResults=10,
    #         singleEvents=True,
    #         orderBy='startTime'
    #     ).execute()
        
    #     context['events'] = events_result.get('items', [])
    #     return context