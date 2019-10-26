from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core import serializers


from .forms import CampesinoForm
from campesinos.models import Campesino
from .logic.logic_campesino import get_campesinos, create_campesino, get_ofertas_campesino, get_ofertas_productos_campesino

# Create your views here.

def campesinos_list(request):
  campesinos = get_campesinos()
  qs_json = serializers.serialize('json', campesinos)
  return HttpResponse(qs_json, content_type='application/json')

def campesino_create(request):
  if request.method == 'POST':
    form = CampesinoForm(request.POST)
    if form.is_valid():
      create_campesino(form)
      messages.add_message(request, messages.SUCCESS, 'Product created successfully')
      return HttpResponseRedirect(reverse('campesino_new'))
    else:
      print(form.errors)
  else:
    form = CampesinoForm()
  
  context = {
    'form': form,
  }
  return render(request, 'campesinos/campesino_form.html', context)

def ofertas_de_campesinos(request, name):
  ofertas = get_ofertas_campesino(name)
  qs_json = serializers.serialize('json', ofertas)
  return HttpResponse(qs_json, content_type='application/json')

def ofertas_productos_de_campesinos(request, name):
  ofertas_productos = get_ofertas_productos_campesino(name)
  qs_json = serializers.serialize('json', ofertas_productos)
  return HttpResponse(qs_json, content_type='application/json')