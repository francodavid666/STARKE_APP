from ast import pattern
from urllib.parse import urlparse
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('formulario_login/', formulario_login, name= 'formulario_login'),
    path('usuario_creado/', usuario_creado, name= 'usuario_creado'),
    path('clientes/', clientes, name= 'clientes'),
    path('add_cliente/', add_cliente, name ='add_cliente'),
    path('detalle_cliente/<id>', detalle_cliente, name ='detalle_cliente'),
    path('modificar_datos_personales/<id>', modificar_datos_personales, name ='modificar_datos_personales'),
    path('eliminar_cliente/<id>', eliminar_cliente, name ='eliminar_cliente'),
    path('ficha_tecnica/<id>/<nombre>/<dni>',ficha_tecnica, name ='ficha_tecnica'),
]
