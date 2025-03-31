from rest_framework import viewsets, mixins

from ..models import Category
from ..serializers import  CategorySerializer


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
