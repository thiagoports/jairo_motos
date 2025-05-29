from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm

# Create your views here.

class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset = None):
        return self.request.user

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
    