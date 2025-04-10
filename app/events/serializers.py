from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'photo',
            'description',
            'location',
            'start_date',
            'end_date',
            'created_at',
        ]
