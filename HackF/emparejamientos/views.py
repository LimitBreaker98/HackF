from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers

from .logic.logic_emparejamiento import *

# Create your views here.
def get_top_3_offers(request):
  ofertas = get_emparejamientos()
  qs_json = serializers.serialize('json', ofertas)
  return HttpResponse(qs_json, content_type='application/json')