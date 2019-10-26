from ..models import Producto
from campesinos.models import Campesino
from campesinos.logic import *

def get_productos():
  queryset = Producto.objects.all()[:10]
  return (queryset)

def create_producto(form):
  producto = form.save()
  producto.save()
  return ()

def get_productos_campesino(name):
  campesino = Campesino.objects.get(nombre = name)
  prods = campesino.producto_set.all()
  return (prods)