from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class RegistrarUsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(RegistrarUsuarioForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

