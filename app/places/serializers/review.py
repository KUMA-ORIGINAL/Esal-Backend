from rest_framework import serializers

from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Добавим информацию о пользователе в выводе

    class Meta:
        model = Review
        fields = [
            'id', 'place', 'user', 'text', 'rating', 'created_at',
        ]
