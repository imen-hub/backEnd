from rest_framework import serializers
from .models import Teacher , Class


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'