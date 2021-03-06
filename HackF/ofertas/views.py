from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core import serializers
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import OfertaForm
from ofertas.models import Oferta
from .logic.logic_oferta import *

# Create your views here.

class OfertaUpdate(UpdateView):
  model = Oferta
  fields = [
    'fecha_entrega',
    'ubicacion_entrega',
    'estado',
    'campesino',
    'minorista'
  ]
  success_url = reverse_lazy('oferta_list')

def oferta_list(request):
  ofertas = get_ofertas()
  qs_json = serializers.serialize('json', ofertas)
  return HttpResponse(qs_json, content_type='application/json')

def oferta_create(request):
  if request.method == 'POST':
    form = OfertaForm(request.POST)
    if form.is_valid():
      create_oferta(form)
      messages.add_message(request, messages.SUCCESS, 'oferta created successfully')
      return HttpResponseRedirect(reverse('oferta_new'))
    else:
      print(form.errors)
  else:
    form = OfertaForm()
  
  context = {
    'form': form,
  }
  return render(request, 'ofertas/oferta_form.html', context)

def productos_de_oferta(request, pk):
  productos = get_productos_oferta(pk)
  qs_json = serializers.serialize('json', productos)
  return HttpResponse(qs_json, content_type='application/json')