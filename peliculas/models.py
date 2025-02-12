from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.IntegerField()
    duracion = models.IntegerField(help_text="Duración en minutos")

    def __str__(self):
        return self.titulo
