from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.campesinos_list, name='campesinos_list'),
    path('new', csrf_exempt(views.campesino_create), name='campesino_new'),
    path('<str:name>/ofertas', views.ofertas_de_campesinos, name='get_ofertas_campesino'),
    path('<str:name>/ofertas_productos', views.ofertas_productos_de_campesinos, name='get_ofertas_productos_campesino' )
]