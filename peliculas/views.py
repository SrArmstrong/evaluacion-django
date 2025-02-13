from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pelicula
from .serializers import PeliculaSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated] # Autentificación de usuario