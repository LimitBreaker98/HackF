from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path('', views.producto_list, name='producto_list'),
  path('new', csrf_exempt(views.producto_create), name='producto_new'),
  path('campesino/<str:name>',views.productos_de_campesino, name='get_productos_campesino')
]