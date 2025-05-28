from django.urls import path
from motos import views

urlpatterns = [
    path('', views.motos),
]