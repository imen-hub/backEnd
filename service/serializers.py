from rest_framework import serializers
from .models import CatchingUp , Meeting , Result , Events


class CatchingUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatchingUp
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = '__all__'
