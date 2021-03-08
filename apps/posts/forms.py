from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('titulo', 'categoria', 'contenido', 'miniatura', 'autor')
		exclude = ['slug']
		#Esto es para que me use todos los campos definidos en la clase Post que se encuentra en models.py