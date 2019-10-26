from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.campesinos_list, name='campesinos_list'),
    path('new', csrf_exempt(views.campesino_create), name='campesino_new')
]