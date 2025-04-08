from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions, generics, status, viewsets
from rest_framework.response import Response

from ..serializers import MeSerializer, MeUpdateSerializer, FavoriteListSerializer
from  places.models import Place

User = get_user_model()


@extend_schema(tags=['Users Me'])
class MeViewSet(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes  = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return MeUpdateSerializer
        return MeSerializer

    def get_object(self):
        return self.request.user


@extend_schema(tags=['Favorite places'])
@extend_schema_view(
    list=extend_schema(
        summary='Получение избранных мест'
    ),
    retrieve=extend_schema(
        summary='Добавлние и удаление из избранных',
        description='При запросе передается id места и добавляется в '
                    'избранные, при повторном запросе удаляется из избранных',
    )
)
class FavoritePlacesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FavoriteListSerializer
    lookup_field = 'place_id'

    def get_queryset(self):
        user = self.request.user
        return user.favorite_places.all()

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        place = get_object_or_404(Place, pk=kwargs.get('place_id'))

        if place in user.favorite_places.all():
            user.favorite_places.remove(place)
            return Response({'message': 'Place removed from favorites'},
                            status=status.HTTP_200_OK)
        user.favorite_places.add(place)
        return Response({'message': 'Place added to favorites'},
                        status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user, context={'request': request})
        return Response(serializer.data)
