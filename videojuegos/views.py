from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Videojuego
from .serializers import VideojuegoSerializer
from .permissions import EsAdministrador, EsEliminador, EsVisualizador

class VideojuegoViewSet(viewsets.ModelViewSet):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer
    permission_classes = [IsAuthenticated] # Autentificación de usuario

    def get_permissions(self):
        "Asigna permisos según el método HTTP."
        if self.request.method in ['POST', 'PUT','PATCH']:
            return [EsAdministrador()]
        elif self.request.method == 'DELETE':
            return [EsEliminador()]
        elif self.request.method == 'GET':
            return [EsVisualizador()]
        else:
            return [IsAuthenticated()]