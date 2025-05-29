from django.views.generic import ListView, View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Moto
from .forms import SignUpForm

# Class Based views:
class MotoListView(LoginRequiredMixin, ListView):
    model = Moto
    template_name = 'motos/index.html'
    context_object_name = 'motos'
    login_url = 'login'

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form':form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'registration/signup.html', {'form':form})
