from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Videojuego
from .serializers import VideojuegoSerializer

class VideojuegoViewSet(viewsets.ModelViewSet):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer
    permission_classes = [IsAuthenticated] # Autentificación de usuario