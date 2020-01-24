from rest_framework import serializers
from .models import *

class EventDetailSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = (
            'title',
            'summary',
            'event_type',
            'date',
            'deadline',
            'detailed_information',
            'thumb',
            'background',
            'link',
            )
class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'date')
