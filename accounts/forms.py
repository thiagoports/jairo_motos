from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'nome_completo', 'telefone', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'nome_completo', 'telefone', 'email')
        