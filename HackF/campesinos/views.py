from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .forms import CampesinoForm
from campesinos.models import Campesino
from .logic.logic_campesino import get_campesinos, create_campesino

# Create your views here.

def campesinos_list(request):
  campesinos = get_campesinos()
  context = {
    'campesinos_list': campesinos
  }
  return render(request, 'campesinos/campesinos_list.html', context)

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