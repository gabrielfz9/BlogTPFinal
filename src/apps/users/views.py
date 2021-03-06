from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from . forms import RegistrarUsuarioForm
from . models import User

class RegistrarUsuario(CreateView):
	model = User
	form_class = RegistrarUsuarioForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('home')

