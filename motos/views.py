from django.shortcuts import render
from .models import Moto

def motos(request):
    motos = Moto.objects.all()
    return render(request, 'motos/index.html', {'motos': motos})
