from django import views
from django.urls import path, include

from chat.views import index

from .views import * 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',inicio,name='inicio'),
    path('login/', login_view,name='login'),
    path('registro/', register,name='register'),
    path('logout/', LogoutView.as_view(template_name='AppBanco/logout.html'),name='logout'),
    path('clientes/', clientes,name='clientes'),
    path('productos/', productos,name='productos'),
    path('sucursales/', sucursales,name='sucursales'),
    path('buscar_cliente/',buscar_cliente,name='buscar_cliente'),
    path('buscar/',buscar,name='buscar'),
    path('leerclientes/', leerclientes, name='leerclientes'),
    path('eliminarcliente/<cliente_nombre>/', eliminarclientes, name='eliminarcliente'),
    path('editarcliente/<cliente_nombre>/', editarcliente, name='editarcliente'),
    path('leerclientes/inicio', inicio, name='inicio'),
    path('clientes/inicio', inicio, name='inicio'),
    path('productos/inicio', inicio, name='inicio'),
    path('sucursales/inicio', inicio, name='inicio'),
    path('clientes/leerclientes', leerclientes, name='leerclientes'),
    path('clientes/agregarcliente', agregarclientes, name='agregarclientes'),
    path('editarperfil', editarperfil, name='editarperfil'),
    path('about', about, name='about'),
    path('chat', index, name='chat')    
]