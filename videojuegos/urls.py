from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideojuegoViewSet

router = DefaultRouter()
router.register(r'videojuegos', VideojuegoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
