from django import forms
from .models import Post, Categoria, Comentarios

choices = Categoria.objects.all().values_list('nombre','nombre')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('__all__')
		exclude = ['slug', 'fecha_publicacion']
		widgets = {
			'categoria': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comentarios
		fields = ('user', 'comentario')
