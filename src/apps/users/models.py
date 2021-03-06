from django.db import models #ESTO ES PARA PODER USAR LA BASE DE DATOS
from django.contrib.auth.models import AbstractUser

############################PARA LA TABLA USUARIO EN LA BASE DE DATOS###############################
class User(AbstractUser): #A partir de ahora la tabla de usuarios para la autenticacion es esta (User) y el dia de mañana puedo añadir mas campos. #Luego en los settings de le da permiso. AUTH_USER_MODEL = 'users.User'	<-- ('nombreDeLaAPP.nombreDeLaClase')
	nacionalidad = models.CharField(max_length = 30, null = True)
	bio = models.CharField(max_length = 250, null = True)
	ocupacion = models.CharField(max_length = 50, null = True)
	hobby = models.CharField(max_length = 100, null = True)
	face = models.CharField(max_length = 100, null = True)
	twitter = models.CharField(max_length = 100, null = True)
	insta = models.CharField(max_length = 100, null = True)
	snapchat = models.CharField(max_length = 100, null = True)
	youtube = models.CharField(max_length = 100, null = True)
	tiktok = models.CharField(max_length = 100, null = True)
	wapp = models.CharField(max_length = 100, null = True)
	web = models.CharField(max_length = 100, null = True)
	avatar = models.ImageField(upload_to='usuarios/avatares', blank=True, null=True)
	fechaModif = models.DateTimeField(auto_now=True)
	fecha_creacion = models.DateField('Fecha de creación', auto_now_add = True) #auto_now = False es para que no modifique su fecha si se llega a actualizar

	def __str__(self):
		return self.username
