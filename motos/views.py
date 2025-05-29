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
    paginate_by = 8
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset()

        marca = self.request.GET.get('marca')
        modelo = self.request.GET.get('modelo')
        preco_max = self.request.GET.get('preco_max')
        ano = self.request.GET.get('ano')

        if marca and marca != 'TODAS':
            queryset = queryset.filter(marca=marca)
        if modelo:
            queryset = queryset.filter(modelo__icontains=modelo)
        if preco_max:
            queryset = queryset.filter(preco__lte=preco_max)
        if ano:
            queryset = queryset.filter(ano=ano)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Moto._meta.get_field('marca').choices
        context['valores_get'] = self.request.GET  
        return context

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
