from ..models import Empresa
from campesinos.models import Campesino
from campesinos.logic import *

def get_empresas():
  queryset = Empresa.objects.all()[:10]
  return (queryset)

def create_empresa(form):
  empresa = form.save()
  empresa.save()
  return ()

def get_ofertas_empresa(pk):
  empresa = Empresa.objects.get(id = pk)
  ofertas = empresa.oferta_set.all()
  return (ofertas)