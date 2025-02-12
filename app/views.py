from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'plantilla/home.html')

@login_required
def productos(request):
    return render(request, 'plantilla/productos.html')