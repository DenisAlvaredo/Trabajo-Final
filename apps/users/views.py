from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from . forms import RegistrarUsuarioForm
from . models import User

# Create your views here.
class RegistrarUsuario(CreateView):
	model = User
	form_class = RegistrarUsuarioForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('login')

class EditarUsuario(UpdateView):
	model = User
	form_class = UserChangeForm
	template_name = 'users/profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user