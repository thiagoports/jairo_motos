from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.  

class CustomUser(AbstractUser):
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20,
                                validators=[
                                    RegexValidator(
                                        regex = r'^\d{10,11}$',
                                        message='Digite um número com DDD, somente números (ex: 11999999999).'
                                    )
                                ])
    email = models.EmailField(unique=True)
