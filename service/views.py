from django.shortcuts import render
from rest_framework import viewsets
from .models import CatchingUp ,Meeting , Result , Events
from .serializers import CatchingUpSerializer ,MeetingSerializer , ResultSerializer ,EventsSerializer


class CatchingUpViewSet(viewsets.ModelViewSet):

    serializer_class = CatchingUpSerializer 
    queryset = CatchingUp.objects.all()

class MeetingViewSet(viewsets.ModelViewSet):

    serializer_class = MeetingSerializer 
    queryset = Meeting.objects.all()

class ResultViewSet(viewsets.ModelViewSet):

    serializer_class = ResultSerializer
    queryset = Result.objects.all()

class EventsViewSet(viewsets.ModelViewSet):

    serializer_class = EventsSerializer
    queryset =Events.objects.all()