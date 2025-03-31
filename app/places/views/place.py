from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, mixins, permissions, status
from rest_framework.response import Response

from ..models import Place
from ..serializers import PlaceSerializer


@extend_schema(tags=['Place'])
class PlaceViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


@extend_schema(tags=['Likes'])
@extend_schema_view(
    retrieve=extend_schema(
        summary='Лайк поста',
        description='При запросе лайк добавляется к посту по id, '
                    'повторный запрос удаляет лайк'
    ),
)
class PlaceLikeViewSet(viewsets.GenericViewSet,
                         mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'place_id'

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        place = get_object_or_404(Place, pk=kwargs.get('place_id'))
        if place.likes.filter(id=request.user.id).exists():
            place.likes.remove(user)
        else:
            place.likes.add(user)
        place.like_count = place.likes.count()
        place.save(update_fields=['like_count'])

        return Response({'message': 'Like updated successfully'}, status=status.HTTP_200_OK)


@extend_schema(tags=['Update view'])
@extend_schema_view(
    retrieve=extend_schema(
        summary='Обновление просмотра поста',
        description='При запросе добавляется к посту +1 просмотр по id',
        responses={status.HTTP_200_OK: 'View count updated successfully'}
    ),
)
class ViewCountUpdateViewSet(viewsets.GenericViewSet,
                             mixins.RetrieveModelMixin):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'place_id'

    def retrieve(self, request, *args, **kwargs):
        place = get_object_or_404(Place, pk=kwargs.get('place_id'))
        place.view_count += 1
        place.save()
        return Response(
            {'message': 'View count updated successfully',
             'view_count': place.view_count},
            status=status.HTTP_200_OK,
        )

