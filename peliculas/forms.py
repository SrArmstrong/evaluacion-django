from django import forms
from .models import Peliculas

class PeliculasForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = ['titulo', 'anio','duracion']
