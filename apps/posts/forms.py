from django import forms
from .models import Post, Categoria

choices = Categoria.objects.all().values_list('nombre','nombre')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('__all__')
		exclude = ['author', 'slug', 'fecha_publicacion']

		widgets = {
			'categoria': forms.Select(choices=choices, attrs={'class': 'form-control'})
		}