from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path('', views.oferta_list, name='oferta_list'),
  path('new', csrf_exempt(views.oferta_create), name='oferta_new'),
  path('<int:pk>/productos', views.productos_de_oferta, name='get_productos_oferta')
]