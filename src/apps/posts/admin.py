from django.contrib import admin
from .models import Categoria, Post

#Barra de búsqueda para mi sitio de admin:
class CategoriaAdmin(admin.ModelAdmin):
	search_fields = ['nombre'] #aqui se le pide que busque por los nombre registrados en la creacion de categorias
	list_display = ('nombre', 'estado', 'fecha_creacion') #esto para tener un display sobre las categorias creadas con los datos solicitados

class PostAdmin(admin.ModelAdmin):
	search_fields = ['titulo']
	list_display = ('titulo', 'categoria')
		
admin.site.register(Categoria, CategoriaAdmin) #agrego el sitio de segundas, para que se cargue la clase primero, de otro modo arroja error
admin.site.register(Post, PostAdmin)
