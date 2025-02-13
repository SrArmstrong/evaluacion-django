from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pelicula
from .serializers import PeliculaSerializer
from .permissions import EsAdministrador, EsEliminador, EsVisualizador

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated] # Autentificación de usuario

    def get_permissions(self):
        "Asigna permisos según el método HTTP."
        if self.request.method in ['POST', 'PUT']:
            return [EsAdministrador()]
        elif self.request.method == 'DELETE':
            return [EsEliminador()]
        elif self.request.method == 'GET':
            return [EsVisualizador()]
        return super().get_permissions()