from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nome de usuário',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['username', 'email', 'password1', 'password2']:
            if field in self.fields:
                self.fields[field].help_text = ''

        self.fields['username'].error_messages.update({
            'required': 'Este campo é obrigatório.',
            'unique': 'Este nome de usuário já existe.'
        })
        self.fields['email'].error_messages.update({
            'required': 'Este campo é obrigatório.',
            'invalid': 'Informe um e-mail válido.'
        })
        self.fields['password1'].error_messages.update({
            'required': 'Este campo é obrigatório.'
        })
        self.fields['password2'].error_messages.update({
            'required': 'Este campo é obrigatório.',
            'password_mismatch': 'As senhas não coincidem.'
        })
