from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

############################PARA LA TABLA USUARIO EN LA BASE DE DATOS###############################
class User(AbstractUser): #A partir de ahora la tabla de usuarios para la autenticacion es esta (User) y el dia de mañana puedo añadir mas campos. #Luego en los settings de le da permiso. AUTH_USER_MODEL = 'users.User'	<-- ('nombreDeLaAPP.nombreDeLaClase')
	nacionalidad = models.CharField(max_length = 30, null = False, blank=True)
	bio = models.CharField(max_length = 250, null = False, blank=True)
	face = models.CharField(max_length = 100, null = False, blank=True)
	wapp = models.CharField(max_length = 100, null = False, blank=True)
	web = models.CharField(max_length = 100, null = False, blank=True)
	avatar = models.ImageField('Foto de Perfil', upload_to='avatar', blank=True, null=True)
	fechaModif = models.DateTimeField(auto_now=True)
	fecha_creacion = models.DateField('Fecha de creación', auto_now_add = True) #auto_now = False es para que no modifique su fecha si se llega a actualizar

	def __str__(self):
		return self.username
