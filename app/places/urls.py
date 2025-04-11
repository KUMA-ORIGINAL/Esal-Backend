from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PlaceViewSet, CategoryViewSet, ReviewViewSet, PlaceLikeViewSet, ViewCountUpdateViewSet

router = DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r"places/(?P<place_id>\d+)/reviews", ReviewViewSet)
router.register(r'like', PlaceLikeViewSet, basename='article-like')
router.register(r'update-view', ViewCountUpdateViewSet, basename='update-view')

urlpatterns = [
    path('', include(router.urls)),
]
