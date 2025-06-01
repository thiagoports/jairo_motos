from django.views.generic import ListView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Moto, Acessorio, Carrinho
from .forms import SignUpForm

# Class Based views:

# O CERTO ERA PUXAR A VIEW DE ACCOUNTS
# AQUI ESTÁ ERRADO
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

class AcessorioView(LoginRequiredMixin, ListView):
    model = Acessorio
    # trocar motos/index.html para loja/index.html
    template_name = 'loja/index.html'
    context_object_name = 'acessorios'
    paginate_by = 8
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset()

        nome = self.request.GET.get('nome')
        tipo = self.request.GET.get('tipo')
        preco_max = self.request.GET.get('preco_max')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if tipo and tipo != 'TODOS':
            queryset = queryset.filter(tipo=tipo)
        if preco_max:
            try:
                preco_valor = float(preco_max)
                queryset = queryset.filter(preco__lte=preco_valor)
            except ValueError:
                pass
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipos'] = Acessorio._meta.get_field('tipo').choices  
        context['valores_get'] = self.request.GET
        return context

class CarrinhoView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        #função que vai pegar o carrinho do usuario e se num tiver meu fi cria um carrinho pra ele
        carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)

        contexto = {
            'carrinho': carrinho,
            'moto': carrinho.moto if carrinho.moto else None,
            'acessorios': carrinho.acessorios.all()
        }
        return render(request, 'loja/carrinho.html', contexto)
    
    def post(self, request):
        # Para simplificar, espera no POST os ids da moto e acessórios para atualizar o carrinho
        moto_id = request.POST.get('moto_id')
        acessorios_ids = request.POST.getlist('acessorios_ids')

        carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)

        if moto_id:
            moto = get_object_or_404(Moto, id=moto_id)
            carrinho.moto = moto

        carrinho.acessorios.set(Acessorio.objects.filter(id__in=acessorios_ids))
        carrinho.save()

        return redirect('carrinho')  # nome da url para a view do carrinho