from django.db import models

class Videojuego(models.Model):
    nombre = models.CharField(max_length=200)
    anio = models.IntegerField()
    creador = models.CharField(max_length=200, help_text="Nombre del creador")
    tipo = models.CharField(max_length=200, help_text="Tipo de videojugo")

    def __str__(self):
        return self.nombre
