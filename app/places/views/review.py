from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, mixins, permissions

from ..models import Review
from ..permissions import IsAuthorOrReadOnly
from ..serializers import ReviewReadSerializer, ReviewWriteSerializer


@extend_schema(tags=['Place review'])
@extend_schema_view(
    create=extend_schema(
        summary='Создание отзыва для места',
        description=''
    ),
    list=extend_schema(
        summary='Получение комментариев для места'
    ),
    partial_update=extend_schema(
        summary='Частичное обновление существующего отзыва'
    ),
    update=extend_schema(
        summary='Обновление существующего отзыва'
    ),
    destroy=extend_schema(
        summary='Удаление отзыва'
    )
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def get_queryset(self):
        res = super().get_queryset()
        place_id = self.kwargs.get("place_id")
        return res.filter(place_id=place_id)

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ReviewWriteSerializer
        return ReviewReadSerializer

    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (IsAuthorOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()
