from rest_framework import serializers

from .category import CategorySerializer
from ..models import Place


class PlaceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'description', 'photo', 'category','rating', 'address',
            'facebook', 'instagram', 'twitter', 'youtube', 'tiktok',
            'view_count', 'like_count', 'likes'
        ]


class PlaceListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'description', 'photo', 'category', 'rating',
            'view_count', 'like_count', 'likes'
        ]
