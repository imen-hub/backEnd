from django.shortcuts import render

from rest_framework import viewsets
from .models import Teacher , Class
from .serializers import TeacherSerializer , ClassSerializer


class TeacherViewSet(viewsets.ModelViewSet):

    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class ClassViewSet(viewsets.ModelViewSet):

    serializer_class = ClassSerializer
    queryset = Class.objects.all()