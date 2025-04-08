from django.contrib.auth import get_user_model
from rest_framework import serializers

from places.serializers import PlaceListSerializer

User = get_user_model()


class MeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'photo')


class MeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'photo')


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'photo')


class FavoriteListSerializer(serializers.ModelSerializer):
    favorite_places = PlaceListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('favorite_places',)
