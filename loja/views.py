from django.views.generic import ListView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Moto, Acessorio, Carrinho, ItemCarrinho
from .forms import SignUpForm

# Class Based views:


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/signup.html', {'form': form})


class MotoListView(LoginRequiredMixin, ListView):
    model = Moto
    template_name = 'loja/index.html'
    context_object_name = 'loja'
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
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        itens = carrinho.itens.select_related('moto')

        filtros = request.GET
        motos = Moto.objects.all()

        if filtros.get('marca') and filtros['marca'] != 'TODAS':
            motos = motos.filter(marca=filtros['marca'])
        if filtros.get('modelo'):
            motos = motos.filter(modelo__icontains=filtros['modelo'])
        if filtros.get('preco_max'):
            motos = motos.filter(preco__lte=filtros['preco_max'])
        if filtros.get('ano'):
            motos = motos.filter(ano=filtros['ano'])

        contexto = {
            'loja': motos,
            'marcas': Moto._meta.get_field('marca').choices,
            'valores_get': filtros,
            'carrinho': carrinho,
            'itens': itens
        }

        return render(request, 'loja/index.html', contexto)

    def post(self, request):
        moto_id = request.POST.get('moto_id')
        acao = request.POST.get('acao')

        if not moto_id or not moto_id.isdigit():
            return redirect('home')

        moto = Moto.objects.filter(id=moto_id).first()
        if not moto:
            return redirect('home')

        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

        if acao == 'remover':
            ItemCarrinho.objects.filter(carrinho=carrinho, moto=moto).delete()
        else:
            item, created = ItemCarrinho.objects.get_or_create(
                carrinho=carrinho, moto=moto)
            if not created:
                item.quantidade += 1
                item.save()

        return redirect('home')
