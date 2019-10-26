from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core import serializers


from .forms import ProductoForm
from productos.models import Producto
from .logic.logic_producto import get_productos, create_producto, get_productos_campesino

# Create your views here.

def producto_list(request):
  productos = get_productos()
  print(type(productos))
  qs_json = serializers.serialize('json', productos)
  context = {
    'producto_list': productos
  }
  return HttpResponse(qs_json, content_type='application/json')

def producto_create(request):
  if request.method == 'POST':
    form = ProductoForm(request.POST)
    if form.is_valid():
      create_producto(form)
      messages.add_message(request, messages.SUCCESS, 'Product created successfully')
      return HttpResponseRedirect(reverse('producto_new'))
    else:
      print(form.errors)
  else:
    form = ProductoForm()
  
  context = {
    'form': form,
  }
  return render(request, 'productos/producto_form.html', context)

def productos_de_campesino(request, name):
  productos = get_productos_campesino(name)
  context = {
    'producto_list': productos
  }
  return render(request, 'productos/producto_list.html', context)
