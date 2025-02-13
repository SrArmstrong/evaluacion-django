from django import forms
from .models import Videojuegos

class VideojuegosForm(forms.ModelForm):
    class Meta:
        model = Videojuegos
        fields = ['nombre', 'anio','creador','tipo']
