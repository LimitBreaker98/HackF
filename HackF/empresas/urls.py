from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path('', views.empresa_list, name='empresa_list'),
  path('new', csrf_exempt(views.empresa_create), name='empresa_new'),
  path('<int:pk>/ofertas',views.ofertas_de_empresa, name='get_ofertas_empresa')
]