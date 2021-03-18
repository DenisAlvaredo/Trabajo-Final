from django.contrib import admin
from django import forms
from .forms import PostForm
from .models import Categoria, Post, Comentarios

choices = Categoria.objects.all().values_list('nombre','nombre')

choice_list = []

for item in choices:
	choice_list.append(item)

#Barra de búsqueda para mi sitio de admin:
class CategoriaAdmin(admin.ModelAdmin):
	search_fields = ['nombre'] #aqui se le pide que busque por los nombre registrados en la creacion de categorias
	list_display = ('nombre', 'estado', 'fecha_creacion') #esto para tener un display sobre las categorias creadas con los datos solicitados

class PostAdmin(admin.ModelAdmin):
	search_fields = ['titulo']
	list_display = ('titulo', 'categoria')
	class Meta:
		model = Post
		fields = ('titulo','contenido')
		widgets = {
			'categoria': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
		}


admin.site.register(Categoria, CategoriaAdmin) #agrego el sitio de segundas, para que se cargue la clase primero, de otro modo arroja error
admin.site.register(Post, PostAdmin)
admin.site.register(Comentarios)