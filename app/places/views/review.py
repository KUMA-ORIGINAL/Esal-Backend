from rest_framework import viewsets, mixins

from ..models import Review
from ..serializers import ReviewSerializer


class ReviewViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
