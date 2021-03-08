from django.contrib import admin
from .models import User

# Register your models here.
class ListAdmin(admin.ModelAdmin):
	search_fields = ['username'] #aqui se le pide que busque por los nombre registrados en la creacion de categorias
	list_display = ('username', 'estado') #esto para tener un display sobre las categorias creadas con los datos solicitados

admin.site.register(User, ListAdmin)