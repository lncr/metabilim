from rest_framework import serializers
from .models import *

class EventDetailSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = serializers.SlugRelatedField(many=True,
                                        slug_field='title',
                                        read_only=True)
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
            'tags'
            )
class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_type', 'title', 'summary')
