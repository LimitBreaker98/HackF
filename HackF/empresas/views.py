from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core import serializers


from .forms import EmpresaForm
from empresas.models import Empresa
from .logic.logic_empresa import get_empresas, create_empresa, get_ofertas_empresa

# Create your views here.

def empresa_list(request):
  empresas = get_empresas()
  qs_json = serializers.serialize('json', empresas)
  return HttpResponse(qs_json, content_type='application/json')

def empresa_create(request):
  if request.method == 'POST':
    form = EmpresaForm(request.POST)
    if form.is_valid():
      create_empresa(form)
      messages.add_message(request, messages.SUCCESS, 'Company created successfully')
      return HttpResponseRedirect(reverse('empresa_new'))
    else:
      print(form.errors)
  else:
    form = EmpresaForm()
  
  context = {
    'form': form,
  }
  return render(request, 'empresas/empresa_form.html', context)

def ofertas_de_empresa(request, pk):
  ofertas = get_ofertas_empresa(pk)
  context = {
    'oferta_list': ofertas
  }
  return render(request, 'ofertas/oferta_list.html', context)
