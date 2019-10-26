from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .forms import ProductoForm
from productos.models import Producto
from .logic.logic_producto import get_productos, create_producto

# Create your views here.

def producto_list(request):
  productos = get_productos()
  context = {
    'producto_list': productos
  }
  return render(request, 'productos/producto_list.html', context)

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
    form = PurchaseForm()
  
  context = {
    'form': form,
  }
  return render(request, 'productos/producto_form.html', context)