from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .models import Post, Categoria
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin

#####################CREACION DE LOS POSTS###############################

class PostCreateView(LoginRequiredMixin, CreateView): #entra heredando el createView y carga el formulario de forms.py y lo manda a post_Create.html
	model = Post
	form_class = PostForm
	template_name = 'posts/post_create.html'
	success_url = reverse_lazy('home')

############################LISTAR POSTS##################################

class PostListView(ListView):
	queryset = Post.objects.all().order_by('-fecha_publicacion')
	model = Post # Modelo creado en models.py el cual se creo con los campos a usar en la creacion del post
	template_name = 'posts/post_list'

#####################CATEGORIAS DE LOS POSTS##############################

class Cultura(TemplateView): #no olvidarse importar TemplateView
	template_name = 'posts/cultura.html'

class Tecnologia(TemplateView):
	template_name = 'posts/tecnologia.html'

class Gaming(TemplateView):
	template_name = 'posts/gaming.html'

class Peliculas(TemplateView):
	template_name = 'posts/peliculas.html'

class Series(TemplateView):
	template_name = 'posts/series.html'

class Anime(TemplateView):
	template_name = 'posts/anime.html'

class Musica(TemplateView):
	template_name = 'posts/musica.html'

#####################AQUI TERMINA CATEGORIAS DE LOS POSTS####################