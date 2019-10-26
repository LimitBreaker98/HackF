from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .forms import OfertaForm
from ofertas.models import Oferta
from .logic.logic_oferta import *

# Create your views here.

def oferta_list(request):
  ofertas = get_ofertas()
  context = {
    'oferta_list': ofertas
  }
  return render(request, 'ofertas/oferta_list.html', context)

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

def productos_de_oferta(request, id):
  oferta = get_productos_oferta(id)
  context = {
    'oferta_list': oferta
  }
  return render(request, 'ofertas/oferta_list.html', context)
