from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from . views import *
from apps.users.views import RegistrarUsuario

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Base.as_view(), name = 'home'),

    path('Login/', auth.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('Logout/', auth.LogoutView.as_view(), name = 'logout'),
    path('Register/', RegistrarUsuario.as_view(), name = 'register'),


    path('', include('apps.posts.urls', 'post')), #aqui se le avisa que la app post tiene su propia url y , 'post' sera el nombre que represente a todas las urls dentro de la aplicacion posts#


]
