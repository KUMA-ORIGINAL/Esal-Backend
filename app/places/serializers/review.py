from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Review

User = get_user_model()


class UserReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'photo')


class ReviewReadSerializer(serializers.ModelSerializer):
    user = UserReviewSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'place', 'user', 'text', 'rating', 'created_at', 'updated_at'
        ]


class ReviewWriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = [
            'id', 'place', 'user', 'text', 'rating',
        ]
