from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class RegistrarUsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(RegistrarUsuarioForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None


class EditUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2','first_name', 'last_name', 'avatar', 'nacionalidad', 'bio', 'face', 'wapp', 'web']

	def __init__(self, *args, **kwargs):
		super(EditUserForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

#class VerUsuarioForm(forms.ModelForm):
#	class Meta:
#		model = User
#		fields = ('username', 'email','first_name', 'last_name', 'avatar', 'nacionalidad', 'bio', 'face', 'wapp', 'web')
