"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from biblioteca.views import *
urlpatterns = [
    path('libro/eliminar', eliminar_libro, name = 'eliminar_libro'),
    path('libro/editar', editar_libro, name = 'editar_libro'),
    path('libro/agregar', agregar_libro, name = 'agregar_libro'),
    path('', listar_libros, name = 'listar_libros'),

    path('biblioteca/eliminar', eliminar_biblioteca, name = 'eliminar_biblioteca'),
    path('biblioteca/editar', editar_biblioteca, name = 'editar_biblioteca'),
    path('biblioteca/agregar', agregar_biblioteca, name = 'agregar_biblioteca'),
    path('biblioteca/', listar_bibliotecas, name = 'listar_bibliotecas'),
    
    path('genero/eliminar', eliminar_genero, name = 'eliminar_genero'),
    path('genero/editar', editar_genero, name = 'editar_genero'),
    path('genero/agregar', agregar_genero, name = 'agregar_genero'),
    path('genero/', listar_generos, name = 'listar_generos'),

    path('ciudad/eliminar', eliminar_ciudad, name = 'eliminar_ciudad'),
    path('ciudad/editar', editar_ciudad, name = 'editar_ciudad'),
    path('ciudad/agregar', agregar_ciudad, name = 'agregar_ciudad'),
    path('ciudad/', listar_ciudades, name = 'listar_ciudades'),

    path('admin/', admin.site.urls),
]
