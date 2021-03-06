from django.urls import path
from . import views
from . views import *

app_name = 'posts'

urlpatterns = [
	path('list/', PostListView.as_view(), name = 'posts_list'),
    path('subir_post/', PostCreateView.as_view(), name = 'create_post'), # Aqui create_post le dice a django que levante PostCreateView como una vista
    path('cultura/', Cultura.as_view(), name = 'cultura'),
    path('tecnologia/', Tecnologia.as_view(), name = 'tecnologia'),
    path('gaming/', Gaming.as_view(), name = 'gaming'),
    path('peliculas/', Peliculas.as_view(), name = 'peliculas'),
    path('series/', Series.as_view(), name = 'series'),
    path('anime/', Anime.as_view(), name = 'anime'),
    path('musica/', Musica.as_view(), name = 'musica'),
     
]
