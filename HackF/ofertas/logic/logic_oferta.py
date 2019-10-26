from ..models import Oferta
from productos.models import Producto

def get_ofertas():
  queryset = Oferta.objects.all()[:10]
  return (queryset)

def create_oferta(form):
  oferta = form.save()
  oferta.save()
  return ()

def get_productos_oferta(id):
  oferta = Oferta.objects.get(pk = id)
  prods = oferta.producto_set.all()
  return (prods)