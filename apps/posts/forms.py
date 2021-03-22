from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Post, Categoria, Comentarios

choices = Categoria.objects.all().values_list('nombre','nombre')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('__all__')
		exclude = ['slug', 'fecha_publicacion', 'author']
		widgets = {
			'categoria': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
		}
	

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comentarios
		fields = ('comentario',)



class FormFecha(forms.Form):
	Desde = forms.DateField(widget = SelectDateWidget())
	Hasta = forms.DateField(widget = SelectDateWidget())


#class PostFilter(filters.FilterSet):
 #   # Filtra por las fechas inferiores a la introducida
#    last_update_lte = django_filters.DateTimeFilter(name="last_update", lookup_expr='lte')
 #   # Filtra por las fechas mayores a la introducida
  #  last_update_gte = django_filters.DateTimeFilter(name="last_update", lookup_expr='gte')
   # class Meta:
    #    model = Post
     #   # Especificamos el nombre de los campos filtro
      #  fields = ['last_update_gte', 'last_update_lte']


#class PostFilter2(django_filters.FilterSet):
#	categoria__name = django_filters.CharFilter(lookup_expr='icontains')
#
#	release_year = django_filters.NumberFilter(field_name='fecha_publicacion', lookup_expr='year')
#	release_year__gt = django_filters.NumberFilter(field_name='fecha_publicacion', lookup_expr='year__gt')
#	release_year__lt = django_filters.NumberFilter(field_name='fecha_publicacion', lookup_expr='year__lt')
#
#	class Meta:
#		model = Post
#		fields = ['categoria', 'fecha_publicacion']