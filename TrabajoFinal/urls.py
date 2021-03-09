"""TrabajoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from . import views
from . views import *
from apps.users.views import RegistrarUsuario, EditarUsuario
from apps.posts.views import CategoryView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home'),
    path('posts/', include('apps.posts.urls', 'posts')),

    path('Login/', auth.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('Logout/', auth.LogoutView.as_view(), name = 'logout'),
    path('Register/', RegistrarUsuario.as_view(), name = 'register'),
    path('Edit_Profile/', EditarUsuario.as_view(), name = 'editprofile'),
    path('category/<str:cats>', CategoryView, name = 'category'),
    #path('', include('apps.posts.urls', 'post')), #aqui se le avisa que la app post tiene su propia url y , 'post' sera el nombre que represente a todas las urls dentro de la aplicacion posts#
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)