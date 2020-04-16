from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
