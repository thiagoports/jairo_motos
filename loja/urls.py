from django.urls import path
from . import views

urlpatterns = [
    path('carrinho/', views.CarrinhoView.as_view(), name='carrinho'),
    path('home/', views.CarrinhoView.as_view(), name='home'),

]
