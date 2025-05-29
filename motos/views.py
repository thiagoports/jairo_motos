from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Moto
from .forms import SignUpForm

@login_required(login_url='login')
def motos(request):
    motos = Moto.objects.all()
    return render(request, 'motos/index.html', {'motos': motos})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)             
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
